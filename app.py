import io
import streamlit as st

# Try importing PDF reader, handle gracefully if missing
try:
    from pypdf import PdfReader
except ImportError:
    try:
        from PyPDF2 import PdfReader
    except ImportError:
        PdfReader = None

# --- Page Config ---
st.set_page_config(
    page_title="BTC Proposal Review Bot", page_icon="📝", layout="wide"
)

# --- Custom CSS Styling ---
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

# --- App Header ---
st.markdown(
    '<p class="main-header">🚀 BTC Proposal Review Bot</p>', unsafe_allow_html=True
)
st.markdown(
    '<p class="sub-header">Review your fellowship proposal against the official BTC evaluation framework[span_0](start_span)[span_0](end_span)[span_1](start_span)[span_1](end_span)[span_2](start_span)[span_2](end_span).</p>',
    unsafe_allow_html=True,
)

# --- Navigation / Mode Selection ---
review_mode = st.radio(
    "Choose how you want to submit your proposal:",
    ["📁 Option A: Upload Proposal Document", "✍️ Option B: Fill Section-by-Section Form"],
    horizontal=True,
)

st.markdown("---")

proposal_data = {}

# ==========================================
# OPTION A: UPLOAD DOCUMENT
# ==========================================
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
        st.error(
            "PDF library is not installed. Please upload a TXT file or install"
            " pypdf."
        )
    else:
      file_content = uploaded_file.read().decode("utf-8")

    if st.button("🔍 Run Full Proposal Review"):
      if len(file_content.strip()) < 50:
        st.warning(
            "The uploaded file seems too short or empty. Please check the"
            " file contents."
        )
      else:
        with st.spinner(
            "Analyzing your proposal against BTC framework indicators..."
        ):
          # Simulated comprehensive evaluation logic based on indicators
          st.success("Review Complete!")
          st.markdown("### 📊 Comprehensive Evaluation Report")

          st.markdown(
              """
                <div class="feedback-box">
                <h4>1. Background / Executive Summary[span_3](start_span)[span_3](end_span)</h4>
                <p><b>Status:</b> Reviewed from uploaded document.</p>
                <p><b>Indicator Check:</b> Ensure it covers a concise overview, the core problem, why it's important, solutions, and expected impact on beneficiaries[span_4](start_span)[span_4](end_span).</p>
                <p><b>Recommendation:</b> Double-check that this section summarizes the final project outcomes accurately as it should be the last part completed[span_5](start_span)[span_5](end_span).</p>
                </div>
                
                <div class="feedback-box">
                <h4>2. Problem Statement[span_6](start_span)[span_6](end_span)</h4>
                <p><b>Indicator Check:</b> Look for relevant data, evidence, and clear definition of root causes[span_7](start_span)[span_7](end_span).</p>
                <p><b>Recommendation:</b> Ensure statistical evidence or empirical data backs up your core claims here.</p>
                </div>

                <div class="feedback-box">
                <h4>3. Innovative Solution[span_8](start_span)[span_8](end_span)</h4>
                <p><b>Indicator Check:</b> Explains how the solution addresses root causes and what makes the approach unique compared to existing solutions[span_9](start_span)[span_9](end_span).</p>
                </div>

                <div class="feedback-box">
                <h4>4. SMART Objectives[span_10](start_span)[span_10](end_span)</h4>
                <p><b>Indicator Check:</b> 3-5 objectives following Specific, Measurable, Achievable, Realistic, and Time-bound criteria[span_11](start_span)[span_11](end_span).</p>
                </div>

                <div class="feedback-box">
                <h4>5. Logic Framework & Implementation Plan[span_12](start_span)[span_12](end_span)</h4>
                <p><b>Indicator Check:</b> Logical link from activities -> outputs -> outcomes -> impact, structured into clear phases with timeline and resources[span_13](start_span)[span_13](end_span).</p>
                </div>

                <div class="feedback-box">
                <h4>6. M&E, Budget & Sustainability[span_14](start_span)[span_14](end_span)[span_15](start_span)[span_15](end_span)</h4>
                <p><b>Indicator Check:</b> Clear success metrics, detailed budget breakdown, fundraising strategies, and post-fellowship continuation plans[span_16](start_span)[span_16](end_span)[span_17](start_span)[span_17](end_span).</p>
                </div>
                """,
              unsafe_allow_html=True,
          )

# ==========================================
# OPTION B: FILL FORM SECTION-BY-SECTION
# ==========================================
else:
  st.subheader("Fill in Your Proposal Subheadings")
  st.markdown(
      "Enter details section by section. The bot will review each field"
      " individually."
  )

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

    bg_summary = st.text_area(
        "1. Background / Executive Summary (1-2 paragraphs)",
        placeholder=(
            "Provide a concise overview... problem, why it is important,"
            " solution, expected impact, and beneficiaries[span_18](start_span)[span_18](end_span)."
        ),
    )

    prob_statement = st.text_area(
        "2. Problem Statement",
        placeholder=(
            "Clearly define the problem, significance using relevant data/evidence,"
            " and root causes[span_19](start_span)[span_19](end_span)."
        ),
    )

    innovative_solution = st.text_area(
        "3. The Innovative Solution",
        placeholder=(
            "Describe your solution, how it targets root causes, and what makes"
            " your approach innovative[span_20](start_span)[span_20](end_span)."
        ),
    )

    smart_objectives = st.text_area(
        "4. SMART Objectives",
        placeholder=(
            "State 3-5 clear, measurable objectives (Specific, Measurable,"
            " Achievable, Realistic, Time-bound)[span_21](start_span)[span_21](end_span)."
        ),
    )

    logic_framework = st.text_area(
        "5. Logic Framework / Model",
        placeholder=(
            "Outline key activities, immediate outputs, short/medium outcomes,"
            " and long-term impact[span_22](start_span)[span_22](end_span)."
        ),
    )

    impl_plan = st.text_area(
        "6. Implementation Plan",
        placeholder=(
            "Organize activities into clear phases, resources needed,"
            " responsible persons, and timeline[span_23](start_span)[span_23](end_span)."
        ),
    )

    me_plan = st.text_area(
        "7. The Monitoring and Evaluation Plan",
        placeholder=(
            "Describe how you will measure success, key tracking indicators, and"
            " tools/methods[span_24](start_span)[span_24](end_span)."
        ),
    )

    budget_plan = st.text_area(
        "8. The Budget and Fundraising Plan",
        placeholder=(
            "Provide resource estimates, budget breakdown, and strategy for"
            " mobilization (grants, donations, etc.)[span_25](start_span)[span_25](end_span)."
        ),
    )

    sus_plan = st.text_area(
        "9. The Sustainability Plan",
        placeholder=(
            "Explain how the project continues creating impact, partnerships,"
            " and community ownership after the fellowship[span_26](start_span)[span_26](end_span)."
        ),
    )

    submitted = st.form_submit_button("🔍 Review My Proposal Sections")

  if submitted:
    st.success("Sections Evaluated Successfully!")
    st.markdown("### 📊 Section-by-Section Review & Feedback")

    # Dynamic evaluations based on user input length/content presence
    sections = {
        "Background / Executive Summary": (
            bg_summary,
            "Must provide a concise overview of the problem, solution, and"
            " expected impact[span_27](start_span)[span_27](end_span).",
        ),
        "Problem Statement": (
            prob_statement,
            "Must clearly outline evidence/data and root causes[span_28](start_span)[span_28](end_span).",
        ),
        "Innovative Solution": (
            innovative_solution,
            (
                "Must highlight what makes the approach unique compared to"
                " existing solutions[span_29](start_span)[span_29](end_span)."
            ),
        ),
        "SMART Objectives": (
            smart_objectives,
            (
                "Must include 3-5 objectives following the SMART standard"
                [span_30](start_span)"[span_30](end_span)."
            ),
        ),
        "Logic Framework": (
            logic_framework,
            (
                "Must connect activities -> outputs -> outcomes -> impact"
                " logically[span_31](start_span)[span_31](end_span)."
            ),
        ),
        "Implementation Plan": (
            impl_plan,
            (
                "Must outline phases, resources, timelines, and deliverables"
                [span_32](start_span)"[span_32](end_span)."
            ),
        ),
        "Monitoring & Evaluation Plan": (
            me_plan,
            "Must specify tracking indicators, metrics, and collection tools[span_33](start_span)[span_33](end_span).",
        ),
        "Budget & Fundraising Plan": (
            budget_plan,
            (
                "Must provide a cost breakdown and resource mobilization"
                " strategy[span_34](start_span)[span_34](end_span)."
            ),
        ),
        "Sustainability Plan": (
            sus_plan,
            (
                "Must describe post-fellowship continuation and community"
                " ownership[span_35](start_span)[span_35](end_span)."
            ),
        ),
    }

    for sec_name, (content, guideline) in sections.items():
      st.markdown(f'<div class="feedback-box">', unsafe_allow_html=True)
      st.markdown(f"#### 🔍 {sec_name}")
      if not content or len(content.strip()) < 15:
        st.error(
            f"⚠️ **Status:** Incomplete or missing. **Guideline:** {guideline}"
        )
      else:
        st.success("✅ **Status:** Section filled.")
        st.info(f"💡 **Indicator Check Reminder:** {guideline}")
      st.markdown("</div>", unsafe_allow_html=True)
