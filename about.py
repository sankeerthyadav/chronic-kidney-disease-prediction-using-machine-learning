
import streamlit as st

def show_about():
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Times+New+Roman&display=swap');

        .about-box {
            font-family: 'Times New Roman', serif;
            background-color: #ffffff;
            padding: 30px 40px;
            border-radius: 12px;
            box-shadow: 0 6px 18px rgba(0, 0, 0, 0.1);
            max-width: 850px;
            margin: 30px auto;
            font-size: 18px;
            line-height: 1.6;
            transition: all 0.3s ease-in-out;
        }

        .about-box:hover {
            transform: scale(1.01);
            box-shadow: 0 10px 24px rgba(0, 0, 0, 0.15);
        }

        .about-box h2 {
            color: #003366;
        }

        .stMarkdown {
            padding: 0 !important;
        }
    </style>
    """, unsafe_allow_html=True)

    with st.expander("ℹ️ About This Project", expanded=True):
        st.markdown('<div class="about-box">', unsafe_allow_html=True)

        st.markdown("## 🩺 Chronic Kidney Disease Prediction Using 🧠 Machine Learning")

        st.markdown("### 🌐 Project Overview")
        st.markdown("""
        This project utilizes a **machine learning model** to predict the risk of Chronic Kidney Disease (CKD) based on clinical and laboratory data provided by users.
        Its main objective is to enable early identification of CKD, supporting timely medical intervention and improving patient outcomes.

        🔍 **Key Features:**
        - Gathers structured patient information such as laboratory test results and vital signs.
        - Employs a trained machine learning model to estimate the likelihood of CKD.
        - Provides predictions through a user-friendly and interactive web application interface.
        """)

        st.markdown("### 📖 Chronic Kidney Disease Overview")
        st.markdown("""
        Chronic Kidney Disease (CKD) is a long-term condition where the kidneys are damaged and can't filter blood properly, leading to a buildup of waste in the body.
        It develops slowly and often shows no symptoms until the disease is advanced. Common causes include diabetes, high blood pressure, and heart disease, while age and gender also influence risk.
        Symptoms may include back or stomach pain, fever, vomiting, and rash. Prevention largely focuses on managing diabetes and high blood pressure to reduce the risk of kidney damage.
        """)

        st.markdown("### 💬 Motivation")
        st.markdown("""
        Chronic Kidney Disease (CKD) is a global health challenge, often going undiagnosed until it's too late.
        With this project, the goal is to explore how machine learning can assist healthcare professionals and researchers by offering early warnings based on clinical indicators.
        """)



        st.markdown("💡 **Why it matters:**")
        st.markdown("""
        - CKD is a serious condition that often goes undiagnosed until later stages.
        - Early prediction can encourage further medical testing and awareness.
        - Leveraging machine learning supports more accurate, data-driven decisions in healthcare.
        """)

        st.markdown("🛠️ **Technologies Used:**")
        st.markdown("""
        - **Python** (for data processing and modeling)
        - **Pandas**, **Scikit-learn** (for data science and ML)
        - **Streamlit** (for building the interactive web application)
        - **SHAP** (for model interpretability and feature contribution analysis)
        - **Google Colab** (for development and experimentation)
        """)

        st.markdown("🧪**Dataset Details:**")
        st.markdown("""
        - The model is trained on a public CKD dataset containing 400 patient records.
        - It includes lab values, symptoms, and clinical data such as age, blood pressure, creatinine levels, and more.
        - Data preprocessing included handling missing values, encoding categorical features, and normalization.
        """)

        st.markdown("⚙️ **Model Summary:**")
        st.markdown("""
        - A **Random Forest Classifier** was chosen for its robustness on small, mixed-type datasets.
        - The model achieved an **accuracy of 99%** during cross-validation.
        - Hyperparameter tuning and feature selection were used to improve performance.
        - Model interpretability was enhanced using **SHAP values** to understand feature contributions to predictions.
        - The model's confidence scores help identify predictions requiring further clinical review.
        """)

        st.markdown("### ⚠️ **Disclaimer:**")
        st.markdown("""
        This tool is for **educational and research use only**.
        It is **not a diagnostic tool** and should not be used for medical decisions.
        Always consult a licensed healthcare provider.
        > **Note:** This model provides a confidence score representing the predicted probability of the outcome.
        > Predictions with confidence below 70% are less reliable and should be interpreted cautiously.
        > In such cases, additional clinical evaluation and human review are strongly recommended to ensure accurate diagnosis.
        """)

        st.markdown('</div>', unsafe_allow_html=True)
