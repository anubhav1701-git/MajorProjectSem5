import pandas as pd
import matplotlib.pyplot as plt

from sklearn.model_selection import train_test_split
from sklearn.linear_model import LinearRegression
from sklearn.tree import DecisionTreeRegressor
from sklearn.ensemble import RandomForestRegressor

from sklearn.metrics import mean_absolute_error
from sklearn.metrics import mean_squared_error
from sklearn.metrics import r2_score


# Load dataset
df = pd.read_csv("dataset/molecules_with_descriptors.csv")

# Select features
features = [
    "MolWt", "LogP", "TPSA", "HBD",
    "HBA", "RotatableBonds",
    "RingCount", "HeavyAtoms"
]

X = df[features]

# Target
y = df["measured log solubility in mols per litre"]

# Split data
X_train, X_test, y_train, y_test = train_test_split(
    X, y, test_size=0.2, random_state=42
)

# Models
models = {
    "Linear Regression": LinearRegression(),
    "Decision Tree": DecisionTreeRegressor(random_state=42),
    "Random Forest": RandomForestRegressor(
        n_estimators=100, random_state=42
    )
}

results = []

# Train and evaluate
for name, model in models.items():

    model.fit(X_train, y_train)

    predictions = model.predict(X_test)

    results.append({
        "Model": name,
        "MAE": mean_absolute_error(y_test, predictions),
        "RMSE": mean_squared_error(y_test, predictions) ** 0.5,
        "R2": r2_score(y_test, predictions)
    })

# Comparison table
results_df = pd.DataFrame(results)

print("\nMODEL COMPARISON:")
print(results_df.to_string(index=False))

# Best model
best_model = results_df.sort_values(
    by="R2", ascending=False
).iloc[0]

print("\nBEST MODEL:", best_model["Model"])

# Plot comparison
results_df.plot(
    x="Model",
    y="R2",
    kind="bar",
    legend=False,
    title="Model R2 Comparison"
)

plt.ylabel("R2 Score")
plt.tight_layout()
plt.savefig("model_comparison.png")
plt.show()

# Save results
results_df.to_csv("model_comparison.csv", index=False)