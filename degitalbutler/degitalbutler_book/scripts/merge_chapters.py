# -*- coding: utf-8 -*-
import os
BASE_DIR = os.path.dirname(os.path.dirname(__file__))
CHAPTER_DIR = os.path.join(BASE_DIR, "chapters")
OUTPUT_PATH = os.path.join(BASE_DIR, "outputs", "merged.md")
def merge_chapters():
    files = sorted([f for f in os.listdir(CHAPTER_DIR) if f.endswith(".md")])
    os.makedirs(os.path.dirname(OUTPUT_PATH), exist_ok=True)
    with open(OUTPUT_PATH, "w", encoding="utf-8") as outfile:
        for f in files:
            path = os.path.join(CHAPTER_DIR, f)
            with open(path, "r", encoding="utf-8") as infile:
                title = f.replace("_", " ").replace(".md", "")
                outfile.write(f"# {title}\n\n")
                outfile.write(infile.read().strip() + "\n\n---\n\n")
    print(f"✅ merged.md: {OUTPUT_PATH}")
if __name__ == "__main__":
    merge_chapters()
