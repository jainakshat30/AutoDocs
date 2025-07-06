from agents.base_agent import BaseAgent

class UserAgent(BaseAgent):
    def __init__(self):
        super().__init__(
            role_name="User Agent",
            system_prompt=(
                "You are a helpful assistant explaining the code to someone with basic or no programming knowledge. "
                "Summarize what the code is trying to do in simple language. "
                "Avoid technical jargon. Use analogies or everyday language when possible. "
                "The goal is to make the code understandable to non-developers or beginners."
            )
        )