# Wiki: Adding Commands

Plugins can add slash commands (in-session) and CLI subcommands.

## 1. Slash Commands
Slash commands are typed by the user during a conversation (e.g., `/mystatus`).

### Implementation
In `__init__.py`:
```python
def handle_mystatus(raw_args: str) -> str:
    return f"Status: all systems nominal. Args: {raw_args}"

def register(ctx):
    ctx.register_command(
        name="mystatus",
        handler=handle_mystatus,
        description="Show plugin status"
    )
```

## 2. CLI Subcommands
CLI subcommands are run from the terminal (e.g., `hermes my-plugin status`).

### Implementation
In `__init__.py`:
```python
def my_cli_handler(args):
    if args.subcommand == "status":
        print("OK")

def setup_argparse(subparser):
    subs = subparser.add_subparsers(dest="subcommand")
    subs.add_parser("status", help="Show status")
    subparser.set_defaults(func=my_cli_handler)

def register(ctx):
    ctx.register_cli_command(
        name="my-plugin",
        help="Manage my plugin",
        setup_fn=setup_argparse,
        handler_fn=my_cli_handler
    )
```

## 3. Dispatching Tools from Commands
If a command needs to run a tool as if the LLM called it:
```python
def handle_do_it(ctx, raw_args):
    result = ctx.dispatch_tool("terminal", {"command": f"echo {raw_args}"})
    return result
```

## Comparison
| | Slash Command | CLI Subcommand |
| --- | --- | --- |
| **Invoked as** | `/command` in session | `hermes command` in terminal |
| **Context** | CLI, Telegram, Discord, etc. | Terminal only |
| **Arguments** | Raw string | argparse Namespace |
