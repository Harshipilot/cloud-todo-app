import streamlit as st
from datetime import datetime

# -------- Sample Agent Database with Photos ----------
AGENTS = {
    "12345": {
        "name_en": "Ravi Kumar",
        "name_hi": "रवि कुमार",
        "company_en": "SafeHomes Pvt Ltd",
        "company_hi": "सेफहोम्स प्रा. लि.",
        "phone": "9876543210",
        "photo": "https://randomuser.me/api/portraits/men/65.jpg"
    },
    "67890": {
        "name_en": "Meena Sharma",
        "name_hi": "मीना शर्मा",
        "company_en": "Secure Sales",
        "company_hi": "सिक्योर सेल्स",
        "phone": "9123456780",
        "photo": "https://randomuser.me/api/portraits/women/44.jpg"
    }
}

if "reports" not in st.session_state:
    st.session_state.reports = []

if "verifications" not in st.session_state:
    st.session_state.verifications = []

# ---------- Language Support & Theme -------------
if "lang" not in st.session_state:
    st.session_state.lang = "en"
LANG = st.session_state.lang

def get_text(eng, hin):
    return hin if LANG == "hi" else eng

def header(text_en, text_hi):
    st.markdown(f"## {get_text(text_en, text_hi)}")

def bullet(text_en, text_hi):
    st.markdown(f"- {get_text(text_en, text_hi)}")

def banner():
    st.markdown(
        "<div style='background-color: #8ecae6; padding: 16px; text-align: center; border-radius: 12px;'>"
        "<h2>🌏 " +
        get_text("Empower your community with trust!", "अपने समुदाय का विश्वास बढ़ाएँ!") +
        " 🌏</h2></div>", unsafe_allow_html=True)

# ------------ Sidebar & Navigation ---------------
st.sidebar.image("https://i.imgur.com/UmtG3to.png", width=180)
lang_choice = st.sidebar.radio(
    "Language / भाषा चुनें",
    ("English", "हिंदी"),
    index=0 if LANG == "en" else 1
)
LANG = "en" if lang_choice == "English" else "hi"
st.session_state.lang = LANG

menu_options = [
    get_text("🏠 Home", "🏠 होम"),
    get_text("🔎 Verify Agent", "🔎 एजेंट सत्यापित करें"),
    get_text("👤 Recent Verified Agents", "👤 हाल के सत्यापित एजेंट"),
    get_text("🛡 Safety Tips", "🛡 सुरक्षा सुझाव"),
    get_text("🚩 Report Suspicious", "🚩 संदिग्ध रिपोर्ट करें"),
    get_text("📋 Community Reports", "📋 समुदाय रिपोर्ट"),
    get_text("❓ Help & FAQs", "❓ सहायता / सामान्य प्रश्न"),
]
menu = st.sidebar.selectbox(get_text("Select Page", "पेज चुनें"), menu_options)

st.markdown("<style>footer{visibility:hidden}</style>", unsafe_allow_html=True)
st.markdown(
    "<div style='background-color: #219ebc; color:white; padding: 14px; border-radius:8px; font-size:28px; text-align:center;'>"
    "eBharosa 🙏</div>",
    unsafe_allow_html=True
)
banner()

# ---------- Pages -------------------

# HOMEPAGE with counters and motivational quote
if menu == get_text("🏠 Home", "🏠 होम"):
    header("Welcome to eBharosa!", "ई भरोसा में स्वागत है!")
    st.image("https://i.imgur.com/eiGUu0X.png", use_column_width=True)
    st.markdown(f"<div style='background-color: #d9ed92; padding:10px; border-radius:8px'><b>{get_text('Be vigilant, be safe.', 'सतर्क रहें, सुरक्षित रहें।')}</b></div>", unsafe_allow_html=True)
    st.write(get_text("Verify, report, and empower safety in your locality.", "अपने इलाके में सत्यापित करें, रिपोर्ट करें, और सुरक्षा बढ़ाएँ।"))

    col1, col2, col3 = st.columns(3)
    col1.metric(get_text("Agents Verified", "सत्यापित एजेंट"), f"{len(st.session_state.verifications)}")
    col2.metric(get_text("Tips Read", "पढ़े गए सुझाव"), f"{70 + len(st.session_state.verifications) * 2}")
    col3.metric(get_text("Community Reports", "समुदाय रिपोर्ट"), f"{len(st.session_state.reports)}")

    st.info(get_text(
        "Stay informed. Share eBharosa with family and friends for a safer tomorrow.",
        "जानकारी रखें। अपने परिवार और मित्रों के साथ ई भरोसा साझा करें।"
    ))

# AGENT VERIFICATION page
elif menu == get_text("🔎 Verify Agent", "🔎 एजेंट सत्यापित करें"):
    header("Agent Verification", "एजेंट सत्यापन")
    st.write(get_text(
        "Enter the Agent ID below to check verification status.",
        "एजेंट आईडी दर्ज करें और सत्यापन स्थिति देखें।"
    ))
    agent_id = st.text_input(get_text("Agent ID", "एजेंट आईडी"))
    if st.button(get_text("Verify Now", "अब सत्यापित करें")) or st.session_state.get("auto_verified"):
        st.session_state.auto_verified = False  # Reset flag
        if agent_id.strip() in AGENTS:
            agent = AGENTS[agent_id.strip()]
            st.success(get_text("✅ Agent Verified!", "✅ एजेंट सत्यापित है!"))
            col1, col2 = st.columns([1,3])
            col1.image(agent['photo'], width=90)
            col2.markdown(
                f"{get_text('Name', 'नाम')}:** {agent[get_text('name_en','name_hi')]}\n\n"
                f"{get_text('Company', 'कंपनी')}:** {agent[get_text('company_en','company_hi')]}\n\n"
                f"{get_text('Contact', 'संपर्क')}:** {agent['phone']}"
            )
            st.session_state.verifications.append({'id': agent_id.strip(), 'dt': datetime.now()})
        elif agent_id.strip():
            st.error(get_text("❌ Agent NOT Found or NOT Verified!", "❌ एजेंट सत्यापित नहीं है!"))
        else:
            st.warning(get_text("Please enter Agent ID.", "कृपया एजेंट आईडी दर्ज करें।"))

    st.write(get_text(
        "💡 Tip: Only trust agents who are verified by eBharosa.",
        "💡 सुझाव: केवल ई भरोसा द्वारा सत्यापित एजेंटों पर विश्वास करें।"
    ))

# RECENT VERIFIED AGENTS page
elif menu == get_text("👤 Recent Verified Agents", "👤 हाल के सत्यापित एजेंट"):
    header("Recent Verified Agents", "हाल के सत्यापित एजेंट")
    if st.session_state.verifications:
        for v in st.session_state.verifications[-5:][::-1]:
            aid = v['id']
            agent = AGENTS.get(aid)
            if agent:
                st.markdown(
                    f"<div style='background-color: #f0efeb; padding:8px; border-radius:8px; margin-bottom:4px;'>"
                    f"<img src='{agent['photo']}' width='55' style='float:left;margin-right:10px;border-radius:50%'>"
                    f"<b>{agent[get_text('name_en','name_hi')]}</b> ({get_text('ID','आईडी')} {aid})<br>"
                    f"{get_text('Company','कंपनी')}: {agent[get_text('company_en','company_hi')]}<br>"
                    f"<span style='color: #50a825'>{get_text('Verified on','सत्यापन दिनांक')}: {v['dt'].strftime('%d-%b-%Y %I:%M %p')}</span>"
                    f"</div>", unsafe_allow_html=True
                )
            st.markdown("---")
    else:
        st.info(get_text("No agents verified recently.", "हाल ही में कोई एजेंट सत्यापित नहीं हुआ है।"))

# SAFETY TIPS page (interactive categories)
elif menu == get_text("🛡 Safety Tips", "🛡 सुरक्षा सुझाव"):
    header("Safety Tips", "सुरक्षा सुझाव")
    with st.expander(get_text("At Your Doorstep", "आपके दरवाजे पर")):
        bullet("Ask for agent's ID and photo.", "एजेंट का आईडी और फोटो मांगे।")
        bullet("Check authenticity before allowing entry.", "प्रवेश की अनुमति देने से पहले प्रामाणिकता जांचें।")
    with st.expander(get_text("Personal Safety", "व्यक्तिगत सुरक्षा")):
        bullet("Never share OTP or bank info.", "ओटीपी और बैंक जानकारी साझा न करें।")
        bullet("Inform family before meeting agents.", "परिवार को मिलने की जानकारी दें।")
    with st.expander(get_text("Online Safety", "ऑनलाइन सुरक्षा")):
        bullet("Do not click suspicious links.", "संदिग्ध लिंक पर क्लिक न करें।")
        bullet("Beware of fake social profiles.", "फर्जी सोशल प्रोफाइल से सावधान रहें।")
    st.success(get_text(
        "Share these tips with your community.",
        "इन सुझावों को अपने समुदाय के साथ साझा करें।"
    ))

# REPORT SUSPICIOUS AGENT page
elif menu == get_text("🚩 Report Suspicious", "🚩 संदिग्ध रिपोर्ट करें"):
    header("Report a Suspicious Agent", "संदिग्ध एजेंट की रिपोर्ट करें")
    st.write(get_text(
        "Protect others by reporting suspicious behaviour.",
        "संदिग्ध व्यवहार की रिपोर्ट कर दूसरों की रक्षा करें।"
    ))
    col1, col2 = st.columns(2)
    name_value = col1.text_input(get_text("Agent Name/ID (optional)", "एजेंट नाम/आईडी (ऐच्छिक)"))
    detail_value = col2.text_area(get_text("Behaviour Details", "व्यवहार विवरण"))
    if st.button(get_text("Submit Report 🚩", "रिपोर्ट सबमिट करें 🚩")):
        if detail_value.strip():
            st.session_state.reports.append({
                'name': name_value.strip(),
                'details': detail_value.strip(),
                'lang': LANG,
                'dt': datetime.now()
            })
            st.success(get_text("Report submitted. Thank you!", "रिपोर्ट सबमिट हो गई। धन्यवाद!"))
        else:
            st.warning(get_text("Please enter behaviour details.", "कृपया व्यवहार विवरण दर्ज करें।"))
    st.image("https://i.imgur.com/lBBdIOu.png", width=240)

# COMMUNITY REPORTS page (cards)
elif menu == get_text("📋 Community Reports", "📋 समुदाय रिपोर्ट"):
    header("Community Reports", "समुदाय रिपोर्ट देखें")
    if st.session_state.reports:
        for idx, rp in enumerate(st.session_state.reports[::-1][:10], start=1):
            st.markdown(
                f"<div style='background-color: #fffbe7; border-left: 8px solid #f94144; padding:10px; border-radius:6px; margin-bottom:8px;'>"
                f"<b>{get_text('Report #','रिपोर्ट #')} {idx}</b><br>"
                f"{get_text('Agent','एजेंट')}: <b>{rp['name'] if rp['name'] else get_text('N/A','नहीं')}</b><br>"
                f"{get_text('Details','विवरण')}: {rp['details']}<br>"
                f"<span style='color: #4361ee'>{rp['dt'].strftime('%d-%b-%Y %I:%M %p')}</span>"
                f"</div>", unsafe_allow_html=True
            )
    else:
        st.info(get_text("No reports yet. Be the first to report suspicious activity!", "अभी तक कोई रिपोर्ट नहीं है। पहली रिपोर्ट आप दर्ज करें!"))

# HELP & FAQ page
elif menu == get_text("❓ Help & FAQs", "❓ सहायता / सामान्य प्रश्न"):
    header("Frequently Asked Questions", "सामान्य प्रश्न")
    st.markdown("<div style='background-color:#e9ecef;padding:10px;border-radius:6px;'>"
                "<b>💡 " + get_text("Your safety is our priority.", "आपकी सुरक्षा हमारी प्राथमिकता है।") + "</b></div>", unsafe_allow_html=True)
    with st.expander(get_text("ℹ How to verify an agent?", "ℹ एजेंट को कैसे सत्यापित करें?")):
        st.write(get_text(
            "Go to 'Verify Agent' page, enter their ID, and check their status. Verified agents show their details and photo.",
            "'एजेंट सत्यापित करें' पेज पर जाएँ, आईडी दर्ज करें और स्थिति देखें।"
        ))
    with st.expander(get_text("🚩 How to report suspicious agents?", "🚩 संदिग्ध एजेंट की रिपोर्ट कैसे करें?")):
        st.write(get_text(
            "Use 'Report Suspicious' to submit the incident. It is shared with the community, no personal info required.",
            "‘संदिग्ध रिपोर्ट करें’ पर जाकर घटना दर्ज करें। यह समुदाय के साथ साझा होता है।"
        ))
    with st.expander(get_text("🛡 Safety advice for families?", "🛡 परिवारों के लिए सुरक्षा सलाह?")):
        st.write(get_text(
            "Educate all family members, check IDs, and do not share private info with visitors.",
            "परिवार के सभी सदस्यों को प्रशिक्षित करें, आईडी जांचें और आगंतुकों से निजी जानकारी साझा न करें।"
        ))
    st.image("https://i.imgur.com/IsoJo2T.png", width=320)

# ---- Footer ----
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<div style='color:gray;text-align:center;font-size:15px'>"
    "© 2025 eBharosa | " + get_text("Made with ❤ for safe communities.", "सुरक्षित समुदायों के लिए ❤ के साथ बनाया गया।") +
    "</div>", unsafe_allow_html=True
)
