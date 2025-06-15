<<<<<<< HEAD
import streamlit as st
from huggingface_hub import InferenceClient

# Page configuration
st.set_page_config(page_title="Farmasist AI Chatbot 🌾")

# Load Hugging Face API token from secrets
HF_TOKEN = st.secrets["HUGGINGFACE"]["API_TOKEN"]

# Initialize Hugging Face Inference Client with nscale
client = InferenceClient(
    provider="nscale",
    api_key=HF_TOKEN,
)

# App title and instructions
st.title("🌿 Farmasist: Your Agriculture AI Assistant")
st.write("Ask me anything about farming, crops, and soil conditions!")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_input = st.chat_input("👨‍🌾 You:")

# Function to query your Llama model
def get_farmasist_response(prompt):
    try:
        completion = client.chat.completions.create(
            model="meta-llama/Llama-3.3-70B-Instruct",
            messages=[
                {"role": "user", "content": prompt}
            ],
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {e}"

# Process user input and generate response
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    with st.spinner("Thinking... 🌱"):
        reply = get_farmasist_response(user_input)
    
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)




=======
import streamlit as st
from huggingface_hub import InferenceClient

# Page configuration
st.set_page_config(page_title="Farmasist AI Chatbot 🌾")

# Load Hugging Face API token from secrets
HF_TOKEN = st.secrets["HUGGINGFACE"]["API_TOKEN"]

# Initialize Hugging Face Inference Client with nscale
client = InferenceClient(
    provider="nscale",
    api_key=HF_TOKEN,
)

# App title and instructions
st.title("🌿 Farmasist: Your Agriculture AI Assistant")
st.write("Ask me anything about farming, crops, and soil conditions!")

# Initialize session state for chat history
if "messages" not in st.session_state:
    st.session_state.messages = []

# Display previous chat messages
for message in st.session_state.messages:
    with st.chat_message(message["role"]):
        st.write(message["content"])

# User input
user_input = st.chat_input("👨‍🌾 You:")

# Function to query your Llama model
def get_farmasist_response(prompt):
    try:
        completion = client.chat.completions.create(
            model="meta-llama/Llama-3.3-70B-Instruct",
            messages=[
                {"role": "user", "content": prompt}
            ],
        )
        return completion.choices[0].message.content
    except Exception as e:
        return f"❌ Error: {e}"

# Process user input and generate response
if user_input:
    st.session_state.messages.append({"role": "user", "content": user_input})
    with st.chat_message("user"):
        st.write(user_input)

    with st.spinner("Thinking... 🌱"):
        reply = get_farmasist_response(user_input)
    
    st.session_state.messages.append({"role": "assistant", "content": reply})
    with st.chat_message("assistant"):
        st.write(reply)




>>>>>>> 20da698cce7d124a23ecf63dc52c150b9eed8ab2
