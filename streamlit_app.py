import pdfkit
from jinja2 import Environment, PackageLoader, select_autoescape, FileSystemLoader
from datetime import date
import streamlit as st
from streamlit.components.v1 import iframe

st.set_page_config(layout="centered", page_icon="🎓", page_title="Certificate Generator")
st.title("🎓Certificate PDF Generator")

st.write(
    "Here you can use Streamlit to make a PDF generator app in just a few lines of code!"
)

left, right = st.columns(2)

right.write("Here's the Sample Template that you will get:")

right.image("template.png", width=300)

env = Environment(loader=FileSystemLoader("."), autoescape=select_autoescape())
template = env.get_template("template.html")


left.write("Fill in the data:")
form = left.form("template_form")
student = form.text_input("Student name")
course = form.selectbox(
    "Choose course",
    ["Advanced Core JAVA", "Advanced Python", "MERN Stack Development", "MEAN Stack Development", "DevOps Engineering"
    "Data Science", "Blockchain Development"],
    index=0,
)
grade = form.slider("Grade", 1, 100, 70)
submit = form.form_submit_button("Generate PDF")

if submit:
    html = template.render(
        student=student,
        course=course,
        grade=f"{grade}/100",
        date=date.today().strftime("%B %d, %Y"),
    )

    pdf = pdfkit.from_string(html, False)
    st.balloons()

    right.success("🎉Your Certificate was generated!")
    # st.write(html, unsafe_allow_html=True)
    # st.write("")
    right.download_button(
        "⬇️Download PDF",
        data=pdf,
        file_name="Course-Certificate.pdf",
        mime="application/octet-stream",
    )
