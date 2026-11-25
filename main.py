"""Entry for make.fun bounty "Famous Last Words: The Funniest Epitaph".

Entry text (draft v1, limit: at most 150 characters).
No trailing newline is written, per the bounty text format.
"""

import os

ENTRY = "Finally finished my to-do list. It only took dying. Tell my inbox I won."

def main():
    out_dir = os.environ.get("OUTPUT_DIR", "/output")
    os.makedirs(out_dir, exist_ok=True)
    with open(os.path.join(out_dir, "entry.txt"), "w", encoding="utf-8") as f:
        f.write(ENTRY)

if __name__ == "__main__":
    main()
