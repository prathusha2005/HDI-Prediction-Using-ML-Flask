from pathlib import Path

import joblib
import numpy as np
import pandas as pd
from flask import Flask, render_template, request

# Define the base folder so the application can locate the trained model.
BASE_DIR = Path(__file__).resolve().parent.parent
MODEL_PATH = BASE_DIR / "Model" / "HDI_LinearRegression_Model.pkl"

app = Flask(__name__)

# This list matches the feature columns used during notebook training.
FEATURE_COLUMNS = [
    "Country",
    "Life expectancy",
    "Mean years of schooling",
    "Expected years of schooling",
    "Gross National Income (GNI) per capita",
]


def load_model():
    """Load the saved machine learning pipeline from disk."""
    if not MODEL_PATH.exists():
        raise FileNotFoundError(f"Model file not found at {MODEL_PATH}")

    return joblib.load(MODEL_PATH)


try:
    model = load_model()
    model_error = None
except Exception as exc:
    model = None
    model_error = str(exc)


def validate_and_build_dataframe(form_data):
    """Validate user input and convert it into the same DataFrame structure used in training."""
    errors = []

    # Country name is optional, but we still provide a default value.
    country_name = (form_data.get("country_name") or "").strip() or "Unknown"

    # Define the expected numeric ranges for each input field.
    validation_rules = {
        "life_expectancy": {
            "label": "Life Expectancy",
            "min": 40,
            "max": 90,
            "message": "between 40 and 90 years",
        },
        "mean_years_schooling": {
            "label": "Mean Years of Schooling",
            "min": 0,
            "max": 20,
            "message": "between 0 and 20",
        },
        "expected_years_schooling": {
            "label": "Expected Years of Schooling",
            "min": 0,
            "max": 25,
            "message": "between 0 and 25",
        },
        "gni_per_capita": {
            "label": "Gross National Income (GNI) per Capita",
            "min": 100,
            "max": 100000,
            "message": "between 100 and 100000",
        },
    }

    values = {}

    for field_name, rule in validation_rules.items():
        raw_value = (form_data.get(field_name) or "").strip()

        if not raw_value:
            errors.append(f"{rule['label']} is required.")
            continue

        try:
            numeric_value = float(raw_value)
        except ValueError:
            errors.append(f"{rule['label']} must be a valid number.")
            continue

        if not (rule["min"] <= numeric_value <= rule["max"]):
            errors.append(
                f"{rule['label']} must be in the valid range of {rule['message']}."
            )
            continue

        values[field_name] = numeric_value

    if errors:
        return None, errors

    # Build the DataFrame in the same order expected by the trained pipeline.
    input_frame = pd.DataFrame(
        [
            {
                "Country": country_name,
                "Life expectancy": values["life_expectancy"],
                "Mean years of schooling": values["mean_years_schooling"],
                "Expected years of schooling": values["expected_years_schooling"],
                "Gross National Income (GNI) per capita": values["gni_per_capita"],
            }
        ],
        columns=FEATURE_COLUMNS,
    )

    return input_frame, []


def get_hdi_category(prediction_value):
    """Map a predicted HDI score to a human-readable development category."""
    if prediction_value >= 0.800:
        return "🟢 Very High Human Development"
    if prediction_value >= 0.700:
        return "🔵 High Human Development"
    if prediction_value >= 0.550:
        return "🟡 Medium Human Development"
    return "🔴 Low Human Development"


@app.route("/", methods=["GET", "POST"])
def home():
    """Render the form and handle prediction requests."""
    prediction = None
    category = None
    error_message = None
    form_data = {}

    if request.method == "POST":
        form_data = request.form.to_dict()

        input_frame, errors = validate_and_build_dataframe(request.form)

        if errors:
            error_message = "Please correct the following issues: " + " ".join(errors)
        elif model is None:
            error_message = f"The trained model could not be loaded. Details: {model_error}"
        else:
            try:
                # Use the trained pipeline exactly as it was used in the notebook.
                prediction_value = model.predict(input_frame)[0]
                clipped_prediction = float(np.clip(prediction_value, 0.0, 1.0))
                prediction = round(clipped_prediction, 3)
                category = get_hdi_category(prediction)
            except Exception as exc:
                error_message = f"Prediction failed. Please check your input. Error: {exc}"

    return render_template(
        "index.html",
        prediction=prediction,
        error_message=error_message,
        form_data=form_data,
        model_error=model_error,
        category=category,
    )


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0", port=5000)
