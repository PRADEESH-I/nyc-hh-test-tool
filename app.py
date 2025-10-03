import streamlit as st
import google.generativeai as genai

# Page config
st.set_page_config(page_title="NYC H+H Test Script Query Tool", layout="wide")

st.title("NYC H+H Test Script Query Tool")
st.write("Ask questions about your OTL + Absence test scripts.")

# Configure Gemini API
genai.configure(api_key=st.secrets["GEMINI_API_KEY"])
model = genai.GenerativeModel("gemini-1.5-flash")

# Input box for query
query = st.text_input("Enter your question:")

if query:
    with st.spinner("Thinking..."):
        try:
            # Simple call to Gemini (no RAG context yet)
            prompt = f"""
            You are a helpful assistant. The user asked:
            {query}
            Answer clearly and concisely.
            """
            response = model.generate_content(prompt)

            st.subheader("Answer:")
            st.write(response.text)

        except Exception as e:
            st.error(f"Error: {e}")
