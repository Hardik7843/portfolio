import streamlit as st
import pandas as pd
import streamlit.components.v1 as components
# from streamlit_timeline import timeline
from PIL import Image
import json
# from streamlit.components.v1 import html
# from streamlit_modal import Modal



# st.title("Welcom to my portfolio")
# img = open("images\page_icon.png")
# img = Image.open("images\page_icon.png")
# page_config = {"page_title": "Hardik's portfolio", "page_icon": img , "layout":"wide"}
# st.set_page_config(**page_config)

# Reading all the text files
about_file_path = r'text\about.txt' # My introduction
skill_file_path = r'text\skills.txt' # Skills List
tools_file_path = r'text\tools.txt' # Tools & Technologies 

# Reading JSON Files
certificates = r'JSON\certificates.json'
profiles = r'JSON\profiles.json'


def show_details():
    st.write("📧: hardikprajapati7843@gmail.com")
    st.write("📞: +91 7715891774")

widget_count = 0

# tabs = ["About","Skills","Education","Projects", "Social","Acheivements"]

# tab1, tab2, tab3, tab4 , tab5, tab6 = st.tabs(tabs)

tabs = ["About","Skills","Education", "Social"]

tab1, tab2, tab3 , tab5 = st.tabs(tabs)

with tab1:
    st.title("About my self")
    with st.container():
        f = open(about_file_path,'r')
        text = f.read()

        components.html(
            f"""
            <div class="card">
                <div class="card-body">
                    <div style="text-align: justify; color: white">
                        {text}
                    </div>
                </div>
            </div>
            """,
            height=400,
            scrolling=True,
        )

with tab2:
    st.title("Skillset")
    
    with st.container():
        # for tech skills
        st.header("Technical Skills")

        with open(skill_file_path , 'r') as f:
            skills = f.readlines()
            num_cols = 4
            col = st.columns(num_cols)
            # col = st.columns(len(skills))
            for i,skill in enumerate(skills):
                idx = i % num_cols
                widget_count += 1 
                col[idx].button(skill.strip() , key = widget_count)
    
    st.markdown('---')

    with st.container():
        # for tool known
        st.header("Tools")
        with open(tools_file_path , 'r') as f:
            tools = f.readlines()
            num_cols = 4
            col = st.columns(num_cols)
            # col = st.columns(len(skills))
            for i,tool in enumerate(tools):
                idx = i % num_cols
                widget_count += 1
                col[idx].button(tool.strip() , key = widget_count)

    st.markdown('---')

    with st.container():
        st.header("Certifications")
        st.markdown("  ")
        with open(certificates , 'r') as certificates:
            certificates = json.load(certificates)
            i = 0 
            num_cols = 2
            col = st.columns(num_cols)
            for certificate in certificates:
                idx = i % num_cols
                with col[idx]:
                    st.write(f"**Name:** {certificate['name']}")
                    st.write(f"**Date:** {certificate['date']}")
                    st.write(f"**Provider:** {certificate['provider']}")
                    st.write(f"**Description:** {certificate['description']}")
                    widget_count += 1
                    url = certificate['url']
                    path = f"images\{certificate['name']}.png"
                    if st.button("View Credentials" , key = widget_count):
                        st.markdown(f'<a href="{url}" target="_blank">Click Here if not visible</a>', unsafe_allow_html=True)
                        st.image(image = path)
                    st.markdown("---")
                    i = i+1


with tab3:
    st.title("Educational Persuits")
    education = pd.read_csv("education.csv" , index_col = None)
    education.set_index('Degree' , inplace= True)
    st.table(data = education)

# with tab4:
#     st.title("Projects Basket")

with tab5:
    # st.title("Get in Touch with Me")
    st.header("Social Platforms")
    with open(profiles , 'r') as profiles:
        profiles = json.load(profiles)
        num_cols = 3
        col = st.columns(num_cols)
        i = 0
        idx = 0
        for profile in profiles:
            idx = i % num_cols
            with col[idx]:
                path = profile['path']
                url = profile['url']
                name = profile['name']
                components.html(f"""<a href={url} target="_blank"><img alt="LinkedIn" width="40px" src={path}></a><br><p style = "color: white;">{name}</p>""" , height = 100)
                # st.info("Click on Icon to access Profile" , icon= "🔗")
                # st.markdown(f'<a href={url} target="_blank">Access Profile</a>')
                i += 1   

 

# with tab6:
#     st.title("Accomplishments Worth Sharing")

with st.sidebar:
    st.image("images\linkedin.png")
    # widget_count += 1
    contact_btn_state = st.button("Wish to connect?", key = 'contact' )
    if 'contact' not in st.session_state:
        # if st.session_state["contact"]:
        #     st.session_state["contact"] = True
        # else:
        #     st.session_state["contact"] = False
        st.session_state['contact'] = contact_btn_state
    
    if st.session_state["contact"]:
        st.write("📧: hardikprajapati7843@gmail.com")
        st.write("📞: +91 7715891774")


# with st.container():
#     st.subheader("About")
#     f = open(r'text\about.txt','r')
#     text = f.read()

#     components.html(
#         f"""
#         <div class="card">
#             <div class="card-body">
#                 <div style="text-align: justify; color: white">
#                     {text}
#                 </div>
#             </div>
#         </div>
#         """,
#         height=400,
#         scrolling=True,
#     )



