# chronic-kidney-disease-prediction-using-machine-learning
# 🩺<img width="118" height="85" alt="image" src="https://github.com/user-attachments/assets/945ea020-8a50-4fa3-8141-48f7c9dc7245" />
 Chronic Kidney Disease (CKD) Prediction using Machine Learning

---

## 📌 About the Project

Chronic Kidney Disease (CKD) is a major non-communicable disease affecting 10–15% of the global population. Early detection is crucial to prevent severe complications such as hypertension, anemia, bone disorders, and kidney failure.

This project develops an **intelligent machine learning-based clinical decision support system** that:

* Predicts whether a patient has CKD or not (**binary classification**)
* Dynamically estimates **eGFR (Estimated Glomerular Filtration Rate)**
* Interprets the **CKD stage (Stage 1 to Stage 5)**
* Explains predictions using **SHAP (Explainable AI)**
* Provides a **user-friendly Streamlit web application**

---

## 🎯 Objectives

✔ Early detection of CKD using Machine Learning
✔ Handle missing data, outliers, and class imbalance
✔ Compare 7 ML models and select the best one
✔ Use **Random Forest** as the final model
✔ Integrate **SHAP for interpretability**
✔ Deploy as a web app using **Streamlit**

---

## 🧠 Machine Learning Models Used

We trained and compared the following models:

* Logistic Regression
* Decision Tree
* Random Forest ✅ *(Best Model)*
* SVM (RBF Kernel)
* Linear SVM
* K-Nearest Neighbors (KNN)
* Artificial Neural Network (ANN)

🏆 **Final Model Selected: Random Forest**

---

## 📊 Dataset

* **File used:** `Kidney_disease.csv`
* **Source:** UCI Machine Learning Repository
* **Records:** 400
* **Features:** 25
* **Classes:**

  * `ckd` → 250 samples
  * `notckd` → 150 samples

### Dataset Challenges & Solutions

| Issue            | Solution                          |
| ---------------- | --------------------------------- |
| Missing values   | Random sampling + Mode imputation |
| Class imbalance  | `class_weight='balanced'`         |
| Categorical data | Label Encoding                    |
| Mild outliers    | Detected but retained             |

---

## ⚙️ Methodology
<img width="982" height="947" alt="image" src="https://github.com/user-attachments/assets/6bd17c2e-c9e2-477d-8b56-bb257d6acc7e" />

To ensure realistic model performance and avoid overly optimistic results, the project follows a data leakage–free machine learning pipeline.

🧠 What is Data Leakage?

Data leakage occurs when information from the test set unintentionally influences the training process, leading to artificially high accuracy that does not generalize to real-world data.

### Step 1 — Leakage-Safe Data Preprocessing

To ensure realistic and unbiased model performance, a leakage-free preprocessing strategy was adopted.

✅ Data Cleaning & Standardization

* Column names were cleaned, standardized, and renamed for better interpretability
* Irrelevant features such as ID were removed
* Inconsistent categorical values were normalized (e.g., yes/no, present/notpresent → 1/0)

✅ Data Type Conversion

*Numeric values stored as text (e.g., packed cell volume, WBC count) were converted to proper  numerical format
* Ensured uniform data types across all features

### Step 2 — Train-Test Split (Before Preprocessing)

To avoid data leakage, the dataset was split at an early stage:
* 80% Training Data
* 20% Testing Data (unseen data)
* Stratified sampling was used to preserve class distribution

👉 This ensures that the test data remains completely independent and simulates real-world scenarios.

### Step 3 — Missing Value Imputation

A structured imputation strategy was applied separately for different feature types:
| Feature Type     | Strategy Used     |
| ---------------- | ----------------- |
| Continuous       | Mean Imputation   |
| Skewed Numerical | Median Imputation |
| Categorical      | Mode Imputation   |


🔐 Key Improvement:

* Imputers were fitted only on training data
* The learned values were then applied to the test data

👉 This prevents leakage of statistical information from the test set into the model.

### Step 4 — Categorical Encoding (Safe Encoding)

* Categorical features were encoded after splitting the dataset
* Converted into numerical labels using category-based encoding
* Unknown or missing categories were handled safely

👉 Ensures that no information from test data influences training.

### Step 5 — Feature Engineering & Validation

* Ensured all numerical features are in float format
* Categorical features converted into integer codes
* Final dataset validated to confirm zero missing values before training

### Step 6 — Model Training

The final model used:

* Algorithm: Random Forest Classifier
* Number of Trees: 200
* Class Handling: class_weight='balanced'
* Random State: 42 (for reproducibility)

💡 Why Random Forest?

* Handles mixed data types effectively
* Robust to noise and outliers
* No requirement for feature scaling
* Reduces overfitting through ensemble learning


### Step 7 — Model Evaluation (Unbiased Testing)

The model was evaluated on completely unseen test data using:

* Accuracy
* Precision
* Recall
* F1-score
* Confusion Matrix

👉 Since preprocessing was performed only using training data, the evaluation reflects true generalization performance.


### Confusion Matrix

<img width="498" height="455" alt="download" src="https://github.com/user-attachments/assets/ba979b37-8500-4928-8c78-5ccc943a0e48" />

<img width="622" height="470" alt="download (1)" src="https://github.com/user-attachments/assets/8014809c-56aa-4456-82e6-fae0168597b4" />


Interpretation:

* 30 patients correctly predicted as **NOT CKD (Class 0)**
* 50 patients correctly predicted as **CKD (Class 1)**
* **0 false positives and 0 false negatives**


### Classification Report

| Class       | Precision | Recall   | F1-score | Support |
| ----------- | --------- | -------- | -------- | ------- |
| 0 (Not CKD) | **1.00**  | **1.00** | **1.00** | 30      |
| 1 (CKD)     | **1.00**  | **1.00** | **1.00** | 50      |

**Overall Accuracy: 1.00 (100%)**

* **Macro Avg:** 1.00
* **Weighted Avg:** 1.00

👉 This confirms that the model perfectly separated CKD and non-CKD cases on unseen test data.


### Step 8 — Model Saving

* The trained model was serialized using Pickle
* Saved as: ckd_random_forest_model.pkl
* Enables easy deployment in the Streamlit web application

### 🚀 Key Improvement Over Previous Approach

| Aspect                 | Previous Approach | Improved Approach        |
| ---------------------- | ----------------- | ------------------------ |
| Preprocessing Order    | Before split      | After split ✅            |
| Missing Value Handling | Full dataset      | Training-only learning ✅ |
| Data Leakage           | Possible          | Eliminated ✅             |
| Model Evaluation       | Overestimated     | Realistic & reliable ✅   |

---


## 🧮 Dynamic eGFR Calculation

The system calculates eGFR using the **CKD-EPI 2021 equation** and assigns CKD stage automatically:

| Stage    | eGFR Range |
| -------- | ---------- |
| Stage 1  | ≥ 90       |
| Stage 2  | 60–89      |
| Stage 3a | 45–59      |
| Stage 3b | 30–44      |
| Stage 4  | 15–29      |
| Stage 5  | < 15       |

This helps doctors understand **disease severity**, not just a binary prediction.

---

## 🧠 **Explainability using SHAP (Expanded Section)**

Machine learning models like Random Forest are powerful but act as “black boxes.” To make the system **clinically trustworthy**, we integrated **SHAP (SHapley Additive exPlanations)**.

### Why SHAP was used:

SHAP helps:

* Explain **why** the model made a prediction
* Identify **which features pushed the decision toward CKD or NOT CKD**
* Provide transparency for doctors and clinicians

### How SHAP was applied in this project:

We used:

1️⃣ **Global SHAP Explanation**

* Shows which features are most important across the entire dataset
* Helps understand key clinical drivers of CKD prediction
* Identifies critical biomarkers such as:

  * Serum creatinine
  * Blood urea
  * Hemoglobin
  * Blood pressure
  * Albumin

2️⃣ **Local SHAP Explanation (Individual Patient)**
For each patient prediction, SHAP explains:

* Which features increased CKD risk
* Which features reduced CKD risk
* By how much each feature contributed

3️⃣ **SHAP Waterfall Plot**

* Visual breakdown of one patient’s prediction
* Starts from base probability
* Shows step-by-step feature impact
* Very useful for medical interpretation

### Benefit of SHAP in Healthcare

SHAP makes the system:

* Transparent
* Clinically interpretable
* Trustworthy
* Suitable for decision support in hospitals

---

## 🌐 Web Application (Streamlit UI)

The system is deployed as a **multi-page Streamlit web app** with the following pages:

1️⃣ **About the Project** → (`about.py`)
2️⃣ **User Instructions** → (`user_instructions.py`)
3️⃣ **Model Prediction & SHAP** → (`model.py`)
4️⃣ **Medical References** → (`medicalinfo.py`)

The main entry point is:

```
app.py
```

---

## 🛠️ Tech Stack

| Component      | Tool                        |
| -------------- | --------------------------- |
| Language       | Python, HTML, CSS           |
| ML Library     | Scikit-learn                |
| Explainability | SHAP                        |
| Visualization  | Matplotlib, Seaborn, Plotly |
| Web App        | Streamlit                   |
| Platform       | Google Colab, VS code       |

---

## 🚀 How to Run the Project

### Step 1 — Clone the Repository

```bash
git clone https://github.com/your-username/ckd-prediction.git
cd ckd-prediction
```

### Step 2 — Install Dependencies

```bash
pip install -r requirements.txt
```

### Step 3 — Run Streamlit App

```bash
streamlit run app.py
```

---

## 📁 Repository Structure

```
ckd-prediction/
│── Kidney_disease.csv
│── ckd_random_forest_model.pkl
│── app.py
│── model.py
│── user_instructions.py
│── about.py
│── medicalinfo.py
│── requirements.txt
└── README.md
```

---

## ✅ Strengths

* **100% test accuracy**
* Handles missing data & imbalance
* Explainable AI using SHAP
* Real-time eGFR & staging
* Doctor-friendly interface

---

## ⚠️ Limitations

* Dataset is relatively small (400 samples)
* Needs external validation on hospital data
* Random Forest is less interpretable than Logistic Regression

---

### Screenshots

**About The Project Page**

<img width="982" height="623" alt="image" src="https://github.com/user-attachments/assets/20061945-1ffa-4c69-ac1b-e841fff74b2c" />

**Navigation Bar** 

<img width="671" height="491" alt="image" src="https://github.com/user-attachments/assets/fc2e3006-1bd3-4484-8c30-95e7d57f420f" />

**User Instructions Page** 

<img width="982" height="573" alt="image" src="https://github.com/user-attachments/assets/54d878b6-c4d3-43ef-9bd4-c19b5da46aae" />

**Model Prediction Page**

<img width="960" height="548" alt="image" src="https://github.com/user-attachments/assets/73297c0a-f0fa-480b-918f-bd72048699db" />

<img width="961" height="400" alt="image" src="https://github.com/user-attachments/assets/ab1bc39c-2724-4819-a576-efa49fab02d1" />

**Prediction** 

<img width="983" height="280" alt="image" src="https://github.com/user-attachments/assets/5a76cc6f-0e1b-4d2e-a491-b427979fd331" />

**eGFR calculation and Stage Interpretation** 

<img width="982" height="527" alt="image" src="https://github.com/user-attachments/assets/63a9f43d-4ade-4f3c-b0e7-d36e7247fffc" />

<img width="984" height="283" alt="image" src="https://github.com/user-attachments/assets/7c1292d8-5da9-411b-9e6e-26f45c275e58" />

**SHAP with Prediction Probabilities**

<img width="982" height="239" alt="image" src="https://github.com/user-attachments/assets/ee54ff7f-b0aa-4641-8089-871bdb340323" />

**SHAP Waterfall Plot for local explanation**

<img width="982" height="745" alt="image" src="https://github.com/user-attachments/assets/db2a7cc9-e747-48c2-822b-5c94faaf17c6" />

**Model Output Explanation**

<img width="982" height="921" alt="image" src="https://github.com/user-attachments/assets/f20ff1f6-b241-4f96-a66b-d400479ed0f9" />

**Additive Check Of Model Explanation**

<img width="982" height="295" alt="image" src="https://github.com/user-attachments/assets/26a846ef-8b60-429d-aaba-41c5a7275acb" />

---

## 🔮 Future Work

* Train on More Bigger real hospital dataset
* Add mobile app support
* Integrate live lab reports
* Add deep learning model
* Deploy on cloud (Streamlit Cloud / Heroku)

---

## 📚 References

1. UCI CKD Dataset
2. KDIGO Guidelines
3. SHAP: Lundberg & Lee (2017)
4. WHO CKD Reports

---

### ⭐ If you found this project useful, please give it a star on GitHub!
