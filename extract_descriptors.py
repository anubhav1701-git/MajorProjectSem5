import pandas as pd

from rdkit import Chem
from rdkit.Chem import Descriptors
from rdkit.Chem import rdMolDescriptors

# Load dataset
df = pd.read_csv("dataset/delaney-processed.csv")

# Function to extract descriptors
def calculate_descriptors(smiles):

    mol = Chem.MolFromSmiles(smiles)

    if mol is None:
        return None

    return {
        "MolWt": Descriptors.MolWt(mol),

        "LogP": Descriptors.MolLogP(mol),

        "TPSA": Descriptors.TPSA(mol),

        "HBD": Descriptors.NumHDonors(mol),

        "HBA": Descriptors.NumHAcceptors(mol),

        "RotatableBonds":
            Descriptors.NumRotatableBonds(mol),

        "RingCount": rdMolDescriptors.CalcNumRings(mol),

        "HeavyAtoms": Descriptors.HeavyAtomCount(mol)
    }


# Extract descriptors for every molecule
features = df["smiles"].apply(calculate_descriptors)

# Convert into DataFrame
features_df = pd.DataFrame(features.tolist())

# Combine with original dataset
result = pd.concat([df, features_df], axis=1)

# Save extracted features
result.to_csv(
    "dataset/molecules_with_descriptors.csv",
    index=False
)

print("\nMOLECULAR DESCRIPTORS:")
print(features_df.head())

print("\nDESCRIPTOR SHAPE:")
print(features_df.shape)

print("\nDESCRIPTORS EXTRACTED SUCCESSFULLY!")