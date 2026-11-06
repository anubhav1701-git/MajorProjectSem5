# 🧬 Drug Molecule Property Prediction Using Machine Learning

### An AI-powered platform for molecular property prediction, drug-likeness analysis, and chemical structure visualization.

<p align="center">
  <img src="https://img.shields.io/badge/Python-3.x-blue?logo=python" />
  <img src="https://img.shields.io/badge/Machine%20Learning-Scikit--learn-orange" />
  <img src="https://img.shields.io/badge/Backend-FastAPI-green?logo=fastapi" />
  <img src="https://img.shields.io/badge/Frontend-React-61DAFB?logo=react" />
  <img src="https://img.shields.io/badge/Cheminformatics-RDKit-purple" />
</p>

---

## 📌 Overview

Drug Molecule Property Prediction is a machine learning-based application designed to predict the water solubility of chemical molecules using their SMILES representations.

The system extracts molecular descriptors using RDKit and applies trained machine learning algorithms to estimate molecular solubility.

It also provides molecular structure visualization, Lipinski Rule of Five analysis, prediction history, and interactive data visualization through a React-based dashboard.

The project aims to demonstrate how machine learning and cheminformatics can support early-stage molecular property analysis.

## ✨ Key Features

- **SMILES-Based Prediction:** Enter a molecular SMILES string to predict water solubility.
- **Molecular Descriptor Extraction:** Calculate molecular weight, LogP, TPSA, hydrogen bond donors, acceptors, and other descriptors.
- **Machine Learning Models:** Train and compare Linear Regression, Decision Tree, and Random Forest.
- **Best Model Selection:** Select Random Forest based on evaluation performance.
- **Molecule Visualization:** Generate 2D molecular structure images using RDKit.
- **Lipinski Rule of Five:** Evaluate molecular drug-likeness using four Lipinski criteria.
- **Prediction History:** Save and review previous predictions.
- **Interactive Charts:** Visualize prediction history and molecular analysis.
- **FastAPI Backend:** Provide REST API endpoints for molecular prediction.

## 🧠 Machine Learning Approach

### Dataset

The project uses the ESOL (Delaney) dataset for aqueous solubility prediction.

- Dataset: ESOL / Delaney solubility dataset
- Number of molecules: 1,128
- Target variable: Experimental Log Solubility (LogS)
- Input representation: SMILES

### Molecular Descriptors

RDKit is used to extract eight molecular descriptors:

| Descriptor | Description |
|---|---|
| MolWt | Molecular weight |
| LogP | Lipophilicity |
| TPSA | Topological polar surface area |
| HBD | Hydrogen bond donors |
| HBA | Hydrogen bond acceptors |
| RotatableBonds | Number of rotatable bonds |
| RingCount | Number of rings |
| HeavyAtoms | Number of heavy atoms |

### Models Trained

Three machine learning algorithms were evaluated:

1. Linear Regression
2. Decision Tree Regressor
3. Random Forest Regressor

### Model Performance

Evaluation results on the project's test split:

| Model | MAE | RMSE | R² Score |
|---|---:|---:|---:|
| Linear Regression | 0.8076 | 1.0689 | 0.7583 |
| Decision Tree | 0.7365 | 1.0908 | 0.7483 |
| **Random Forest** | **0.5530** | **0.8053** | **0.8628** |

**Selected Model: Random Forest Regressor**

The Random Forest model achieved the best overall performance among the three evaluated models.

## ⚙️ Technology Stack

| Category | Technologies |
|---|---|
| Programming Language | Python |
| Machine Learning | Scikit-learn |
| Cheminformatics | RDKit |
| Data Processing | Pandas, NumPy |
| Backend | FastAPI |
| Frontend | React.js |
| Charts | Recharts |
| Model Storage | Joblib |
| API Testing | FastAPI Swagger UI |
| Version Control | Git, GitHub |

## 🏗️ System Architecture

```text
              USER
                |
                v
       REACT FRONTEND
                |
                v
         FASTAPI BACKEND
                |
                v
        SMILES VALIDATION
                |
                v
       RDKit DESCRIPTOR EXTRACTION
                |
                v
       MOLECULAR FEATURE MATRIX
                |
                v
       RANDOM FOREST MODEL
                |
                v
       SOLUBILITY PREDICTION
                |
          +-----+------+
          |            |
          v            v
    LIPINSKI       MOLECULAR
    ANALYSIS      VISUALIZATION
          |            |
          +-----+------+
                |
                v
        RESULTS DASHBOARD
```

## 📁 Project Structure

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
│   └── vite.config.js
│
├── drug_solubility_model.pkl
├── feature_names.pkl
├── compare_models.py
├── extract_descriptors.py
├── train_models.py
├── save_model.py
├── requirements.txt
├── model_comparison.csv
├── model_comparison.png
├── .gitignore
└── README.md
```

## 🚀 Installation and Setup

### Prerequisites

- Python 3
- Node.js and npm
- Git
- VS Code (recommended)

### 1. Clone the Repository

```bash
git clone https://github.com/anubhav1701-git/MajorProjectSem5.git
```

```bash
cd MajorProjectSem5
```

### 2. Create Python Virtual Environment

```bash
python -m venv venv
```

Activate it on Windows:

```powershell
venv\Scripts\activate
```

### 3. Install Python Dependencies

```bash
pip install -r requirements.txt
```

### 4. Start FastAPI Backend

From the project root:

```bash
uvicorn backend.main:app --reload
```

Backend URL:

```text
http://127.0.0.1:8000
```

API documentation:

```text
http://127.0.0.1:8000/docs
```

### 5. Start React Frontend

Open another terminal:

```bash
cd frontend
```

Install frontend dependencies:

```bash
npm install
```

Start the development server:

```bash
npm run dev
```

Frontend URL:

```text
http://localhost:5173
```

## 🔌 API Endpoints

| Method | Endpoint | Description |
|---|---|---|
| GET | `/` | Check API status |
| POST | `/predict` | Predict molecular solubility |
| GET | `/visualize` | Generate molecular structure image |

### Example Prediction Request

**Endpoint:**

```text
POST /predict
```

**Request Body:**

```json
{
  "smiles": "CCO"
}
```

The API returns predicted LogS, molecular descriptors, and Lipinski analysis.

## 🧪 Example Molecule

**Ethanol**

SMILES:

```text
CCO
```

The system parses the SMILES, extracts molecular descriptors, predicts water solubility, and evaluates Lipinski criteria.

## 🔮 Future Enhancements

The following features are planned for future development:

- Explainable AI using SHAP.
- Molecular similarity search using RDKit fingerprints.
- Molecule Combiner supporting mixture analysis and hybrid molecule generation.
- Batch prediction for multiple SMILES.
- Prediction uncertainty and applicability-domain analysis.
- ADMET property prediction using suitable datasets and trained models.
- Advanced molecular comparison.
- Downloadable molecular analysis reports.

## ⚠️ Limitations and Disclaimer

- Predictions are computational estimates and are not experimental measurements.
- The current model predicts aqueous solubility, not drug efficacy or clinical safety.
- Lipinski Rule of Five analysis is a drug-likeness screening heuristic, not proof that a molecule is a suitable drug.
- The model's reliability may be limited for molecules that differ substantially from its training dataset.
- This project is intended for educational and research purposes, not medical decision-making.

## 👨‍💻 Developer

**Anubhav Tripathi**

B.Tech – Computer Science Engineering (AI & ML)

IILM University, Greater Noida

**Areas of Interest:**
- Machine Learning
- Artificial Intelligence
- Drug Discovery
- Data Science
- Cheminformatics

## 🔗 Project Links

- **GitHub Repository:** https://github.com/anubhav1701-git/MajorProjectSem5

---

⭐ If you find this project interesting, consider giving the repository a star!

**Built with Python, Machine Learning, RDKit, FastAPI and React.**
