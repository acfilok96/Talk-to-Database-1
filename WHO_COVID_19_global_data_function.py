import streamlit as st
from functions import *
from chat_function import *

def wHO_COVID_19_global_data(database = "WHO_COVID_19_global_data.db"):
    
    col1, col2 = st.columns(2)
    
    with col1:
        show_advanced_info_1 = st.toggle(":blue[*Show database*]", value = True)
        
        if show_advanced_info_1:
            data = showTable(database)
            st.write(data)
            
    with col2:
        ChatFunction(database)
