"""
MindHaven AI - Railway Production Web Server
Serves the MindHaven AI Web Application and Interactive Counselor on Railway.
"""

import os
import sys
from http.server import HTTPServer, SimpleHTTPRequestHandler
from pathlib import Path

PROJECT_ROOT = Path(__file__).resolve().parent
WEB_DIR = PROJECT_ROOT / "web_demo"
PORT = int(os.environ.get("PORT", 8080))


class MindHavenHTTPHandler(SimpleHTTPRequestHandler):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, directory=str(WEB_DIR), **kwargs)

    def do_GET(self):
        # Health check endpoint for Railway
        if self.path == "/health" or self.path == "/api/health":
            self.send_response(200)
            self.send_header("Content-Type", "application/json")
            self.end_headers()
            self.wfile.write(b'{"status": "ok", "app": "MindHaven AI", "version": "1.0.0"}')
            return
        return super().do_GET()

    def log_message(self, format, *args):
        sys.stderr.write(f"[{self.log_date_time_string()}] {format % args}\n")


def main():
    server_address = ("0.0.0.0", PORT)
    httpd = HTTPServer(server_address, MindHavenHTTPHandler)
    print("=" * 60)
    print("  MindHaven AI Web Server Started Successfully!")
    print(f"  Listening on: http://0.0.0.0:{PORT}")
    print(f"  Serving Directory: {WEB_DIR}")
    print("=" * 60)
    try:
        httpd.serve_forever()
    except KeyboardInterrupt:
        print("\nShutting down server...")
        httpd.server_close()


if __name__ == "__main__":
    main()
