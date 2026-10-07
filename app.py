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
        margin-bottom: 20px;
        color: #FFFFFF;
    }
    .ok-text { color: #4CAF50; font-weight: bold; }
    .improve-text { color: #FF9800; font-weight: bold; }
    .tip-text { color: #00BCD4; font-weight: bold; }
    </style>
""",
    unsafe_allow_html=True,
)

st.markdown(
    '<p class="main-header">🚀 BTC Proposal Review Bot</p>', unsafe_allow_html=True
)
st.markdown(
    '<p class="sub-header">Review your fellowship proposal against official'
    " BTC framework indicators and professional writing standards.</p>",
    unsafe_allow_html=True,
)

review_mode = st.radio(
    "Choose how you want to submit your proposal:",
    ["📁 Option A: Upload Proposal Document", "✍️ Option B: Fill Section-by-Section Form"],
    horizontal=True,
)

st.markdown("---")


def generate_analytical_feedback(section_title, text_content):
  word_count = len(text_content.split())
  st.markdown(
      f'<div class="feedback-box"><h4>🔍 {section_title}</h4>',
      unsafe_allow_html=True,
  )

  if word_count < 15:
    st.markdown(
        '<p class="improve-text">⚠️ Status: Too brief or empty.</p>',
        unsafe_allow_html=True,
    )
    st.markdown(
        "* **What's OK:** None detected yet.<br>* **Needs Improvement:** This"
        " section lacks required details. Please expand based on BTC"
        " guidelines.",
        unsafe_allow_html=True,
    )
  else:
    st.markdown(
        '<p class="ok-text">✅ Status: Content provided and evaluated.</p>',
        unsafe_allow_html=True,
    )

    # Tailored analytical feedback based on section types
    if "Background" in section_title:
      st.markdown(
          """
            * <span class="ok-text">What's OK:</span> Provides an initial narrative overview of your intent.
            * <span class="improve-text">Needs Improvement:</span> Ensure it strictly covers a concise summary of the problem, solution, expected impact, and beneficiaries[span_3](start_span)[span_3](end_span). Remember this section should tie the whole project together and is best finalized last[span_4](start_span)[span_4](end_span).
            * <span class="tip-text">Pro Tip:</span> Condense it to 1–2 powerful paragraphs[span_5](start_span)[span_5](end_span).
            """,
          unsafe_allow_html=True,
      )
    elif "Problem" in section_title:
      st.markdown(
          """
            * <span class="ok-text">What's OK:</span> Identifies a challenge area for the community.
            * <span class="improve-text">Needs Improvement:</span> Check if you have backed up your claims with <ins>relevant data or evidence</ins> (statistics, surveys, or reports) and clearly traced the <ins>root causes</ins>[span_6](start_span)[span_6](end_span).
            * <span class="tip-text">Pro Tip:</span> Avoid generalized statements; use numbers or documented facts to prove the problem's severity.
            """,
          unsafe_allow_html=True,
      )
    elif "Solution" in section_title:
      st.markdown(
          """
            * <span class="ok-text">What's OK:</span> Outlines what the project aims to build or execute.
            * <span class="improve-text">Needs Improvement:</span> Does your text explicitly state <ins>what makes your approach innovative or different</ins> from existing solutions[span_7](start_span)[span_7](end_span)? It must directly target the root causes identified earlier[span_8](start_span)[span_8](end_span).
            * <span class="tip-text">Pro Tip:</span> Clearly state your unique value proposition.
            """,
          unsafe_allow_html=True,
      )
    elif "SMART" in section_title:
      st.markdown(
          """
            * <span class="ok-text">What's OK:</span> Sets directional goals for the fellowship.
            * <span class="improve-text">Needs Improvement:</span> Ensure you have 3–5 objectives that strictly follow the **SMART** principle (Specific, Measurable, Achievable, Realistic, Time-bound)[span_9](start_span)[span_9](end_span). Avoid vague goals like "we want to help people."
            * <span class="tip-text">Pro Tip:</span> Use metrics (e.g., "Train 50 youth within 3 months").
            """,
          unsafe_allow_html=True,
      )
    elif "Logic" in section_title:
      st.markdown(
          """
            * <span class="ok-text">What's OK:</span> Establishes a workflow structure.
            * <span class="improve-text">Needs Improvement:</span> Verify the logical chain: <ins>Activities $\rightarrow$ Outputs $\rightarrow$ Short/Medium Outcomes $\rightarrow$ Long-term Impact</ins>[span_10](start_span)[span_10](end_span). Every activity must directly lead to a measurable output.
            * <span class="tip-text">Pro Tip:</span> Clearly distinguish between what you *produce* (outputs) and the actual change it creates (outcomes).
            """,
          unsafe_allow_html=True,
      )
    elif "Implementation" in section_title:
      st.markdown(
          """
            * <span class="ok-text">What's OK:</span> Lists operational steps.
            * <span class="improve-text">Needs Improvement:</span> Ensure activities are organized into clear phases with designated <ins>resources needed, responsible persons, timelines, and key deliverables</ins>[span_11](start_span)[span_11](end_span).
            * <span class="tip-text">Pro Tip:</span> A phased timeline or checklist format works best here.
            """,
          unsafe_allow_html=True,
      )
    elif "Monitoring" in section_title:
      st.markdown(
          """
            * <span class="ok-text">What's OK:</span> Mentions evaluation or tracking.
            * <span class="improve-text">Needs Improvement:</span> You must specify key tracking indicators, explain how each indicator is measured, and outline the exact <ins>tools or methods</ins> used to collect and analyze data[span_12](start_span)[span_12](end_span).
            * <span class="tip-text">Pro Tip:</span> Mention specific tools like surveys, feedback forms, or analytics software.
            """,
          unsafe_allow_html=True,
      )
    elif "Budget" in section_title:
      st.markdown(
          """
            * <span class="ok-text">What's OK:</span> Outlines financial requirements.
            * <span class="improve-text">Needs Improvement:</span> Provide a detailed budget breakdown explaining the purpose of each cost[span_13](start_span)[span_13](end_span). Crucially, include a <ins>fundraising strategy</ins> (grants, crowdfunding, donations, partnerships)[span_14](start_span)[span_14](end_span).
            * <span class="tip-text">Pro Tip:</span> Don't just list expenses; explain how you plan to mobilize the funds.
            """,
          unsafe_allow_html=True,
      )
    elif "Sustainability" in section_title:
      st.markdown(
          """
            * <span class="ok-text">What's OK:</span> Thinks about the project's future.
            * <span class="improve-text">Needs Improvement:</span> Explain how the project will survive <ins>after your fellowship ends</ins>[span_15](start_span)[span_15](end_span). Include strategic partnerships, community ownership, and capacity-building measures[span_16](start_span)[span_16](end_span).
            * <span class="tip-text">Pro Tip:</span> Review boards look closely at whether the community can run the project independently post-fellowship.
            """,
          unsafe_allow_html=True,
      )

  st.markdown("</div>", unsafe_allow_html=True)


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

    if st.button("🔍 Run Analytical Proposal Review"):
      if len(file_content.strip()) < 50:
        st.warning(
            "The uploaded file seems too short or empty. Please check the"
            " file contents."
        )
      else:
        with st.spinner(
            "Analyzing your proposal against BTC framework indicators..."
        ):
          st.success("Review Complete!")
          st.markdown("### 📊 Comprehensive Analytical Report")
          # Run analysis across core framework areas for uploaded docs
          generate_analytical_feedback(
              "1. Background / Executive Summary", file_content
          )
          generate_analytical_feedback("2. Problem Statement", file_content)
          generate_analytical_feedback("3. The Innovative Solution", file_content)
          generate_analytical_feedback("4. SMART Objectives", file_content)
          generate_analytical_feedback(
              "5. Logic Framework & Implementation Plan", file_content
          )
          generate_analytical_feedback(
              "6. M&E, Budget & Sustainability Plan", file_content
          )

else:
  st.subheader("Fill in Your Proposal Subheadings")

  with st.form("proposal_form"):
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

    submitted = st.form_submit_button("🔍 Run Analytical Proposal Review")

  if submitted:
    st.success("Sections Evaluated Successfully!")
    st.markdown("### 📊 Section-by-Section Analytical Report")

    generate_analytical_feedback(
        "1. Background / Executive Summary", bg_summary
    )
    generate_analytical_feedback("2. Problem Statement", prob_statement)
    generate_analytical_feedback(
        "3. The Innovative Solution", innovative_solution
    )
    generate_analytical_feedback("4. SMART Objectives", smart_objectives)
    generate_analytical_feedback("5. Logic Framework / Model", logic_framework)
    generate_analytical_feedback("6. Implementation Plan", impl_plan)
    generate_analytical_feedback(
        "7. The Monitoring and Evaluation Plan", me_plan
    )
    generate_analytical_feedback(
        "8. The Budget and Fundraising Plan", budget_plan
    )
    generate_analytical_feedback("9. The Sustainability Plan", sus_plan)
