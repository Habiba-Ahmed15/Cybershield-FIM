import hashlib
import os

HASH_FILE = "baseline.txt"

def calculate_file_hash(file_path):
    sha256_hash = hashlib.sha256()
    try:
        with open(file_path, "rb") as f:
            for byte_block in iter(lambda: f.read(4096), b""):
                sha256_hash.update(byte_block)
        return sha256_hash.hexdigest()
    except Exception as e:
        print(f"Error reading {file_path}: {e}")
        return None

if __name__ == "__main__":
    print("--- CyberShield FIM Active ---")
    target_file = "test.txt"
    
    if not os.path.exists(target_file):
        with open(target_file, "w") as f:
            f.write("Hello, CyberShield!")
        print(f"[+] Created test file: {target_file}")

    current_hash = calculate_file_hash(target_file)

    if not os.path.exists(HASH_FILE):
        with open(HASH_FILE, "w") as f:
            f.write(current_hash)
        print(f"[+] Baseline saved successfully! Hash: {current_hash}")
    else:
        with open(HASH_FILE, "r") as f:
            saved_hash = f.read().strip()
        
        print(f"[*] Saved Baseline: {saved_hash}")
        print(f"[*] Current Hash:   {current_hash}")
        
        if saved_hash == current_hash:
            print("[+] SUCCESS: File integrity is intact. No changes detected!")
        else:
            print("[!] ALERT: File has been modified! Integrity compromised!")
