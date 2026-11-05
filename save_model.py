import pandas as pd
import joblib

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor

# Load dataset
df = pd.read_csv("dataset/molecules_with_descriptors.csv")

# Select features
features = [
    "MolWt",
    "LogP",
    "TPSA",
    "HBD",
    "HBA",
    "RotatableBonds",
    "RingCount",
    "HeavyAtoms"
]

X = df[features]

# Target
y = df["measured log solubility in mols per litre"]

# Split dataset
X_train, X_test, y_train, y_test = train_test_split(
    X, y,
    test_size=0.2,
    random_state=42
)

# Create Random Forest model
model = RandomForestRegressor(
    n_estimators=100,
    random_state=42
)

# Train model
model.fit(X_train, y_train)

# Save model
joblib.dump(model, "drug_solubility_model.pkl")

# Save feature names
joblib.dump(features, "feature_names.pkl")

print("Random Forest model saved successfully!")