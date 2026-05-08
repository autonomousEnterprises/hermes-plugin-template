# Hermes Plugin Standards

These are the invariant coding standards for building `hermes-agent` plugins.

## 1. Tool Handler Signatures
All tool handlers must follow this signature:
```python
def handler_name(args: dict, **kwargs) -> str:
    # args: contains the parameters passed by the LLM
    # kwargs: reserved for future framework context
    ...
    return json.dumps({"result": "..."})
```

## 2. Return Format
- **ALWAYS** return a JSON-encoded string.
- Even on error, return a JSON string with an `error` key.
- Never return `None`, `dict`, or raw objects directly.

## 3. Error Handling
- **Never raise exceptions** inside a tool handler.
- Use `try...except` blocks to catch all potential errors.
- Return errors as JSON: `{"error": "Specific error message"}`.

## 4. Message Injection
Plugins can inject messages into the active conversation using `ctx.inject_message()`.
```python
ctx.inject_message("Notification: Process complete.", role="user")
```
- **CLI Mode Only**: Returns `True` if queued, `False` if unavailable (e.g., gateway mode).
- **Idle**: Starts a new turn.
- **Mid-turn**: Interrupts the current operation.

## 5. Manifest (`plugin.yaml`)
Always include `name`, `version`, and `description`.

### Environment Variables (`requires_env`)
Use the rich format for a better installation experience:
```yaml
requires_env:
  - name: MY_API_KEY
    description: "API key for the MyService"
    url: "https://myservice.com/keys"
    secret: true # Hides input during prompt
```

## 6. Registration
- All registration must happen inside the `register(ctx)` function in `__init__.py`.
- Use `ctx.register_tool()`, `ctx.register_hook()`, `ctx.register_command()`, etc.

## 7. Performance & Safety
- Keep tool handlers efficient.
- Avoid long-blocking operations without timeouts.
- Do not access sensitive data outside the provided context or user-approved paths.
