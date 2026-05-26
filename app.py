"""
app.py
======
Main Flask application for the Diabetes Prediction System.

Routes:
  GET  /          → Home page with prediction form
  POST /predict   → Process form data, run ML model, show result
  GET  /about     → About / model stats page
"""

from flask import Flask, render_template, request, jsonify
import joblib
import numpy as np
import os
import json

# ─── App Setup ────────────────────────────────────────────────────────────────
app = Flask(__name__)

BASE_DIR    = os.path.dirname(os.path.abspath(__file__))
MODEL_PATH  = os.path.join(BASE_DIR, "models", "diabetes_model.pkl")
SCALER_PATH = os.path.join(BASE_DIR, "models", "scaler.pkl")
STATS_PATH  = os.path.join(BASE_DIR, "models", "model_stats.json")

# ─── Load Model & Scaler once at startup ──────────────────────────────────────
try:
    model  = joblib.load(MODEL_PATH)
    scaler = joblib.load(SCALER_PATH)
    with open(STATS_PATH) as f:
        model_stats = json.load(f)
    print("✅ Model and scaler loaded successfully.")
except Exception as e:
    print(f"❌ Error loading model: {e}")
    print("   Please run: python train_model.py first!")
    model, scaler, model_stats = None, None, {}

# ─── Feature metadata (for validation & display) ─────────────────────────────
FEATURES = [
    {"name": "Pregnancies",              "min": 0,     "max": 20,   "step": 1,    "unit": "times"},
    {"name": "Glucose",                  "min": 44,    "max": 200,  "step": 1,    "unit": "mg/dL"},
    {"name": "BloodPressure",            "min": 24,    "max": 122,  "step": 1,    "unit": "mm Hg"},
    {"name": "SkinThickness",            "min": 7,     "max": 99,   "step": 1,    "unit": "mm"},
    {"name": "Insulin",                  "min": 14,    "max": 850,  "step": 1,    "unit": "μU/mL"},
    {"name": "BMI",                      "min": 10.0,  "max": 70.0, "step": 0.1,  "unit": "kg/m²"},
    {"name": "DiabetesPedigreeFunction", "min": 0.078, "max": 2.5,  "step": 0.001,"unit": "score"},
    {"name": "Age",                      "min": 21,    "max": 90,   "step": 1,    "unit": "years"},
]


def validate_input(form_data):
    """Validate and parse form input. Returns (values_list, error_message)."""
    values = []
    for feat in FEATURES:
        name = feat["name"]
        try:
            val = float(form_data.get(name, ""))
        except (ValueError, TypeError):
            return None, f"Invalid value for {name}. Please enter a number."
        if val < feat["min"] or val > feat["max"]:
            return None, f"{name} must be between {feat['min']} and {feat['max']}."
        values.append(val)
    return values, None


# ─── Routes ───────────────────────────────────────────────────────────────────

@app.route("/")
def index():
    """Render the home/prediction form page."""
    return render_template("index.html", features=FEATURES)


@app.route("/predict", methods=["POST"])
def predict():
    """Handle form submission, run prediction, return result page."""
    if model is None:
        return render_template("result.html",
                               error="Model not loaded. Run train_model.py first.",
                               features=FEATURES)

    # 1. Validate input
    values, error = validate_input(request.form)
    if error:
        return render_template("index.html", features=FEATURES, error=error,
                               form_data=request.form)

    # 2. Preprocess
    input_array  = np.array([values])
    input_scaled = scaler.transform(input_array)

    # 3. Predict
    prediction   = model.predict(input_scaled)[0]           # 0 or 1
    probability  = model.predict_proba(input_scaled)[0]     # [prob_0, prob_1]
    prob_percent = round(probability[1] * 100, 2)           # % chance of diabetes

    # 4. Build user-friendly input dict for display
    input_display = {
        feat["name"]: {"value": values[i], "unit": feat["unit"]}
        for i, feat in enumerate(FEATURES)
    }

    return render_template(
        "result.html",
        prediction   = int(prediction),
        probability  = prob_percent,
        prob_no_diab = round(probability[0] * 100, 2),
        input_data   = input_display,
        model_stats  = model_stats,
    )


@app.route("/about")
def about():
    """Model info and stats page."""
    return render_template("about.html", model_stats=model_stats)


@app.route("/api/predict", methods=["POST"])
def api_predict():
    """JSON API endpoint for predictions (bonus feature)."""
    if model is None:
        return jsonify({"error": "Model not loaded"}), 500
    data = request.get_json(force=True)
    values, error = validate_input(data)
    if error:
        return jsonify({"error": error}), 400
    input_scaled = scaler.transform([values])
    pred  = int(model.predict(input_scaled)[0])
    proba = model.predict_proba(input_scaled)[0].tolist()
    return jsonify({
        "prediction": pred,
        "label": "Diabetic" if pred == 1 else "Non-Diabetic",
        "probability_diabetic": round(proba[1]*100, 2),
        "probability_non_diabetic": round(proba[0]*100, 2),
    })


# ─── Run ──────────────────────────────────────────────────────────────────────
if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
