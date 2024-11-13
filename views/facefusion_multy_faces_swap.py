import streamlit as st
st.title("facefusion_multy_faces_swap")
img=st.image(["assets/f1.png","assets/f2.png","assets/f3.png"],width=230)
col1,col2=st.columns(2,gap='small',vertical_alignment="top")
with col1:
    #st.image("assets/rami1-modified.png",width=230)
    st.title("befor_swap", anchor=False)
    st.video("assets/facefusion_multy_faces_swap1.mp4")
with col2:
    st.title("after_swap", anchor=False)
    st.video("assets/facefusion_multy_faces_swap2.mp4")
    #st.write("Electronic engineer, oracl databse sql/plsql,postgresdb ,python computer vision detection object ,developer flutter.📞+963933210196 -📧ramisalh21022.gmail.com")    
    
st.write("download from :{https://github.com/ramisalh21022/ramifaces}")