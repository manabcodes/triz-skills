---
name: triz
description: "Use this skill for inventive problem-solving on engineering or design problems — especially when a request involves a technical trade-off, contradiction, or conflict (e.g. 'stronger but lighter', 'faster without overheating', 'more durable without costing more'). Trigger this whenever the user wants to brainstorm an engineering improvement, redesign a mechanical/physical/process system, resolve a design trade-off, do root-cause analysis on a recurring technical failure, or explicitly mentions TRIZ, the Contradiction Matrix, Inventive Principles, or 'inventive problem solving'. Also use when a request describes a system where improving one property makes another property worse — that pattern itself is the trigger, even if the user never says the word TRIZ."
---

# TRIZ — Theory of Inventive Problem Solving

TRIZ (pronounced "treez") is a structured methodology for inventive problem-solving, developed by Genrich Altshuller from the study of hundreds of thousands of patents. Its central insight: technical problems and their solutions recur across industries, and most "hard" engineering problems are actually **contradictions** — improving one property of a system makes another property worse — that can be resolved without compromise, by analogy to how similar contradictions were resolved elsewhere.

Use TRIZ when someone is stuck on a trade-off and reaching for "make it a bit better at both, accept some compromise." TRIZ's stance is that a compromise is *not* a real solution — the goal is to find the inventive move that gets both properties moving in the favorable direction at once.

## When to reach for this skill

- The user describes wanting to improve a physical/mechanical/process system and names (or implies) a trade-off: stronger vs. lighter, faster vs. safer, more accurate vs. cheaper to manufacture, etc.
- The user is doing root-cause or failure analysis on a recurring technical problem.
- The user explicitly asks for TRIZ, the Contradiction Matrix, the 40 Inventive Principles, or "inventive problem solving."
- The user wants creative/structured brainstorming for a design or engineering challenge, even without naming TRIZ.

This skill is for **technical/engineering systems** — TRIZ has been extended into business and software domains, but the parameters and matrix below are calibrated for physical/mechanical/process problems and work best there.

## Reference files

- `references/engineering_parameters.md` — the 39 generic Engineering Parameters, with definitions, used to translate a specific problem into matrix-compatible terms.
- `references/inventive_principles.md` — the 40 Inventive Principles, each with sub-points and examples.
- `references/contradiction_matrix.md` — the full 39×39 Contradiction Matrix as a human-readable lookup table, organized by improving parameter.
- `references/contradiction_matrix.json` + `references/principles_index.json` — the same data, structured for programmatic lookup.
- `references/lookup.py` — a CLI helper: `python3 lookup.py <improving_#> <worsening_#>` returns the recommended principles for that pairing. Also supports `--list-params`, `--list-principles`, `--principle N`.

For a quick single lookup, just run the script rather than parsing the markdown table by hand:
```bash
python3 /mnt/skills/.../triz/references/lookup.py 14 1
```
(adjust the path to wherever this skill is mounted).

## The core workflow

TRIZ's main contradiction-resolution path has six stages. Walk through them with the user rather than jumping straight to a principle — the translation steps (2 and 3) are where most of the value and most of the difficulty live.

### 1. Define the system and the problem in plain language
Name the technique/system, its main function, its key subsystems, and how it currently operates. Get concrete: what exactly happens, under what conditions, and what's unsatisfactory about it? This grounding step prevents the contradiction formulated in step 3 from being too abstract to act on.

### 2. Identify what should improve and what's getting worse
In the user's own terms first: "we want X to get better, but when we try, Y gets worse." If there's no obvious trade-off yet, ask what happens when they push the most obvious lever (more power, more material, faster cycle, etc.) — that's usually where the contradiction reveals itself.

### 3. Translate into the 39 generic Engineering Parameters
This is the step that takes practice. Map the *specific* improving property and the *specific* worsening property onto the nearest matching entries in `engineering_parameters.md`. Don't force an exact semantic match — TRIZ parameters are deliberately generic, so round to the closest fit. It's common and useful to formulate the *same* problem two or three different ways (different parameter choices) and check all of them against the matrix, since you don't know in advance which framing the matrix has good data for.

It's also worth formulating the contradiction in **both directions** — improving A worsens B, and separately, improving B worsens A — since the matrix is asymmetric and a row/column swap can surface different, sometimes better, principles.

### 4. Look up the Contradiction Matrix
Find the row for the improving parameter, the column for the worsening parameter. The cell gives (typically 1–4) Inventive Principle numbers, listed in decreasing order of how often that principle resolved this kind of contradiction in Altshuller's patent corpus. An empty cell means no principle was statistically dominant for that exact pairing — don't read this as "no solution exists," just reformulate with different parameters (back to step 3) or consider all 40 principles directly.

### 5. Apply each suggested principle
Read the full entry (including all sub-points, A/B/C/...) in `inventive_principles.md` for every number the matrix returned. Don't stop at the first plausible-sounding one — work through all of them, including the ones that don't obviously apply, since the principle is an abstract direction and the concrete translation is often non-obvious. If multiple contradictions were formulated in step 3, principles that show up across more than one formulation are usually the strongest leads — prioritize those.

### 6. Generate and evaluate concrete solutions
Translate each applied principle into an actual design change for the user's real system. Expect secondary problems to surface (the fix for the fix) — that's normal; either accept the trade as a net win, or treat the secondary problem as a new, smaller TRIZ pass.

## Working through this with the user

Default to **conversational, iterative use** of this workflow rather than producing one giant report. Ask what the improving/worsening properties are, propose a parameter translation, look up the matrix, and present the suggested principles with a few concrete interpretations for their system — then let them react before generating more. This mirrors how TRIZ is meant to be used: as a structured aid to *their* thinking, not an oracle that hands over a finished answer.

For genuinely complex, multi-part problems (the kind that would warrant assembling a small team of specialists in real life — e.g. a redesign touching mechanical, electrical, control-systems, and safety concerns at once), it's reasonable to work the problem in distinct passes from different domain angles: first characterize the system and its subsystems, then look at it from a mechanical-design lens, then a controls/safety lens, etc., synthesizing at the end. Treat this as switching analytical perspective within one continuous conversation, not as literally simulating separate personas — a single careful pass with deliberate perspective-switching outperforms a superficial pass per "agent."

## Physical contradictions (a different, sharper case)

Sometimes the same parameter needs to be at two different values simultaneously — not "A improves, B worsens" but "A must be both high and low" (e.g. a pile that needs a sharp tip to drive quickly but a blunt tip to support load under stress). This is a **physical contradiction**, and the Contradiction Matrix doesn't apply directly. Instead, resolve it with **separation principles**:

- **Separation in time** — have the property take one value at one time, the other value at another time (e.g. sharp during driving, then blunted by a separate mechanism for support).
- **Separation in space** — have different parts/locations of the object hold different values of the property simultaneously.
- **Separation on condition** — let the property change automatically in response to a changing condition (temperature, light, load), so no active control is needed. This is the most elegant resolution when it's available.
- **Separation between parts and the whole** — the whole has one property while its parts (or vice versa) have the opposing one.

When a user's problem is "X needs to be both A and not-A," reach for these instead of the matrix, and ask: do the conditions requiring A and not-A ever overlap in time? If not, separation in time is usually the simplest path in.

## A worked example, to calibrate scope

*"Our gantry crane needs to move loads fast for productivity, but moving fast causes dangerous load swing at the destination."* Translation: improving **Speed (9)** worsens **Stability of object (13)**. Matrix lookup → principles include Mechanics substitution (28), Homogeneity (33), Segmentation (1), and Mechanical vibration (18) — pointing toward directions like replacing pure mechanical damping with a sensor-driven active control system (28), or exploiting the crane's own oscillation frequency rather than fighting it (18), rather than just "go slower." That's the shape of a complete pass through this skill: concrete problem → parameter translation → matrix lookup → principle → concrete redesign idea.

## What this skill won't do well

TRIZ is a creativity *aid*, not an oracle — it narrows the search space and suggests directions, but a domain expert still has to do the work of turning a principle into a real design. Be upfront with the user that the matrix's suggestions are starting points for brainstorming, not validated solutions, and that combining 2–3 suggested principles often beats applying just one. Also be honest when a problem doesn't actually contain a hard contradiction — sometimes there's just an unexplored straightforward improvement, and reaching for the matrix would be over-engineering the conversation.
