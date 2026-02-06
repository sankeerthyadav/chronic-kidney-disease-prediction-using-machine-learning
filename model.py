
import streamlit as st
import numpy as np
import pandas as pd
import shap
import matplotlib.pyplot as plt
import pickle
import streamlit.components.v1 as components

def st_shap(plot, height=None):
    shap_html = f"<head>{shap.getjs()}</head><body>{plot.html()}</body>"
    components.html(shap_html, height=height or 400, scrolling=True)

def show_model():

    # Load the model
    with open('ckd_random_forest_model.pkl', 'rb') as model_file:
        rf = pickle.load(model_file)

    # ==========================
    # eGFR Calculation Function
    # ==========================
    def calculate_egfr_ckd_epi_2021(serum_creatinine, age, gender):
        gender = gender.lower()
        if gender == 'female':
            k = 0.7
            alpha = -0.241
            gender_factor = 1.012
        elif gender == 'male':
            k = 0.9
            alpha = -0.302
            gender_factor = 1.0
        else:
            raise ValueError("Gender must be 'male' or 'female'.")
        scr_k = serum_creatinine / k
        egfr = 142 * (min(scr_k, 1) ** alpha) * (max(scr_k, 1) ** -1.200) * (0.9938 ** age) * gender_factor
        return round(egfr, 2)

    # ==========================
    # Final Interpretation Logic
    # ==========================
    def generate_ckd_interpretation(
        creatinine, age, gender,
        albumin, blood_urea, hemoglobin,
        hypertension, diabetes_mellitus, anemia
    ):
        report = []
        egfr_value = calculate_egfr_ckd_epi_2021(creatinine, age, gender)

        # eGFR Stage
        if egfr_value >= 90:
            stage = "G1 (Normal or High)"
            desc = ("Your eGFR indicates Stage G1, meaning kidney filtration is within the normal or high range. "
                    "At this stage, kidney damage may still exist if there are signs like protein in the urine or imaging abnormalities. "
                    "It’s important to monitor other indicators, especially in patients with diabetes or hypertension.")
        elif 60 <= egfr_value < 90:
            stage = "G2 (Mildly Decreased)"
            desc = ("Your eGFR suggests Stage G2, which represents mildly decreased kidney function. "
                    "This may be considered normal in older adults but can indicate early CKD if other markers of kidney damage are present. "
                    "Further evaluation of urine and imaging findings is essential to confirm CKD diagnosis.")
        elif 45 <= egfr_value < 60:
            stage = "G3a (Mild to Moderate Decrease)"
            desc = ("Your eGFR falls under Stage G3a CKD, showing a mild to moderate reduction in kidney function. "
                    "This stage is usually asymptomatic but increases the risk for cardiovascular disease and CKD progression. "
                    "Regular monitoring of blood pressure, albuminuria, and metabolic complications is recommended.")
        elif 30 <= egfr_value < 45:
            stage = "G3b (Moderate to Severe Decrease)"
            desc = ("You are in Stage G3b CKD, with moderately to severely reduced kidney function. "
                    "Symptoms like fatigue, fluid retention, or high blood pressure may appear at this stage. "
                    "Clinical management should focus on slowing decline and preparing for more advanced care if needed.")
        elif 15 <= egfr_value < 30:
            stage = "G4 (Severe Decrease)"
            desc = ("Your eGFR is in the Stage G4 range, indicating severely impaired kidney function. "
                    "At this stage, patients are at high risk for complications like anemia, bone disease, and electrolyte imbalances. "
                    "Nephrology referral is strongly recommended, along with planning for renal replacement therapy.")
        else:
            stage = "G5 (Kidney Failure)"
            desc = ("Your eGFR is below 15, which means you are in Stage G5 CKD — also known as end-stage kidney disease (ESKD). "
                    "This requires urgent evaluation for dialysis or kidney transplant. "
                    "Management focuses on symptom control, electrolyte balance, and renal replacement preparation.")

        report.append(
            f"<h4>eGFR Status: <strong>{stage}</strong></h4>"
            f"<P>Your estimated glomerular filtration rate (eGFR) is <strong>{egfr_value} mL/min/1.73m²</strong></p>"
            f"<p>which falls into <strong>Stage {stage.split()[0]}</strong>.</p>"
            f"<p>{desc}</P>"
        )


        # Albuminuria from level 0–5
        albumin_levels = {
            0: ("A1 (Normal)", "Your albuminuria level is normal... minimal kidney damage. Continue routine checks."),
            1: ("A1 (Mildly Increased)", "Mild increase... early sign of kidney damage. Monitor and control risks."),
            2: ("A2 (Moderately Increased)", "Moderate protein in urine... kidney stress. Requires monitoring."),
            3: ("A2 (Moderately Severe)", "Moderately severe... clear kidney damage. Clinical management advised."),
            4: ("A3 (Severely Increased)", "Severely elevated... risk for progression. Needs intensive management."),
            5: ("A3 (Nephrotic Range)", "Nephrotic range... advanced disease. Urgent nephrology referral advised.")
        }

        if albumin in albumin_levels:
            a_stage, a_desc = albumin_levels[albumin]
            report.append(f"<p><strong>Albuminuria🧪: {a_stage}</strong><br>{a_desc}</p>")
        else:
            report.append("<p><strong>Albuminuria🧪: Invalid Level</strong><br>The provided albumin level is outside expected range.</p>")

        # Hypertension
        if hypertension == 'yes':
            report.append("<p><strong>Hypertension⚠️💓: Present</strong><br>Elevated BP contributes to kidney damage. Strict BP control is needed.</p>")
        else:
            report.append("<p><strong>Hypertension⚠️💓: Not Present</strong><br>Normal BP is protective. Continue regular monitoring.</p>")

        # Diabetes
        if diabetes_mellitus == 'yes':
            report.append("<p><strong>Diabetes Mellitus📉: Present</strong><br>Diabetes is a major CKD cause. Maintain strict glucose control.</p>")
        else:
            report.append("<p><strong>Diabetes Mellitus📉: Not Present</strong><br>Absence reduces risk. Maintain healthy lifestyle.</p>")

        # Hemoglobin
        if gender == "male":
            if hemoglobin < 13.8:
                report.append(f"<p><strong>Hemoglobin🩸: {hemoglobin} g/dL (Low)</strong><br>Possible anemia. Causes include iron deficiency, chronic disease (e.g., CKD), or blood loss. Monitor for fatigue, pallor, and shortness of breath. Further evaluation recommended.</p>")
            elif hemoglobin > 17.2:
                report.append(f"<p><strong>Hemoglobin🩸: {hemoglobin} g/dL (High)</strong><br>May result from dehydration, smoking, or underlying conditions like polycythemia. Consider diagnostic follow-up.</p>")
            else:
                report.append(f"<p><strong>Hemoglobin🩸: {hemoglobin} g/dL (Normal)</strong><br>Hemoglobin is within normal range. Continue routine monitoring.</p>")

        elif gender == "female":
            if hemoglobin < 12.1:
                report.append(f"<p><strong>Hemoglobin🩸: {hemoglobin} g/dL (Low)</strong><br>Possible anemia. Causes include iron deficiency, chronic illness, or blood loss. Monitor symptoms and assess iron status if needed.</p>")
            elif hemoglobin > 15.1:
                report.append(f"<p><strong>Hemoglobin🩸: {hemoglobin} g/dL (High)</strong><br>Could be related to dehydration, smoking, or medical conditions like polycythemia vera. Further testing may be needed.</p>")
            else:
                report.append(f"<p><strong>Hemoglobin🩸: {hemoglobin} g/dL (Normal)</strong><br>Hemoglobin is within normal range. No action needed beyond routine care.</p>")

        else:
            report.append("<p><strong>Error:</strong> Gender must be 'male' or 'female'.</p>")

        # Anemia
        if anemia == 'yes':
            report.append("<p><strong>Anemia🩸😴: Present</strong><br>Reduced red cell production common in CKD. May need treatment.</p>")
        else:
            report.append("<p><strong>Anemia🩸😴: Not Present</strong><br>Anemia absent currently. Reassess periodically.</p>")

        return "".join(report)


    # ==========================
    # Streamlit App UI
    # ==========================

    st.title("🔬 Chronic Kidney Disease Prediction & Interpretation")

    st.header("🔢 Enter Patient Data")

    # Create a clean 2-column layout
    with st.container():
        col1, col2 = st.columns(2)

        with col1:
            age = st.number_input("Age👵👴 (years)", min_value=1, max_value=90, value=51)
            blood_pressure = st.number_input("Blood Pressure 💓(mmHg)", min_value=50, max_value=180, value=76)
            specific_gravity = st.number_input("Specific Gravity💧", min_value=1.005, max_value=1.025, value=1.017,step=0.001,format="%.3f")
            blood_glucose_random = st.number_input("Blood Glucose Random🧍‍♂️🩸 (mg/dL)", min_value=22.0, max_value=490.0, value=148.34)
            blood_urea = st.number_input("Blood Urea💉 (mg/dL)", min_value=1.5, max_value=391.0, value=58.03)
            serum_creatinine = st.number_input("Serum Creatinine🧬 (mg/dL)", min_value=0.4, max_value=76.0, value=3.04,step=0.001,format="%.3f")
            potassium = st.number_input("Potassium💥 (mEq/L)", min_value=2.5, max_value=47.0, value=4.68)

        with col2:
            red_blood_cell_count = st.number_input("Red Blood Cell Count🩸", min_value=2.1, max_value=8.0, value=4.73)
            hemoglobin = st.number_input("Hemoglobin🩸 (g/dL)", min_value=3.1, max_value=17.8, value=12.60)
            white_blood_cell_count = st.number_input("White Blood Cell Count⚪🦠", min_value=2200, max_value=26400, value=8374)
            sodium = st.number_input("Sodium🧫 (mEq/L)", min_value=4.5, max_value=163.0, value=137.57)
            packed_cell_volume = st.number_input("Packed Cell Volume🧪", min_value=9.0, max_value=54.0, value=38.77)
            gender = st.selectbox("Gender🚹 / 🚺", ["male", "female"])
            albumin = st.selectbox("Albuminuria Level🧪", [0, 1, 2, 3, 4, 5])
            sugar = st.selectbox("Sugar Level📉", [0, 1, 2, 3, 4, 5])

    # More conditions
    st.subheader("🧾 Additional Medical Conditions")
    col3, col4 = st.columns(2)

    with col3:
        red_blood_cell = st.selectbox("Red Blood Cell🔴", ["normal", "abnormal"])
        pus_cell = st.selectbox("Pus Cell🧫", ["normal", "abnormal"])
        pus_cell_clumps = st.selectbox("Pus Cell Clumps🔬", ["present", "not present"])
        bacteria = st.selectbox("Bacteria🦠", ["present", "not present"])

    with col4:
        hypertension = st.selectbox("Hypertension⚠️💓", ["yes", "no"])
        diabetes_mellitus = st.selectbox("Diabetes Mellitus📈", ["yes", "no"])
        cad = st.selectbox("Coronary Artery Disease🫀", ["yes", "no"])
        appetite = st.selectbox("Appetite🍽️", ["good", "poor"])
        pedal_edema = st.selectbox("Pedal Edema🦶💧", ["yes", "no"])
        anemia = st.selectbox("Anemia🩸😴", ["yes", "no"])


    if st.button("🧠 Predict Chronic Kidney Disease"):
        # Prepare input for model
        model_input = np.array([[age,
                             blood_pressure,
                             specific_gravity,
                             albumin,
                             sugar,
                             1 if red_blood_cell == 'normal' else 0,  # Encode red_blood_cell
                             1 if pus_cell == 'normal' else 0,  # Encode pus_cell
                             1 if pus_cell_clumps == 'present' else 0,  # Encode pus_cell_clumps
                             1 if bacteria == 'present' else 0,  # Encode bacteria
                             blood_glucose_random,
                             blood_urea,
                             serum_creatinine,
                             sodium,
                             potassium,
                             hemoglobin,
                             packed_cell_volume,
                             white_blood_cell_count,
                             red_blood_cell_count,
                             1 if hypertension == 'yes' else 0,  # Encode hypertension
                             1 if diabetes_mellitus == 'yes' else 0,  # Encode diabetes_mellitus
                             1 if cad == 'yes' else 0,  # Encode coronary_artery_disease
                             1 if appetite == 'good' else 0,  # Encode appetite
                             1 if pedal_edema == 'yes' else 0,  # Encode pedal_edema
                             1 if anemia == 'yes' else 0,]])  # Encode anemia

        prediction = rf.predict(model_input)[0]
        prediction_proba_all = rf.predict_proba(model_input)[0]
        prediction_proba = prediction_proba_all[prediction]   # Probability for predicted class (0 or 1)


        # Display result
        st.subheader("🧠 Chronic Kidney Disease Prediction")

        if prediction == 1:
            st.error("*CKD Prediction: Positive*")
            st.markdown("There is *Chronic Kidney Disease* based on the entered parameters. Further evaluation and laboratory tests are recommended to confirm the diagnosis.")
        else:
            st.success("*CKD Prediction: Negative*")
            st.markdown("There is no *Chronic Kidney Disease* based on the entered parameters. However, regular monitoring is advised.")
        # Display confidence score for both cases
        st.markdown(f"**Model Confidence Score:** {prediction_proba:.2f}")
        # Additional dynamic warning if model confidence is low
        if prediction_proba < 0.7:
            st.warning("⚠️ The model's confidence is below 70%. A human review or further clinical evaluation is strongly recommended.")

    # Prepare the model input for interpretation (You don't need to re-enter the data)
    model_input = np.array([[
                         age,
                         blood_pressure,
                         specific_gravity,
                         albumin,
                         sugar,
                         1 if red_blood_cell == 'normal' else 0,
                         1 if pus_cell == 'normal' else 0,
                         1 if pus_cell_clumps == 'present' else 0,
                         1 if bacteria == 'present' else 0,
                         blood_glucose_random,
                         blood_urea,
                         serum_creatinine,
                         sodium,
                         potassium,
                         hemoglobin,
                         packed_cell_volume,
                         white_blood_cell_count,
                         red_blood_cell_count,
                         1 if hypertension == 'yes' else 0,
                         1 if diabetes_mellitus == 'yes' else 0,
                         1 if cad == 'yes' else 0,
                         1 if appetite == 'good' else 0,
                         1 if pedal_edema == 'yes' else 0,
                         1 if anemia == 'yes' else 0 ]])

    # SHAP expects feature names
    feature_names = ['age', 'blood_pressure', 'specific_gravity', 'albumin', 'sugar','red_blood_cells','pus_cell','pus_cell_clumps', 'bacteria',
                     'blood_glucose_random', 'blood_urea', 'serum_creatinine','sodium','potassium',
                     'hemoglobin','packed_cell_volume', 'white_blood_cell_count', 'red_blood_cell_count',
                     'hypertension', 'diabetes_mellitus', 'coronary_artery_disease',
                     'appetite', 'pedal_edema', 'anemia']

    input_df = pd.DataFrame(model_input, columns=feature_names)

    # Predict Button
    if st.button("🔍 Generate Clinical Interpretation"):
        st.dataframe(input_df) # Display the input data Frame

        # Calculate eGFR
        egfr_value = calculate_egfr_ckd_epi_2021(serum_creatinine, age, gender)


        # Show visual eGFR
        egfr_percent = min(int((egfr_value / 120) * 100), 100)
        st.subheader("🧪 eGFR(Estimated Glomerular Filtration Rate) Scale")
        st.progress(egfr_percent)
        st.caption(f"**eGFR**: {egfr_value} mL/min/1.73m²")

        # Generate interpretation
        interpretation = generate_ckd_interpretation(
            creatinine=serum_creatinine,
            age=age,
            gender=gender,
            albumin=albumin,
            blood_urea=blood_urea,
            hemoglobin=hemoglobin,
            hypertension=hypertension,
            diabetes_mellitus=diabetes_mellitus,
            anemia=anemia
        )



        # Display Interpretation
        st.subheader("🩺 Clinical Interpretation")
        st.markdown(interpretation,unsafe_allow_html=True)



    # ================================
    # SHAP Local Explanation Section
    # ================================


    st.subheader("📊 SHAP Local Explanation")
    st.markdown("This plot explains which features most influenced this specific prediction:")

    # Make prediction
    pred_proba = rf.predict_proba(input_df)[0]
    pred_class = rf.predict(input_df)[0]
    class_names = {0: "Negative", 1: "Positive"}
    st.write(f"### Prediction: **{class_names[pred_class]}**")
    st.write(f"Probability of Positive: **{pred_proba[1]:.2f}**")
    st.write(f"Probability of Negative: **{pred_proba[0]:.2f}**")

    # Use SHAP TreeExplainer
    explainer = shap.TreeExplainer(rf)
    shap_values = explainer.shap_values(input_df)

    # get SHAP explanation for the first (and Only)input row
    shap_vals = shap_values[0, :, pred_class]  # SHAP values for the predicted class (first instance)
    expected_val = explainer.expected_value[pred_class] # Base value for the predicted class (first instance)

    # Plot SHAP waterfall for class 1 (CKD Positive)
    # Plot SHAP waterfall for the first (and only) instance
    explanation=shap.Explanation(
      values = shap_vals,
      base_values = expected_val,
      data=input_df.iloc[0],
      feature_names=feature_names,
    )
    shap.plots.waterfall(explanation,max_display=15,show=False) # plot SHAP waterfall plot

    # Display in Streamlit
    st.pyplot(plt.gcf())



    # ================================
    # Human-readable Explanation
    # ================================
    st.markdown("### 🧑‍⚕️ Case Summary: Model Output Explained:")

    # Use base value for the predicted class
    base_value = explainer.expected_value[pred_class]
    # Use SHAP values for the predicted class and current input
    shap_contributions = shap_values[0, :, pred_class]  # SHAP values for input
    # Predicted probability for the predicted class
    prediction_prob = pred_proba[pred_class]  # From pred_proba = rf.predict_proba(input_df)[0]

    # Show base value
    st.markdown(
        f"<p style='font-size:20px; font-weight:bold;'>Base Value: {base_value:.2f} "
        f"(average model output for <strong>{class_names[pred_class]}</strong> cases)</p>",
        unsafe_allow_html=True
    )
    # Show predicted probability
    st.markdown(
        f"<p style='font-size:20px;'>Predicted Probability of "
        f"<strong>{class_names[pred_class]}</strong>: "
        f"<strong>{pred_proba[pred_class]:.2f}</strong></p>",
        unsafe_allow_html=True
    )

    def get_effect_description(shap_val, pred_class):
        if shap_val == 0:
            return "had no effect on CKD risk"

        if pred_class == 1:  # CKD predicted
            return "increased CKD risk" if shap_val > 0 else "decreased CKD risk"
        else:  # No CKD predicted
            return ("increased likelihood of not having CKD" if shap_val > 0
                else "decreased likelihood of not having CKD (i.e., indirectly favors CKD)")


    st.markdown("### 📌 Feature-level explanations of CKD risk:")
    breakdown_lines = []

    # Iterate through all features and SHAP values
    for feature, shap_val in zip(feature_names, shap_contributions):
        direction = "+" if shap_val >= 0 else "–"

        # Always define 'value' first for this feature
        value = input_df.at[0, feature]

        # Get human-readable explanation based on predicted class
        effect = get_effect_description(shap_val, pred_class)

        # Add human-readable explanations for each feature
        if feature == "age":
            explanation = f"Age was {value} , which {effect}"
        elif feature == "blood_pressure":
            explanation = f"Blood pressure was {value}, which {effect}"
        elif feature == "specific_gravity":
            explanation = f"Specific gravity was {value}, which {effect}"
        elif feature == "albumin":
            explanation = f"Albumin level was {value}, which {effect}"
        elif feature == "sugar":
            explanation = f"Sugar level was {value}, which {effect}"
        elif feature == "red_blood_cells":
            explanation = f"{'normal' if value == 1 else 'abnormal'} red blood cell which {effect}"
        elif feature == "pus_cell":
            explanation = f"{'normal' if value == 1 else 'abormal'} pus cell {effect}"
        elif feature == "pus_cell_clumps":
            explanation = f"{'present' if value == 1 else 'not present'} pus cell clumps {effect}"
        elif feature == "bacteria":
            explanation = f"{'present' if value == 1 else 'not present'} bacteria {effect}"
        elif feature == "blood_glucose_random":
            explanation = f"Random blood glucose was {value}, which {effect}"
        elif feature == "blood_urea":
            explanation = f"Blood urea was {value}, which {effect}"
        elif feature == "serum_creatinine":
            explanation = f"Serum creatinine was {value}, which {effect}"
        elif feature == "sodium":
            explanation = f"Sodium was {value}, which {effect}"
        elif feature == "potassium":
            explanation = f"Potassium was {value}, which {effect}"
        elif feature == "hemoglobin":
            explanation = f"Hemoglobin was {value}, which {effect}"
        elif feature == "packed_cell_volume":
            explanation = f"Packed cell volume was {value}, which {effect}"
        elif feature == "white_blood_cell_count":
            explanation = f"WBC count was {value}, which {effect}"
        elif feature == "red_blood_cell_count":
            explanation = f"RBC count was {value}, which {effect}"
        elif feature == "hypertension":
            explanation = f"{'yes' if value == 1 else 'no'} hypertension which {effect}"
        elif feature == "diabetes_mellitus":
            explanation = f"{'yes' if value == 1 else 'no'} diabetes mellitus which {effect}"
        elif feature == "coronary_artery_disease":
            explanation = f"{'yes' if value == 1 else 'no'} coronary artery disease which {effect}"
        elif feature == "appetite":
            explanation = f"{'good' if value == 1 else 'poor'} appetite which {effect}"
        elif feature == "pedal_edema":
            explanation = f"{'yes' if value == 1 else 'no'} pedal edema which {effect}"
        elif feature == "anemia":
            explanation = f"{'yes' if value == 1 else 'no'} anemia which {effect}"

        else:
            explanation = f"{feature} had an unknown impact"

        breakdown_lines.append(f"{direction} **{feature.replace('_', ' ').title()}**: {shap_val:+.10f} ({explanation})")

    # Show all contributions with explanations
    st.markdown("<br>".join(breakdown_lines),unsafe_allow_html=True)

    # Display the Final Result
    # Get predicted class (0 = No CKD, 1 = CKD)
    predicted_class = rf.predict(model_input)[0]

    # Get the probability of the predicted class
    predicti_prob = rf.predict_proba(model_input)[0][predicted_class]

    # Set label and color
    if predicted_class == 1:
        diagnosis = "Positive"
        color = "red"
    else:
        diagnosis = "Negative"
        color = "green"

    # Display result in Streamlit
    st.markdown(
    f"<p style='font-size:20px;'><strong>= Final Prediction:</strong> "
    f"<span style='color:{color};'>{diagnosis} "
    f"({int(predicti_prob * 100)}% predicted confidence)</span></p>",
    unsafe_allow_html=True
    )

    # ================================
    # Additive Check Section
    # ================================
    st.markdown("### 🔍 Additive Check of Model Explanation")

    # Retrieve predicted probability (for the specific instance)
    pred_proba = rf.predict_proba(input_df)[0]
    pred_class = rf.predict(input_df)[0]  # Predicted class
    class_names = {0: "Negative", 1: "Positive"}
    predicted_output = pred_proba[pred_class]

    # Calculate the sum of SHAP values for the predicted class
    shap_contributions = shap_values[0, :, pred_class] # SHAP values for the instance
    shap_sum = shap_contributions.sum()  # Sum of SHAP values for all features

    # Get the base value for the predicted class
    base_value = expected_val  # Base value for the predicted class

    # Total log-odds from SHAP
    total_log_odds = base_value + shap_sum

    # Convert log-odds to predicted probability using sigmoid

    shap_pred_proba = 1 / (1 + np.exp(-total_log_odds))
    # Check the additive property (base value + sum of SHAP values should equal model output)
    additive_check = base_value + shap_sum

    # Display results
    st.write(f"**Predicted Output:** {predicted_output:.2f} (probability of {class_names[pred_class]})")
    st.write(f"**Base Value:** {base_value:.2f}")
    st.write(f"**Sum of SHAP Values:** {shap_sum:.10f}")
    st.write(f"**Additive Check (Base Value + SHAP Sum):** {additive_check:.10f}")

    # Add a small tolerance due to floating point calculations
    tolerance = 1e-3
    if abs(additive_check - predicted_output) < tolerance:
        st.success("✅ Additive Check Passed! The SHAP values correctly sum to the predicted output.")
    else:
        st.error(f"❌ Additive Check Failed! The SHAP values do not sum to the predicted output. Difference: {additive_check - predicted_output:.10f}")

    