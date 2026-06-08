import streamlit as st
import pandas as pd
import joblib

# ---------------- PAGE CONFIG ----------------
st.markdown("""
<style>

/* Main Background */
.stApp{
    background-color:#f4f7fc;
}

/* Sidebar */
section[data-testid="stSidebar"]{
    background:#ffffff;
    border-right:1px solid #e5e7eb;
}

/* Header */
.title{
    text-align:center;
    color:#1e3a8a;
    font-size:55px;
    font-weight:bold;
}

.subtitle{
    text-align:center;
    color:#64748b;
    font-size:20px;
    margin-bottom:20px;
}

/* Metric Cards */
[data-testid="metric-container"]{
    background:white;
    padding:20px;
    border-radius:15px;
    border:1px solid #e5e7eb;
    box-shadow:0 4px 12px rgba(0,0,0,0.08);
}

/* Select Boxes */
.stSelectbox > div > div{
    border-radius:10px;
}

/* Predict Button */
.stButton > button{
    background:linear-gradient(90deg,#2563eb,#06b6d4);
    color:white;
    border:none;
    border-radius:12px;
    height:55px;
    font-size:18px;
    font-weight:bold;
    width:100%;
}

/* Salary Card */
.salary-card{
    background:linear-gradient(135deg,#2563eb,#06b6d4);
    padding:45px;
    border-radius:20px;
    text-align:center;
    color:white;
    margin-top:20px;
    box-shadow:0 8px 20px rgba(37,99,235,0.25);
}

.salary-card h1{
    font-size:60px;
    margin:10px 0;
}

.salary-card h2{
    font-size:28px;
    margin-bottom:10px;
}

/* Footer */
.footer{
    text-align:center;
    color:#64748b;
    padding-top:30px;
}

</style>
""", unsafe_allow_html=True)
# ---------------- HEADER ----------------

st.markdown("""
<div class="title">
💰 Job Salary Prediction System
</div>

<div class="subtitle">
Predict Employee Salary using Machine Learning
</div>
""", unsafe_allow_html=True)

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
