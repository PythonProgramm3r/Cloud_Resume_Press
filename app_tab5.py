import streamlit as st
import logging

@st.cache_data
def load_personal_documents():
    """
    Loads the resume and ethos documents from local files.
    Caches the content to avoid re-reading from disk on every interaction.
    """
    try:
     
        # Read the resume text file
        with open("resume.txt", "r") as f:
            resume_content = f.read()

        if not resume_content.strip():
            st.warning("The resume.txt file appears to be empty or could not be read. The model's answers may be limited.")

        # Combine all document contents into a single context string
        full_context = f"DERRICK'S RESUME:\n{resume_content}"
        return full_context

    except FileNotFoundError as e:
        st.error(f"Error: A required document is missing: {e.filename}. Please make sure 'resume.txt' and 'derrick_ethos.txt' are in the same directory as the app.")
        return None
    except Exception as e:
        st.error(f"An error occurred while loading documents: {e}")
        logging.error(f"Error loading personal documents: {e}")
        return None

def render_personal_qa_tab(model):
    """
    Renders the Derrick Kaliney Q&A tab, using pre-loaded documents.
    """
    st.subheader("Derrick Kaliney's Personal Q&A Agent")
    st.markdown("""
    Ask a question about Derrick.
    The model will answer based on Derrick's pre-loaded resume and personal ethos documents.
    """)

    document_context = load_personal_documents()
    if not document_context:
        st.stop()

    question = st.text_input("Ask a question about Derrick Kaliney:", "What makes this candidate a good fit for a high-stakes, autonomous role?")

    if st.button("Generate Answer", key="personal_qa_button"):
        prompt = f"""
        You are Derrick Kaliney's personal hiring assistant. Your task is to answer questions about Derrick Kaliney based on the provided context documents.
        Label any statements you invent, hallucinate, or infer information beyond what is written.

        CONTEXT DOCUMENTS:
        ---
        {document_context}
        ---

        Based on these documents, please answer the following question: {question}
        """
        with st.spinner("Generating answer..."):
            response = model.generate_content(prompt)
            st.success("Answer generated!")
            st.markdown(response.text)