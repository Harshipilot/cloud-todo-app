import streamlit as st

# ------------- Demo Agent Database --------------
AGENTS = {
    "12345": {
        "name_en": "Ravi Kumar",
        "name_hi": "रवि कुमार",
        "company_en": "SafeHomes Pvt Ltd",
        "company_hi": "सेफहोम्स प्रा. लि.",
        "phone": "9876543210"
    },
    "67890": {
        "name_en": "Meena Sharma",
        "name_hi": "मीना शर्मा",
        "company_en": "Secure Sales",
        "company_hi": "सिक्योर सेल्स",
        "phone": "9123456780"
    }
}

# ----------- Suspicious Reports (in-memory for demo) -----------
if "reports" not in st.session_state:
    st.session_state.reports = []

# ----------- Multilingual Support -------------
if "lang" not in st.session_state:
    st.session_state["lang"] = "en"
LANG = st.session_state["lang"]

def get_text(eng, hin):
    return hin if LANG == "hi" else eng

def header(text_en, text_hi):
    st.markdown(f"## {get_text(text_en, text_hi)}")

def subheader(text_en, text_hi):
    st.markdown(f"### {get_text(text_en, text_hi)}")

def bullet(text_en, text_hi):
    st.markdown(f"- {get_text(text_en, text_hi)}")

def refresh_lang():
    st.session_state.lang = LANG

# ----- Sidebar: Main Navigation & Language -----
st.sidebar.markdown("## eBharosa")
lang_choice = st.sidebar.radio(
    "Language / भाषा चुनें",
    ("English", "हिंदी"),
    index=0 if LANG == "en" else 1
)
LANG = "en" if lang_choice == "English" else "hi"
st.session_state.lang = LANG

menu_options = [
    get_text("Home", "होम"),
    get_text("Verify Agent", "एजेंट सत्यापित करें"),
    get_text("Agent Info", "एजेंट जानकारी"),
    get_text("Safety Tips", "सुरक्षा सुझाव"),
    get_text("Report Suspicious", "संदिग्ध रिपोर्ट करें"),
    get_text("View Reports", "रिपोर्ट देखें"),
    get_text("Help/FAQ", "सहायता / सामान्य प्रश्न")
]
menu = st.sidebar.selectbox(get_text("Main Menu", "मुख्य मेनू"), menu_options)

st.title(get_text("eBharosa 🙏", "ई भरोसा 🙏"))

# ----- Dynamic Pages -----

# -- Home Page --
if menu == get_text("Home", "होम"):
    header("Welcome to eBharosa!", "ई भरोसा में स्वागत है!")
    st.write(get_text(
        "A safety app for verifying agents, accessing safety tips, and protecting your community.",
        "सुरक्षा ऐप: एजेंटों की जाँच करें, सुरक्षा सुझाव पाएं, और अपने समुदाय को सुरक्षित रखें।"
    ))

# -- Verify Agent Page --
elif menu == get_text("Verify Agent", "एजेंट सत्यापित करें"):
    header("Agent Verification", "एजेंट सत्यापन")
    agent_id = st.text_input(get_text("Enter Agent ID", "एजेंट आईडी दर्ज करें"))
    if st.button(get_text("Verify", "सत्यापित करें")):
        if agent_id.strip() in AGENTS:
            st.success(get_text("Agent Verified!", "एजेंट सत्यापित है!"))
            agent = AGENTS[agent_id.strip()]
            st.session_state['last_agent'] = agent_id.strip()
            st.info(get_text("Click on 'Agent Info' page for more information.", "अधिक जानकारी के लिए 'एजेंट जानकारी' पेज देखें।"))
        elif agent_id.strip():
            st.error(get_text("Agent NOT Verified!", "एजेंट सत्यापित नहीं है!"))
        else:
            st.warning(get_text("Please enter an Agent ID.", "कृपया एजेंट आईडी दर्ज करें।"))

# -- Agent Info Page --
elif menu == get_text("Agent Info", "एजेंट जानकारी"):
    header("Agent Information", "एजेंट जानकारी")
    agent_id = st.session_state.get('last_agent')
    if agent_id and agent_id in AGENTS:
        agent = AGENTS[agent_id]
        st.write(get_text("Agent Name:", "एजेंट नाम:"), agent[get_text("name_en", "name_hi")])
        st.write(get_text("Company:", "कंपनी:"), agent[get_text("company_en", "company_hi")])
        st.write(get_text("Contact Number:", "संपर्क नंबर:"), agent['phone'])
        st.success(get_text("This agent is trusted and verified in our database.", "यह एजेंट विश्वासपात्र और सत्यापित है।"))
    else:
        st.info(get_text(
            "No verified agent selected. Please verify an agent first.",
            "कोई सत्यापित एजेंट नहीं चुना गया। कृपया पहले एजेंट सत्यापित करें।"
        ))

# -- Safety Tips Page --
elif menu == get_text("Safety Tips", "सुरक्षा सुझाव"):
    header("Safety Tips for You", "आपके लिए सुरक्षा सुझाव")
    with st.expander(get_text("Home Entry", "घर में प्रवेश")):
        bullet("Always check agent's official documents.", "हमेशा एजेंट के दस्तावेज़ जांचें।")
        bullet("Never allow strangers in home alone.", "अनजान व्यक्ति को अकेले घर में न प्रवेश दें।")
    with st.expander(get_text("Verification", "सत्यापन")):
        bullet("Ask for company ID card.", "कंपनी आईडी कार्ड मांगें।")
        bullet("Call company helpline for verification.", "सत्यापन के लिए कंपनी हेल्पलाइन पर कॉल करें।")
    with st.expander(get_text("Reporting", "रिपोर्टिंग")):
        bullet("Report suspicious persons to authorities.", "संदिग्ध व्यक्तियों की अधिकारियों को रिपोर्ट करें।")

# -- Report Suspicious Page --
elif menu == get_text("Report Suspicious", "संदिग्ध रिपोर्ट करें"):
    header("Report Suspicious Agent", "संदिग्ध एजेंट की रिपोर्ट करें")
    report_name = st.text_input(get_text("Agent Name or ID (optional)", "एजेंट का नाम या आईडी (ऐच्छिक)"))
    report_details = st.text_area(get_text("Details", "विवरण"))
    if st.button(get_text("Submit Report", "रिपोर्ट सबमिट करें")):
        if report_details.strip():
            st.session_state['reports'].append({
                'name': report_name,
                'details': report_details,
                'lang': LANG
            })
            st.success(get_text("Report Submitted!", "रिपोर्ट सबमिट हो गई!"))
        else:
            st.warning(get_text("Please enter report details.", "कृपया विवरण दर्ज करें।"))

# -- View Reports Page --
elif menu == get_text("View Reports", "रिपोर्ट देखें"):
    header("Community Suspicious Reports", "समुदाय की संदिग्ध रिपोर्ट")
    reports = st.session_state['reports']
    if reports:
        for idx, rp in enumerate(reports[::-1], start=1):
            st.write(f"{idx}. {get_text('Name/ID', 'नाम/आईडी')}:** {rp['name'] if rp['name'] else get_text('N/A', 'नहीं')}")
            st.write(f"   {get_text('Details', 'विवरण')}: {rp['details']}")
            st.markdown("---")
    else:
        st.info(get_text("No reports yet.", "अभी तक कोई रिपोर्ट नहीं है।"))

# -- Help/FAQ Page --
elif menu == get_text("Help/FAQ", "सहायता / सामान्य प्रश्न"):
    header("Help & FAQ", "सहायता एवं सामान्य प्रश्न")
    with st.expander(get_text("How to verify an agent?", "एजेंट को सत्यापित कैसे करें?")):
        st.write(get_text(
            "Go to the Verify Agent page, enter their ID, and check if they are verified.",
            "एजेंट आईडी दर्ज करें और सत्यापन पृष्ठ पर परिणाम देखें।"
        ))
    with st.expander(get_text("How to report suspicious agents?", "संदिग्ध एजेंट की रिपोर्ट कैसे करें?")):
        st.write(get_text(
            "Fill the report form on 'Report Suspicious' and submit.",
            "‘संदिग्ध रिपोर्ट करें’ पृष्ठ पर विवरण भरें और सबमिट करें।"
        ))
    with st.expander(get_text("How to keep family safe from fraud?", "परिवार को धोखाधड़ी से कैसे बचाएँ?")):
        st.write(get_text(
            "Never share personal or financial info with unknown agents.",
            "अनजान एजेंट से व्यक्तिगत या वित्तीय जानकारी साझा न करें।"
        ))
