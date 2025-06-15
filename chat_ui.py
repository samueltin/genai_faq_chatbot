import streamlit as st
import app as app

st.title("Insurance FAQ Chatbot")
st.write("Ask your questions about insurance policies, claims, and more!")

# Initialize chat history in session state
if "chat_history" not in st.session_state:
    st.session_state.chat_history = []

# === Chat History Panel ===
st.subheader("Chat History")
if st.session_state.chat_history:
    for entry in st.session_state.chat_history:
        st.markdown(f"**You:** {entry['user']}")
        st.markdown(f"**Bot:** {entry['bot']}")
else:
    st.info("No messages yet. Ask your first question below.")

with st.form("chat_form"):
    text = st.text_area("Enter your question:")
    submitted = st.form_submit_button("Submit")
    if submitted:
        # Here you would call your queryLLM function to get a response
        response = app.query_llm(text, k=4)
        # st.write(f"Response: {response.content}")

        # Store question/response in history
        st.session_state.chat_history.append({
            "user": text.strip(),
            "bot": response.content if hasattr(response, "content") else str(response)
        })

        st.session_state.user_input = ""

        # Rerun to display updated chat
        # st.experimental_rerun()
