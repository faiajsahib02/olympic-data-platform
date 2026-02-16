import os

def check_file_exists(filepath):
    """Verify the data arrived"""
    if not os.path.exists(filepath):
        raise FileNotFoundError(f"CRITICAL: Data file missing at {filepath}")
    print(f"File found! Size: {os.path.getsize(filepath)} bytes")