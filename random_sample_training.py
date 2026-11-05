
import pandas as pd
import numpy as np
import joblib

import matplotlib.pyplot as plt
import seaborn as sns

from sklearn.model_selection import train_test_split
from sklearn.ensemble import RandomForestRegressor
from sklearn.metrics import mean_absolute_error, mean_squared_error, r2_score

# 1. Load dataset
df = pd.read_csv("dataset/molecules_with_descriptors.csv")

print("Original Dataset Shape:", df.shape)

# 2. Define input features
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

target = "measured log solubility in mols per litre"

# 3. Remove rows with missing values
df = df[features + [target]].dropna()

# 4. Randomly select 800 molecules
sample_size = min(800, len(df))

sample_df = df.sample(
    n=sample_size,
    random_state=42
)

print("Randomly Selected Molecules:", len(sample_df))

# 5. Prepare X and y
X = sample_df[features]
y = sample_df[target]

# 6. Split into training and testing data
X_train, X_test, y_train, y_test = train_test_split(
    X,
    y,
    test_size=0.2,
    random_state=42
)

print("Training Samples:", len(X_train))
print("Testing Samples:", len(X_test))

# 7. Create Random Forest model
model = RandomForestRegressor(
    n_estimators=200,
    random_state=42,
    n_jobs=-1
)

# 8. Train the model
print("\nTraining Random Forest Model...")
model.fit(X_train, y_train)

print("Model Training Completed!")

# 9. Make predictions
y_pred = model.predict(X_test)

# 10. Evaluate model
mae = mean_absolute_error(y_test, y_pred)
rmse = np.sqrt(mean_squared_error(y_test, y_pred))
r2 = r2_score(y_test, y_pred)

print("\n----- MODEL PERFORMANCE -----")
print("MAE:", round(mae, 4))
print("RMSE:", round(rmse, 4))
print("R2 Score:", round(r2, 4))

# 11. Save trained model
joblib.dump(model, "random_sample_model.pkl")
joblib.dump(features, "random_sample_features.pkl")

print("\nModel saved successfully!")
print("Files: random_sample_model.pkl")
print("       random_sample_features.pkl")


# 12. Graph 1: Actual vs Predicted Values

plt.figure(figsize=(8, 6))

plt.scatter(y_test, y_pred, alpha=0.7)

plt.plot(
    [y_test.min(), y_test.max()],
    [y_test.min(), y_test.max()],
    linestyle="--"
)

plt.xlabel("Actual Solubility")
plt.ylabel("Predicted Solubility")
plt.title("Actual vs Predicted Solubility")
plt.grid(True)
plt.tight_layout()
plt.savefig("actual_vs_predicted.png")
plt.show()


# 13. Graph 2: Feature Importance

importance = model.feature_importances_

plt.figure(figsize=(9, 6))

plt.barh(features, importance)

plt.xlabel("Importance Score")
plt.ylabel("Molecular Features")
plt.title("Random Forest Feature Importance")
plt.tight_layout()
plt.savefig("feature_importance.png")
plt.show()


# 14. Graph 3: Residual Distribution

residuals = y_test - y_pred

plt.figure(figsize=(8, 6))

plt.hist(residuals, bins=20)

plt.xlabel("Prediction Error")
plt.ylabel("Frequency")
plt.title("Residual Distribution")
plt.grid(True)
plt.tight_layout()
plt.savefig("residual_distribution.png")
plt.show()

print("\nAll graphs saved successfully!")
