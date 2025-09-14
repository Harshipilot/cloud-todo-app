import streamlit as st

# App title
st.set_page_config(page_title="Marghadarshak - Empowering Rural Youth", layout="wide")

# --- Hero Section ---
st.title("🌟 Marghadarshak")
st.subheader("Empowering Rural Youth with Career Guidance & Skill Development")
st.caption("By Team Binary Brains (Team 14)")

# Navigation with tabs
tabs = st.tabs([
    "🚀 Challenge", 
    "💡 Solution", 
    "✨ Features", 
    "👩‍🎓 Age Group Guidance", 
    "📞 Sahayak AI", 
    "👨‍💻 Team"
])

# --- Challenge Tab ---
with tabs[0]:
    st.header("🚀 The Challenge: Untapped Potential")
    st.write("""
    Many students in rural and underserved regions face significant barriers to career development.  
    They often lack access to tailored guidance and tools, leading to a misalignment between aspirations 
    and available opportunities. This directly impacts skill program enrollment and employability.
    """)
    st.button("I Agree ✅")

# --- Solution Tab ---
with tabs[1]:
    st.header("💡 Our Solution: Marghadarshak")
    st.write("""
    *Marghadarshak* (“The Guide”) is a career development companion app.  
    It helps students discover interests, build personalized career paths, and access learning resources, 
    internships, and competitions. With **offline AI support**, no student is left behind.
    """)
    if st.button("See How It Works"):
        st.success("✔️ Students explore careers, get AI-guided roadmaps, and connect to opportunities!")

# --- Features Tab ---
with tabs[2]:
    st.header("✨ Core Features")
    features = {
        "🌐 Multilingual & Accessible": "Guidance in multiple local languages.",
        "🛤️ Dynamic Career Roadmaps": "Step-by-step guidance adapting to student progress.",
        "⚡ Streamlined Registration": "Auto-fill for events and competitions.",
        "🤖 AI-Driven Personalization": "Skill-based recommendations and feedback.",
        "📈 Real-time Profile Updates": "Adapts to user interests and activities."
    }
    for f, desc in features.items():
        if st.button(f):
            st.info(desc)

# --- Age Group Guidance Tab ---
with tabs[3]:
    st.header("👩‍🎓 Tailored Guidance by Age")

    col1, col2 = st.columns(2)

    with col1:
        st.subheader("Age 13–17 (School Students)")
        st.markdown("""
        - 📘 Homework Help & AI support  
        - 🎮 Educational Games & quizzes  
        - 📚 Notes & practice tests  
        - 🎨 Skill Discovery (coding, art, science)  
        - 🌍 Career Awareness (simple terms)  
        - 🏆 Mini Challenges & contests  
        - 👥 Peer Groups & safe collaboration  
        """)
        st.button("Explore 13–17 Features")

    with col2:
        st.subheader("Age 17+ (College & Beyond)")
        st.markdown("""
        - 💼 Internships & work exposure  
        - ⚔️ Competitions & Hackathons  
        - 👨‍🏫 Mentorship with professionals  
        - 🛤️ Career Roadmaps  
        - 📜 Upskilling & certifications  
        - 🔍 Job Opportunities  
        - 🌐 Networking & alumni connections  
        """)
        st.button("Explore 17+ Features")

# --- Sahayak Offline AI ---
with tabs[4]:
    st.header("📞 Sahayak: Offline AI Support")
    st.write("Even without internet, students can access AI-powered career guidance using phone calls.")
    steps = [
        "1️⃣ Dial service number",
        "2️⃣ Asterisk answers the call",
        "3️⃣ Speech-to-Text → processed by Local ChatGPT",
        "4️⃣ AI response → Text-to-Speech → student hears reply"
    ]
    for step in steps:
        st.checkbox(step)

    if st.button("Simulate Call"):
        st.success("📞 Connected! AI is answering student queries...")

# --- Team Section ---
with tabs[5]:
    st.header("👨‍💻 Meet the Team")
    st.write("Team **Binary Brains** (Team No. 14)")
    team_members = ["✨ Priya Bhargavi", "✨ Harshith"]
    for member in team_members:
        st.button(member)
