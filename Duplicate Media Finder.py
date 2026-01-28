# LEVEL 6: Confirm duplicates using file fingerprints (hashes)
# Same size = possible duplicates
# Same hash = real duplicates (exact match)

import os
import hashlib

folder = input("Enter a folder path: ").strip()

media_extensions = [
    ".jpg", ".jpeg", ".png", ".webp", ".gif",
    ".mp4", ".mov", ".mkv", ".avi"
]

# 1) Group media files by size
size_map = {}

for current_folder, subfolders, filenames in os.walk(folder):
    for name in filenames:
        lower_name = name.lower()

        # Only keep media files
        is_media = False
        for ext in media_extensions:
            if lower_name.endswith(ext):
                is_media = True
                break

        if not is_media:
            continue

        full_path = os.path.join(current_folder, name)

        try:
            size = os.path.getsize(full_path)
        except OSError:
            continue

        if size not in size_map:
            size_map[size] = []
        size_map[size].append(full_path)

# 2) Make a fingerprint (hash) for a file
def get_file_hash(path):
    hasher = hashlib.sha256()

    try:
        with open(path, "rb") as f:
            while True:
                chunk = f.read(1024 * 1024)  # 1MB
                if not chunk:
                    break
                hasher.update(chunk)
    except OSError:
        return None

    return hasher.hexdigest()

# 3) For same-size groups, group by hash
hash_map = {}

for size, paths in size_map.items():
    if len(paths) < 2:
        continue

    for path in paths:
        file_hash = get_file_hash(path)
        if file_hash is None:
            continue

        if file_hash not in hash_map:
            hash_map[file_hash] = []
        hash_map[file_hash].append(path)

# 4) Print real duplicates (same hash)
print("\nREAL duplicates:\n")

group_num = 1
found_any = False

for file_hash, paths in hash_map.items():
    if len(paths) >= 2:
        found_any = True
        print(f"--- Group {group_num} | {len(paths)} files ---")
        for p in paths:
            print(" ", p)
        print()
        group_num += 1

if not found_any:
    print("No exact duplicates found.")
