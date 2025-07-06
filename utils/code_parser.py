import ast
import nbformat

def extract_code_info(file_path):
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            source_code = f.read()
        tree = ast.parse(source_code)
        functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
        classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
        return {"code": source_code, "functions": functions, "classes": classes}
    except Exception:
        return None

def extract_notebook_code(file_path):
    try:
        nb = nbformat.read(file_path, as_version=4)
        code = ""
        for cell in nb.cells:
            if cell.cell_type == "code":
                code += cell.source + "\n\n"
        return code.strip()
    except Exception:
        return None