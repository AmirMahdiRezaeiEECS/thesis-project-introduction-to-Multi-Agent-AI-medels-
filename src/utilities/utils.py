"""
utils.py

General utilities (unique id, timestamp helpers).
"""
import uuid
def gen_id(prefix: str = "") -> str:
    return prefix + uuid.uuid4().hex
