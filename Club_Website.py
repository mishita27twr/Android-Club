import streamlit as st
from PIL import Image
import os

# ==============================
# CUSTOM CSS FOR SOLID COLORS
# ==============================
st.markdown("""
    <style>
        /* Full black background */
        .stApp {
            background-color: #000000 !important;
        }

        /* TAGLINE */
        .tagline {
            font-size: 28px !important;
            text-align: center;
            color: #ffff99;
            margin-bottom: 60px;
        }

        /* SECTION HEADERS - Solid Red */
        .section-header {
            font-size: 42px !important;
            font-weight: 800;
            text-align: center;
            color: #FF0000 !important;
            margin-top: 60px;
            margin-bottom: 15px;
        }

        /* UNDERLINE */
        .underline {
            width: 120px;
            height: 4px;
            background: #FF0000 !important;
            margin: 0 auto 40px auto;
            border-radius: 10px;
        }

        /* CONTENT */
        .content {
            font-size: 20px !important;
            line-height: 1.8;
            color: #ffff66;
            text-align: justify;
            margin-left: 10%;
            margin-right: 10%;
        }

        /* EVENT CARDS */
        .event-box {
            background-color: #0a0a0a;
            padding: 25px;
            border-radius: 15px;
            margin-bottom: 30px;
            box-shadow: 0px 0px 25px rgba(255, 0, 0, 0.8);
        }

        .event-box h3 {
            color: #00FF00 !important;
        }

        /* LINKS IN CONTACT */
        .content a {
            color: #ffff66 !important;
            text-decoration: none;
        }
    </style>
""", unsafe_allow_html=True)

# ==============================
# HEADER WITH LOGO
# ==============================

logo_path = "android_club_vit_bhopal_logo.jpeg"
if not os.path.exists(logo_path):
    st.error(f"Logo not found! Please place 'android_club_vit_bhopal_logo.jpeg' in the same folder as this script.")
else:
    logo = Image.open(logo_path)
    col1, col2 = st.columns([1, 4])
    with col1:
        st.image(logo, width=80)  # Adjust width if needed
    with col2:
        st.markdown(
            '<span style="color:#00FF00; font-size:60px; font-weight:bold; vertical-align:middle;">ANDROID CLUB</span>',
            unsafe_allow_html=True
        )

# Tagline
st.markdown('<p class="tagline">Where Innovation Meets Creativity 🚀</p>', unsafe_allow_html=True)

# ------------------------------
# Welcome Section
# ------------------------------
st.markdown('<h2 class="section-header">Welcome</h2>', unsafe_allow_html=True)
st.markdown('<div class="underline"></div>', unsafe_allow_html=True)
st.markdown('<p class="content">Welcome to the Android Club of VIT Bhopal! We are a vibrant community of developers, learners, and innovators who are passionate about building solutions using Android, Python, AI, and emerging technologies. Whether you are a beginner or an expert, this is your space to explore, collaborate, and grow. ✨</p>', unsafe_allow_html=True)

# ------------------------------
# About Us
# ------------------------------
st.markdown('<h2 class="section-header">About Us</h2>', unsafe_allow_html=True)
st.markdown('<div class="underline"></div>', unsafe_allow_html=True)
st.markdown('<p class="content">The Android Club is not just about coding—it’s about innovation, teamwork, and problem-solving. Our mission is to empower students with hands-on technical skills, foster collaboration, and create impactful projects. From workshops on cutting-edge technologies to exciting hackathons, we provide a platform to transform ideas into reality. 🌟</p>', unsafe_allow_html=True)

# ------------------------------
# Projects
# ------------------------------
st.markdown('<h2 class="section-header">Projects</h2>', unsafe_allow_html=True)
st.markdown('<div class="underline"></div>', unsafe_allow_html=True)
st.markdown('<p class="content">Our members have developed projects ranging from Android apps to AI-powered tools. We focus on real-world problem solving, ensuring that every project adds value to the community. Stay tuned for highlights of our best creations! 🔥</p>', unsafe_allow_html=True)

# ------------------------------
# Events
# ------------------------------
st.markdown('<h2 class="section-header">Events</h2>', unsafe_allow_html=True)
st.markdown('<div class="underline"></div>', unsafe_allow_html=True)

# Past Event
st.markdown('''
<div class="event-box">
    <h3>📌 Pydroid X – Workshop + Hackathon</h3>
    <p class="content">An electrifying 3-day event where participants explored Machine Learning & Cyber Security while building real-world projects. With curated datasets, hands-on workshops, and a high-energy hackathon, the event was a massive success! 💻</p>
    <p class="content"><b>Dates:</b> July 24–26, 2025 <br>
    <b>Venue:</b> AB-02 Auditorium <br>
    <b>Registration Fee:</b> Rs. 99</p>
</div>
''', unsafe_allow_html=True)

# Upcoming Event
st.markdown('''
<div class="event-box">
    <h3>🚀 Meet & Greet 3.0 – Freshers Tech Welcome</h3>
    <p class="content">The Android Club proudly presents Meet & Greet 3.0 – an epic welcome event exclusively for freshers! Dive into prompt engineering, take part in your first ideathon, and connect with brilliant peers. No coding experience required – just bring your ideas! 🎉</p>
    <p class="content"><b>Date:</b> September 18th, 2025 <br>
    <b>Time:</b> 1:15 PM – 4:20 PM <br>
    <b>Venue:</b> AB-02 Auditorium 02</p>
</div>
''', unsafe_allow_html=True)

# ------------------------------
# Contact
# ------------------------------
st.markdown('<h2 class="section-header">Contact</h2>', unsafe_allow_html=True)
st.markdown('<div class="underline"></div>', unsafe_allow_html=True)
st.markdown('''
<p class="content">
📧 Email: <a href="mailto:androidclub@vitbhopal.ac.in" target="_blank">androidclub@vitbhopal.ac.in</a><br>
📸 Instagram: <a href="https://www.instagram.com/androidclub_vitb/" target="_blank">@androidclub_vitb</a><br>
🔗 LinkedIn: <a href="https://www.linkedin.com/company/androidclub-vitb/" target="_blank">Android Club VIT Bhopal</a><br>
<b>Faculty Coordinator:</b> Dr. Adarsh Patel
</p>
''', unsafe_allow_html=True)
