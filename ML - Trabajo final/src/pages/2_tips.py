import streamlit as st
from PIL import Image

st.set_page_config(page_title="Level of adaptability to online education", layout='wide')

st.markdown("<h2 style='text-align: center; color: black;'>Easy tips for Taking Online Classes effectively </h2>", unsafe_allow_html=True)

import base64
def add_bg_from_local(image_file):
    with open(image_file, "rb") as image_file:
        encoded_string = base64.b64encode(image_file.read())
    st.markdown(
    f"""
    <style>
    .stApp {{
        background-image: url(data:image/{"png"};base64,{encoded_string.decode()});
        background-size: cover
    }}
    </style>
    """,
    unsafe_allow_html=True
    )


add_bg_from_local("C://Users//Usuario//Desktop//The Bridge//ML - Trabajo final//src//images//back.jpg") 

st.write('<p style="font-size:26px; color:black;"> 1. Treat an online course like a “real” course. </p>', unsafe_allow_html=True)
st.write('<p style="font-size:22px; color:black;"> When it comes to online classes, you need to have the discipline to sit down and say, “I am going to work on this,” as well as the dedication to actually follow through. Though you can be flexible as to when you choose to complete your work during the week, you can’t put it off indefinitely. </p>', unsafe_allow_html=True)

st.write('<p style="font-size:26px; color:black;"> 2. Hold yourself accountable. </p>', unsafe_allow_html=True)
st.write('<p style="font-size:22px; color:black;"> Set goals at the beginning of the semester, and check in with yourself weekly. In a traditional classroom setting, you’ll often receive verbal or visual reminders of an assignment’s upcoming due date. But without a professor actively reminding you, it’s up to you to make sure you’ve allotted enough time to complete the work so you’re not starting an assignment the day before it’s due. </p>', unsafe_allow_html=True)

st.write('<p style="font-size:26px; color:black;"> 3. Practice time management. </p>', unsafe_allow_html=True)
st.write('<p style="font-size:22px; color:black;"> The flexibility to create your own schedule is often one of the biggest appeals of taking online classes. But that freedom can also be detrimental if you do not have solid time management skills. Without them, you might easily to find yourself cramming before classes or handing in subpar assignments. </p>', unsafe_allow_html=True)

st.write('<p style="font-size:26px; color:black;"> 4. Create a regular study space and stay organized. </p>', unsafe_allow_html=True)
st.write('<p style="font-size:22px; color:black;"> Set up a dedicated learning environment for studying. By completing your work there repeatedly, you’ll begin to establish a routine. Whether your workspace is your kitchen table, a library, or the corner booth in a local coffee shop, it’s important to determine what type of environment will work best for you. Experiment to discover which type of setting boosts your productivity. Wherever you choose, make sure there’s high-speed internet access so you’re not trying to take an online course over a lagging connection. Setting up a regular workspace or office will also help you to stay organized. Knowing exactly where important dates, files, forms, syllabi, books, and assignments live will help keep you on track towards hitting your goals. </p>', unsafe_allow_html=True)

st.write('<p style="font-size:26px; color:black;"> 5. Eliminate distractions. </p>', unsafe_allow_html=True)
st.write('<p style="font-size:22px; color:black;"> Exactly how much of a challenge these distractions will prove to be will depend on your own unique personality and situation. Some might find that they can tune out a noisy home by listening to music. Others might choose to work from a local coffee shop or library to eliminate their urge to multitask at home. Ultimately, you will need to find a strategy that works best for you. Regardless of where you choose to work, consider turning your cell phone off to avoid losing focus every time a text message or notification pops up. And if you’re still having trouble resisting the temptation to check your email or surf the web, try downloading a website blocker. Using applications like Cold Turkey and Freedom can help eliminate distractions by blocking the apps or websites that tend to compete for your attention, such as Facebook and Twitter. </p>', unsafe_allow_html=True)

st.write('<p style="font-size:26px; color:black;"> 6. Figure Out How You Learn Best. </p>', unsafe_allow_html=True)
st.write('<p style="font-size:22px; color:black;"> Once you’ve established where you’ll learn, think about when and how you accomplish your best work. If you’re a morning person, make time to study first thing. More of a night owl? Set aside an hour or two after dinner to cozy up to your computer. If the kids require your morning and evening attention, try to carve out a study session mid-day while they’re at school. Brew your usual cup of coffee, put on your go-to playlist, and do whatever you need to get into the zone and down to business. Not everyone learns the same way, so think about what types of information help you best grasp new concepts and employ relevant study strategies. If you’re a visual learner, for example, print out transcripts of the video lectures to review. Learn best by listening? Make sure to build time into your schedule to play and replay all audio- and video-based course content. </p>', unsafe_allow_html=True)

st.write('<p style="font-size:26px; color:black;"> 7. Actively participate. </p>', unsafe_allow_html=True)
st.write('<p style="font-size:22px; color:black;"> Participate in the course’s online forum to help you better understand course materials and engage with fellow classmates. This might involve commenting on a classmate’s paper on a discussion board or posting a question about a project you’re working on. Read what other students and your professor are saying, and if you have a question, ask for clarification. If you do feel yourself falling behind, speak up. Don’t wait until an assignment is almost due to ask questions or report issues. Email your professor and be proactive in asking for help. </p>', unsafe_allow_html=True)

st.write('<p style="font-size:26px; color:black;"> 8. Leverage your network. </p>', unsafe_allow_html=True)
st.write('<p style="font-size:22px; color:black;"> Online classes may sometimes make you feel like you are learning on your own, but this couldn’t be further from the truth. Most online courses are built around the concept of collaboration, with professors and instructors actively encouraging that students work together to complete assignments and discuss lessons. Build relationships with other students by introducing yourself and engaging in online discussion boards. Your peers can be a valuable resource when preparing for exams or asking for feedback on assignments. Don’t be afraid to turn to them to create a virtual study group. Chances are good that they will appreciate it just as much as you will. </p>', unsafe_allow_html=True)

img_tips = Image.open("C://Users//Usuario//Desktop//The Bridge//ML - Trabajo final//src//images//810-978x652.jpg")
col1, col2, col3 = st.columns(3)

with col1:
    st.write(' ')

with col2:
    st.image(img_tips)

with col3:
    st.write(' ')