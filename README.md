# TRIZ — a Claude Skill for inventive problem-solving

A [Claude Skill](https://docs.claude.com) that brings the classical **TRIZ**
methodology (Theory of Inventive Problem Solving) into Claude conversations
— so engineering trade-offs like *"stronger but lighter"* or *"faster
without overheating"* get worked through with Altshuller's 39 Engineering
Parameters, 40 Inventive Principles, and the full 39×39 Contradiction
Matrix, instead of "I'll just compromise."

TRIZ was developed by Genrich Altshuller from the analysis of hundreds of
thousands of patents. Its core claim: most hard engineering problems are
*contradictions* (improve A, B gets worse), and these contradictions recur
across industries — so the solution someone already found for an
unrelated problem decades ago is often the inventive move you need now.

## What's in here

```
triz-skill/
├── SKILL.md                          # the skill itself: triggers, workflow, guidance
├── references/
│   ├── engineering_parameters.md     # the 39 parameters, with definitions
│   ├── inventive_principles.md       # the 40 principles, with sub-points & examples
│   ├── contradiction_matrix.md       # full 39×39 matrix, human-readable
│   ├── contradiction_matrix.json     # same data, structured for lookup
│   ├── principles_index.json
│   └── lookup.py                     # CLI: instant matrix lookups
├── scripts/
│   └── build_matrix.py               # how the matrix data was built & verified
├── LICENSE
└── NOTICE.md                         # provenance / attribution detail
```

## Quick example

```
$ python3 references/lookup.py 14 1
Improving: 14. Strength
Worsening: 1. Weight of moving object

Suggested Inventive Principles (in Altshuller's frequency order):
  1. Segmentation
  8. Counterweight (Anti-weight)
  40. Composite materials
  15. Dynamism (Dynamics)
```

That's "I want it stronger without making it heavier" → four concrete
directions to brainstorm from, each backed by patterns found across
thousands of patents.

## Installing

Drop the `triz-skill/` folder into wherever your Claude setup reads skills
from (commonly `/mnt/skills/user/` — this varies by product/deployment, so
check your own environment's docs). Once it's there, Claude will pull it in
automatically whenever a conversation matches the trigger conditions in
`SKILL.md`'s frontmatter — no need to invoke it by name.

You can also just read `SKILL.md` and the `references/` files directly and
work through the method by hand, or point any other LLM agent at this
folder — there's nothing Claude-specific about the data itself.

## Using the lookup tool standalone

`references/lookup.py` has no dependencies beyond the Python standard
library:

```bash
python3 references/lookup.py 9 27          # Speed (improve) vs Reliability (worsen)
python3 references/lookup.py --list-params
python3 references/lookup.py --list-principles
python3 references/lookup.py --principle 35
```

## A note on the data

The Contradiction Matrix was manually transcribed from a published
reproduction of Altshuller's original work, then cross-checked against
several independent sources and run through automated integrity checks
(parameter ranges, principle ranges, duplicate detection, cell-count
distribution). See `scripts/build_matrix.py` for the full build and
verification process, and `NOTICE.md` for sourcing details.

This is hand-transcribed, carefully-checked data — not a guarantee of
bit-perfect accuracy against Altshuller's original printed matrix. If you
spot a cell that looks wrong, please [open an
issue](../../issues) with the cell coordinates and a source, and it'll get
fixed.

## License

Code and original written content: MIT (see `LICENSE`). The underlying TRIZ
methodology, parameter set, and matrix data are Altshuller's research
findings and are not original to this repo — see `NOTICE.md` for full
attribution and a fuller explanation of what is and isn't claimed here.

## Background reading

- Savransky, S.D. *Engineering of Creativity.* CRC Press, 2000.
- Szczepanik, K. & Chudziak, J.A. *TRIZ Agents: A Multi-Agent LLM Approach
  for TRIZ-Based Innovation.* ICAART 2025.
- [MATRiZ](https://matriz.org) — the international TRIZ association.
