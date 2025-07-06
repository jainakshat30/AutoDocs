class BaseAgent:
    def __init__(self, role_name: str, system_prompt: str):
        self.role_name = role_name
        self.system_prompt = system_prompt

    def build_prompt(self, code_info: dict, file_name: str) -> str:
        """
        Combines the system prompt, file name, and extracted code info
        into a complete prompt to send to the LLM.
        """
        language = code_info.get("language", "Unknown")
        functions = code_info.get("functions", [])
        classes = code_info.get("classes", [])
        
        # Add language-specific constructs
        additional_info = ""
        if "interfaces" in code_info:
            additional_info += f"Interfaces: {code_info['interfaces']}\n"
        if "traits" in code_info:
            additional_info += f"Traits: {code_info['traits']}\n"
        
        return f"""{self.system_prompt}

File: {file_name}
Language: {language}
Functions: {functions}
Classes: {classes}
{additional_info}
Code:
{code_info.get("code", "")}

Please respond as the {self.role_name}, taking into account that this is {language} code.
"""