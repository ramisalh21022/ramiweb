import streamlit as st
from forms.contact import contact_form
#st.title("about me")
@st.dialog("Contact Me")
def show_contact_form():
    contact_form()


col1,col2=st.columns(2,gap='small',vertical_alignment="top")
with col1:
    st.image("assets/rami1-modified.png",width=230)
with col2:
    st.title("rami s.h", anchor=False)
    st.write("Electronic engineer, oracl databse sql/plsql,postgresdb ,python computer vision detection object ,developer flutter.📞+963933210196 -📧ramisalh21022.gmail.com")    
    if st.button("✉️Contact Me"):
        show_contact_form()  

# --- EXPERIENCE & QUALIFICATIONS ---
#st.write("\n")
st.subheader("Experience & Qualifications", anchor=False)
st.write(
    """
    - 10 Years experience in Oracle database sql/plsql 
    - developer of flutter dart and make apk apps
    - Good understanding of python computer vision and detectin object dataset and train dataset
    - working with paddleOcr and easyOcr and teseeractOcr  and recognition voice in python
    """
)

# --- SKILLS ---
#st.write("\n")
st.subheader("Hard Skills", anchor=False)
st.write(
    """
    - Programming: Python , SQL/plsql, VB.net,flutter
    - ComputerVision: YOLOV10, YOLOV11
    - Databases: Postgres, Oracle, MySQL
    """
)        