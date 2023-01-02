from pathlib import Path

import streamlit as st
from PIL import Image


#---Path Settings---
current_dir=Path(__file__).parent if "___file___" in locals() else Path.cwd()
css_file="C:/Users/nara1005/Desktop/Rameshcv/styles/main.css"
resume_file="C:/Users/nara1005/Desktop/Rameshcv/assets/Ramesh_Profile.pdf"
profile_pic="C:/Users/nara1005/Desktop/Rameshcv/assets/Ramesh_pic.jpg"








#---General Settings---
Page_title="Digital CV | Ramesh Nataraj"
Page_icon=":wave:"
Name="Ramesh Nataraj"
Description="""
Data Analyst, assisting enterprises by supporting data-driven decision-making.
"""
Email="rameshnraj1822@gmail.com"
Social_media={
    "LinkedIn":"https://www.linkedin.com/in/ramesh-nataraj-3a4a3619a",
    "Naukri":"https://www.naukri.com/mnjuser/profile?id=&orgn=homepage",
    "Github":"https://github.com/RameshNRaj"
}
Projects={
    "> Procurement Analytics - Analysing the entire supply chain procurement process",
    "> HR Data Analysis - The core values of organization is impacting the culture of employees",
    "> Walmart Sales Visualization - Visualizing the data science predicted project",
}

st.set_page_config(page_title=Page_title, page_icon=Page_icon)



#---Load css,pdf & profile pic---
with open(css_file) as f:
    st.markdown("<style>{}</style>".format(f.read()), unsafe_allow_html=True)
with open(resume_file, "rb") as pdf_file:
    PDFbyte=pdf_file.read()
profile_pic=Image.open(profile_pic)

#---columns---
col1,col2=st.columns(2, gap="small")
with col1:
    st.image(profile_pic, width=230)

with col2:
    st.title(Name)
    st.write(Description)
    st.download_button(
        label="Download Resume",
        data=PDFbyte,
        file_name=resume_file,
        mime="application/octet-stream",
    )
    st.write(Email)






#---Social Links---
st.write("#")
cols=st.columns(len(Social_media))
for index, (platform, link) in enumerate(Social_media.items()):
    cols[index].write(f"[{platform}]({link})")


 #---Experience & Qualification---
st.write("#")
st.subheader("Experience & Qualifications")
st.write("---")
st.write(
    """
Extensive experience of 1.6 years as a Data Analyst.
Strong hands on experience and knowledge in Python, SQL and Excel.
Good understanding of statistical principles and their respective applications.
Excellent team-player and displaying strong sense of initiative on task.
"""
)     


#---Skills---
st.write("#")
st.subheader("Hard Skills")
st.write("---")
st.write(
    """
> Programming: Python (Numpy, Pandas), SQL \n
> Data Visualization: PowerBI, MS Excel, Matplotlib, Seaborn \n
> Modeling: Logistic regression, linear regression \n
> Databases: MySQL
"""
)




#---Work History---
st.write("#")
st.subheader("Work History")
st.write("---")

#---Job---
st.write("Data Analyst | NielsenIQ India Pvt Ltd")
st.write("09/2021 - Present")
st.write(
    """
Collecting, collating and carrying out complex data analysis in support of management & clients request.    
"""
)


#---Projects & Accomplishments---
st.write("#")
st.subheader("Projects & Accomplishments")
st.write("---")
st.write(
    """
    > Procurement Analytics - Analysing the entire supply chain procurement process. \n
    > HR Data Analysis - The core values of organization is impacting the culture of employees. \n
    > Walmart Sales Visualization - Visualizing the data science predicted project.
    """
    )

#--for projects in Projects():
    #--st.write(f"[{Projects}]")












