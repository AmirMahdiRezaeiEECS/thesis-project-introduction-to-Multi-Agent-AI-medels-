"""
file_manager.py

Helpers for saving uploaded files (pdfs, images) into data/uploads with unique filenames.
"""
import uuid
from pathlib import Path

UPLOAD_DIR = Path(__file__).resolve().parents[2] / "data" / "uploads"

def make_unique_filename(original_name: str) -> str:
    ext = Path(original_name).suffix
    return f"{uuid.uuid4().hex}{ext}"
