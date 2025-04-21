# 🩺 Personalized Healthcare & Medicine Prediction App

This is a Streamlit web application that predicts a healthcare outcome or condition based on patient input features using a machine learning model (XGBoost).

---

## 🚀 Features

- Trains an XGBoost model on a healthcare dataset
- Interactive Streamlit web interface
- User input fields for real-time prediction
- Easily deployable via Streamlit Cloud or any cloud service

---

## 📁 Files in This Repo

| File | Description |
|------|-------------|
| `train_model.py` | Trains the ML model using `healthcare_dataset.csv` and saves it as `model.pkl` |
| `app.py` | Streamlit app that loads the model and takes user input to predict |
| `requirements.txt` | Python dependencies needed to run the app |
| `README.md` | This file — documentation for your project |
| `healthcare_dataset.csv` | *(You must add this)* Your dataset containing features and a `target` column |

---

## 🛠 How to Run Locally

### 1. Clone the repo

```bash
git clone https://github.com/your-username/your-repo-name.git
cd your-repo-name
