import streamlit as st
from supabase import create_client, Client

# Page settings
st.set_page_config(
    page_title="Katia Ferreira Portfolio",
    page_icon="🎬",
    layout="wide"
)

# Connect to Supabase securely
@st.cache_resource
def init_connection():
    url = st.secrets["SUPABASE_URL"]
    key = st.secrets["SUPABASE_KEY"]
    return create_client(url, key)

supabase = init_connection()

# Custom CSS
st.markdown("""
    <style>
    .main-title { font-size: 42px; font-weight: bold; color: #ffffff; text-align: center; }
    .subtitle { font-size: 20px; color: #aaaaaa; text-align: center; margin-bottom: 30px; }
    </style>
""", unsafe_allow_html=True)

# Sidebar menu
st.sidebar.title("🎬 Menu")
menu = st.sidebar.radio(
    "Select a page:",
    ["Home", "Showreel", "Photo Gallery", "CV", "Contact"]
)

# 1. Home
if menu == "Home":
    st.markdown('<p class="main-title">Katia Ferreira</p>', unsafe_allow_html=True)
    st.markdown('<p class="subtitle">Actress • Model • Performing Artist</p>', unsafe_allow_html=True)
    col1, col2 = st.columns([1, 2])
    with col1:
        st.info("🖼️ Profile image will go here\n\n(e.g., `st.image('assets/profile.jpg')`)")
    with col2:
        st.subheader("Welcome!")
        st.write("""
        Here you can write a detailed introduction about Katia Ferreira,
        her interests, her career, and what she wants the world to know about her.
        """)

# 2. Showreel
elif menu == "Showreel":
    st.title("🎥 Showreel and Videos")
    st.write("Acting, performance, or commercial videos will be displayed here.")

# 3. Photo Gallery
elif menu == "Photo Gallery":
    st.title("📸 Photo Gallery")
    st.write("A collection of different shoots and portfolio photos.")
    col1, col2, col3 = st.columns(3)
    with col1:
        st.info("Image 1")
    with col2:
        st.info("Image 2")
    with col3:
        st.info("Image 3")

# 4. CV
elif menu == "CV":
    st.title("📄 Experience and Education (CV)")
    st.subheader("🎭 Theatre and Film Work")
    st.write("- **Project Name 1** (Role Name) - Year")

# 5. Contact (Supabase Connection)
elif menu == "Contact":
    st.title("📬 Contact")
    st.write("Contact form for agencies or directors.")

    with st.form("contact_form", clear_on_submit=True):
        name = st.text_input("Your Name")
        email = st.text_input("Email")
        message = st.text_area("Message")
        submit = st.form_submit_button("Send Message")

        if submit:
            if name and email and message:
                try:
                    # Insert data into Supabase
                    data = {"name": name, "email": email, "message": message}
                    supabase.table("contact_messages").insert(data).execute()
                    st.success("Thank you! Your message has been sent successfully.")
                except Exception as e:
                    st.error(f"An error occurred: {e}")
            else:
                st.warning("Please fill in all fields before submitting.")

# Footer
st.markdown("---")
st.markdown(
    "<p style='text-align: center; color: gray;'>Katia Ferreira Portfolio • 2026</p>",
    unsafe_allow_html=True
)