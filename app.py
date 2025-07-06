import streamlit as st
import zipfile
import os
import shutil
import uuid
from git import Repo

from utils.code_parser import extract_code_info, extract_notebook_code
from utils.llm_wrapper import get_doc_from_llm
from utils.pdf_exporter import markdown_to_pdf
from agents.architect import ArchitectAgent
from agents.developer import DeveloperAgent
from agents.user import UserAgent

st.set_page_config(page_title="AutoDocs 🔍", layout="wide")
st.title("📄 AutoDocs — AI-Powered Code Documentation")
st.markdown("> Upload a `.zip` of your project or clone a public GitHub repo.\n\nSupports `.py` and `.ipynb` files.")

agents = [ArchitectAgent(), DeveloperAgent(), UserAgent()]
docs = {}

# --- Zip Upload ---
uploaded_file = st.file_uploader("📦 Upload a .zip of your Python project", type="zip")

if uploaded_file:
    temp_dir = "temp_code"
    if os.path.exists(temp_dir):
        shutil.rmtree(temp_dir)
    os.makedirs(temp_dir, exist_ok=True)

    with zipfile.ZipFile(uploaded_file, 'r') as zip_ref:
        zip_ref.extractall(temp_dir)

    st.success("✅ Code extracted successfully!")

    with st.spinner("🧠 Generating documentation using AI agents..."):
        for root, dirs, files in os.walk(temp_dir):
            for file in files:
                if not (file.endswith(".py") or file.endswith(".ipynb")):
                    continue

                path = os.path.join(root, file)
                code_info = None

                if file.endswith(".py"):
                    code_info = extract_code_info(path)
                elif file.endswith(".ipynb"):
                    code = extract_notebook_code(path)
                    if code:
                        code_info = {"code": code, "functions": [], "classes": []}

                if not code_info:
                    continue

                file_doc = {}
                for agent in agents:
                    prompt = agent.build_prompt(code_info, file)
                    doc = get_doc_from_llm(prompt)
                    file_doc[agent.role_name] = doc

                docs[file] = file_doc

    st.success("📚 Documentation generated!")

    for file_name, agent_docs in docs.items():
        st.subheader(f"📄 {file_name}")
        for role, content in agent_docs.items():
            with st.expander(f"🧠 {role}"):
                st.markdown(content)

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("💾 Export to Markdown"):
            os.makedirs("docs", exist_ok=True)
            with open("docs/auto_docs.md", "w", encoding="utf-8") as f:
                for file_name, agent_docs in docs.items():
                    f.write(f"\n\n### {file_name}\n")
                    for role, content in agent_docs.items():
                        f.write(f"\n#### {role}\n{content}\n")
            st.success("✅ Saved to docs/auto_docs.md")

            with open("docs/auto_docs.md", "r", encoding="utf-8") as f_md:
                md = f_md.read()
            pdf_path = markdown_to_pdf(md)
            if pdf_path and os.path.exists(pdf_path):
                with open(pdf_path, "rb") as f_pdf:
                    st.download_button(
                        label="📄 Download PDF",
                        data=f_pdf,
                        file_name="AutoDocs_Report.pdf",
                        mime="application/pdf"
                    )
                st.success("✅ PDF generated and ready to download!")
            else:
                st.error("❌ Failed to generate PDF.")


# --- GitHub Clone Section ---
st.markdown("---")
st.subheader("🐙 Clone a GitHub Python Repo Instead")
repo_url = st.text_input("🔗 Paste public GitHub repo URL")
use_repo = st.button("⬇️ Clone and Generate Docs")

# Initialize session state for docs
if 'docs' not in st.session_state:
    st.session_state.docs = {}

if use_repo and repo_url:
    temp_repo_dir = f"temp_repo_{uuid.uuid4().hex[:6]}"
    try:
        with st.spinner("📥 Cloning repo..."):
            Repo.clone_from(repo_url, temp_repo_dir)
        st.success("✅ Repo cloned!")

        docs = {}
        with st.spinner("🧠 Generating documentation using AI agents..."):
            for root, dirs, files in os.walk(temp_repo_dir):
                for file in files:
                    if not (file.endswith(".py") or file.endswith(".ipynb")):
                        continue

                    path = os.path.join(root, file)
                    code_info = None

                    if file.endswith(".py"):
                        code_info = extract_code_info(path)
                    elif file.endswith(".ipynb"):
                        notebook_code = extract_notebook_code(path)
                        if notebook_code:
                            code_info = {"code": notebook_code, "functions": [], "classes": []}

                    if not code_info:
                        continue

                    file_doc = {}
                    for agent in agents:
                        prompt = agent.build_prompt(code_info, file)
                        doc = get_doc_from_llm(prompt)
                        file_doc[agent.role_name] = doc
                    docs[file] = file_doc

        # Store docs in session state
        st.session_state.docs = docs
        st.success("📚 Documentation generated!")

        st.header("🧾 Documentation Preview")

        for file_name, agent_docs in docs.items():
            st.subheader(f"📄 `{file_name}`")
            for role, content in agent_docs.items():
                with st.expander(f"🧠 {role} Agent"):
                    st.markdown(content)

    except Exception as e:
        st.error(f"❌ Failed to clone repository: {str(e)}")
        if os.path.exists(temp_repo_dir):
            shutil.rmtree(temp_repo_dir)

# Show docs preview and export buttons if docs exist
if st.session_state.docs:
    st.markdown("---")
    st.markdown("### ✅ All docs generated! Click below to export:")

    col1, col2, col3 = st.columns([1, 2, 1])
    with col2:
        if st.button("💾 Export to Markdown"):
            os.makedirs("docs", exist_ok=True)
            with open("docs/auto_docs.md", "w", encoding="utf-8") as f:
                for file_name, agent_docs in st.session_state.docs.items():
                    f.write(f"\n\n### {file_name}\n")
                    for role, content in agent_docs.items():
                        f.write(f"\n#### {role}\n{content}\n")
            st.success("✅ Saved to docs/auto_docs.md")

    # Always show the Export to PDF button if markdown exists
    if os.path.exists("docs/auto_docs.md"):
        with open("docs/auto_docs.md", "r", encoding="utf-8") as f_md:
            md = f_md.read()

        st.markdown("---")
        st.subheader("📄 Export Markdown to PDF")

        col1, col2, col3 = st.columns([1, 2, 1])
        with col2:
            if st.button("📄 Export to PDF"):
                pdf_path = markdown_to_pdf(md)
                if pdf_path and os.path.exists(pdf_path):
                    with open(pdf_path, "rb") as f_pdf:
                        st.download_button(
                            label="⬇️ Download PDF",
                            data=f_pdf,
                            file_name="AutoDocs_Report.pdf",
                            mime="application/pdf"
                        )
                    st.success("✅ PDF generated and ready to download!")
                else:
                    st.error("❌ Failed to generate PDF.")