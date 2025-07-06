import ast
import nbformat
import re
from typing import Dict, List, Optional

def extract_code_info(file_path: str) -> Optional[Dict]:
    """Extract code information from various programming language files."""
    try:
        with open(file_path, "r", encoding="utf-8") as f:
            source_code = f.read()
        
        file_extension = file_path.lower().split('.')[-1]
        
        if file_extension == 'py':
            return parse_python(source_code)
        elif file_extension in ['cpp', 'cc', 'cxx', 'hpp', 'h']:
            return parse_cpp(source_code)
        elif file_extension in ['java']:
            return parse_java(source_code)
        elif file_extension in ['js']:
            return parse_javascript(source_code)
        elif file_extension in ['ts', 'tsx']:
            return parse_typescript(source_code)
        elif file_extension in ['go']:
            return parse_go(source_code)
        elif file_extension in ['rs']:
            return parse_rust(source_code)
        elif file_extension in ['cs']:
            return parse_csharp(source_code)
        elif file_extension in ['php']:
            return parse_php(source_code)
        elif file_extension in ['rb']:
            return parse_ruby(source_code)
        elif file_extension in ['swift']:
            return parse_swift(source_code)
        elif file_extension in ['kt']:
            return parse_kotlin(source_code)
        elif file_extension in ['scala']:
            return parse_scala(source_code)
        else:
            # Generic parser for other languages
            return parse_generic(source_code)
            
    except Exception:
        return None

def parse_python(source_code: str) -> Dict:
    """Parse Python code using AST."""
    tree = ast.parse(source_code)
    functions = [node.name for node in ast.walk(tree) if isinstance(node, ast.FunctionDef)]
    classes = [node.name for node in ast.walk(tree) if isinstance(node, ast.ClassDef)]
    return {"code": source_code, "functions": functions, "classes": classes, "language": "Python"}

def parse_cpp(source_code: str) -> Dict:
    """Parse C++ code using regex patterns."""
    functions = []
    classes = []
    
    # Function patterns (simplified)
    func_patterns = [
        r'\w+\s+(\w+)\s*\([^)]*\)\s*\{',  # Basic function
        r'(\w+)\s*\([^)]*\)\s*\{',        # Function without return type
        r'(\w+)\s*::\s*(\w+)\s*\([^)]*\)\s*\{',  # Class method
    ]
    
    # Class patterns
    class_patterns = [
        r'class\s+(\w+)',
        r'struct\s+(\w+)',
        r'template\s*<[^>]*>\s*class\s+(\w+)',
    ]
    
    for pattern in func_patterns:
        matches = re.finditer(pattern, source_code, re.MULTILINE)
        for match in matches:
            if len(match.groups()) == 1:
                functions.append(match.group(1))
            elif len(match.groups()) == 2:
                functions.append(f"{match.group(1)}::{match.group(2)}")
    
    for pattern in class_patterns:
        matches = re.finditer(pattern, source_code, re.MULTILINE)
        for match in matches:
            classes.append(match.group(1))
    
    return {"code": source_code, "functions": list(set(functions)), "classes": list(set(classes)), "language": "C++"}

def parse_java(source_code: str) -> Dict:
    """Parse Java code using regex patterns."""
    functions = []
    classes = []
    
    # Method patterns
    method_patterns = [
        r'(?:public|private|protected|static|\s) +[\w\<\>\[\]]+\s+(\w+) *\([^\)]*\) *\{?[^\{]*\{',
        r'(\w+)\s*\([^)]*\)\s*\{',
    ]
    
    # Class patterns
    class_patterns = [
        r'class\s+(\w+)',
        r'public\s+class\s+(\w+)',
        r'interface\s+(\w+)',
        r'enum\s+(\w+)',
    ]
    
    for pattern in method_patterns:
        matches = re.finditer(pattern, source_code, re.MULTILINE)
        for match in matches:
            functions.append(match.group(1))
    
    for pattern in class_patterns:
        matches = re.finditer(pattern, source_code, re.MULTILINE)
        for match in matches:
            classes.append(match.group(1))
    
    return {"code": source_code, "functions": list(set(functions)), "classes": list(set(classes)), "language": "Java"}

def parse_javascript(source_code: str) -> Dict:
    """Parse JavaScript code using regex patterns."""
    functions = []
    classes = []
    
    # Function patterns
    func_patterns = [
        r'function\s+(\w+)\s*\(',
        r'const\s+(\w+)\s*=\s*\([^)]*\)\s*=>',
        r'let\s+(\w+)\s*=\s*\([^)]*\)\s*=>',
        r'var\s+(\w+)\s*=\s*\([^)]*\)\s*=>',
        r'(\w+)\s*:\s*function\s*\(',
        r'(\w+)\s*\([^)]*\)\s*\{',
    ]
    
    # Class patterns
    class_patterns = [
        r'class\s+(\w+)',
    ]
    
    for pattern in func_patterns:
        matches = re.finditer(pattern, source_code, re.MULTILINE)
        for match in matches:
            functions.append(match.group(1))
    
    for pattern in class_patterns:
        matches = re.finditer(pattern, source_code, re.MULTILINE)
        for match in matches:
            classes.append(match.group(1))
    
    return {"code": source_code, "functions": list(set(functions)), "classes": list(set(classes)), "language": "JavaScript"}

def parse_typescript(source_code: str) -> Dict:
    """Parse TypeScript code using regex patterns."""
    functions = []
    classes = []
    interfaces = []
    
    # Function patterns (including TypeScript specific)
    func_patterns = [
        r'function\s+(\w+)\s*\(',
        r'const\s+(\w+)\s*:\s*[^=]*=\s*\([^)]*\)\s*=>',
        r'let\s+(\w+)\s*:\s*[^=]*=\s*\([^)]*\)\s*=>',
        r'(\w+)\s*\([^)]*\)\s*:\s*[^{]*\{',
    ]
    
    # Class and interface patterns
    class_patterns = [
        r'class\s+(\w+)',
        r'interface\s+(\w+)',
        r'type\s+(\w+)\s*=',
    ]
    
    for pattern in func_patterns:
        matches = re.finditer(pattern, source_code, re.MULTILINE)
        for match in matches:
            functions.append(match.group(1))
    
    for pattern in class_patterns:
        matches = re.finditer(pattern, source_code, re.MULTILINE)
        for match in matches:
            if 'interface' in pattern:
                interfaces.append(match.group(1))
            elif 'type' in pattern:
                classes.append(match.group(1))
            else:
                classes.append(match.group(1))
    
    return {
        "code": source_code, 
        "functions": list(set(functions)), 
        "classes": list(set(classes)), 
        "interfaces": list(set(interfaces)),
        "language": "TypeScript"
    }

def parse_go(source_code: str) -> Dict:
    """Parse Go code using regex patterns."""
    functions = []
    structs = []
    
    # Function patterns
    func_patterns = [
        r'func\s+(\w+)\s*\(',
        r'func\s*\([^)]*\)\s*(\w+)\s*\(',
    ]
    
    # Struct patterns
    struct_patterns = [
        r'type\s+(\w+)\s+struct',
    ]
    
    for pattern in func_patterns:
        matches = re.finditer(pattern, source_code, re.MULTILINE)
        for match in matches:
            functions.append(match.group(1))
    
    for pattern in struct_patterns:
        matches = re.finditer(pattern, source_code, re.MULTILINE)
        for match in matches:
            structs.append(match.group(1))
    
    return {"code": source_code, "functions": list(set(functions)), "classes": list(set(structs)), "language": "Go"}

def parse_rust(source_code: str) -> Dict:
    """Parse Rust code using regex patterns."""
    functions = []
    structs = []
    traits = []
    
    # Function patterns
    func_patterns = [
        r'fn\s+(\w+)\s*\(',
        r'impl\s+[^{]*\{\s*fn\s+(\w+)\s*\(',
    ]
    
    # Struct and trait patterns
    struct_patterns = [
        r'struct\s+(\w+)',
        r'trait\s+(\w+)',
    ]
    
    for pattern in func_patterns:
        matches = re.finditer(pattern, source_code, re.MULTILINE)
        for match in matches:
            functions.append(match.group(1))
    
    for pattern in struct_patterns:
        matches = re.finditer(pattern, source_code, re.MULTILINE)
        for match in matches:
            if 'trait' in pattern:
                traits.append(match.group(1))
            else:
                structs.append(match.group(1))
    
    return {
        "code": source_code, 
        "functions": list(set(functions)), 
        "classes": list(set(structs)), 
        "traits": list(set(traits)),
        "language": "Rust"
    }

def parse_csharp(source_code: str) -> Dict:
    """Parse C# code using regex patterns."""
    functions = []
    classes = []
    
    # Method patterns
    method_patterns = [
        r'(?:public|private|protected|internal|\s) +[\w\<\>\[\]]+\s+(\w+)\s*\([^\)]*\)\s*\{',
        r'(\w+)\s*\([^)]*\)\s*\{',
    ]
    
    # Class patterns
    class_patterns = [
        r'class\s+(\w+)',
        r'public\s+class\s+(\w+)',
        r'interface\s+(\w+)',
        r'struct\s+(\w+)',
    ]
    
    for pattern in method_patterns:
        matches = re.finditer(pattern, source_code, re.MULTILINE)
        for match in matches:
            functions.append(match.group(1))
    
    for pattern in class_patterns:
        matches = re.finditer(pattern, source_code, re.MULTILINE)
        for match in matches:
            classes.append(match.group(1))
    
    return {"code": source_code, "functions": list(set(functions)), "classes": list(set(classes)), "language": "C#"}

def parse_php(source_code: str) -> Dict:
    """Parse PHP code using regex patterns."""
    functions = []
    classes = []
    
    # Function patterns
    func_patterns = [
        r'function\s+(\w+)\s*\(',
        r'public\s+function\s+(\w+)\s*\(',
        r'private\s+function\s+(\w+)\s*\(',
        r'protected\s+function\s+(\w+)\s*\(',
    ]
    
    # Class patterns
    class_patterns = [
        r'class\s+(\w+)',
        r'interface\s+(\w+)',
        r'trait\s+(\w+)',
    ]
    
    for pattern in func_patterns:
        matches = re.finditer(pattern, source_code, re.MULTILINE)
        for match in matches:
            functions.append(match.group(1))
    
    for pattern in class_patterns:
        matches = re.finditer(pattern, source_code, re.MULTILINE)
        for match in matches:
            classes.append(match.group(1))
    
    return {"code": source_code, "functions": list(set(functions)), "classes": list(set(classes)), "language": "PHP"}

def parse_ruby(source_code: str) -> Dict:
    """Parse Ruby code using regex patterns."""
    functions = []
    classes = []
    
    # Method patterns
    method_patterns = [
        r'def\s+(\w+)',
        r'def\s+self\.(\w+)',
    ]
    
    # Class patterns
    class_patterns = [
        r'class\s+(\w+)',
        r'module\s+(\w+)',
    ]
    
    for pattern in method_patterns:
        matches = re.finditer(pattern, source_code, re.MULTILINE)
        for match in matches:
            functions.append(match.group(1))
    
    for pattern in class_patterns:
        matches = re.finditer(pattern, source_code, re.MULTILINE)
        for match in matches:
            classes.append(match.group(1))
    
    return {"code": source_code, "functions": list(set(functions)), "classes": list(set(classes)), "language": "Ruby"}

def parse_swift(source_code: str) -> Dict:
    """Parse Swift code using regex patterns."""
    functions = []
    classes = []
    
    # Function patterns
    func_patterns = [
        r'func\s+(\w+)\s*\(',
        r'static\s+func\s+(\w+)\s*\(',
    ]
    
    # Class patterns
    class_patterns = [
        r'class\s+(\w+)',
        r'struct\s+(\w+)',
        r'enum\s+(\w+)',
        r'protocol\s+(\w+)',
    ]
    
    for pattern in func_patterns:
        matches = re.finditer(pattern, source_code, re.MULTILINE)
        for match in matches:
            functions.append(match.group(1))
    
    for pattern in class_patterns:
        matches = re.finditer(pattern, source_code, re.MULTILINE)
        for match in matches:
            classes.append(match.group(1))
    
    return {"code": source_code, "functions": list(set(functions)), "classes": list(set(classes)), "language": "Swift"}

def parse_kotlin(source_code: str) -> Dict:
    """Parse Kotlin code using regex patterns."""
    functions = []
    classes = []
    
    # Function patterns
    func_patterns = [
        r'fun\s+(\w+)\s*\(',
        r'fun\s+[^)]*\)\s*:\s*[^{]*\{',
    ]
    
    # Class patterns
    class_patterns = [
        r'class\s+(\w+)',
        r'interface\s+(\w+)',
        r'object\s+(\w+)',
    ]
    
    for pattern in func_patterns:
        matches = re.finditer(pattern, source_code, re.MULTILINE)
        for match in matches:
            functions.append(match.group(1))
    
    for pattern in class_patterns:
        matches = re.finditer(pattern, source_code, re.MULTILINE)
        for match in matches:
            classes.append(match.group(1))
    
    return {"code": source_code, "functions": list(set(functions)), "classes": list(set(classes)), "language": "Kotlin"}

def parse_scala(source_code: str) -> Dict:
    """Parse Scala code using regex patterns."""
    functions = []
    classes = []
    
    # Function patterns
    func_patterns = [
        r'def\s+(\w+)\s*\(',
        r'def\s+(\w+)\s*:',
    ]
    
    # Class patterns
    class_patterns = [
        r'class\s+(\w+)',
        r'trait\s+(\w+)',
        r'object\s+(\w+)',
    ]
    
    for pattern in func_patterns:
        matches = re.finditer(pattern, source_code, re.MULTILINE)
        for match in matches:
            functions.append(match.group(1))
    
    for pattern in class_patterns:
        matches = re.finditer(pattern, source_code, re.MULTILINE)
        for match in matches:
            classes.append(match.group(1))
    
    return {"code": source_code, "functions": list(set(functions)), "classes": list(set(classes)), "language": "Scala"}

def parse_generic(source_code: str) -> Dict:
    """Generic parser for unsupported languages."""
    return {"code": source_code, "functions": [], "classes": [], "language": "Unknown"}

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

def get_supported_extensions() -> List[str]:
    """Get list of supported file extensions."""
    return [
        '.py', '.ipynb',  # Python
        '.cpp', '.cc', '.cxx', '.hpp', '.h',  # C++
        '.java',  # Java
        '.js', '.jsx',  # JavaScript
        '.ts', '.tsx',  # TypeScript
        '.go',  # Go
        '.rs',  # Rust
        '.cs',  # C#
        '.php',  # PHP
        '.rb',  # Ruby
        '.swift',  # Swift
        '.kt',  # Kotlin
        '.scala',  # Scala
    ]