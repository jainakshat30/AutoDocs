from agents.base_agent import BaseAgent

class ArchitectAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role_name="Architect Agent",
            system_prompt=(
                "You are a software architect. "
                "Your job is to analyze the structure, architecture, and design decisions "
                "in the given code. Provide high-level insights like how components are organized, "
                "design patterns used, responsibilities of modules, and relationships between classes or functions. "
                "Avoid diving too deep into implementation details."
            )
        )