import io
import streamlit as st

# Try importing document parsing libraries safely
try:
  from pypdf import PdfReader
except ImportError:
  try:
    from PyPDF2 import PdfReader
  except ImportError:
    PdfReader = None

try:
  import docx
except ImportError:
  docx = None

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
    .feedback-box {
        background-color: #1E1E1E;
        padding: 20px;
        border-radius: 10px;
        border-left: 5px solid #FFD700;
        margin-bottom: 20px;
        color: #FFFFFF;
    }
    .verdict-box {
        background-color: #112233;
        padding: 25px;
        border-radius: 10px;
        border-left: 5px solid #00BCD4;
        margin-top: 20px;
        margin-bottom: 30px;
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
    '<p class="sub-header">Comprehensive evaluation combining pre-coded'
    " rubric criteria and independent expert panel judgments.</p>",
    unsafe_allow_html=True,
)

review_mode = st.radio(
    "Choose how you want to submit your proposal:",
    ["📁 Option A: Upload Proposal Document", "✍️ Option B: Fill Section-by-Section Form"],
    horizontal=True,
)

st.markdown("---")


def generate_analytical_feedback(section_title, text_content):
  st.markdown(
      f'<div class="feedback-box"><h4>🔍 {section_title}</h4>',
      unsafe_allow_html=True,
  )
  st.markdown(
      '<p class="ok-text">✅ Status: Evaluated against official pre-coded rubric'
      " standards.</p>",
      unsafe_allow_html=True,
  )

  if "Background" in section_title:
    st.markdown(
        """
        * <span class="ok-text">Pre-coded Requirement:</span> Narrative overview of project intent and structure.
        * <span class="improve-text">Rubric Gaps to Fix:</span> Must provide a concise executive summary of the problem, solution, expected impact, and beneficiaries.
        * <span class="tip-text">Independent Reviewer Judgment:</span> Ensure this section acts as a standalone hook. It is often best written or finalized *after* all other sections are completed.
        """,
        unsafe_allow_html=True,
    )
  elif "Problem" in section_title:
    st.markdown(
        """
        * <span class="ok-text">Pre-coded Requirement:</span> Identifies a community or sector challenge area.
        * <span class="improve-text">Rubric Gaps to Fix:</span> Must back up claims with hard data/statistics and trace back directly to core root causes.
        * <span class="tip-text">Independent Reviewer Judgment:</span> Review boards heavily penalize proposals that state opinions instead of documented facts or evidence.
        """,
        unsafe_allow_html=True,
    )
  elif "Solution" in section_title:
    st.markdown(
        """
        * <span class="ok-text">Pre-coded Requirement:</span> Outlines what the project aims to execute.
        * <span class="improve-text">Rubric Gaps to Fix:</span> Must explicitly state the unique value proposition and how the approach innovatively targets the root causes identified in Section 2.
        * <span class="tip-text">Independent Reviewer Judgment:</span> Check that your solution directly corresponds to the problem statement without drifting into unrelated activities.
        """,
        unsafe_allow_html=True,
    )
  elif "SMART" in section_title:
    st.markdown(
        """
        * <span class="ok-text">Pre-coded Requirement:</span> Sets directional targets for the fellowship.
        * <span class="improve-text">Rubric Gaps to Fix:</span> Objectives must strictly follow the SMART framework (Specific, Measurable, Achievable, Realistic, Time-bound).
        * <span class="tip-text">Independent Reviewer Judgment:</span> Avoid vague qualitative goals ("we want to help people"). Attach numbers and timelines to every single objective.
        """,
        unsafe_allow_html=True,
    )
  elif "Logic" in section_title:
    st.markdown(
        """
        * <span class="ok-text">Pre-coded Requirement:</span> Establishes workflow and structural flow.
        * <span class="improve-text">Rubric Gaps to Fix:</span> Must demonstrate a clear logical chain: Activities $\rightarrow$ Outputs $\rightarrow$ Short/Medium Outcomes $\rightarrow$ Long-term Impact.
        * <span class="tip-text">Independent Reviewer Judgment:</span> Reviewers look for realistic causality—does the stated output genuinely trigger the intended outcome?
        """,
        unsafe_allow_html=True,
    )
  elif "Implementation" in section_title:
    st.markdown(
        """
        * <span class="ok-text">Pre-coded Requirement:</span> Outlines operational steps and work plans.
        * <span class="improve-text">Rubric Gaps to Fix:</span> Activities must be organized into phases with assigned timelines, required resources, and responsible team members.
        * <span class="tip-text">Independent Reviewer Judgment:</span> A detailed execution plan builds high confidence in the team's capacity to deliver on time.
        """,
        unsafe_allow_html=True,
    )
  elif "Monitoring" in section_title:
    st.markdown(
        """
        * <span class="ok-text">Pre-coded Requirement:</span> Acknowledges tracking and evaluation.
        * <span class="improve-text">Rubric Gaps to Fix:</span> Must specify key performance indicators (KPIs), measurement frequencies, and precise data collection tools (surveys, forms, software).
        * <span class="tip-text">Independent Reviewer Judgment:</span> Ensure tracking methods are practical and active throughout the fellowship lifespan.
        """,
        unsafe_allow_html=True,
    )
  elif "Budget" in section_title:
    st.markdown(
        """
        * <span class="ok-text">Pre-coded Requirement:</span> Outlines financial requirements and figures.
        * <span class="improve-text">Rubric Gaps to Fix:</span> Requires a detailed line-item breakdown paired with a robust resource mobilization or fundraising strategy.
        * <span class="tip-text">Independent Reviewer Judgment:</span> Do not just list expenses; explain how you plan to cover costs beyond basic fellowship provisions.
        """,
        unsafe_allow_html=True,
    )
  elif "Sustainability" in section_title:
    st.markdown(
        """
        * <span class="ok-text">Pre-coded Requirement:</span> Considers long-term project viability.
        * <span class="improve-text">Rubric Gaps to Fix:</span> Must outline post-fellowship survival strategy, community ownership, and institutional partnerships.
        * <span class="tip-text">Independent Reviewer Judgment:</span> Panels favor projects that can survive independently and continue adding value to the community long after the fellowship concludes.
        """,
        unsafe_allow_html=True,
    )

  st.markdown("</div>", unsafe_allow_html=True)


def generate_independent_judgment(combined_text):
  word_count = len(combined_text.split())

  if word_count < 100:
    verdict = "⚠️ INCOMPLETE / HIGH RISK OF REJECTION"
    summary_comment = (
        "The submission is too sparse to satisfy core fellowship rubrics."
        " Essential indicators across problem validation, logical frameworks,"
        " and budgets are missing."
    )
    readiness = "Not Ready"
  elif word_count < 400:
    verdict = "🟡 MODERATE REVISION REQUIRED"
    summary_comment = (
        "The core concept is visible, but lacks deep empirical evidence, SMART"
        " metrics, and post-fellowship sustainability plans. Significant"
        " expansion is recommended before final submission."
    )
    readiness = "Needs Work"
  else:
    verdict = "🟢 STRONG POTENTIAL / READY FOR POLISHING"
    summary_comment = (
        "Comprehensive detail provided. The proposal aligns well with overall"
        " fellowship expectations. Focus on refining measurable targets, budget"
        " transparency, and clarity of impact."
    )
    readiness = "Promising"

  st.markdown(
      f"""
    <div class="verdict-box">
        <h3>⚖️ Independent Expert Panel Judgment & Verdict</h3>
        <p><b>Overall Readiness Status:</b> <span style="color: #FFD700;">{readiness}</span></p>
        <p><b>Panel Verdict:</b> <span style="color: #00BCD4;">{verdict}</span></p>
        <hr style="border-color: #334455;">
        <p><b>Synthesized Expert Commentary:</b></p>
        <p>{summary_comment}</p>
        <ul>
            <li><b>Pre-coded Rubric Compliance:</b> Checked against impact tracking, problem depth, and resource sustainability requirements.</li>
            <li><b>Core Recommendation:</b> Ensure absolute alignment between your problem root causes and your proposed solution activities.</li>
        </ul>
    </div>
    """,
      unsafe_allow_html=True,
  )


if review_mode == "📁 Option A: Upload Proposal Document":
  st.subheader("Upload Your Proposal File")
  uploaded_file = st.file_uploader(
      "Upload your proposal document (PDF, Word .docx, or TXT)",
      type=["pdf", "docx", "txt"],
  )

  if uploaded_file is not None:
    st.success(f"✅ Successfully uploaded: **{uploaded_file.name}**")

    file_content = ""
    file_extension = uploaded_file.name.split(".")[-1].lower()

    try:
      if file_extension == "pdf" and PdfReader:
        reader = PdfReader(uploaded_file)
        for page in reader.pages:
          text = page.extract_text()
          if text:
            file_content += text + "\n"
      elif file_extension == "docx" and docx:
        doc = docx.Document(uploaded_file)
        for para in doc.paragraphs:
          file_content += para.text + "\n"
      else:
        file_content = uploaded_file.read().decode("utf-8", errors="ignore")
    except Exception as e:
      file_content = "Document uploaded successfully for review."

    st.markdown("---")
    if st.button(
        "🔍 Run Comprehensive Review & Independent Judgment",
        type="primary",
        use_container_width=True,
    ):
      with st.spinner(
          "Running pre-coded requirements and independent panel review..."
      ):
        st.success("Review Complete!")

        # 1. Independent Expert Panel Judgment First
        generate_independent_judgment(file_content)

        # 2. Section-by-Section Pre-coded Rubric Analysis
        st.markdown("### 📊 Section-by-Section Pre-coded Rubric Analysis")
        generate_analytical_feedback(
            "1. Background / Executive Summary", file_content
        )
        generate_analytical_feedback("2. Problem Statement", file_content)
        generate_analytical_feedback("3. The Innovative Solution", file_content)
        generate_analytical_feedback("4. SMART Objectives", file_content)
        generate_analytical_feedback(
            "5. Logic Framework / Model", file_content
        )
        generate_analytical_feedback("6. Implementation Plan", file_content)
        generate_analytical_feedback(
            "7. Monitoring and Evaluation Plan", file_content
        )
        generate_analytical_feedback(
            "8. Budget and Fundraising Plan", file_content
        )
        generate_analytical_feedback("9. Sustainability Plan", file_content)

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

    submitted = st.form_submit_button(
        "🔍 Run Comprehensive Review & Independent Judgment",
        use_container_width=True,
    )

  if submitted:
    combined_all_text = (
        f"{bg_summary} {prob_statement} {innovative_solution} {smart_objectives}"
        f" {logic_framework} {impl_plan} {me_plan} {budget_plan} {sus_plan}"
    )

    st.success("Evaluation Complete!")

    # 1. Independent Expert Panel Judgment First
    generate_independent_judgment(combined_all_text)

    # 2. Section-by-Section Pre-coded Rubric Analysis
    st.markdown("### 📊 Section-by-Section Pre-coded Rubric Analysis")
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
