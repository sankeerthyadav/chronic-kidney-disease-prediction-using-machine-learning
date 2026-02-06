
import streamlit as st

def show_instructions():
    # Custom CSS styling for centered, elegant layout
    st.markdown("""
    <style>
        @import url('https://fonts.googleapis.com/css2?family=Times+New+Roman&display=swap');

        .instructions-box {
            font-family: 'Times New Roman', serif;
            background-color: #fff;
            padding: 30px 40px;
            border-radius: 12px;
            box-shadow: 0 6px 18px rgba(0, 0, 0, 0.1);
            max-width: 850px;
            margin: 30px auto;
            line-height: 1.6;
            font-size: 18px;
            transition: all 0.3s ease-in-out;
        }

        .instructions-box h2, .instructions-box h3 {
            color: #003366;
            margin-bottom: 10px;
        }

        .instructions-box:hover {
            transform: scale(1.01);
            box-shadow: 0 10px 24px rgba(0, 0, 0, 0.15);
        }

        .stMarkdown {
            padding: 0 !important;
        }
    </style>
    """, unsafe_allow_html=True)

    with st.expander("ℹ️ User Instructions", expanded=True):
        st.markdown('<div class="instructions-box">', unsafe_allow_html=True)

        st.markdown("## 📝 User Instructions")

        st.markdown("### 🔢 Input Guidelines")
        st.markdown("""
        - **Age**: Enter the patient’s age (2–90 years).
        - **Blood Pressure**: Enter systolic blood pressure in mmHg (50–180).
        - **Specific Gravity**: Urine test value between 1.005 and 1.025.
        - **Albumin & Sugar**: Use a scale of 0–5 based on lab results.
        - **Blood Glucose Random**: Random blood sugar in mg/dL (22–490).
        - **Blood Urea & Serum Creatinine**: Enter values from the patient’s lab report.
        - **Sodium & Potassium**: Use values in mEq/L or as reported by the lab.
        - **Hemoglobin & Packed Cell Volume**: Based on CBC results.
        - **White & Red Blood Cell Count**: Enter count per microliter (µL).

        ✅ Use dropdowns for categorical fields (e.g., Red Blood Cell: normal/abnormal).
        """)

        st.markdown("### 🎯 Tips for Better Accuracy")
        st.markdown("""
        - Use values directly from the patient’s lab results for best accuracy.
        - Avoid guessing or skipping fields if possible.
        - If uncertain, consult with a clinician or refer to medical records.
        """)

        st.markdown("### ⚠️ Disclaimer")
        st.markdown("""
        This application is intended for **educational and research purposes only**.

        - It is **not a diagnostic tool**.
        - Do **not** use it to make medical decisions.
        - Always consult a licensed healthcare provider for diagnosis and treatment.
        """)

        st.markdown("### 📊 How to Interpret Results")
        st.markdown("""
        - Enter all required clinical and laboratory values, then click **Predict** to generate the result.  
        - The model will output a prediction indicating whether Chronic Kidney Disease (CKD) is likely or not based on the input data.  
        - Along with the prediction, a confidence score shows the models certainty in its prediction.  
        - If the confidence score is below 70%, the model will advise further human review or clinical evaluation.  
        - The model also provides feature-level explanations using SHAP values, which show how each input factor influenced the risk prediction.  
        - Please remember, this prediction is **not a confirmed diagnosis** and should be used for informational purposes only. Always consult a healthcare professional for medical advice.
        """)

        st.markdown("### 🛠️ Troubleshooting")
        st.markdown("""
        - Make sure all fields are filled and within the suggested range.
        - If you see an error, check if any numeric field is left empty or has invalid input.
        - Refresh the page if inputs become unresponsive or if prediction doesn't run.
        """)

        st.markdown('</div>', unsafe_allow_html=True)
