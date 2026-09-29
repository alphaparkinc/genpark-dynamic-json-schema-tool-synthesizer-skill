"""Dynamic JSON Schema Tool Synthesizer.
100% Python Standard Library.
"""

import inspect

class ToolSchemaSynthesizer:
    """Inspects Python callables and generates compliant MCP tool definitions and JSON schemas."""
    @staticmethod
    def function_to_schema(fn):
        sig = inspect.signature(fn)
        doc = inspect.getdoc(fn) or "No description provided."
        type_mapping = {int: "integer", float: "number", str: "string", bool: "boolean", list: "array", dict: "object"}
        properties = {}
        required = []
        for name, param in sig.parameters.items():
            ann = param.annotation
            json_type = type_mapping.get(ann, "string")
            properties[name] = {"type": json_type, "description": f"Parameter {name}"}
            if param.default is inspect.Parameter.empty:
                required.append(name)
        return {
            "name": fn.__name__,
            "description": doc.split("\n")[0],
            "inputSchema": {
                "type": "object",
                "properties": properties,
                "required": required
            }
        }
