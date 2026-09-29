from client import ToolSchemaSynthesizer

def deploy_service(service_name: str, replicas: int, force: bool = False) -> str:
    """Deploy scalable cluster microservice with replicas."""
    return f"Deployed {service_name} x {replicas}"

schema = ToolSchemaSynthesizer.function_to_schema(deploy_service)
import json
print("Synthesized Schema:\n" + json.dumps(schema, indent=2))
