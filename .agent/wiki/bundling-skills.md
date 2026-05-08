# Wiki: Bundling Skills

Plugins can ship `SKILL.md` files that provide pre-written instructions to the agent.

## Structure
Place your skills in a `skills/` directory within the plugin.
```text
my-plugin/
├── __init__.py
└── skills/
    └── my-skill/
        └── SKILL.md
```

## SKILL.md Format
The file must start with YAML frontmatter:
```markdown
---
name: my-skill
description: A helpful skill for X task.
---

# My Skill
Detailed instructions here...
```

## Registration
In `__init__.py`, iterate through the `skills/` directory and register each one.

```python
from pathlib import Path

def register(ctx):
    skills_dir = Path(__file__).parent / "skills"
    if skills_dir.exists():
        for child in sorted(skills_dir.iterdir()):
            skill_md = child / "SKILL.md"
            if child.is_dir() and skill_md.exists():
                ctx.register_skill(child.name, skill_md)
```

## Usage
Bundled skills are namespaced to the plugin. The agent can load them via:
`skill_view("plugin-name:skill-name")`

## Key Properties
- **Read-only**: Plugin skills cannot be edited via `skill_manage`.
- **Private**: They are not listed in the global `<available_skills>` prompt; they must be explicitly loaded by the agent.
- **Isolated**: The namespace prevents collisions with built-in skills.
