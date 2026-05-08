# Wiki: Adding Tools

This guide explains how to add a new tool to this Hermes plugin.

## Step 1: Define the Schema
In `schemas.py`, add a new dictionary defining your tool.

```python
MY_TOOL = {
    "name": "my_tool",
    "description": "Describe EXACTLY what this tool does and when to use it.",
    "parameters": {
        "type": "object",
        "properties": {
            "param1": {
                "type": "string",
                "description": "Description of the parameter",
            },
        },
        "required": ["param1"],
    },
}
```

## Step 2: Implement the Handler
In `tools.py`, write the Python function that executes the tool logic.

```python
import json

def my_tool(args: dict, **kwargs) -> str:
    param1 = args.get("param1")
    try:
        # Perform logic here
        result = f"Processed {param1}"
        return json.dumps({"success": True, "result": result})
    except Exception as e:
        return json.dumps({"success": False, "error": str(e)})
```

## Step 3: Register the Tool
In `__init__.py`, update the `register()` function.

```python
from . import schemas, tools

def register(ctx):
    ctx.register_tool(
        name="my_tool",
        toolset="my-plugin",
        schema=schemas.MY_TOOL,
        handler=tools.my_tool,
        # Optional: Hide tool if requirements aren't met
        check_fn=lambda: _has_dependencies() 
    )

def _has_dependencies():
    try:
        import some_optional_lib
        return True
    except ImportError:
        return False
```

## Step 4: Update the Manifest
In `plugin.yaml`, add your tool to the `provides_tools` list (optional but recommended for documentation).

```yaml
provides_tools:
  - my_tool
```

## Tips
- **Namespacing**: Use a consistent `toolset` name (usually the plugin name).
- **Context**: If you need access to the agent's context, check `kwargs`.
- **Testing**: Start Hermes with `HERMES_ENABLE_PROJECT_PLUGINS=true` and try to trigger the tool with a prompt.
- **Conditional Visibility**: Use `check_fn` to prevent the model from seeing a tool if its dependencies (libraries, API keys, etc.) are missing.
