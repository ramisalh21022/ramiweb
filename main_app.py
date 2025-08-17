from pathlib import Path
import json
import streamlit as st
from streamlit_lottie import st_lottie
from streamlit_extras.let_it_rain import rain
# Directories and file paths
THIS_DIR = Path(__file__).parent
CSS_FILE = THIS_DIR / "style" / "style.css"
ASSETS = THIS_DIR / "assets"
#LOTTIE_ANIMATION = ASSETS / "animation_holiday.json"
LOTTIE_ANIMATION = ASSETS / "Animation.json"
# Function to load and display the Lottie animation
def load_lottie_animation(file_path):
    with open(file_path, "r") as f:
        return json.load(f)
# Function to apply snowfall effect💕🎊🎉
def run_snow_animation():
    rain(emoji="❄️", font_size=20, falling_speed=5, animation_length="infinite")
# Function to get the name from query parameters
def get_person_name():
    query_params = st.experimental_get_query_params()
    return query_params.get("name", ["Friend"])[0]
# Page configuration
#st.set_page_config(page_title="Happy Holidays", page_icon="🎄")
# Run snowfall animation
run_snow_animation()
# Apply custom CSS
with open(CSS_FILE) as f:
    st.markdown(f"<style>{f.read()}</style>", unsafe_allow_html=True)
# Display header with personalized name
#PERSON_NAME = get_person_name()
#st.header(f"Happy Holidays, {PERSON_NAME}! 🎄", anchor=False)
# Display the Lottie animation
lottie_animation = load_lottie_animation(LOTTIE_ANIMATION)
st_lottie(lottie_animation, key="lottie-holiday", height=300)

about_page=st.Page("views/about_me.py",title="ABOUT ME",icon=":material/account_circle:",default=True,)
project_16_page=st.Page("views/education-app.py",title="education-app-store-in-flutter-database",icon=":material/bar_chart:",)

project_15_page=st.Page("views/whatsapp-n8nr.py",title="automation-supermarket-n8n-bootwhatsapp",icon=":material/bar_chart:",)
project_14_page=st.Page("views/pet-stor-flutter-supabase.py",title="application-mobil-web-for-pet-store-in-flutter-supabase",icon=":material/bar_chart:",)
project_12_page=st.Page("views/mall_robbery.py",title="mall_robbery",icon=":material/bar_chart:",)
project_11_page=st.Page("views/peoplecounter_enter_exit.py",title="peoplecounter_enter_exit",icon=":material/bar_chart:",)
project_10_page=st.Page("views/yolo11-detect-speed-car.py",title="yolo11-detect-speed-car",icon=":material/bar_chart:",)
project_1_page=st.Page("views/detected_img_video_camera.py",title="detected_img_video_camera",icon=":material/bar_chart:",)
project_2_page=st.Page("views/plate_licens_yolo10.py",title="plate_licens_yolo10",icon=":material/smart_toy:",)
project_3_page=st.Page("views/Fire_dataset_yolo5.py",title="Fire_dataset_yolo5",icon=":material/smart_toy:",)
project_4_page=st.Page("views/deepsort_yolo10.py",title="deepsort_yolo10",icon=":material/smart_toy:",)
project_5_page=st.Page("views/enter_to_exls_voice_text.py",title="enter_to_exls_voice_text",icon=":material/smart_toy:",)
project_6_page=st.Page("views/ocr_text_arabic.py",title="ocr_text_arabic",icon=":material/smart_toy:",)
project_7_page=st.Page("views/PDF-read_streamlit.py",title="PDF-read_streamlit",icon=":material/smart_toy:",)
project_8_page=st.Page("views/market.py",title="market",icon=":material/smart_toy:",)
project_9_page=st.Page("views/exam_class_list_except.py",title="exam_class_list_except",icon=":material/smart_toy:",)


pg=st.navigation ({"info":[about_page],"projects":[project_16_page,project_15_page,project_14_page,project_12_page,project_11_page,project_10_page,project_1_page,project_2_page,project_3_page,project_4_page,project_5_page,project_6_page,project_7_page,project_8_page,project_9_page]},)
#pg=st.navigation (pages=[about_page,project_1_page,project_2_page])
st.logo("assets/LOGOrami.png")
#st.sidebar.markdown("Made with ❤️❤️ by Rami")
#st.subheader("Hard Skills", anchor=False)
st.sidebar.markdown(
    """
    Hard Skills:
    - Programming: Python , SQL/plsql, VB.net,flutter
    - ComputerVision: YOLOV10, YOLOV11
    - Databases: Postgres, Oracle, MySQL
    """
)   
st.sidebar.markdown("Made with ❤️❤️ by Rami")    
pg.run()
