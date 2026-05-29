from __future__ import annotations

from typing import Callable, Dict, Any


class ToolRegistry:
    def __init__(self):
        self._tools: Dict[str, Callable[..., Any]] = {}

    def register(self, name: str, function: Callable[..., Any]):
        self._tools[name] = function

    def call(self, name: str, **kwargs) -> Any:
        if name not in self._tools:
            raise KeyError(f"Tool '{name}' is not registered")
        return self._tools[name](**kwargs)

    def list_tools(self) -> list[str]:
        return sorted(self._tools.keys())
