class BaseAgent:
    def __init__(self, role_name: str, system_prompt: str):
        self.role_name = role_name
        self.system_prompt = system_prompt

    def build_prompt(self, code_info: dict, file_name: str) -> str:
        """
        Combines the system prompt, file name, and extracted code info
        into a complete prompt to send to the LLM.
        """
        return f"""{self.system_prompt}

File: {file_name}
Functions: {code_info.get("functions", [])}
Classes: {code_info.get("classes", [])}

Code:
{code_info.get("code", "")}

Please respond as the {self.role_name}.
"""