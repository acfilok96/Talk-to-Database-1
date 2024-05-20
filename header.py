import streamlit as st
from sales_function import Sales
from student_function import Student
from corona_report_function import Corona_report
from WHO_COVID_19_global_data_function import wHO_COVID_19_global_data

st.set_page_config(page_title='Talk to Database', layout="wide", page_icon = 'Image/d2.jpg', initial_sidebar_state = 'auto')

st.markdown("""
<style>
.big-font-1 {
    font-size:20px !important;
    text-align: center; 
    color: yellow
}
</style>
""", unsafe_allow_html=True)


def main(): 
    st.sidebar.markdown('<p class="big-font-1">Talk to Database</p>', unsafe_allow_html=True)
    st.sidebar.image("Image/17.png")
    
    option_2 = st.sidebar.selectbox(""":blue[**Choose Database**]""", ("sales", "student", "corona_report")) # , "WHO_COVID_19_global_data"
    
    if option_2 == "sales":
        Sales("sales.db")
    
    elif option_2 == "student":
        Student("student.db")

    elif option_2 == "corona_report":
        Corona_report("corona_report.db")

    # elif option_2 == "WHO_COVID_19_global_data":
    #     wHO_COVID_19_global_data("WHO_COVID_19_global_data.db")
        
    show_advanced_info_1 = st.sidebar.toggle(":blue[*Show Application Details*]", value = True)
    
    if show_advanced_info_1:
        st.sidebar.info("""

                    **Generative AI application**

                    - **About:** *Talk with the database*
                    
                    - **Model:** *Gemini backend*
                    
                    - **Language:** *English*
                    
                    - **Release Date:** *March, 2024*
                    
                    """)
        
    show_advanced_info_2 = st.sidebar.toggle(":blue[*Show Developer Details*]", value = False)
   
    if show_advanced_info_2:
        st.sidebar.info("""
                    
                    *This appplication has been created by [:blue[Dipankar Porey]](https://www.linkedin.com/in/dipankar-porey-403320259/), 
                    Former Technology Consultant, Senior at Ernst & Young LLP.* 
                    
                    """)    
    
if __name__ == '__main__':
    main()

