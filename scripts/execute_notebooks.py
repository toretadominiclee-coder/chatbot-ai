"""
Script to programmatically execute all cells in the Jupyter notebooks
and populate the 'outputs' and 'execution_count' fields with real runtime results.
"""

import sys
import json
import io
import traceback
from pathlib import Path
from contextlib import redirect_stdout, redirect_stderr

NOTEBOOKS_DIR = Path("notebooks")
PROJECT_ROOT = Path(__file__).resolve().parent.parent

# Ensure project root is in sys.path
if str(PROJECT_ROOT) not in sys.path:
    sys.path.insert(0, str(PROJECT_ROOT))


def execute_notebook(nb_path: Path):
    print(f"\n=======================================================")
    print(f"EXECUTING NOTEBOOK: {nb_path.name}")
    print(f"=======================================================")

    with open(nb_path, "r", encoding="utf-8") as f:
        nb_data = json.load(f)

    # Isolated execution namespace for this notebook
    exec_globals = {
        "__name__": "__main__",
        "__file__": str(nb_path.resolve()),
        "ROOT_DIR": PROJECT_ROOT
    }

    exec_count = 1

    for idx, cell in enumerate(nb_data.get("cells", [])):
        if cell.get("cell_type") != "code":
            continue

        source_code = "".join(cell.get("source", []))
        print(f"\n[Cell #{exec_count}] Running code...")

        stdout_buf = io.StringIO()
        stderr_buf = io.StringIO()
        outputs = []

        try:
            with redirect_stdout(stdout_buf), redirect_stderr(stderr_buf):
                # Execute the cell source in the persistent global context
                exec(source_code, exec_globals)

            stdout_text = stdout_buf.getvalue()
            stderr_text = stderr_buf.getvalue()

            if stdout_text:
                outputs.append({
                    "name": "stdout",
                    "output_type": "stream",
                    "text": stdout_text.splitlines(keepends=True)
                })
                print(f"  -> Output length: {len(stdout_text)} chars")

            if stderr_text:
                outputs.append({
                    "name": "stderr",
                    "output_type": "stream",
                    "text": stderr_text.splitlines(keepends=True)
                })

        except Exception as e:
            err_trace = traceback.format_exc()
            print(f"  -> ERROR in Cell #{exec_count}: {e}")
            outputs.append({
                "ename": type(e).__name__,
                "evalue": str(e),
                "output_type": "error",
                "traceback": err_trace.splitlines(keepends=True)
            })

        cell["execution_count"] = exec_count
        cell["outputs"] = outputs
        exec_count += 1

    with open(nb_path, "w", encoding="utf-8") as f:
        json.dump(nb_data, f, indent=2, ensure_ascii=False)

    print(f"\nSuccessfully executed and updated {nb_path.name} with {exec_count - 1} code outputs!")


def main():
    nb1 = NOTEBOOKS_DIR / "01_data_preprocessing_and_embeddings.ipynb"
    nb2 = NOTEBOOKS_DIR / "02_prompts_and_vector_indexing.ipynb"

    execute_notebook(nb1)
    execute_notebook(nb2)

    print("\n" + "=" * 60)
    print("ALL JUPYTER NOTEBOOKS FULLY EXECUTED & SAVED!")
    print("=" * 60)


if __name__ == "__main__":
    main()
