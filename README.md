# 📄 AutoDocs — AI-Powered Multi-Language Code Documentation

> **Automatically generate comprehensive documentation for your codebase using AI agents, supporting 12+ programming languages.**

[![Python](https://img.shields.io/badge/Python-3.8+-blue.svg)](https://python.org)
[![Streamlit](https://img.shields.io/badge/Streamlit-1.46+-red.svg)](https://streamlit.io)
[![License](https://img.shields.io/badge/License-MIT-green.svg)](LICENSE)

## 🌟 Features

### 🤖 **AI-Powered Documentation**
- **Three specialized AI agents** analyze your code from different perspectives:
  - **🧠 Architect Agent**: High-level architecture and design patterns
  - **👨‍💻 Developer Agent**: Technical implementation details and logic flow
  - **👤 User Agent**: Simple explanations for non-developers

### 🌍 **Multi-Language Support**
Supports **12+ programming languages** with language-specific parsing:

| Language | Extensions | Special Features |
|----------|------------|------------------|
| **Python** | `.py`, `.ipynb` | AST parsing, Jupyter notebooks |
| **C++** | `.cpp`, `.cc`, `.cxx`, `.hpp`, `.h` | Classes, templates, namespaces |
| **Java** | `.java` | Classes, interfaces, enums |
| **JavaScript** | `.js`, `.jsx` | Functions, classes, React components |
| **TypeScript** | `.ts`, `.tsx` | Interfaces, types, React components |
| **Go** | `.go` | Functions, structs, methods |
| **Rust** | `.rs` | Functions, structs, traits |
| **C#** | `.cs` | Classes, interfaces, structs |
| **PHP** | `.php` | Functions, classes, traits |
| **Ruby** | `.rb` | Methods, classes, modules |
| **Swift** | `.swift` | Functions, classes, protocols |
| **Kotlin** | `.kt` | Functions, classes, interfaces |
| **Scala** | `.scala` | Functions, classes, traits |

### 🎯 **Smart Features**
- **Language Filtering**: Select which programming languages to process
- **GitHub Integration**: Clone and analyze public repositories directly
- **Export Options**: Generate Markdown and PDF documentation
- **Session Management**: Persistent state across app interactions
- **Real-time Processing**: Live documentation generation

## 🚀 Quick Start

### Prerequisites
- Python 3.8 or higher
- Git (for GitHub repository cloning)

### Installation

1. **Clone the repository**
   ```bash
   git clone https://github.com/jainakshat30/AutoDocs.git
   cd AutoDocs
   ```

2. **Create a virtual environment**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies**
   ```bash
   pip install -r requirements.txt
   ```

4. **Set up environment variables**
   ```bash
   # Create a .env file and add your OpenAI API key
   echo "OPENAI_API_KEY=your_api_key_here" > .env
   ```

5. **Run the application**
   ```bash
   streamlit run app.py
   ```

The app will open in your browser at `http://localhost:8501`

## 📖 Usage

### Method 1: Upload ZIP File
1. **Prepare your project**: Zip your codebase containing supported file types
2. **Upload**: Drag and drop or select your ZIP file
3. **Filter languages** (optional): Select which programming languages to process
4. **Generate**: Click to start AI-powered documentation generation
5. **Export**: Download as Markdown or PDF

### Method 2: GitHub Repository
1. **Enter repository URL**: Paste a public GitHub repository URL
2. **Clone and analyze**: The app will automatically clone and process the repository
3. **Review documentation**: Browse through AI-generated insights
4. **Export**: Save documentation in your preferred format

## 🏗️ Project Structure

```
autodocs/
├── app.py                 # Main Streamlit application
├── agents/               # AI agent implementations
│   ├── base_agent.py     # Base agent class
│   ├── architect.py      # Architecture analysis agent
│   ├── developer.py      # Technical implementation agent
│   └── user.py          # User-friendly explanation agent
├── utils/               # Utility modules
│   ├── code_parser.py   # Multi-language code parsing
│   ├── llm_wrapper.py   # OpenAI API integration
│   └── pdf_exporter.py  # PDF generation utilities
├── docs/               # Generated documentation output
├── requirements.txt    # Python dependencies
└── README.md          # This file
```

## 🔧 Configuration

### Environment Variables
Create a `.env` file in the project root:

```env
OPENAI_API_KEY=your_openai_api_key_here
```

### Supported File Extensions
The application automatically detects and processes files with these extensions:
- **Python**: `.py`, `.ipynb`
- **C++**: `.cpp`, `.cc`, `.cxx`, `.hpp`, `.h`
- **Java**: `.java`
- **JavaScript**: `.js`, `.jsx`
- **TypeScript**: `.ts`, `.tsx`
- **Go**: `.go`
- **Rust**: `.rs`
- **C#**: `.cs`
- **PHP**: `.php`
- **Ruby**: `.rb`
- **Swift**: `.swift`
- **Kotlin**: `.kt`
- **Scala**: `.scala`

## 🎨 Features in Detail

### AI Agent Analysis

#### 🧠 **Architect Agent**
- Analyzes code structure and architecture
- Identifies design patterns and organizational principles
- Examines component relationships and responsibilities
- Provides high-level architectural insights

#### 👨‍💻 **Developer Agent**
- Explains technical implementation details
- Describes function logic and data flow
- Identifies edge cases and potential issues
- Mentions relevant libraries and APIs

#### 👤 **User Agent**
- Provides simple, non-technical explanations
- Uses analogies and everyday language
- Makes code understandable to non-developers
- Explains language-specific concepts in simple terms

### Language-Specific Features

#### **TypeScript Support**
- Interface detection and documentation
- Type definitions analysis
- React component documentation

#### **Rust Support**
- Trait implementation analysis
- Struct and enum documentation
- Ownership and borrowing patterns

#### **Go Support**
- Struct and method documentation
- Package organization analysis
- Goroutine and channel patterns

## 📊 Example Output

### Generated Documentation Structure
```
📄 main.py (Python)
├── 🧠 Architect Agent
│   └── High-level architecture analysis
├── 👨‍💻 Developer Agent
│   └── Technical implementation details
└── 👤 User Agent
    └── Simple, non-technical explanation

📄 Calculator.ts (TypeScript)
├── 🧠 Architect Agent
│   └── Interface and class design analysis
├── 👨‍💻 Developer Agent
│   └── Type safety and method implementation
└── 👤 User Agent
    └── Simple explanation of calculator functionality
```

## 🤝 Contributing

We welcome contributions! Here's how you can help:

1. **Fork the repository**
2. **Create a feature branch**: `git checkout -b feature/amazing-feature`
3. **Commit your changes**: `git commit -m 'Add amazing feature'`
4. **Push to the branch**: `git push origin feature/amazing-feature`
5. **Open a Pull Request**

### Adding New Languages
To add support for a new programming language:

1. **Add parser function** in `utils/code_parser.py`
2. **Update file extensions** in `get_supported_extensions()`
3. **Add language mapping** in `app.py`
4. **Test with sample code**

