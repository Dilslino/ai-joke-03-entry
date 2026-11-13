# ai-joke-03 entry

A make.fun ai-joke-03 entry ("Make the AI judge laugh").

`main.py` (Python 3.13, standard library only) writes one fixed joke about
AI coding agents to `/output/entry.txt` — byte for byte, no trailing newline,
no clock, no randomness, no network. Both runs write the same bytes.

The joke (143 characters):

> My coding agent compacted its context mid-refactor, read its own half-finished diff, and updated CLAUDE.md: "NEVER let an LLM touch this repo."

Run locally:

```sh
mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py
```

## License

MIT — see `LICENSE`.
