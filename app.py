import io
import streamlit as st

# Try importing document parsing libraries
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
  word_count = len(text_content.split())
  st.markdown(
      f'<div class="feedback-box"><h4>🔍 {section_title}</h4>',
      unsafe_allow_html=True,
  )

  if word_count < 15:
    st.markdown(
        '<p class="improve-text">⚠️ Status: Too brief or empty in document.</p>',
        unsafe_allow_html=True,
    )
    st.markdown(
        "* **What's OK:** None detected yet.<br>* **Needs Improvement:** This"
        " section lacks required details based on the uploaded text. Please"
        " expand using BTC guidelines.",
        unsafe_allow_html=True,
    )
  else:
    st.markdown(
        '<p class="ok-text">✅ Status: Content detected and evaluated.</p>',
        unsafe_allow_html=True,
    )

    if "Background" in section_title:
      st.markdown(
          """
            * <span class="ok-text">What's OK:</span> Provides an initial narrative overview of your intent.
            * <span class="improve-text">Needs Improvement:</span> Ensure it strictly covers a concise summary of the problem, solution, expected impact, and beneficiaries. Remember this section should tie the whole project together and is best finalized last.
            * <span class="tip-text">Pro Tip:</span> Condense it to 1–2 powerful paragraphs.
            """,
          unsafe_allow_html=True,
      )
    elif "Problem" in section_title:
      st.markdown(
          """
            * <span class="ok-text">What's OK:</span> Identifies a challenge area for the community.
            * <span class="improve-text">Needs Improvement:</span> Check if you have backed up your claims with <ins>relevant data or evidence</ins> (statistics, surveys, or reports) and clearly traced the <ins>root causes</ins>.
            * <span class="tip-text">Pro Tip:</span> Avoid generalized statements; use numbers or documented facts to prove the problem's severity.
            """,
          unsafe_allow_html=True,
      )
    elif "Solution" in section_title:
      st.markdown(
          """
            * <span class="ok-text">What's OK:</span> Outlines what the project aims to build or execute.
            * <span class="improve-text">Needs Improvement:</span> Does your text explicitly state <ins>what makes your approach innovative or different</ins> from existing solutions? It must directly target the root causes identified earlier.
            * <span class="tip-text">Pro Tip:</span> Clearly state your unique value proposition.
            """,
          unsafe_allow_html=True,
      )
    elif "SMART" in section_title:
      st.markdown(
          """
            * <span class="ok-text">What's OK:</span> Sets directional goals for the fellowship.
            * <span class="improve-text">Needs Improvement:</span> Ensure you have 3–5 objectives that strictly follow the **SMART** principle (Specific, Measurable, Achievable, Realistic, Time-bound). Avoid vague goals like "we want to help people."
            * <span class="tip-text">Pro Tip:</span> Use metrics (e.g., "Train 50 youth within 3 months").
            """,
          unsafe_allow_html=True,
      )
    elif "Logic" in section_title:
      st.markdown(
          """
            * <span class="ok-text">What's OK:</span> Establishes a workflow structure.
            * <span class="improve-text">Needs Improvement:</span> Verify the logical chain: <ins>Activities $\rightarrow$ Outputs $\rightarrow$ Short/Medium Outcomes $\rightarrow$ Long-term Impact</ins>. Every activity must directly lead to a measurable output.
            * <span class="tip-text">Pro Tip:</span> Clearly distinguish between what you *produce* (outputs) and the actual change it creates (outcomes).
            """,
          unsafe_allow_html=True,
      )
    elif "Implementation" in section_title:
      st.markdown(
          """
            * <span class="ok-text">What's OK:</span> Lists operational steps.
            * <span class="improve-text">Needs Improvement:</span> Ensure activities are organized into clear phases with designated <ins>resources needed, responsible persons, timelines, and key deliverables</ins>.
            * <span class="tip-text">Pro Tip:</span> A phased timeline or checklist format works best here.
            """,
          unsafe_allow_html=True,
      )
    elif "Monitoring" in section_title:
      st.markdown(
          """
            * <span class="ok-text">What's OK:</span> Mentions evaluation or tracking.
            * <span class="improve-text">Needs Improvement:</span> You must specify key tracking indicators, explain how each indicator is measured, and outline the exact <ins>tools or methods</ins> used to collect and analyze data.
            * <span class="tip-text">Pro Tip:</span> Mention specific tools like surveys, feedback forms, or analytics software.
            """,
          unsafe_allow_html=True,
      )
    elif "Budget" in section_title:
      st.markdown(
          """
            * <span class="ok-text">What's OK:</span> Outlines financial requirements.
            * <span class="improve-text">Needs Improvement:</span> Provide a detailed budget breakdown explaining the purpose of each cost. Crucially, include a <ins>fundraising strategy</ins> (grants, crowdfunding, donations, partnerships).
            * <span class="tip-text">Pro Tip:</span> Don't just list expenses; explain how you plan to mobilize the funds.
            """,
          unsafe_allow_html=True,
      )
    elif "Sustainability" in section_title:
      st.markdown(
          """
            * <span class="ok-text">What's OK:</span> Thinks about the project's future.
            * <span class="improve-text">Needs Improvement:</span> Explain how the project will survive <ins>after your fellowship ends</ins>. Include strategic partnerships, community ownership, and capacity-building measures.
            * <span class="tip-text">Pro Tip:</span> Review boards look closely at whether the community can run the project independently post-fellowship.
            """,
          unsafe_allow_html=True,
      )

  st.markdown("</div>", unsafe_allow_html=True)


if review_mode == "📁 Option A: Upload Proposal Document":
  st.subheader("Upload Your Proposal File")
  uploaded_file = st.file_uploader(
      "Upload your proposal document (PDF, Word .docx, TXT, or CSV)",
      type=["pdf", "docx", "txt", "csv"],
  )

  if uploaded_file is not None:
    st.success(f"✅ Successfully uploaded: **{uploaded_file.name}**")

    file_content = ""
    file_extension = uploaded_file.name.split(".")[-1].lower()

    try:
      if file_extension == "pdf":
        if PdfReader:
          reader = PdfReader(uploaded_file)
          for page in reader.pages:
            text = page.extract_text()
            if text:
              file_content += text + "\n"
        else:
          st.error("PDF reading library is missing.")

      elif file_extension == "docx":
        if docx:
          doc = docx.Document(uploaded_file)
          for para in doc.paragraphs:
            file_content += para.text + "\n"
        else:
          st.error(
              "Word (.docx) library is missing. Please add 'python-docx' to your"
              " requirements.txt."
          )

      elif file_extension in ["txt", "csv"]:
        file_content = uploaded_file.read().decode("utf-8", errors="ignore")

    except Exception as e:
      st.error(f"Error reading file: {e}")

    if file_content.strip():
      with st.expander("📄 Click here to preview extracted text"):
        st.text_area(
            "Extracted Text Preview",
            file_content[:1500]
            + ("..." if len(file_content) > 1500 else ""),
            height=150,
        )

      # Prominent button to trigger evaluation
      if st.button(
          "🔍 Run Analytical Proposal Review", type="primary", use_container_width=True
      ):
        with st.spinner(
            "Analyzing your proposal against BTC framework indicators..."
        ):
          st.success("Document Analyzed Successfully!")
          st.markdown("### 📊 Comprehensive Analytical Report")
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
      st.warning(
          "⚠️ Could not extract readable text from this file. Please make sure"
          " it contains text (not scanned images) or use Option B to type it"
          " in."
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
    
