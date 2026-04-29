from flask import Flask, request, jsonify
import joblib
import pandas as pd

app = Flask(__name__)
model = joblib.load('vuln_model.pkl')

@app.route('/')
def home():
    return "🤖 AI-Enhanced DevSecOps: Vuln Risk Predictor on Docker/EKS"

@app.route('/predict', methods=['POST'])
def predict():
    data = request.json
    df = pd.DataFrame([data])
    risk = model.predict_proba(df)[0][1] * 100
    return jsonify({
        "risk_score": f"{risk:.1f}%",
        "alert": "🚨 PATCH CRITICAL" if risk > 50 else "✅ Low Risk"
    })

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)
