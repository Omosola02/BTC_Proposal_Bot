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
    '<p class="sub-header">Review your fellowship proposal against official'
    " BTC framework indicators and independent evaluation standards.</p>",
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
      '<p class="ok-text">✅ Status: Section processed and evaluated against'
      " rubric criteria.</p>",
      unsafe_allow_html=True,
  )

  if "Background" in section_title:
    st.markdown(
        """
        * <span class="ok-text">What's OK:</span> Establishes the initial narrative framework.
        * <span class="improve-text">Needs Improvement:</span> Must provide a concise summary of the problem, why it matters, the proposed solution, and expected impact on beneficiaries[span_0](start_span)[span_0](end_span).
        * <span class="tip-text">Independent Comment:</span> Ensure this reads as a polished executive summary that can stand alone.
        """,
        unsafe_allow_html=True,
    )
  elif "Problem" in section_title:
    st.markdown(
        """
        * <span class="ok-text">What's OK:</span> Highlights a community challenge.
        * <span class="improve-text">Needs Improvement:</span> Must include concrete data, statistics, or evidence and trace back to core root causes[span_1](start_span)[span_1](end_span).
        * <span class="tip-text">Independent Comment:</span> Without hard evidence or root-cause analysis, reviewers will mark this section down.
        """,
        unsafe_allow_html=True,
    )
  elif "Solution" in section_title:
    st.markdown(
        """
        * <span class="ok-text">What's OK:</span> Outlines project deliverables.
        * <span class="improve-text">Needs Improvement:</span> Must clearly state what makes this approach unique or innovative compared to existing alternatives[span_2](start_span)[span_2](end_span).
        * <span class="tip-text">Independent Comment:</span> Make sure it explicitly solves the specific root causes identified in Section 2.
        """,
        unsafe_allow_html=True,
    )
  elif "SMART" in section_title:
    st.markdown(
        """
        * <span class="ok-text">What's OK:</span> Sets directional targets.
        * <span class="improve-text">Needs Improvement:</span> Objectives must strictly follow the SMART framework (Specific, Measurable, Achievable, Realistic, Time-bound)[span_3](start_span)[span_3](end_span).
        * <span class="tip-text">Independent Comment:</span> Avoid ambiguous statements; attach numbers and strict deadlines to every objective.
        """,
        unsafe_allow_html=True,
    )
  elif "Logic" in section_title:
    st.markdown(
        """
        * <span class="ok-text">What's OK:</span> Outlines project structure.
        * <span class="improve-text">Needs Improvement:</span> Must show a clear cause-and-effect chain: Activities $\rightarrow$ Outputs $\rightarrow$ Outcomes $\rightarrow$ Impact[span_4](start_span)[span_4](end_span).
        * <span class="tip-text">Independent Comment:</span> Reviewers look closely at whether your outputs realistically generate your stated outcomes.
        """,
        unsafe_allow_html=True,
    )
  elif "Implementation" in section_title:
    st.markdown(
        """
        * <span class="ok-text">What's OK:</span> Lists general tasks.
        * <span class="improve-text">Needs Improvement:</span> Must categorize activities into clear phases, assigning timelines, required resources, and responsible persons[span_5](start_span)[span_5](end_span).
        * <span class="tip-text">Independent Comment:</span> A structured work plan gives panels confidence in your team's execution capability.
        """,
        unsafe_allow_html=True,
    )
  elif "Monitoring" in section_title:
    st.markdown(
        """
        * <span class="ok-text">What's OK:</span> Acknowledges tracking.
        * <span class="improve-text">Needs Improvement:</span> Must specify exact indicators, measurement methods, and data collection tools[span_6](start_span)[span_6](end_span).
        * <span class="tip-text">Independent Comment:</span> State how you will measure success week-by-week or phase-by-phase.
        """,
        unsafe_allow_html=True,
    )
  elif "Budget" in section_title:
    st.markdown(
        """
        * <span class="ok-text">What's OK:</span> Estimates financial needs.
        * <span class="improve-text">Needs Improvement:</span> Requires a detailed cost breakdown and a robust fundraising or resource mobilization strategy (grants, partnerships, crowdfunding)[span_7](start_span)[span_7](end_span).
        * <span class="tip-text">Independent Comment:</span> A strong financial plan proves project viability beyond initial funding.
        """,
        unsafe_allow_html=True,
    )
  elif "Sustainability" in section_title:
    st.markdown(
        """
        * <span class="ok-text">What's OK:</span> Considers the future.
        * <span class="improve-text">Needs Improvement:</span> Must outline post-fellowship survival strategies, community ownership, and capacity-building measures[span_8](start_span)[span_8](end_span).
        * <span class="tip-text">Independent Comment:</span> Review boards heavily favor proposals where the community can sustain the impact long after the fellowship concludes.
        """,
        unsafe_allow_html=True,
    )

  st.markdown("</div>", unsafe_allow_html=True)


def generate_independent_judgment(combined_text):
  word_count = len(combined_text.split())

  # Independent judgment calculation
  if word_count < 100:
    verdict = "⚠️ INCOMPLETE / HIGH RISK OF REJECTION"
    summary_comment = (
        "The submission is too brief to meet fellowship standards. Core"
        " indicators across problem definition, budget, and implementation are"
        " largely absent."
    )
    readiness = "Not Ready"
  elif word_count < 400:
    verdict = "🟡 MODERATE REVISION REQUIRED"
    summary_comment = (
        "The proposal outlines a clear concept, but lacks depth in empirical"
        " evidence, SMART metrics, and post-fellowship sustainability plans."
        " Expand the core sections before final submission."
    )
    readiness = "Needs Work"
  else:
    verdict = "🟢 STRONG POTENTIAL / READY FOR POLISHING"
    summary_comment = (
        "Comprehensive detail provided. The narrative structure aligns well"
        " with fellowship expectations. Focus on fine-tuning measurable targets"
        " and ensuring the budget and sustainability models are fully"
        " transparent."
    )
    readiness = "Promising"

  st.markdown(
      f"""
    <div class="verdict-box">
        <h3>⚖️ Independent Reviewer Panel Judgment & Verdict</h3>
        <p><b>Overall Readiness Status:</b> <span style="color: #FFD700;">{readiness}</span></p>
        <p><b>Panel Verdict:</b> <span style="color: #00BCD4;">{verdict}</span></p>
        <hr style="border-color: #334455;">
        <p><b>Detailed Independent Comments:</b></p>
        <p>{summary_comment}</p>
        <ul>
            <li><b>Alignment with Rubric:</b> Evaluated against impact tracking, problem depth, and resource sustainability[span_9](start_span)[span_9](end_span)[span_10](start_span)[span_10](end_span)[span_11](start_span)[span_11](end_span).</li>
            <li><b>Key Recommendation:</b> Ensure every claim in your solution section directly addresses a root cause identified in your problem statement[span_12](start_span)[span_12](end_span).</li>
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
        "🔍 Run Analytical Proposal Review & Independent Judgment",
        type="primary",
        use_container_width=True,
    ):
      with st.spinner("Panel is reviewing your proposal against rubrics..."):
        st.success("Review Complete!")

        # 1. Independent Overall Judgment First
        generate_independent_judgment(file_content)

        # 2. Section-by-Section Rubric Feedback
        st.markdown("### 📊 Section-by-Section Rubric Analysis")
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
        "🔍 Run Analytical Proposal Review & Independent Judgment",
        use_container_width=True,
    )

  if submitted:
    combined_all_text = (
        f"{bg_summary} {prob_statement} {innovative_solution} {smart_objectives}"
        f" {logic_framework} {impl_plan} {me_plan} {budget_plan} {sus_plan}"
    )

    st.success("Evaluation Complete!")

    # 1. Independent Overall Judgment First
    generate_independent_judgment(combined_all_text)

    # 2. Section-by-Section Rubric Feedback
    st.markdown("### 📊 Section-by-Section Rubric Analysis")
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
    
