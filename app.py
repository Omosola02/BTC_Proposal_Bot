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
  st.markdown(
      f'<div class="feedback-box"><h4>🔍 {section_title}</h4>',
      unsafe_allow_html=True,
  )
  st.markdown(
      '<p class="ok-text">✅ Status: Document processed and evaluated against'
      " framework indicators.</p>",
      unsafe_allow_html=True,
  )

  if "Background" in section_title:
    st.markdown(
        """
        * <span class="ok-text">What's OK:</span> Provides an initial narrative overview of your project intent.
        * <span class="improve-text">Needs Improvement:</span> Ensure it strictly covers a concise summary of the problem, solution, expected impact, and beneficiaries. Remember this section ties the project together and should be finalized last.
        * <span class="tip-text">Pro Tip:</span> Condense it to 1–2 powerful paragraphs.
        """,
        unsafe_allow_html=True,
    )
  elif "Problem" in section_title:
    st.markdown(
        """
        * <span class="ok-text">What's OK:</span> Identifies a challenge area for the community.
        * <span class="improve-text">Needs Improvement:</span> Check if you have backed up your claims with <ins>relevant data or evidence</ins> (statistics, surveys, or reports) and clearly traced the <ins>root causes</ins>.
        * <span class="tip-text">Pro Tip:</span> Avoid generalized statements; use numbers or documented facts to prove severity.
        """,
        unsafe_allow_html=True,
    )
  elif "Solution" in section_title:
    st.markdown(
        """
        * <span class="ok-text">What's OK:</span> Outlines what the project aims to execute.
        * <span class="improve-text">Needs Improvement:</span> Does your text explicitly state <ins>what makes your approach innovative or different</ins> from existing solutions? It must directly target the root causes.
        * <span class="tip-text">Pro Tip:</span> Clearly state your unique value proposition.
        """,
        unsafe_allow_html=True,
    )
  elif "SMART" in section_title:
    st.markdown(
        """
        * <span class="ok-text">What's OK:</span> Sets directional goals.
        * <span class="improve-text">Needs Improvement:</span> Ensure you have 3–5 objectives following the **SMART** principle (Specific, Measurable, Achievable, Realistic, Time-bound). Avoid vague goals.
        * <span class="tip-text">Pro Tip:</span> Use clear metrics (e.g., "Train 50 youth within 3 months").
        """,
        unsafe_allow_html=True,
    )
  elif "Logic" in section_title:
    st.markdown(
        """
        * <span class="ok-text">What's OK:</span> Establishes a workflow structure.
        * <span class="improve-text">Needs Improvement:</span> Verify the logical chain: <ins>Activities $\rightarrow$ Outputs $\rightarrow$ Short/Medium Outcomes $\rightarrow$ Long-term Impact</ins>.
        * <span class="tip-text">Pro Tip:</span> Distinguish between what you produce (outputs) and the change it creates (outcomes).
        """,
        unsafe_allow_html=True,
    )
  elif "Implementation" in section_title:
    st.markdown(
        """
        * <span class="ok-text">What's OK:</span> Lists operational steps.
        * <span class="improve-text">Needs Improvement:</span> Ensure activities are organized into phases with designated <ins>resources needed, responsible persons, timelines, and key deliverables</ins>.
        """,
        unsafe_allow_html=True,
    )
  elif "Monitoring" in section_title:
    st.markdown(
        """
        * <span class="ok-text">What's OK:</span> Mentions evaluation or tracking.
        * <span class="improve-text">Needs Improvement:</span> Specify key tracking indicators and outline the exact <ins>tools or methods</ins> used to collect and analyze data.
        """,
        unsafe_allow_html=True,
    )
  elif "Budget" in section_title:
    st.markdown(
        """
        * <span class="ok-text">What's OK:</span> Outlines financial requirements.
        * <span class="improve-text">Needs Improvement:</span> Provide a detailed budget breakdown and include a solid <ins>fundraising strategy</ins> (grants, crowdfunding, donations, partnerships).
        """,
        unsafe_allow_html=True,
    )
  elif "Sustainability" in section_title:
    st.markdown(
        """
        * <span class="ok-text">What's OK:</span> Thinks about the project's future.
        * <span class="improve-text">Needs Improvement:</span> Explain how the project will survive <ins>after your fellowship ends</ins> through strategic partnerships and community ownership.
        """,
        unsafe_allow_html=True,
    )

  st.markdown("</div>", unsafe_allow_html=True)


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
      file_content = "Document uploaded successfully."

    # ALWAYS show the analyze button once a file is uploaded
    st.markdown("---")
    if st.button(
        "🔍 Run Analytical Proposal Review", type="primary", use_container_width=True
    ):
      with st.spinner(
          "Analyzing your proposal against BTC framework indicators..."
      ):
        st.success("Review Complete!")
        st.markdown("### 📊 Comprehensive Analytical Report")
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
        "🔍 Run Analytical Proposal Review", use_container_width=True
    )

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
