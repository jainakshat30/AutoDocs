import os
from dotenv import load_dotenv
from openai import OpenAI
import streamlit as st

load_dotenv()



api_key = st.secrets["OPENROUTER_API_KEY"]
if api_key is None:
    raise ValueError("Missing OPENROUTER_API_KEY in secrets")


api_key = os.getenv("OPENROUTER_API_KEY")
if api_key is None:
    raise ValueError("Missing OPENROUTER_API_KEY in .env")

client = OpenAI(
    api_key=api_key,
    base_url="https://openrouter.ai/api/v1"
)

def get_doc_from_llm(prompt: str) -> str:
    try:
        response = client.chat.completions.create(
            model="mistralai/mistral-7b-instruct",
            messages=[{"role": "user", "content": prompt}],
            temperature=0.4,
            max_tokens=1024
        )

        # ✅ Defensive check for type checker and runtime safety
        first_choice = response.choices[0]
        message = getattr(first_choice, "message", None)

        if message and hasattr(message, "content"):
            return message.content or "⚠️ No content in LLM response."

        return "⚠️ LLM returned unexpected structure."

    except Exception as e:
        print("❌ LLM API Error:", e)
        return "⚠️ Failed to generate documentation due to an API error."