import markdown
import pdfkit
import uuid
import os

def markdown_to_pdf(markdown_text: str) -> str | None:
    try:
        html = markdown.markdown(markdown_text, extensions=["fenced_code", "tables"])
        output_path = f"docs/auto_docs_{uuid.uuid4().hex[:6]}.pdf"
        pdfkit.from_string(html, output_path)
        return output_path
    except Exception as e:
        print("❌ PDF Export Error:", e)
        return None