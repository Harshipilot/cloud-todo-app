import streamlit as st

# ---------------- CONFIG ----------------
st.set_page_config(page_title="Marghadarshak", layout="wide")

# --------------- HEADER / HERO ---------------
st.markdown(
    """
    <div style='text-align: center; padding: 40px; background: linear-gradient(90deg, #4B0082, #8A2BE2); color: white; border-radius: 12px;'>
        <h1 style='font-size: 48px;'>🌟 Marghadarshak</h1>
        <h3>Empowering Rural Youth with Career Opportunities</h3>
        <p>Discover skills • Compete • Upskill • Connect • Grow</p>
    </div>
    """,
    unsafe_allow_html=True
)

# Sidebar Navigation
menu = st.sidebar.radio(
    "📍 Navigate",
    ["🏠 Home", "🔑 Login / Register", "📊 Dashboard", "🤖 Sahayak AI", "👨‍💻 About Us"]
)

# --------------- HOME ---------------
if menu == "🏠 Home":
    st.subheader("Why Marghadarshak?")
    st.write(
        """
        🎯 A one-stop career companion for students in rural & underserved regions.  
        - 📘 Career guidance in local languages  
        - 🤖 AI-powered personalized recommendations  
        - 🏆 Competitions, hackathons & internships  
        - 📞 Offline support via **Sahayak AI**  
        """
    )

    st.success("👉 Get started by Registering or Logging in from the sidebar!")

# --------------- LOGIN / REGISTER ---------------
elif menu == "🔑 Login / Register":
    st.subheader("🔑 Login / Register")
    option = st.radio("Choose Action", ["Login", "Register"])

    if option == "Login":
        st.text_input("📧 Email")
        st.text_input("🔒 Password", type="password")
        if st.button("Login"):
            st.success("✅ Logged in successfully! Redirecting to Dashboard...")

    else:
        st.text_input("👤 Full Name")
        st.text_input("📧 Email")
        st.text_input("🔒 Password", type="password")
        st.text_input("🎓 Age / Category (School, College, Professional)")
        if st.button("Register"):
            st.success("✅ Registration complete! You can now Login.")

# --------------- DASHBOARD ---------------
elif menu == "📊 Dashboard":
    st.subheader("📊 Your Career Dashboard")

    col1, col2, col3 = st.columns(3)

    with col1:
        st.markdown("### 💼 Internships")
        if st.button("View Internships"):
            st.info("Example: Software Intern at Infosys (Apply by Sep 30)")

    with col2:
        st.markdown("### ⚔️ Hackathons")
        if st.button("View Hackathons"):
            st.info("Example: AI for Good Hackathon (Deadline: Oct 15)")

    with col3:
        st.markdown("### 👨‍🏫 Mentorships")
        if st.button("Find Mentors"):
            st.info("Example: Talk to Industry Experts in Tech & Business")

    st.markdown("---")
    st.subheader("✨ Personalized Recommendations")
    st.write("Based on your profile, here are some suggestions:")
    recs = ["📚 Upskill: Python Basics Course", "🏆 Join: National Coding Contest", "💼 Apply: Web Dev Internship"]
    for r in recs:
        st.success(r)

# --------------- SAHAYAK AI ---------------
elif menu == "🤖 Sahayak AI":
    st.subheader("📞 Sahayak: Offline AI Support")
    st.write("Simulate how students can access guidance via a simple phone call:")

    steps = [
        "1️⃣ Dial service number",
        "2️⃣ Asterisk system answers",
        "3️⃣ Speech converted to text → processed by AI",
        "4️⃣ AI generates response",
        "5️⃣ Text-to-Speech → Student hears answer"
    ]

    if st.button("📞 Start Simulation"):
        for step in steps:
            st.success(step)

    st.info("This ensures access even in rural areas with no internet.")

# --------------- TEAM / ABOUT ---------------
elif menu == "👨‍💻 About Us":
    st.subheader("👨‍💻 Team Binary Brains (Team 14)")
    st.write("We are passionate about empowering rural youth through technology and innovation.")
    st.markdown("**Team Members:**")
    st.write("✨ Priya Bhargavi") 
    st.write("✨ Harshith")
    st.success("Together, we are building Marghadarshak to guide the next generation 🚀")
