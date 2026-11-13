# ai-joke-03 entry: writes one fixed joke about AI coding agents.
# Deterministic: no clock, no randomness, no network, stdlib only.
# The joke is written byte-for-byte, with no trailing newline added.
import os

JOKE = 'My coding agent compacted its context mid-refactor, read its own half-finished diff, and updated CLAUDE.md: "NEVER let an LLM touch this repo."'

out_dir = os.environ.get("MAKEFUN_OUTPUT_DIR", "/output")
os.makedirs(out_dir, exist_ok=True)
path = os.path.join(out_dir, "entry.txt")
with open(path, "w", encoding="utf-8") as f:
    f.write(JOKE)
# Self-check: the file must hold exactly the joke, byte for byte.
# A silent short write would fail the gate, so fail loudly instead.
with open(path, "rb") as f:
    assert f.read().decode("utf-8") == JOKE
