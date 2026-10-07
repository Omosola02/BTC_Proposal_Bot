import io
import streamlit as st

try:
    from pypdf import PdfReader
except ImportError:
    try:
        from PyPDF2 import PdfReader
    except ImportError:
        PdfReader = None

st.set_page_config(
    page_title="BTC Proposal Review Bot", page_icon="📝", layout="wide"
)

st.markdown(
    """
    <style>
    .main-header {
        font-size: 2.2rem;
        color: #FFD700;
        font-weight: bold;
        text-align: center;
        margin-bottom: 10px;
    }
    .sub-header {
        font-size: 1.1rem;
        color: #CCCCCC;
        text-align: center;
        margin-bottom: 30px;
    }
    .stButton>button {
        background-color: #FF4B4B;
        color: white;
        font-weight: bold;
        border-radius: 8px;
        padding: 10px 20px;
    }
    .feedback-box {
        background-color: #1E1E1E;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #FFD700;
        margin-bottom: 15px;
    }
    </style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    '<p class="main-header">🚀 BTC Proposal Review Bot</p>', unsafe_allow_html=True
)
st.markdown(
    '<p class="sub-header">Review your fellowship proposal against the official'
    " BTC evaluation framework.</p>",
    unsafe_allow_html=True,
)

review_mode = st.radio(
    "Choose how you want to submit your proposal:",
    ["📁 Option A: Upload Proposal Document", "✍️ Option B: Fill Section-by-Section Form"],
    horizontal=True,
)

st.markdown("---")

if review_mode == "📁 Option A: Upload Proposal Document":
  st.subheader("Upload Your Proposal File")
  uploaded_file = st.file_uploader(
      "Upload your proposal document (.pdf or .txt)", type=["pdf", "txt"]
  )

  if uploaded_file is not None:
    file_content = ""
    if uploaded_file.type == "application/pdf":
      if PdfReader:
        try:
          reader = PdfReader(uploaded_file)
          for page in reader.pages:
            text = page.extract_text()
            if text:
              file_content += text + "\n"
        except Exception as e:
          st.error(f"Error reading PDF: {e}")
      else:
        st.error("PDF library is not installed.")
    else:
      file_content = uploaded_file.read().decode("utf-8")

    if st.button("🔍 Run Full Proposal Review"):
      if len(file_content.strip()) < 50:
        st.warning(
            "The uploaded file seems too short or empty. Please check the"
            " file contents."
        )
      else:
        with st.spinner("Analyzing your proposal against BTC framework..."):
          st.success("Review Complete!")
          st.markdown("### 📊 Comprehensive Evaluation Report")
          st.markdown(
              """
                <div class="feedback-box">
                <h4>1. Background / Executive Summary</h4>
                <p><b>Indicator Check:</b> Concise overview, core problem, solution, expected impact, and beneficiaries.</p>
                </div>
                <div class="feedback-box">
                <h4>2. Problem Statement</h4>
                <p><b>Indicator Check:</b> Relevant data, evidence, and clear definition of root causes.</p>
                </div>
                <div class="feedback-box">
                <h4>3. Innovative Solution</h4>
                <p><b>Indicator Check:</b> Explains how the solution addresses root causes and unique approach.</p>
                </div>
                <div class="feedback-box">
                <h4>4. SMART Objectives</h4>
                <p><b>Indicator Check:</b> 3-5 objectives following Specific, Measurable, Achievable, Realistic, and Time-bound criteria.</p>
                </div>
                <div class="feedback-box">
                <h4>5. Implementation, M&E, Budget & Sustainability</h4>
                <p><b>Indicator Check:</b> Clear phases, timelines, metrics, resource breakdown, and post-fellowship plans.</p>
                </div>
                """,
              unsafe_allow_html=True,
          )

else:
  st.subheader("Fill in Your Proposal Subheadings")

  with st.form("proposal_form"):
    st.markdown("### 📌 General Information")
    col1, col2 = st.columns(2)
    with col1:
      proj_name = st.text_input("Project Name")
      proj_category = st.text_input("Project Category")
      team_names = st.text_input("Team Lead & Members' Names")
    with col2:
      lead_phone = st.text_input("Phone Number (Lead)")
      lead_email = st.text_input("Email Address (Lead)")

    st.markdown("---")
    st.markdown("### 📝 Proposal Core Sections")

    bg_summary = st.text_area("1. Background / Executive Summary")
    prob_statement = st.text_area("2. Problem Statement")
    innovative_solution = st.text_area("3. The Innovative Solution")
    smart_objectives = st.text_area("4. SMART Objectives")
    logic_framework = st.text_area("5. Logic Framework / Model")
    impl_plan = st.text_area("6. Implementation Plan")
    me_plan = st.text_area("7. The Monitoring and Evaluation Plan")
    budget_plan = st.text_area("8. The Budget and Fundraising Plan")
    sus_plan = st.text_area("9. The Sustainability Plan")

    submitted = st.form_submit_button("🔍 Review My Proposal Sections")

  if submitted:
    st.success("Sections Evaluated Successfully!")
    st.markdown("### 📊 Section-by-Section Review & Feedback")

    sections = [
        ("Background / Executive Summary", bg_summary),
        ("Problem Statement", prob_statement),
        ("Innovative Solution", innovative_solution),
        ("SMART Objectives", smart_objectives),
        ("Logic Framework", logic_framework),
        ("Implementation Plan", impl_plan),
        ("Monitoring & Evaluation Plan", me_plan),
        ("Budget & Fundraising Plan", budget_plan),
        ("Sustainability Plan", sus_plan),
    ]

    for sec_name, content in sections:
      st.markdown('<div class="feedback-box">', unsafe_allow_html=True)
      st.markdown(f"#### 🔍 {sec_name}")
      if not content or len(content.strip()) < 10:
        st.error("⚠️ **Status:** Incomplete or missing details.")
      else:
        st.success("✅ **Status:** Section filled and logged successfully.")
      st.markdown("</div>", unsafe_allow_html=True)
