DrugPredict AI – Drug Molecule Property Prediction
An AI-powered web application that predicts the aqueous solubility of drug-like molecules using Machine Learning, RDKit and molecular descriptors.

<p align="center">
  <strong>Live Demo:</strong> https://moleculemind-ai.vercel.app
  <br/>
  <strong>Backend API:</strong> https://drungmoleculepredictionai.onrender.com
  <br/>
  <strong>GitHub:</strong> https://github.com/anubhav1701-git/MajorProjectSem5
</p>

📌 About the Project

DrugPredict AI is a machine learning-based molecular property prediction platform. Users can enter a molecule's SMILES (Simplified Molecular Input Line Entry System) representation and obtain its predicted aqueous solubility.

The application uses RDKit to process molecular structures and extract chemical descriptors. A trained Random Forest regression model uses these descriptors to predict solubility.

The platform also provides molecular visualization, molecular descriptor analysis, Lipinski Rule of Five screening, and prediction history.

✨ Features

SMILES Input: Enter molecular structures using SMILES notation.

Solubility Prediction: Predict aqueous solubility using a trained Random Forest model.

2D Molecular Visualization: Generate molecular structure images using RDKit.

Molecular Descriptors: Calculate important chemical properties.

Lipinski Rule of Five: Analyze four basic drug-likeness screening criteria.

Prediction History: Store previous predictions in browser local storage.

Interactive Charts: Visualize predicted solubility using Recharts.

REST API: Access prediction and visualization functionality through FastAPI.

🧪 Molecular Descriptors

The model uses eight molecular descriptors:

Descriptor

Description

MolWt

Molecular weight

LogP

Lipophilicity estimate

TPSA

Topological polar surface area

HBD

Hydrogen bond donors

HBA

Hydrogen bond acceptors

RotatableBonds

Number of rotatable bonds

RingCount

Number of rings

HeavyAtoms

Number of non-hydrogen atoms

🤖 Machine Learning Models

Three regression algorithms were trained and evaluated:

Model

MAE

RMSE

R² Score

Linear Regression

0.8076

1.0689

0.7583

Decision Tree

0.7365

1.0908

0.7483

Random Forest

0.5530

0.8053

0.8628

Selected Model: Random Forest Regressor

The Random Forest model achieved the best overall performance among the three evaluated models on the test split.

🛠️ Technology Stack

Machine Learning & Backend

Python

Scikit-learn

RDKit

Pandas

NumPy

Joblib

FastAPI

Uvicorn

Frontend

React.js

Vite

JavaScript

HTML

CSS

Recharts

Deployment & Version Control

Git and GitHub

Render – Backend hosting

Vercel – Frontend hosting

## 📂 Project Structure

```text
DrugMoleculePropPrediction/
│
├── backend/
│   └── main.py
│
├── dataset/
│   ├── delaney-processed.csv
│   └── molecules_with_descriptors.csv
│
├── frontend/
│   ├── public/
│   ├── src/
│   │   ├── App.jsx
│   │   ├── App.css
│   │   ├── index.css
│   │   └── main.jsx
│   ├── package.json
│   └── index.html
│
├── drug_solubility_model.pkl
├── feature_names.pkl
├── extract_descriptors.py
├── train_models.py
├── compare_models.py
├── save_model.py
├── model_comparison.csv
├── model_comparison.png
├── requirements.txt
└── README.md
```
⚙️ Installation and Setup

1. Clone the Repository

git clone https://github.com/anubhav1701-git/MajorProjectSem5.git
cd MajorProjectSem5

2. Create a Python Virtual Environment

python -m venv venv

Activate it on Windows:

venv\Scripts\activate

3. Install Backend Dependencies

pip install -r requirements.txt

4. Run the FastAPI Backend

From the project root directory:

uvicorn backend.main:app --reload

Backend URL:

http://127.0.0.1:8000

API documentation:

http://127.0.0.1:8000/docs

5. Run the React Frontend

Open another terminal:

cd frontend
npm install
npm install recharts
npm run dev

Frontend URL:

http://localhost:5173

🔗 API Endpoints

Method

Endpoint

Description

GET

/

Check API status

POST

/predict

Predict molecular solubility

GET

/visualize?smiles=CCO

Generate 2D molecular structure

Example Prediction Request

Endpoint:

POST /predict

Request Body:

{
  "smiles": "CCO"
}

The API returns the predicted solubility, molecular descriptors and Lipinski analysis.

📊 Model Evaluation

The models were evaluated using:

MAE (Mean Absolute Error): Measures the average absolute prediction error.

RMSE (Root Mean Squared Error): Measures prediction error while penalizing larger errors.

R² Score: Measures how well the model explains variation in the target values.

The Random Forest model achieved an R² score of 0.8628 on the evaluated test split.

🚀 Deployment

The project is deployed using two separate platforms:

Component

Platform

Link

Frontend

Vercel

https://moleculemind-ai.vercel.app

Backend

Render

https://drungmoleculepredictionai.onrender.com

API Documentation

FastAPI

https://drungmoleculepredictionai.onrender.com/docs

🔬 Dataset

The project uses the ESOL (Delaney) aqueous solubility dataset.

The dataset contains molecular SMILES representations and experimental solubility values used for machine learning development and evaluation.

🔮 Future Enhancements

Explainable AI using SHAP.

Molecular similarity search using RDKit fingerprints.

Prediction uncertainty and applicability domain analysis.

Batch prediction through CSV uploads.

Comparison of multiple molecular structures.

Downloadable prediction reports.

Evaluation on additional external datasets.

⚠️ Limitations and Disclaimer

This project is an academic machine learning application for molecular aqueous solubility prediction.

Predicted solubility is an estimate, not an experimental measurement.

Lipinski Rule of Five screening does not establish drug safety or effectiveness.

The model is not intended for clinical decisions, medical advice or drug development decisions without further scientific validation.

👨‍💻 Author

Anubhav Tripathi

B.Tech – Computer Science Engineering (AI & ML)

IILM University, Greater Noida

GitHub: https://github.com/anubhav1701-git

<p align="center">
  <strong>DrugPredict AI</strong>
  <br/>
  Machine Learning + Chemistry + Innovation
</p>

