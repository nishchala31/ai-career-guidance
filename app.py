import streamlit as st
from google import genai

st.set_page_config(page_title="AI Career Guidance System", page_icon="🎓", layout="wide")

st.title("🎓 AI Career Guidance Platform")

option = st.sidebar.selectbox("Choose a Module", ["Career Guidance Chatbot", "Placement Predictor"])

if "GEMINI_API_KEY" in st.secrets:
    client = genai.Client(api_key=st.secrets["GEMINI_API_KEY"])

    if option == "Career Guidance Chatbot":
        st.subheader("💬 AI Career Guidance Assistant")
        user_query = st.text_input("Ask anything about career paths or interview tips:")
        if st.button("Ask AI"):
            if user_query:
                with st.spinner("Thinking..."):
                    try:
                        response = client.models.generate_content(
                            model="gemini-3.6-flash",
                            contents=user_query,
                        )
                        st.write(response.text)
                    except Exception as e:
                        st.error(f"Error: {e}")

    elif option == "Placement Predictor":
        st.subheader("📊 Campus Placement Prediction")
        cgpa = st.slider("CGPA", 0.0, 10.0, 7.5)
        internships = st.number_input("Number of Internships", 0, 5, 1)
        projects = st.number_input("Number of Projects", 0, 10, 2)

        if st.button("Predict Readiness"):
            readiness_score = (cgpa * 7) + (internships * 10) + (projects * 5)
            st.metric(label="Overall Readiness Score", value=f"{min(readiness_score, 100):.1f} / 100")
            