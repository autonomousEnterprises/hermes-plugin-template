# Wiki: Specialized Plugins

Beyond general plugins (tools and hooks), Hermes supports specialized plugin types for core framework extension.

## 1. Model Provider Plugins
Used to add new LLM backends (e.g., a new proprietary API).
- **Location**: `plugins/model-providers/<name>/`
- **Key API**: `register_provider(ProviderProfile(...))`
- **Manifest**: `kind: model-provider`

## 2. Platform Plugins (Gateways)
Used to add new chat platforms (Discord, Telegram, etc.).
- **Location**: `plugins/platforms/<name>/`
- **Key API**: Subclass `BasePlatformAdapter` and `ctx.register_platform()`.
- **Manifest**: `kind: platform`

## 3. Memory Provider Plugins
Used to replace the cross-session knowledge backend.
- **Location**: `plugins/memory/<name>/`
- **Key API**: Subclass `MemoryProvider`.
- **Discovery**: Uses its own loader; selected via `memory.provider` in config.

## 4. Context Engine Plugins
Used to replace the context-compression strategy.
- **Location**: `plugins/context_engine/<name>/`
- **Key API**: `ctx.register_context_engine()`.

---

**Note**: This repository is optimized for **General Plugins**. If you need to build a specialized provider, refer to the full [Developer Guide](https://hermes-agent.nousresearch.com/docs/developer-guide/model-provider-plugin).
