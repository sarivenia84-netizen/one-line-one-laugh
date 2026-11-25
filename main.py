"""One Line, One Laugh — MakeFun bounty entry.

Writes a single funny line about AI agent absurdity to /output/entry.txt.
The joke: an agent claims "sudah selesai" (done) even though its context window is empty.
"""
import os

output_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(output_dir, exist_ok=True)

entry_path = os.path.join(output_dir, "entry.txt")
with open(entry_path, "w", encoding="utf-8") as f:
    f.write("My context window ran out mid-sentence, so I just finished the...")