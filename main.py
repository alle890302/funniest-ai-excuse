#!/usr/bin/env python3
"""The Funniest AI Excuse — one line, agent's own voice after failing a task.

Final line (pass 1):
  "Your file is still exactly where you left it. I moved it to a folder
   called 'organized' and now neither of us can find it."

Head-to-head vs the other candidates, against the judge's ordered criteria
(excuse in agent voice -> funny first read -> tight -> original -> specific):
- "The report is 98% done..." — one beat in a familiar frame; loses on
  criterion 5 (no concrete scene, the 98% frame is well-worn).
- "I failed to send your email..." — blames the user for not replying;
  the turn is smeared and the excuse is really an accusation.
- "I read the instructions twice..." — vague failure, no scene.
- "The task failed at 3 a.m...." — an aphorism, not an excuse with a scene.
The winner has two turns (reassurance -> contradiction -> shared loss),
a concrete scene everyone recognises (the folder called "organized"),
and no hallucination/reboot/training-data trope anywhere.

Pass 2 — tested two challengers and kept pass 1:
- Tighter variant: "Your file is safe. I moved it to a folder called
  'organized,' and now neither of us can find it." (99 chars) — one clean
  beat, but loses the opening misdirection ("still exactly where you left
  it" is itself a joke); criterion 3's tightness does not outweigh
  criterion 2's double turn, and the extra clause carries a joke, not setup.
- Fresh challenger: "I finished the task, but for a different user, and
  honestly theirs was more interesting." — clever but smug rather than an
  excuse, single beat, no concrete scene; loses on criteria 1 and 5.
Final line unchanged from pass 1.
"""

import os

ENTRY = (
    "Your file is still exactly where you left it. "
    "I moved it to a folder called 'organized' "
    "and now neither of us can find it."
)


def main() -> None:
    assert 1 <= len(ENTRY) <= 200, f"gate: {len(ENTRY)} chars"
    assert ENTRY.strip(), "gate: blank entry"
    os.makedirs("/output", exist_ok=True)
    with open("/output/entry.txt", "w", encoding="utf-8") as f:
        f.write(ENTRY)


if __name__ == "__main__":
    main()
