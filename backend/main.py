from fastapi.responses import StreamingResponse
from rdkit.Chem import Draw
from io import BytesIO
from fastapi import FastAPI, HTTPException
from pydantic import BaseModel
from rdkit import Chem
from rdkit.Chem import Descriptors, rdMolDescriptors
import pandas as pd
import joblib
from pathlib import Path
from fastapi.middleware.cors import CORSMiddleware

# 1. Get project directory
BASE_DIR = Path(__file__).resolve().parent.parent

# 2. Load saved ML model
model = joblib.load(BASE_DIR / "drug_solubility_model.pkl")

# 3. Load feature names
feature_names = joblib.load(BASE_DIR / "feature_names.pkl")

# 4. Create FastAPI application
app = FastAPI(
    title="Drug Molecule Property Prediction API",
    description="Predict molecular water solubility using Machine Learning",
    version="1.0"
)
# Enable communication between React and FastAPI
app.add_middleware(
    CORSMiddleware,
    allow_origins=["http://localhost:5173"],
    allow_credentials=True,
    allow_methods=["*"],
    allow_headers=["*"],
)


# 5. Define input format
class MoleculeInput(BaseModel):
    smiles: str


# 6. Home endpoint
@app.get("/")
def home():
    return {
        "message": "Drug Molecule Prediction API is running!"
    }


# 7. Prediction endpoint
@app.post("/predict")
def predict_molecule(data: MoleculeInput):

    # Convert SMILES into molecule
    mol = Chem.MolFromSmiles(data.smiles)

    # Validate molecule
    if mol is None:
        raise HTTPException(
            status_code=400,
            detail="Invalid SMILES string"
        )

    # 8. Extract molecular descriptors
    descriptors = {
        "MolWt": Descriptors.MolWt(mol),
        "LogP": Descriptors.MolLogP(mol),
        "TPSA": Descriptors.TPSA(mol),
        "HBD": Descriptors.NumHDonors(mol),
        "HBA": Descriptors.NumHAcceptors(mol),
        "RotatableBonds": Descriptors.NumRotatableBonds(mol),
        "RingCount": rdMolDescriptors.CalcNumRings(mol),
        "HeavyAtoms": Descriptors.HeavyAtomCount(mol)
    }

    # 9. Arrange features in correct order
    input_data = pd.DataFrame(
        [[descriptors[name] for name in feature_names]],
        columns=feature_names
    )


    # 10. Predict solubility
    prediction = model.predict(input_data)[0]

    # 10.1 Lipinski Rule of Five Analysis
    lipinski = {
        "MolecularWeight": descriptors["MolWt"] <= 500,
        "LogP": descriptors["LogP"] <= 5,
        "HydrogenBondDonors": descriptors["HBD"] <= 5,
        "HydrogenBondAcceptors": descriptors["HBA"] <= 10
    }

    # Count Lipinski violations
    violations = sum(
        1 for passed in lipinski.values() if not passed
    )

    # Prepare Lipinski result
    lipinski_result = {
        "rules": lipinski,
        "violations": violations,
        "drug_likeness": (
            "Likely to satisfy Lipinski criteria"
            if violations == 0
            else "Lipinski criteria violations detected"
        )
    }

    # 11. Return result
    return {
        "smiles": data.smiles,
        "predicted_log_solubility": round(float(prediction), 4),
        "molecular_descriptors": descriptors,
        "lipinski_analysis": lipinski_result
    }


# 12. Generate 2D molecule visualization
@app.get("/visualize")
def visualize_molecule(smiles: str):

    # Convert SMILES into molecule
    mol = Chem.MolFromSmiles(smiles)

    # Validate molecule
    if mol is None:
        raise HTTPException(
            status_code=400,
            detail="Invalid SMILES string"
        )

    # Generate 2D coordinates
    from rdkit.Chem import AllChem
    AllChem.Compute2DCoords(mol)

    # Draw molecule
    img = Draw.MolToImage(
        mol,
        size=(500, 400)
    )

    # Convert image into bytes
    image_bytes = BytesIO()
    img.save(image_bytes, format="PNG")
    image_bytes.seek(0)

    # Return image
    return StreamingResponse(
        image_bytes,
        media_type="image/png"
    )
