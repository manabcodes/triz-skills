# Provenance & Attribution

This skill packages the classical TRIZ (Theory of Inventive Problem Solving)
contradiction-resolution method for use as a Claude Skill. It does not
originate the TRIZ methodology; it compiles and organizes long-published,
widely-taught material for this specific use case.

## Origin of the underlying methodology

TRIZ was developed by **Genrich Saulovich Altshuller** (1926–1998) starting
in 1946, based on his analysis of hundreds of thousands of patents. The 39
Engineering Parameters, the 40 Inventive Principles, and the Contradiction
Matrix are his original research output, first published in the USSR
starting in 1956 (with Rafael B. Shapiro) and developed over subsequent
decades.

## Sources consulted while building this skill

- **Savransky, Semyon D.** *Engineering of Creativity: Introduction to TRIZ
  Methodology of Inventive Problem Solving.* CRC Press, 2000. Used as the
  primary source for parameter definitions and inventive principle
  descriptions; all text in `references/engineering_parameters.md` and
  `references/inventive_principles.md` was independently written/paraphrased
  from this source, not reproduced verbatim.
- **Szczepanik, Kamil & Chudziak, Jarosław A.** *TRIZ Agents: A Multi-Agent
  LLM Approach for TRIZ-Based Innovation.* ICAART 2025 / arXiv:2506.18783.
  Informed the original framing of this project (a multi-agent TRIZ
  workflow) and the step-by-step process described in `SKILL.md`.
- **Livotov, Pavel & Petrov, Vladimir.** *TRIZ Innovation Technology:
  Product Development and Inventive Problem Solving.* TriS Europe, 2011.
  Cross-referenced for the Contradiction Matrix cell values
  (`references/contradiction_matrix.json` / `.md`).
- Multiple independently published reproductions of Altshuller's matrix
  (academic course materials, triz40.com, MATRiZ training materials) were
  used to cross-check and verify matrix cell values during construction.
  See `scripts/build_matrix.py` for the build/verification process.

## What's original to this repository

- The organization of this material into a Claude Skill (`SKILL.md`
  structure, triggering description, workflow guidance).
- The specific wording of all explanatory text, parameter descriptions, and
  principle write-ups (paraphrased from sources above, not copied).
- `references/lookup.py` and `scripts/build_matrix.py` — original code.
- The cross-verification and cleanup process applied to the matrix data
  (see commit history / `scripts/build_matrix.py` comments for details,
  including a small number of corrected transcription artifacts).

## What's not claimed as original

The TRIZ methodology itself, the 39 Engineering Parameters as a concept set,
the 40 Inventive Principles as a concept set, and the factual content of the
Contradiction Matrix (which row/column pairing maps to which principle
numbers) are Altshuller's research findings, independently documented and
freely republished across dozens of TRIZ training resources worldwide. No
claim of ownership is made over this underlying factual/methodological
content — only over this particular compilation, its wording, and its
packaging as a Claude Skill.

## Corrections welcome

The Contradiction Matrix was manually transcribed and cross-checked against
multiple independent sources, but a table of this size (39×39, ~1,200
populated cells) is not something either a human or an LLM can verify with
100% certainty by inspection alone. If you find a cell that looks wrong,
please open an issue with the cell coordinates and your source, and it'll
get checked and corrected.
