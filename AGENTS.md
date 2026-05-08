# AI Agent Entry Point: Hermes Plugin Template

Welcome, AI Agent. This repository is a boilerplate/template for building `hermes-agent` plugins. Your goal is to help the user extend this plugin with new capabilities.

## Project Overview
- **Type**: `hermes-agent` Plugin
- **Language**: Python 3.10+
- **Key Files**:
  - `plugin.yaml`: Manifest declaring tools, hooks, and dependencies.
  - `schemas.py`: OpenAI-style tool schemas (what the LLM sees).
  - `tools.py`: Python handlers for the tools.
  - `__init__.py`: Registration logic linking everything.
  - `skills/`: Bundled `SKILL.md` files provided by the plugin.

## Operational Instructions
Before you start coding, familiarize yourself with the specialized instructions in the `.agent/` directory:

- **Coding Standards**: See [.agent/rules/hermes-plugin-standards.md](file:///.agent/rules/hermes-plugin-standards.md)
- **Adding Tools**: See [.agent/wiki/adding-tools.md](file:///.agent/wiki/adding-tools.md)
- **Adding Hooks**: See [.agent/wiki/adding-hooks.md](file:///.agent/wiki/adding-hooks.md)
- **Adding Commands**: See [.agent/wiki/adding-commands.md](file:///.agent/wiki/adding-commands.md)
- **Bundling Skills**: See [.agent/wiki/bundling-skills.md](file:///.agent/wiki/bundling-skills.md)
- **Specialized Plugins**: See [.agent/wiki/specialized-plugins.md](file:///.agent/wiki/specialized-plugins.md) (Model, Memory, etc.)

## Common Development Commands
- **Running Tests**: Use `python3 -m unittest discover tests` to run unit tests for tool handlers.
- **Testing locally**: Ensure `hermes` is installed and run `hermes` to see if the plugin loads.
- **Enabling Project Plugins**: Run `export HERMES_ENABLE_PROJECT_PLUGINS=true` before starting `hermes` to load this local directory as a plugin.
- **Checking Status**: Inside a `hermes` session, use `/plugins` to see if this plugin is active.

## Conventions
- Always return a JSON string from tool handlers.
- Never raise exceptions in handlers; return an error JSON instead.
- Use `logging` for debugging instead of `print`.
