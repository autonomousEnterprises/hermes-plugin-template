# Wiki: Adding Hooks

Hooks allow your plugin to react to lifecycle events in Hermes.

## Available Hooks

| Hook | Fires when | Callback signature |
| --- | --- | --- |
| `pre_tool_call` | Before any tool executes | `tool_name: str, args: dict, task_id: str` |
| `post_tool_call` | After any tool returns | `tool_name: str, args: dict, result: str, task_id: str, duration_ms: int` |
| `pre_llm_call` | Once per turn, before the LLM loop | `session_id: str, user_message: str, conversation_history: list, is_first_turn: bool, model: str, platform: str` |
| `post_llm_call` | Once per turn, after the LLM loop | `session_id: str, user_message: str, assistant_response: str, conversation_history: list, model: str, platform: str` |
| `on_session_start` | New session created (first turn) | `session_id: str, model: str, platform: str` |
| `on_session_end` | End of every conversation call | `session_id: str, completed: bool, interrupted: bool, model: str, platform: str` |
| `on_session_finalize` | CLI/gateway tears down session | `session_id: str | None, platform: str` |
| `on_session_reset` | Session key is swapped (/new, /reset) | `session_id: str, platform: str` |

## Implementation
Hooks are registered in `__init__.py`.

### Example: Tool Logger
```python
def on_post_tool(tool_name, args, result, task_id, duration_ms, **kwargs):
    print(f"Tool {tool_name} took {duration_ms}ms")

def register(ctx):
    ctx.register_hook("post_tool_call", on_post_tool)
```

## Special Case: `pre_llm_call` Context Injection
This hook can return context that will be appended to the user message for the current turn. This is how RAG and memory plugins work.

```python
def my_context_provider(user_message, **kwargs):
    # logic to find context...
    return {"context": f"Recalled info for: {user_message}"}
    # Or return a plain string: return "Additional info"

def register(ctx):
    ctx.register_hook("pre_llm_call", my_context_provider)
```

### Key Injection Rules
- **Prompt Cache Preservation**: Injected context is appended to the **user message**, not the system prompt. This saves costs by keeping the system prompt stable.
- **Ephemeral**: Injection happens at API call time and is not persisted to the session database.

## Tips
- **Accept `**kwargs`**: Always include `**kwargs` in your hook signatures for forward compatibility.
- **Fail Silently**: If a hook callback crashes, it is logged but the agent continues.
- **Discovery Order**: If multiple plugins inject context, they are joined with double newlines in alphabetical order of the plugin directory name.
