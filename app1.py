import streamlit as st
from datetime import datetime

# -------- Sample Agent Database ----------
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

if "reports" not in st.session_state:
    st.session_state.reports = []
if "verifications" not in st.session_state:
    st.session_state.verifications = []
if "lang" not in st.session_state:
    st.session_state.lang = "en"
LANG = st.session_state.lang

def get_text(eng, hin):
    return hin if LANG == "hi" else eng

st.set_page_config(page_title="eBharosa", page_icon="🙏")

# ------------ Sidebar & Navigation ---------------
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

# -------- Colored Banner ----------
st.markdown("""
    <div style="background-color:#219ebc; color:white; padding:14px; border-radius:8px; font-size:28px; text-align:center; margin-bottom:10px;">
    🙏 eBharosa &nbsp;🌟
    </div>
""", unsafe_allow_html=True)

# -------- Welcome Box with Info --------
def home_content():
    st.markdown("""
        <div style="background-color:#d9ed92; padding:15px; border-radius:12px; margin-bottom:16px;">
            <h2 style="color:#14213d;">{}</h2>
            <p style="font-size:18px;">
            {}
            </p>
        </div>
    """.format(
        get_text("Welcome to eBharosa!", "ई भरोसा में स्वागत है!"),
        get_text(
            "Empowering citizens and families: verify salesmen/agents, read vital safety tips, and report suspicious persons in your locality.",
            "नागरिकों और परिवारों को सशक्त करें: विक्रेताओं/एजेंटों को सत्यापित करें, सुरक्षा सुझाव पढ़ें, और अपने क्षेत्र में संदिग्ध व्यक्तियों की रिपोर्ट करें।"
        )
    ), unsafe_allow_html=True)
    # Live Counters
    col1, col2, col3 = st.columns(3)
    col1.metric("✅ " + get_text("Agents Verified", "सत्यापित एजेंट"), f"{len(st.session_state.verifications)}")
    col2.metric("📖 " + get_text("Tips Read", "पढ़े गए सुझाव"), f"{70 + len(st.session_state.verifications)*2}")
    col3.metric("🚩 " + get_text("Reports", "रिपोर्ट्स"), f"{len(st.session_state.reports)}")
    st.success(get_text(
        "Stay informed and share eBharosa with your family and friends for a safer community.",
        "जानकारी रखें और अपने परिवार व दोस्तों से eBharosa साझा करें ताकि समुदाय सुरक्षित रहे।"
    ))

# ---------- Pages -------------------
if menu == get_text("🏠 Home", "🏠 होम"):
    home_content()

elif menu == get_text("🔎 Verify Agent", "🔎 एजेंट सत्यापित करें"):
    st.header(get_text("Agent Verification", "एजेंट सत्यापन"))
    st.write(get_text(
        "Enter the Agent ID below to check verification status.",
        "एजेंट आईडी दर्ज करें और सत्यापन स्थिति देखें।"
    ))
    agent_id = st.text_input(get_text("Agent ID", "एजेंट आईडी"))
    if st.button(get_text("Verify Now", "अब सत्यापित करें")):
        if agent_id.strip() in AGENTS:
            agent = AGENTS[agent_id.strip()]
            st.success(get_text("✅ Agent Verified!", "✅ एजेंट सत्यापित है!"))
            st.write("{}:** {}".format(get_text("Name", "नाम"), agent[get_text("name_en", "name_hi")]))
            st.write("{}:** {}".format(get_text("Company", "कंपनी"), agent[get_text("company_en", "company_hi")]))
            st.write("{}:** {}".format(get_text("Contact", "संपर्क"), agent["phone"]))
            st.session_state.verifications.append({'id': agent_id.strip(), 'dt': datetime.now()})
        elif agent_id.strip():
            st.error(get_text("❌ Agent NOT Found or NOT Verified!", "❌ एजेंट सत्यापित नहीं है!"))
        else:
            st.warning(get_text("Please enter Agent ID.", "कृपया एजेंट आईडी दर्ज करें।"))
    st.info(get_text(
        "💡 Tip: Only trust agents who are verified by eBharosa.",
        "💡 सुझाव: केवल eBharosa द्वारा सत्यापित एजेंटों पर विश्वास करें।"
    ))

elif menu == get_text("👤 Recent Verified Agents", "👤 हाल के सत्यापित एजेंट"):
    st.header(get_text("Recent Verified Agents", "हाल के सत्यापित एजेंट"))
    if st.session_state.verifications:
        for v in st.session_state.verifications[-5:][::-1]:
            aid = v['id']
            agent = AGENTS.get(aid)
            if agent:
                st.markdown(
                    "🔹 *{}* ({} {})<br>{}: {}<br><span style='color:#50a825'>{}: {}</span>".format(
                        agent[get_text('name_en','name_hi')], get_text('ID','आईडी'), aid,
                        get_text('Company','कंपनी'), agent[get_text('company_en','company_hi')],
                        get_text('Verified on','सत्यापन दिनांक'), v['dt'].strftime('%d-%b-%Y %I:%M %p')
                    ),
                    unsafe_allow_html=True
                )
                st.markdown("---")
    else:
        st.info(get_text("No agents have been verified recently.", "हाल ही में कोई एजेंट सत्यापित नहीं हुआ है।"))

elif menu == get_text("🛡 Safety Tips", "🛡 सुरक्षा सुझाव"):
    st.header(get_text("Safety Tips", "सुरक्षा सुझाव"))
    with st.expander(get_text("At Your Doorstep", "आपके दरवाजे पर")):
        st.write("• " + get_text("Ask for agent's ID and proof.", "एजेंट का आईडी और प्रमाण मांगे।"))
        st.write("• " + get_text("Check authenticity before allowing entry.", "प्रवेश से पहले प्रामाणिकता जांचें।"))
    with st.expander(get_text("Personal Safety", "व्यक्तिगत सुरक्षा")):
        st.write("• " + get_text("Never share OTP or bank info.", "ओटीपी या बैंक जानकारी साझा न करें।"))
        st.write("• " + get_text("Inform family before meeting agents.", "मुलाकात से पहले परिवार को बताएं।"))
    with st.expander(get_text("Online Safety", "ऑनलाइन सुरक्षा")):
        st.write("• " + get_text("Do not click suspicious links.", "संदिग्ध लिंक पर क्लिक न करें।"))
        st.write("• " + get_text("Beware of fake social profiles.", "फर्जी प्रोफाइल से सावधान रहें।"))
    st.success(get_text(
        "Share these tips with your community.",
        "इन सुझावों को अपने समुदाय के साथ साझा करें।"
    ))

elif menu == get_text("🚩 Report Suspicious", "🚩 संदिग्ध रिपोर्ट करें"):
    st.header(get_text("Report a Suspicious Agent", "संदिग्ध एजेंट की रिपोर्ट करें"))
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

elif menu == get_text("📋 Community Reports", "📋 समुदाय रिपोर्ट"):
    st.header(get_text("Community Reports", "समुदाय रिपोर्ट देखें"))
    if st.session_state.reports:
        for idx, rp in enumerate(st.session_state.reports[::-1][:10], start=1):
            st.markdown(
                "<div style='background-color:#fffbe7; border-left:6px solid #f94144; padding:8px; border-radius:5px; margin-bottom:7px;'>"
                "<b>{} {}</b> | {}: <b>{}</b><br>{}: {}<br><span style='color:#4361ee'>{}</span></div>".format(
                    get_text('Report #','रिपोर्ट #'), idx,
                    get_text('Agent','एजेंट'), rp['name'] if rp['name'] else get_text('N/A','नहीं'),
                    get_text('Details','विवरण'), rp['details'],
                    rp['dt'].strftime('%d-%b-%Y %I:%M %p')
                ),
                unsafe_allow_html=True
            )
    else:
        st.info(get_text("No reports yet. Be the first to report suspicious activity!", "अभी तक कोई रिपोर्ट नहीं है। पहली रिपोर्ट आप दर्ज करें!"))

elif menu == get_text("❓ Help & FAQs", "❓ सहायता / सामान्य प्रश्न"):
    st.header(get_text("Frequently Asked Questions", "सामान्य प्रश्न"))
    st.markdown("<div style='background-color:#e9ecef;padding:10px;border-radius:6px;'>"
                "<b>💡 " + get_text("Your safety is our priority.", "आपकी सुरक्षा हमारी प्राथमिकता है।") + "</b></div>", unsafe_allow_html=True)
    with st.expander(get_text("ℹ How to verify an agent?", "ℹ एजेंट को कैसे सत्यापित करें?")):
        st.write(get_text(
            "Go to 'Verify Agent' page, enter their ID, and check their status.",
            "'एजेंट सत्यापित करें' पेज पर जाएँ, आईडी दर्ज करें और स्थिति देखें।"
        ))
    with st.expander(get_text("🚩 How to report suspicious agents?", "🚩 संदिग्ध एजेंट की रिपोर्ट कैसे करें?")):
        st.write(get_text(
            "Use 'Report Suspicious' to submit the incident.",
            "‘संदिग्ध रिपोर्ट करें’ पर जाकर घटना दर्ज करें।"
        ))
    with st.expander(get_text("🛡 Safety advice for families?", "🛡 परिवारों के लिए सुरक्षा सलाह?")):
        st.write(get_text(
            "Educate all family members, check IDs, and do not share private info with visitors.",
            "परिवार के सभी सदस्यों को प्रशिक्षित करें, आईडी जांचें और आगंतुकों से निजी जानकारी साझा न करें।"
        ))

# ---- Footer ----
st.markdown("<hr>", unsafe_allow_html=True)
st.markdown(
    "<div style='color:gray;text-align:center;font-size:15px'>"
    "© 2025 eBharosa | " + get_text("Made with ❤ for safe communities.", "सुरक्षित समुदायों के लिए ❤ के साथ बनाया गया।") +
    "</div>", unsafe_allow_html=True
)
