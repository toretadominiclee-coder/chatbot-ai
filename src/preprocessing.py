"""
MindHaven AI - Text Preprocessing Pipeline
IS Professional Elective #4 - Gen AI Capstone Project (Checkpoint 1: Deliverable 3)

Performs multi-stage cleaning, normalization, tokenization, and semantic chunking
over messy institutional Mental Health & Introvert Emotional Expression documents.
"""

import os
import re
import json
import unicodedata
from pathlib import Path
from typing import List, Dict, Any, Tuple

RAW_DATA_DIR = Path("data/raw")
PROCESSED_DATA_DIR = Path("data/processed")
PROCESSED_DATA_DIR.mkdir(parents=True, exist_ok=True)


class TextCleaner:
    """Multi-stage cleaner and normalizer for unstructured institutional text."""

    @staticmethod
    def remove_scanned_artifacts(text: str) -> str:
        """Strips header/footer noise, page numbers, and confidentiality banners."""
        # Remove repetitive divider lines
        text = re.sub(r'^[=\-+*_]{3,}\s*$', '', text, flags=re.MULTILINE)
        
        # Remove page number artifacts like [PAGE 1 OF 6 - CONFIDENTIAL], [PAGE 2 OF 5]
        text = re.sub(r'\[PAGE\s+\d+\s+OF\s+\d+[^\]]*\]', '', text, flags=re.IGNORECASE)
        
        # Remove confidentiality banners and uncontrolled copy watermarks
        text = re.sub(r'\*\*\*\s*UNCONTROLLED COPY[^*]*\*\*\*', '', text, flags=re.IGNORECASE)
        text = re.sub(r'\[CONFIDENTIAL[^\]]*\]', '', text, flags=re.IGNORECASE)
        text = re.sub(r'DOCUMENT CODE:[^\n]+', '', text, flags=re.IGNORECASE)
        text = re.sub(r'REVISED:[^\n]+', '', text, flags=re.IGNORECASE)
        
        return text

    @staticmethod
    def normalize_unicode_and_quotes(text: str) -> str:
        """Normalizes Unicode characters, curly quotes, dashes, and bullet symbols."""
        text = unicodedata.normalize('NFKC', text)
        
        # Replace fancy typographic quotes
        text = re.sub(r'[\u2018\u2019\u201B\u2032]', "'", text)
        text = re.sub(r'[\u201C\u201D\u201F\u2033]', '"', text)
        
        # Replace typographic dashes and hyphens
        text = re.sub(r'[\u2013\u2014\u2015]', ' - ', text)
        
        # Normalize bullet point characters
        text = re.sub(r'[\u2022\u2023\u25E6\u2043\u2219]', '- ', text)
        text = re.sub(r'^\s*[\+\*o]\s+', '- ', text, flags=re.MULTILINE)
        text = re.sub(r'-->', '->', text)
        
        return text

    @staticmethod
    def normalize_tables_and_whitespace(text: str) -> str:
        """Converts ASCII table borders into clean readable Markdown text."""
        lines = []
        for line in text.splitlines():
            if re.match(r'^\s*[\+\|][\-+\|]+\s*$', line):
                continue
            if line.strip().startswith('|') and line.strip().endswith('|'):
                cells = [c.strip() for c in line.strip().split('|')[1:-1]]
                cleaned_row = " | ".join(cells)
                lines.append(f"  * {cleaned_row}")
            else:
                lines.append(line)
                
        text = "\n".join(lines)
        text = re.sub(r'\n{3,}', '\n\n', text)
        text = re.sub(r'[ \t]+', ' ', text)
        return text.strip()

    @classmethod
    def clean_text(cls, raw_text: str) -> str:
        """Runs full end-to-end cleaning pipeline."""
        t1 = cls.remove_scanned_artifacts(raw_text)
        t2 = cls.normalize_unicode_and_quotes(t1)
        t3 = cls.normalize_tables_and_whitespace(t2)
        return t3


class TextChunker:
    """Semantic sliding-window and section-based chunker for RAG pipeline."""

    def __init__(self, target_chunk_size: int = 180, overlap: int = 25):
        self.target_chunk_size = target_chunk_size
        self.overlap = overlap

    def chunk_document(self, cleaned_text: str, doc_metadata: Dict[str, Any]) -> List[Dict[str, Any]]:
        """Splits cleaned text into semantically cohesive chunks with metadata."""
        paragraphs = [p.strip() for p in cleaned_text.split('\n\n') if p.strip()]
        
        chunks = []
        current_chunk_words = []
        current_chunk_tokens = 0
        chunk_idx = 1
        
        for para in paragraphs:
            para_words = para.split()
            para_tokens = int(len(para_words) * 1.3)
            
            if current_chunk_tokens + para_tokens > self.target_chunk_size and current_chunk_words:
                chunk_text = " ".join(current_chunk_words)
                chunks.append({
                    "chunk_id": f"{doc_metadata['doc_id']}_c{chunk_idx:02d}",
                    "doc_id": doc_metadata['doc_id'],
                    "title": doc_metadata['title'],
                    "domain": "mental_health_wellness",
                    "category": doc_metadata['category'],
                    "source_file": doc_metadata['filename'],
                    "text": chunk_text,
                    "word_count": len(current_chunk_words),
                    "token_count": int(len(current_chunk_words) * 1.3),
                    "char_count": len(chunk_text)
                })
                chunk_idx += 1
                
                overlap_words = current_chunk_words[-self.overlap:] if len(current_chunk_words) > self.overlap else []
                current_chunk_words = list(overlap_words) + para_words
                current_chunk_tokens = int(len(current_chunk_words) * 1.3)
            else:
                current_chunk_words.extend(para_words)
                current_chunk_tokens += para_tokens
                
        if current_chunk_words:
            chunk_text = " ".join(current_chunk_words)
            chunks.append({
                "chunk_id": f"{doc_metadata['doc_id']}_c{chunk_idx:02d}",
                "doc_id": doc_metadata['doc_id'],
                "title": doc_metadata['title'],
                "domain": "mental_health_wellness",
                "category": doc_metadata['category'],
                "source_file": doc_metadata['filename'],
                "text": chunk_text,
                "word_count": len(current_chunk_words),
                "token_count": int(len(current_chunk_words) * 1.3),
                "char_count": len(chunk_text)
            })
            
        return chunks


def infer_metadata_from_filename(filename: str) -> Dict[str, Any]:
    """Infers emotional health category and document title from naming convention."""
    name_without_ext = Path(filename).stem
    parts = name_without_ext.split('_')
    doc_id = f"{parts[0]}_{parts[1]}"
    doc_num = int(parts[1])
    
    title_words = parts[2:]
    title = " ".join(title_words).title()
    
    if doc_num in [1, 27]:
        category = "Emotional Expression & Journaling"
    elif doc_num in [2, 7, 8, 23, 26]:
        category = "Social Anxiety & Classroom Coping"
    elif doc_num in [3, 10, 14, 22]:
        category = "Dorm Overstimulation & Solitude Recharge"
    elif doc_num in [4, 5, 12, 24]:
        category = "CBT & Cognitive Reframing"
    elif doc_num in [6, 9, 11, 13, 20]:
        category = "Somatic Grounding & Stress Management"
    elif doc_num in [15, 21, 28]:
        category = "Crisis Safety & Emergency Lifelines"
    else:
        category = "Therapy Intake & Self-Advocacy"
            
    return {
        "doc_id": doc_id,
        "title": title,
        "domain": "mental_health_wellness",
        "category": category,
        "filename": filename
    }


def run_pipeline() -> Tuple[List[Dict[str, Any]], Dict[str, Any], List[Dict[str, Any]]]:
    """Executes end-to-end preprocessing over data/raw/ and writes processed datasets."""
    cleaner = TextCleaner()
    chunker = TextChunker(target_chunk_size=180, overlap=25)
    
    raw_files = sorted(list(RAW_DATA_DIR.glob("*.txt")))
    if not raw_files:
        raise FileNotFoundError(f"No raw text files found in {RAW_DATA_DIR.resolve()}!")
        
    all_chunks = []
    before_after_samples = []
    doc_stats = []
    
    total_raw_chars = 0
    total_cleaned_chars = 0
    
    print("=" * 70)
    print("MINDHAVEN AI - MENTAL HEALTH & INTROVERT DATA PIPELINE")
    print(f"Processing {len(raw_files)} documents from {RAW_DATA_DIR}...")
    print("=" * 70)
    
    for idx, filepath in enumerate(raw_files, 1):
        with open(filepath, "r", encoding="utf-8") as f:
            raw_text = f.read()
            
        metadata = infer_metadata_from_filename(filepath.name)
        cleaned_text = cleaner.clean_text(raw_text)
        doc_chunks = chunker.chunk_document(cleaned_text, metadata)
        
        all_chunks.extend(doc_chunks)
        
        raw_char_len = len(raw_text)
        clean_char_len = len(cleaned_text)
        total_raw_chars += raw_char_len
        total_cleaned_chars += clean_char_len
        
        doc_stats.append({
            "doc_id": metadata["doc_id"],
            "title": metadata["title"],
            "category": metadata["category"],
            "raw_chars": raw_char_len,
            "cleaned_chars": clean_char_len,
            "compression_ratio": round(clean_char_len / raw_char_len, 3),
            "num_chunks": len(doc_chunks)
        })
        
        if idx in [1, 2, 4, 15]:
            before_after_samples.append({
                "doc_id": metadata["doc_id"],
                "title": metadata["title"],
                "raw_sample": raw_text[:400] + ("..." if len(raw_text) > 400 else ""),
                "cleaned_sample": cleaned_text[:400] + ("..." if len(cleaned_text) > 400 else ""),
                "changes_applied": [
                    "Stripped scanned header/footer artifacts and confidentiality markers",
                    "Normalized Unicode quotes, dashes, and bullet symbols",
                    "Flattened ASCII table structures into clean bullet points",
                    "Collapsed redundant whitespace and preserved clinical guidance"
                ]
            })
            
        print(f"[{idx:02d}/{len(raw_files):02d}] Processed {filepath.name} -> {len(doc_chunks)} chunks")
        
    corpus_metadata = {
        "project_name": "MindHaven AI (Mental Health & Introvert Emotional Counseling)",
        "total_documents": len(raw_files),
        "total_chunks": len(all_chunks),
        "total_raw_characters": total_raw_chars,
        "total_cleaned_characters": total_cleaned_chars,
        "average_reduction_percentage": f"{round((1 - total_cleaned_chars / total_raw_chars) * 100, 2)}%",
        "average_chunks_per_doc": round(len(all_chunks) / len(raw_files), 2),
        "documents": doc_stats
    }
    
    chunks_path = PROCESSED_DATA_DIR / "processed_chunks.json"
    with open(chunks_path, "w", encoding="utf-8") as f:
        json.dump(all_chunks, f, indent=2, ensure_ascii=False)
        
    metadata_path = PROCESSED_DATA_DIR / "corpus_metadata.json"
    with open(metadata_path, "w", encoding="utf-8") as f:
        json.dump(corpus_metadata, f, indent=2, ensure_ascii=False)
        
    samples_path = PROCESSED_DATA_DIR / "before_after_samples.json"
    with open(samples_path, "w", encoding="utf-8") as f:
        json.dump(before_after_samples, f, indent=2, ensure_ascii=False)
        
    print("\n" + "=" * 70)
    print(f"PREPROCESSING COMPLETE!")
    print(f"Total Mental Health Chunks: {len(all_chunks)}")
    print(f"Saved chunks to: {chunks_path}")
    print("=" * 70)
    
    return all_chunks, corpus_metadata, before_after_samples


if __name__ == "__main__":
    run_pipeline()
