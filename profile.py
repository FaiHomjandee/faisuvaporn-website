import streamlit as st

st.set_page_config(
    page_title="Suvaporn Homjandee",
    page_icon="🌻",
    layout="wide"
)

# ======================
# HEADER
# ======================
st.title("Suvaporn Homjandee")
st.subheader("phD Researcher")

col1, col2 = st.columns([1, 3])

with col1:
    st.image("profile.jpeg", width=250)

with col2:
    st.markdown("""
    ### About Me

    Welcome to my personal website.

    My work focuses on:
    - Sampling Methods
    - Artificial Intelligence
    - Deep Learning
    - Generative AI
    """)

# ======================
# LINKS
# ======================

st.markdown("---")
st.header("Professional Links")

c1, c2 = st.columns(2)

with c1:
    st.link_button(
        "GitHub",
        "https://github.com/FaiHomjandee"
    )

with c2:
    st.link_button(
        "LinkedIn",
        "https://linkedin.com/in/FaiSuvaporn"
    )

# ======================
# PUBLICATIONS
# ======================

st.markdown("---")
st.header("Publications")

papers = [
    {
        "title": "DeepCLSMOTE: deep class-latent synthetic minority oversampling technique",
        "year": "2025",
        "link": "https://www.semanticscholar.org/paper/DeepCLSMOTE%3A-deep-class-latent-synthetic-minority-Homjandee-Sinapiromsaran/a50710b0acdea54286b20638bb2ef9eb0814eb42"
    },
    {
        "title": "A Random Forest with Minority Condensation and Decision Trees for Class Imbalanced Problems",
        "year": "2021",
        "link": "https://www.researchgate.net/publication/354646989_A_Random_Forest_with_Minority_Condensation_and_Decision_Trees_for_Class_Imbalanced_Problems"
    }
]

for paper in papers:
    st.markdown(
        f"""
        **{paper['title']}** ({paper['year']})

        [View Publication]({paper['link']})
        """
    )

# ======================
# PROJECTS
# ======================

st.markdown("---")
st.header("Featured Projects")

projects = [
    {
        "name": "Derma-CoSMO",
        "desc": "Latent-space generative oversampling framework."
    },
    {
        "name": "Medical AI Platform",
        "desc": "Deep learning for diagnostic assistance."
    }
]

for project in projects:
    with st.expander(project["name"]):
        st.write(project["desc"])

# ======================
# CONTACT
# ======================

st.markdown("---")
st.header("📧 Contact")

st.info("Email: suvaporn.h@ku.th")

st.success("Thank you for visiting faisuvaporn.com")
