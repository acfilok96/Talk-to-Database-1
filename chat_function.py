
import streamlit as st
from streamlit_chat import message
from functions import *
import numpy as np

def ChatFunction(database_name):
    
    if "messages_temp_Fdsf" not in st.session_state:
        st.session_state.messages_temp_Fdsf = []


    container_11 = st.container(height = 385, border = False)
    
    k = 1
    with container_11:

        for message_s in st.session_state.messages_temp_Fdsf:
            if message_s["role"] == "Dipankaruser":
                message(message_s["content"], is_user = True, key = str(k) + '_user', avatar_style = "initials", seed = "Dipankar Porey")
            elif message_s["role"] == "Geminiassistant":
                if st.toggle(":green[*Click here for SQL Query*]", value = False, key = str((k*10)+10)):
                    message(str("SQL Query: \n\n")+str(message_s["content"][0]) , key = str(k), avatar_style = "initials", seed = "SQL Query", allow_html=True)
                message(str("General Response: \n\n")+str(message_s["content"][1]) , key = str(k+1), avatar_style = "initials", seed = "General Response", allow_html=True)
                # message(message_s["content"][0], key = str(k), avatar_style = "initials", seed = "Tony", allow_html = True)
                # message(message_s["content"][1], key = str(k+1), avatar_style = "initials", seed = "Tony", allow_html = True)
            k += 1

    def clear_chat_history():
        st.session_state.messages_temp_Fdsf = []
    st.sidebar.button(':green[*Clear chat*]', on_click = clear_chat_history)
            
    if prompt := st.chat_input("Talk to database !"):
        
        st.session_state.messages_temp_Fdsf.append({"role": str("Dipankar")+"user", "content": prompt})
        
        with container_11:

            message(prompt, is_user = True, key = str(k) + '_user', avatar_style = "initials", seed = "Dipankar Porey")

            k += 1
            
            full_response = " "
            with st.spinner(":green[Thinking . . .]"):
                full_response = generateQuery(database_name, prompt)
            if st.toggle(":green[*Click here for SQL Query*]", value = False, key = str((k*10)+10)):
                message(str("SQL Query: \n\n")+str(full_response[0]) , key = str(k), avatar_style = "initials", seed = "SQL Query", allow_html=True)
            message(str("General Response: \n\n")+str(full_response[1]) , key = str(k+1), avatar_style = "initials", seed = "General Response", allow_html=True)
                
            st.session_state.messages_temp_Fdsf.append({"role": str("Gemini")+"assistant", "content": full_response})
