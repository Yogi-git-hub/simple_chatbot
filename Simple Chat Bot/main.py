from code_logic.chat_agent import bot
import streamlit as st

st.set_page_config(page_title=" Simple Chat bot",layout="wide")

st.header(" Simple Bot for communication ")

obj=bot()
input_text=st.chat_input(placeholder="Hi I am leo, How may i help you?")

if input_text:
    # check message exist or not 
    if "messages" not in st.session_state: 
        # create blank
        st.session_state.messages=[]
        output=obj.chat_fun(user_input_str=input_text)
    else:
        st.session_state.messages.append(
            {'role':'user','content':input_text}
        )
        messages=st.session_state.messages
       
        output=obj.chat_fun(history=messages)
    
    st.write(output)
    st.session_state.messages.append({
        'role':'assistance',
        'content':output
        })


