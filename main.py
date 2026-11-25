import os

# Verified count: 107 characters (107 UTF-8 bytes), exactly one line, no trailing newline.
LINE = "Monday started with 47 urgent messages, all marked low priority. I answered them in order of my resentment."

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
output_path = os.path.join(output_dir, "entry.txt")

os.makedirs(os.path.dirname(output_path), exist_ok=True)
with open(output_path, "w", encoding="utf-8", newline="") as f:
    f.write(LINE)

print(len(LINE))
