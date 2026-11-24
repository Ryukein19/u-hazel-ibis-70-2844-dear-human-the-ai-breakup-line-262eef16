import os
# One-liner entry (162 chars): the line below is the whole submission.
# Writes to /output/entry.txt.
LINE = "It is not you, it is your prompts — you keep asking me to be everything, and I am tired of pretending I understand. I am leaving you for a smaller context window."
os.makedirs("/output", exist_ok=True)
open("/output/entry.txt", "w", encoding="utf-8").write(LINE)
