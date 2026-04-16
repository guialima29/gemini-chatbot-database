import streamlit as st
from streamlit_chat import message
from system import returnInfo

def on_input_change(): # add in history and run the AI function 
    user_input = st.session_state.user_input
    st.session_state.past.append(user_input)
    st.session_state.generated.append(returnInfo(user_input))
    st.session_state.user_input = ""

def on_btn_click(): # clear history
    del st.session_state.past[:]
    del st.session_state.generated[:]

# title
st.title("Chatbot Database")
st.divider()

# initialize the chat messages lists in session state if they don't exist yet
# 'past' stores the user's messages
st.session_state.setdefault( 
    'past',
    []
)

# 'generated' stores the assistant's responses
st.session_state.setdefault(
    'generated',
    []
)

# create an empty placeholder in the UI to render the chat dynamically
chat_placeholder = st.empty()

with chat_placeholder.container():
    # loop through the generated responses and display both user and assistant messages
    for i in range(len(st.session_state['generated'])):
        message(st.session_state['past'][i], is_user=True, key=f"{i}_user")
        message (
            st.session_state['generated'][i],
            key=f"{i}",
            allow_html=True,
        )
    # add a button to clear all chat messages
    st.button("Clear message", on_click=on_btn_click)

# input container for the user to type new messages
with st.container():
    st.text_input("Digite alguma coisa...", on_change=on_input_change, key="user_input")