import streamlit as st
import google.generativeai as genai

# Configure the Gemini API key
genai.configure(api_key="YOUR-API-KEY")

# Initialize the chatbot model
model = genai.GenerativeModel("gemini-1.5-flash")

# Set up the Streamlit app layout
st.title("AI Chatbot")
st.write("Ask anything, and I'll do my best to answer!")

# Create a session state to keep track of chat history
if "history" not in st.session_state:
    st.session_state.history = []

# Function to display the chat history
def display_chat():
    for msg in st.session_state.history:
        if msg["role"] == "user":
            st.write(f"**You:** {msg['content']}")
        else:
            st.write(f"**Bot:** {msg['content']}")

# Create an input field for the user query
user_input = st.text_input("You: ", "")

# When the user enters a query, generate the response
if user_input:
    st.session_state.history.append({"role": "user", "content": user_input})
    
    # Generate the AI response only once
    with st.spinner("Generating response..."):
        try:
            # Generate the AI response
            response = model.generate_content(user_input)
            st.session_state.history.append({"role": "bot", "content": response.text})
        except Exception as e:
            st.error(f"An error occurred: {e}")

            
if st.button("Clear Chat History"):
    st.session_state.history.clear()




# Display the chat history after processing
display_chat()