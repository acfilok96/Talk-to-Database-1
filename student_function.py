import streamlit as st
from functions import *
from chat_function import *

def Student(database = "student.db"):
    
    if st.toggle(":blue[*Click here for database*]", value = True): 
        col1, col2 = st.columns(2)
        with col1:
            data = showTable(database)
            st.write(data)
        with col2:
            ChatFunction(database)
    else:
        ChatFunction(database)
