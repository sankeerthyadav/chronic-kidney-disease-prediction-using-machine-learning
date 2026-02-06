

import streamlit as st

def show_medicalinfo():
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

    with st.expander("ℹ️ General Medical Information", expanded=True):
        st.markdown('<div class="about-box">', unsafe_allow_html=True)


        st.markdown("### Risk Factors Section")
        st.markdown("""
        - ⚠️ **Factors to Consider for Chronic Kidney Disease (CKD)**:

        - **Age:** Kidney function naturally declines with age, especially after 60 years.
        - **High Blood Pressure:** Consistently elevated blood pressure can damage kidney blood vessels over time.
        - **Diabetes:** Poorly controlled blood sugar is a leading cause of CKD.
        - **Family History:** A family history of kidney disease increases your risk.
        - **Proteinuria:** Presence of excess protein (albumin) in urine signals kidney damage.
        - **Obesity:** Excess weight stresses kidneys and raises risk of diabetes and hypertension.
        - **Smoking:** Smoking reduces blood flow to kidneys and worsens kidney damage.
        - **Medications:** Long-term use of certain drugs (NSAIDs, some antibiotics) can harm kidneys.
        - **Cardiovascular Disease:** Heart disease and kidney disease are closely linked; each can worsen the other.
        - **Hydration & Diet:** Poor hydration and high salt or protein intake can strain kidneys.
        - **Serum Creatinine:** Indicates kidney filtration efficiency; higher levels suggest reduced kidney function.
        - **Blood Urea Nitrogen (BUN) / Blood Urea:** Waste product filtered by kidneys; elevated levels can mean kidney impairment.
        - **Red Blood Cells (RBC) in Urine:** Presence indicates bleeding or kidney/urinary tract issues.
        - **Sugar (Glucose) in Urine:** Normally absent; presence can signal diabetes or kidney damage.
        - **eGFR (Estimated Glomerular Filtration Rate):** Measures kidney filtering capacity; crucial for staging CKD.
        """)

        st.subheader("📚 Medical Reference Guide")

        st.markdown("### Age")
        st.markdown("""
        - Definition: Your age affects how well your kidneys work. As you get older, your kidneys slowly lose some of their filtering ability. This natural decline means older adults have a higher risk of kidney problems. Monitoring kidney health becomes more important with age.
        - Normal Reference:
        - ✅ No clinical “normal” value.
        - ⚠️ CKD risk increases significantly after age 60.
        """)

        st.markdown("### Blood Pressure")
        st.markdown("""
        - Definition: Blood pressure measures how hard your blood pushes against your artery walls. High blood pressure can damage the tiny blood vessels in your kidneys over time. This makes it harder for kidneys to filter waste properly. Controlling blood pressure helps protect your kidneys.
        - Normal Range:
        - Male & Female:
        - Normal: <120/80 mmHg
        - Elevated: 120–129/<80 mmHg
        - Stage 1 Hypertension: 130–139/80–89 mmHg
        - Stage 2 Hypertension: ≥140/90 mmHg
        """)

        st.markdown("### Specific Gravity (In Urine)")
        st.markdown("""
        - Definition: Specific gravity shows how concentrated your urine is. It tells us how well your kidneys can keep the right balance of water in your body. If your kidneys can’t concentrate urine properly, it might be a sign of kidney problems. This test helps doctors understand kidney function.
        - Normal Range:
        - Male & Female: 1.005 – 1.030
        """)

        st.markdown("### Albumin (Urine Protein Level)")
        st.markdown("""
        - Definition: Albumin is a protein that normally stays in your blood, not your urine. When kidneys are damaged, albumin leaks into the urine, which is a warning sign. The amount of albumin helps doctors see how serious the kidney damage might be. Regular checks can catch kidney problems early.
        - Dataset Levels:
        - 0: Normal
        - 1–2: Mild (A1)
        - 3: Moderate (A2 – moderately increased) which Requires Monitoring
        - 4–5: Severe (A3 – severely increased) which Requires intervention
        - Clinical Urine Albumin-Creatinine Ratio (UACR):
        - A1: <30 mg/g
        - A2: 30–300 mg/g
        - A3: >300 mg/g
        -  Generally Normal albumin level in an adult is between 3.5 to 5.5 grams per deciliter (g/dL)
        """)

        st.markdown("### Blood Glucose Random")
        st.markdown("""
        - Definition: Random blood glucose measures your blood sugar at any time of day. High levels may mean you have diabetes, which is a leading cause of kidney damage. Keeping blood sugar in check helps prevent or slow kidney disease. Doctors use this test to monitor your risk.
        - Normal Range:
        - Male & Female:
        - Normal: <140 mg/dL
        - Prediabetes: 140–199 mg/dL
        - Diabetes: ≥200 mg/dL
        """)

        st.markdown("### Blood Urea")
        st.markdown("""
        - Definition: Urea is a waste product formed when your body breaks down protein. Healthy kidneys filter urea out of your blood and into the urine. High urea levels in blood suggest your kidneys may not be working well. It’s a useful measure of kidney health.
        - Normal Range:
        - Male: 8–24 mg/dL
        - Female: 6–21 mg/dL
        """)

        st.markdown(" ### Sugar (Urine Glucose)")
        st.markdown("""
        - Definition: Normally, sugar is not found in urine. When sugar appears in urine, it usually means blood sugar is too high, like in diabetes. High blood sugar can harm your kidneys over time if not controlled. Finding sugar in urine signals the need to manage diabetes carefully.

        - Level 0 : Negative / Normal, No glucose detected in urine (healthy).
        - Level 1 : Represents a trace amount of glucose. This may occur temporarily after consuming a high-sugar meal or during stress. 100–250 Approximate Glucose Range (mg/dL).⚠️ May be benign; monitor.
        - Level 2 : + (Low) , Slightly elevated; could indicate early glucose spill due to high blood sugar. Approximate Glucose Range (mg/dL) 250–500,⚠️ Consider checking for diabetes risk.
        - Level 3 : ++ (Moderate), Moderate glucose presence; strong sign of impaired glucose metabolism. 500–1000 Approximate Glucose Range (mg/dL),	🚨 Suggestive of diabetes.
        - Level 4 : +++ (High),High level of glucose; kidney threshold clearly exceeded.1000–2000 Approximate Glucose Range (mg/dL), 🚨 Likely uncontrolled diabetes.
        - Level 5 : ++++ (Very High), Extremely high; indicates severe hyperglycemia and risk of complications. >2000 Approximate Glucose Range (mg/dL),🚨🚨 Medical attention urgently required.
        - Also they can be represented has Positive and Negative.
        """)

        st.markdown("### Serum Creatinine")
        st.markdown("""
        - Definition: Creatinine is a waste product created from normal muscle activity. Your kidneys remove creatinine from your blood. When kidneys don’t work well, creatinine builds up in the blood. Measuring creatinine helps doctors assess kidney function.
        - Normal Range:
        - Male: 0.74–1.35 mg/dL
          (Sometimes reported as 65.4 to 119.3 µmol/L)
        - Female: 0.59–1.04 mg/dL
          (Sometimes reported as 52.2 to 91.9 µmol/L)
        """)

        st.markdown("### Sodium")
        st.markdown("""
        - Definition: Sodium is an important mineral that helps control fluid balance and blood pressure in your body. Your kidneys regulate how much sodium stays in your blood or is removed in urine. If kidney function declines, sodium levels can become abnormal. Maintaining proper sodium levels is vital for health.
        - Normal Range:
        - Adult Males & Females:
          135 to 145 mEq/L
          (or mmol/L — both units are used interchangeably)
        """)

        st.markdown("### Potassium")
        st.markdown("""
        - Definition: Potassium helps your muscles and heart work properly. Your kidneys keep potassium levels balanced by removing extra amounts. When kidney function decreases, potassium can build up in your blood. Too much potassium is dangerous and needs close monitoring.
        - Normal Range:
        - Adult Males & Females:
          3.5 to 5.1 mEq/L
          (also reported as mmol/L)
        """)

        st.markdown("### Hemoglobin")
        st.markdown("""
        - Definition: Hemoglobin is the part of red blood cells that carries oxygen throughout your body. Kidney disease can lower hemoglobin levels by reducing the production of a hormone that helps make red blood cells. Low hemoglobin causes anemia, leading to fatigue and weakness. Treating anemia improves quality of life.
        - Normal Range:
        - Male: 13.8 to 17.2 g/dL
        - Female: 12.1 to 15.1 g/dL
        """)

        st.markdown("### Packed Cell Volume")
        st.markdown("""
        - Definition: PCV shows what percentage of your blood is made up of red blood cells. Low PCV means you have fewer red blood cells, which is common in kidney disease. This reduces oxygen delivery to your body’s tissues. Monitoring PCV helps assess anemia in CKD patients.
        - Normal Range:
        - Male: 40.7 to 50.3%
        - Female: 36.1 to 44.3%
        """)

        st.markdown("### White Blood Cell Count")
        st.markdown("""
        - Definition: White blood cells protect your body from infections and fight inflammation. A high WBC count can mean you have an infection or your body is under stress. In kidney disease, infections can be serious and need quick treatment. WBC count helps doctors monitor your health.)
        - Normal Range:
        - Male: 4,500 to 11,000 cells/μL
        - Female: 4,000 to 10,000 cells/μL
        """)

        st.markdown("### Red Blood Cell Count")
        st.markdown("""
        - Definition: Red blood cells carry oxygen from your lungs to the rest of your body. Kidney problems can reduce RBC production, causing anemia and making you tired. A low RBC count means your body isn’t getting enough oxygen. Managing RBC levels is important for overall well-being.
        - Normal Range:
        - Male: 4.7 to 6.1 million cells/μL
        - Female: 4.2 to 5.4 million cells/μL
        """)

        st.markdown("### Bacteria ( In Urine)")
        st.markdown("""
        - Presence of bacteria indicates a urinary tract infection or kidney infection , which can harm kidneys, especially in CKD patients.
          If no bacteria are found, the urine is free of infection.
        """)

        st.markdown("### Red Blood Cell ( In Urine)" )
        st.markdown("""
        - Normal: No or very few red blood cells are present in urine.
        - Abnormal: More than a few red blood cells may indicate bleeding or kidney problems, especially important in CKD.
        """)

        st.markdown("### Pedal Edema")
        st.markdown("""
        - Swelling in the feet or ankles caused by fluid buildup, often due to kidney problems.
          In CKD, it means the kidneys aren’t removing excess fluid properly.
        - Present: Indicates fluid retention and possible worsening kidney function.
        - Not Present: No swelling, which is a good sign for kidney health.
        """)

        st.markdown("### eGFR(Estimated Glomerular Filtration Rate)")
        st.markdown("""
        - Is a test that measures how well your kidneys are working by estimating how much blood they filter per minute. It's a key indicator of kidney health and is used to diagnose and monitor kidney disease.

        - **Stage 1: Normal or High Kidney Function**
          eGFR ≥ 90 mL/min/1.73 m²
          Kidneys work well but may have other signs of kidney damage.

        - **Stage 2: Mild Decrease in Kidney Function**
          eGFR 60–89 mL/min/1.73 m²
          Slight loss of function; usually no symptoms but needs monitoring.

        - **Stage 3a: Mild to Moderate Decrease**
          eGFR 45–59 mL/min/1.73 m²
          Noticeable decline; may have mild symptoms or complications.

        - **Stage 3b: Moderate to Severe Decrease**
          eGFR 30–44 mL/min/1.73 m²
          More serious loss of function; symptoms likely; treatment important.

        - **Stage 4: Severe Decrease**
          eGFR 15–29 mL/min/1.73 m²
          Severe kidney damage; preparation for dialysis or transplant may start.

        - **Stage 5: Kidney Failure (End-Stage Renal Disease)**
          eGFR < 15 mL/min/1.73 m²
          Kidneys can no longer support body; dialysis or transplant required.
        """)
