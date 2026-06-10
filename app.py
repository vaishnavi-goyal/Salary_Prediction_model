import streamlit as st
import pandas as pd
import joblib

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Salary Prediction System",
    page_icon="💰",
    layout="wide"
)

# ---------------- LOAD MODEL ----------------
model = joblib.load("salary_model.pkl")
encoders = joblib.load("encoders.pkl")

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>
.main {
    background-color: #f5f7fa;
}

.title {
    text-align: center;
    color: #2E86C1;
    font-size: 45px;
    font-weight: bold;
}

.subtitle {
    text-align: center;
    color: gray;
    font-size: 18px;
    margin-bottom: 20px;
}

.salary-card {
    background: linear-gradient(135deg,#2E86C1,#48C9B0);
    padding: 25px;
    border-radius: 15px;
    text-align: center;
    color: white;
    font-size: 28px;
    font-weight: bold;
}

.footer {
    text-align:center;
    color:gray;
    padding-top:30px;
}
</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.markdown(
    '<div class="title">💰 Job Salary Prediction System</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">Predict Employee Salary using Machine Learning</div>',
    unsafe_allow_html=True
)

st.divider()

# ---------------- SIDEBAR ----------------
st.sidebar.header("📋 Enter Details")

job_title = st.sidebar.selectbox(
    "💼 Job Title",
    encoders["job_title"].classes_
)

education = st.sidebar.selectbox(
    "🎓 Education Level",
    encoders["education_level"].classes_
)

industry = st.sidebar.selectbox(
    "🏭 Industry",
    encoders["industry"].classes_
)

company_size = st.sidebar.selectbox(
    "🏢 Company Size",
    encoders["company_size"].classes_
)

location = st.sidebar.selectbox(
    "📍 Location",
    encoders["location"].classes_
)

remote_work = st.sidebar.selectbox(
    "🏠 Remote Work",
    encoders["remote_work"].classes_
)

experience = st.sidebar.slider(
    "📈 Experience (Years)",
    0, 40, 1
)

skills = st.sidebar.slider(
    "🛠 Skills Count",
    1, 20, 5
)

certifications = st.sidebar.slider(
    "📜 Certifications",
    0, 5, 0
)

# ---------------- DASHBOARD ----------------
col1, col2, col3 = st.columns(3)

with col1:
    st.metric("Experience", f"{experience} Years")

with col2:
    st.metric("Skills", skills)

with col3:
    st.metric("Certificates", certifications)

st.divider()

# ---------------- PREDICT BUTTON ----------------
if st.button("🚀 Predict Salary", use_container_width=True):

    data = pd.DataFrame([{
        "job_title": encoders["job_title"].transform([job_title])[0],
        "experience_years": experience,
        "education_level": encoders["education_level"].transform([education])[0],
        "skills_count": skills,
        "industry": encoders["industry"].transform([industry])[0],
        "company_size": encoders["company_size"].transform([company_size])[0],
        "location": encoders["location"].transform([location])[0],
        "remote_work": encoders["remote_work"].transform([remote_work])[0],
        "certifications": certifications
    }])

    salary = model.predict(data)[0]

    st.success("✅ Salary Prediction Completed")

    st.markdown(
        f"""
        <div class="salary-card">
        Predicted Salary <br><br>
        💵 ${salary:,.0f}
        </div>
        """,
        unsafe_allow_html=True
    )

    # Salary Category
    if salary < 50000:
        st.warning("📉 Salary Category: Low")
    elif salary < 100000:
        st.info("📊 Salary Category: Medium")
    else:
        st.success("📈 Salary Category: High")

    st.balloons()

# ---------------- FOOTER ----------------
st.markdown(
    """
    <div class="footer">
    Developed using Streamlit & Machine Learning 🚀
    </div>
    """,
    unsafe_allow_html=True
)
