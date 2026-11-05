
import { useState } from "react";
import "./App.css";

import {
  ResponsiveContainer,
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip
} from "recharts";

function App() {
  const [smiles, setSmiles] = useState("CCO");
  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);
  const [error, setError] = useState("");

  // Load previous prediction history
  const [history, setHistory] = useState(() => {
    try {
      return JSON.parse(
        localStorage.getItem("predictionHistory")
      ) || [];
    } catch {
      return [];
    }
  });

  // Lipinski rule names
  const lipinskiLabels = {
    MolecularWeight: "Molecular Weight (≤ 500)",
    LogP: "LogP (≤ 5)",
    HydrogenBondDonors: "H-Bond Donors (≤ 5)",
    HydrogenBondAcceptors: "H-Bond Acceptors (≤ 10)",
  };

  // Predict molecule
  const predictMolecule = async () => {
    setLoading(true);
    setError("");
    setResult(null);

    try {
      const response = await fetch(
        "http://127.0.0.1:8000/predict",
        {
          method: "POST",
          headers: {
            "Content-Type": "application/json",
          },
          body: JSON.stringify({ smiles }),
        }
      );

      const data = await response.json();

      if (!response.ok) {
        throw new Error(
          data.detail || "Prediction failed"
        );
      }

      setResult(data);

      // Create history entry
      const newEntry = {
        id: Date.now(),
        smiles: data.smiles,
        solubility: data.predicted_log_solubility,
        violations: data.lipinski_analysis.violations,
        date: new Date().toLocaleString()
      };

      // Save history in localStorage
      setHistory((previousHistory) => {
        const updatedHistory = [
          ...previousHistory,
          newEntry
        ];

        localStorage.setItem(
          "predictionHistory",
          JSON.stringify(updatedHistory)
        );

        return updatedHistory;
      });

    } catch (err) {
      setError(err.message);
    } finally {
      setLoading(false);
    }
  };

  // Clear history
  const clearHistory = () => {
    setHistory([]);
    localStorage.removeItem("predictionHistory");
  };

  return (
    <div className="app">

      {/* Navbar */}
      <nav className="navbar">
        <h2>⚗ DrugPredict AI</h2>
        <span>Machine Learning Powered</span>
      </nav>

      <main className="container">

        {/* Hero Section */}
        <section className="hero">
          <p className="tag">AI + CHEMISTRY</p>

          <h1>Drug Molecule Property Prediction</h1>

          <p>
            Predict molecular water solubility using
            RDKit and Machine Learning.
          </p>
        </section>

        {/* Input Section */}
        <section className="prediction-card">
          <h2>Enter Molecule SMILES</h2>

          <input
            type="text"
            value={smiles}
            onChange={(e) => setSmiles(e.target.value)}
            placeholder="Enter SMILES, e.g. CCO"
          />

          <button
            onClick={predictMolecule}
            disabled={loading || !smiles.trim()}
          >
            {loading
              ? "Predicting..."
              : "Predict Solubility"}
          </button>

          {error && (
            <p className="error">{error}</p>
          )}
        </section>

        {/* Prediction Results */}
        {result && (
          <section className="results">

            <h2>Prediction Results</h2>

            {/* Solubility */}
            <div className="result-highlight">
              <p>
                Predicted Log Solubility (log mol/L)
              </p>

              <h1>
                {result.predicted_log_solubility}
              </h1>

              <p>SMILES: {result.smiles}</p>
            </div>

            {/* 2D Visualization */}
            <div className="molecule-visualization">
              <h2>2D Molecule Structure</h2>

              <img
                src={`http://127.0.0.1:8000/visualize?smiles=${encodeURIComponent(
                  result.smiles
                )}`}
                alt="2D molecular structure"
                onError={(e) => {
                  e.currentTarget.style.display = "none";
                }}
              />
            </div>

            {/* Molecular Descriptors */}
            <h2>Molecular Descriptors</h2>

            <div className="descriptor-grid">
              {Object.entries(
                result.molecular_descriptors
              ).map(([name, value]) => (
                <div className="descriptor" key={name}>
                  <p>{name}</p>

                  <h3>
                    {typeof value === "number"
                      ? Number(value.toFixed(4))
                      : value}
                  </h3>
                </div>
              ))}
            </div>

            {/* Lipinski Analysis */}
            <h2>Lipinski Rule of Five Analysis</h2>

            <div className="result-highlight">
              <p>Drug-likeness Screening</p>

              <h2>
                {result.lipinski_analysis.drug_likeness}
              </h2>

              <h1>
                {result.lipinski_analysis.violations}
                {" "}Violations
              </h1>
            </div>

            {/* Individual Lipinski Rules */}
            <div className="descriptor-grid">
              {Object.entries(
                result.lipinski_analysis.rules
              ).map(([name, passed]) => (
                <div className="descriptor" key={name}>
                  <p>{lipinskiLabels[name]}</p>

                  <h3
                    style={{
                      color: passed
                        ? "#22c55e"
                        : "#ef4444"
                    }}
                  >
                    {passed ? "✓ PASS" : "✗ FAIL"}
                  </h3>
                </div>
              ))}
            </div>

          </section>
        )}

        {/* STEP 11: HISTORY AND CHARTS */}
        {history.length > 0 && (
          <section className="results">

            {/* Solubility Chart */}
            <h2>Solubility Prediction Chart</h2>

            <div className="prediction-card">

              <ResponsiveContainer
                width="100%"
                height={350}
              >
                <BarChart data={history}>
                  <CartesianGrid
                    strokeDasharray="3 3"
                    stroke="#334155"
                  />

                  <XAxis
                    dataKey="smiles"
                    stroke="#94a3b8"
                  />

                  <YAxis
                    stroke="#94a3b8"
                    label={{
                      value: "Log Solubility",
                      angle: -90,
                      position: "insideLeft"
                    }}
                  />

                  <Tooltip
                    contentStyle={{
                      backgroundColor: "#172033",
                      border: "1px solid #334155",
                      borderRadius: "8px",
                      color: "#ffffff"
                    }}
                  />

                  <Bar
                    dataKey="solubility"
                    fill="#3b82f6"
                    name="Predicted Solubility"
                  />

                </BarChart>
              </ResponsiveContainer>

            </div>

            {/* Prediction History Table */}
            <h2>Prediction History</h2>

            <div className="prediction-card">

              <div style={{ overflowX: "auto" }}>

                <table
                  style={{
                    width: "100%",
                    textAlign: "left",
                    borderCollapse: "collapse"
                  }}
                >

                  <thead>
                    <tr>
                      <th>SMILES</th>
                      <th>Solubility</th>
                      <th>Violations</th>
                      <th>Date & Time</th>
                    </tr>
                  </thead>

                  <tbody>
                    {history.map((item) => (
                      <tr key={item.id}>
                        <td>{item.smiles}</td>

                        <td>
                          {item.solubility}
                        </td>

                        <td>
                          {item.violations}
                        </td>

                        <td>
                          {item.date}
                        </td>
                      </tr>
                    ))}
                  </tbody>

                </table>

              </div>

              {/* Clear History */}
              <button
                onClick={clearHistory}
                style={{
                  marginTop: "20px",
                  backgroundColor: "#dc2626"
                }}
              >
                Clear History
              </button>

            </div>

          </section>
        )}

      </main>

      {/* Footer */}
      <footer>
        DrugPredict AI | Academic Machine Learning Project
      </footer>

    </div>
  );
}

export default App;
