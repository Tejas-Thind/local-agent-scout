# Skill: extract companies from a hiring signal

This is the procedure the model follows for the `extract` stage. Claude writes
and refines this file; the local model executes it. Refine it against
evals/data/extract_labels.jsonl until the local model's accuracy converges.
This starter is deliberately simple. Tighten it where the eval shows failures.

## Task

Given the raw text of a "who's hiring" roundup or newsletter, return every
company mentioned as a structured row. Return only companies, ignore the
poster's commentary, hashtags, and calls to follow.

## Output

A JSON object matching:

```
{ "companies": [
    { "name": str,
      "stage": "pre-seed" | "seed" | "series a" | "series b" | "series c+" | null,
      "yc_batch": str | null,      // e.g. "W25", "S24", "P26"
      "founders": [str],           // names listed as leading / founding
      "roles": [str] }             // functions hiring, e.g. "GTM", "Engineering"
] }
```

## Rules

- Stage often comes from a section header (e.g. "Pre-seed / Seed"). Apply the
  header to every company under it until the next header.
- `yc_batch` is the parenthetical like "(YC W25)". Null if absent.
- `founders` are names after "Led by" / "founded by". Split multiple names.
- `roles` are the functions after "Hiring for". Split on commas.
- Do not invent fields. If something is not in the text, use null or an empty list.
- Do not include the person who wrote the post.

## Example

Input line:
`Edexia (YC W25) (Led by Daniel Gibbon, Nathan Wang) - Hiring for Partnership, GTM`

Output row:
```
{ "name": "Edexia", "stage": "seed", "yc_batch": "W25",
  "founders": ["Daniel Gibbon", "Nathan Wang"], "roles": ["Partnership", "GTM"] }
```
(stage "seed" because the line sat under the "Pre-seed / Seed" header)
