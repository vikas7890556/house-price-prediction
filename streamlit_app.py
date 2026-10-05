import streamlit as st
import pandas as pd
import joblib
from pathlib import Path


# ============================================================
# PAGE CONFIGURATION
# ============================================================

st.set_page_config(
    page_title="House Price Prediction",
    page_icon="🏠",
    layout="wide",
    initial_sidebar_state="collapsed"
)


# ============================================================
# CUSTOM CSS
# ============================================================

st.markdown(
    """
    <style>

    .main {
        padding-top: 2rem;
    }

    .title {
        font-size: 42px;
        font-weight: 700;
        margin-bottom: 5px;
    }

    .subtitle {
        font-size: 18px;
        opacity: 0.75;
        margin-bottom: 30px;
    }

    .section-title {
        font-size: 22px;
        font-weight: 600;
        margin-top: 25px;
        margin-bottom: 10px;
    }

    .prediction-box {
        padding: 25px;
        border-radius: 15px;
        text-align: center;
        margin-top: 25px;
    }

    .prediction-label {
        font-size: 18px;
        opacity: 0.8;
    }

    .prediction-price {
        font-size: 42px;
        font-weight: 700;
        margin-top: 5px;
    }

    </style>
    """,
    unsafe_allow_html=True
)


# ============================================================
# MODEL LOADING
# ============================================================

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "house_price_model.pkl"


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


try:
    model = load_model()

except Exception as e:
    st.error("❌ Unable to load the house price prediction model.")
    st.exception(e)
    st.stop()


# ============================================================
# HEADER
# ============================================================

st.markdown(
    '<div class="title">🏠 House Price Prediction</div>',
    unsafe_allow_html=True
)

st.markdown(
    '<div class="subtitle">'
    'AI-powered house price estimation using a trained Random Forest model'
    '</div>',
    unsafe_allow_html=True
)


# ============================================================
# PROPERTY DETAILS
# ============================================================

st.markdown(
    '<div class="section-title">🏡 Property Details</div>',
    unsafe_allow_html=True
)

col1, col2, col3, col4 = st.columns(4)

with col1:
    bedrooms = st.number_input(
        "Bedrooms",
        min_value=0,
        max_value=20,
        value=3,
        step=1
    )

with col2:
    bathrooms = st.number_input(
        "Bathrooms",
        min_value=0.0,
        max_value=10.0,
        value=2.0,
        step=0.25
    )

with col3:
    floors = st.number_input(
        "Floors",
        min_value=1.0,
        max_value=4.0,
        value=1.0,
        step=0.5
    )

with col4:
    waterfront = st.selectbox(
        "Waterfront",
        options=[0, 1],
        format_func=lambda x: "Yes" if x == 1 else "No"
    )


col1, col2, col3 = st.columns(3)

with col1:
    view = st.slider(
        "View",
        min_value=0,
        max_value=4,
        value=0
    )

with col2:
    condition = st.slider(
        "Condition",
        min_value=1,
        max_value=5,
        value=3
    )

with col3:
    grade = st.slider(
        "Grade",
        min_value=1,
        max_value=13,
        value=7
    )


# ============================================================
# SIZE & AREA
# ============================================================

st.markdown(
    '<div class="section-title">📐 Size & Area</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    sqft_living = st.number_input(
        "Living Area (sqft)",
        min_value=100.0,
        max_value=20000.0,
        value=1800.0,
        step=50.0
    )

with col2:
    sqft_lot = st.number_input(
        "Lot Area (sqft)",
        min_value=100.0,
        max_value=1000000.0,
        value=5000.0,
        step=100.0
    )

with col3:
    sqft_above = st.number_input(
        "Above Ground Area (sqft)",
        min_value=100.0,
        max_value=20000.0,
        value=1500.0,
        step=50.0
    )


col1, col2, col3 = st.columns(3)

with col1:
    sqft_basement = st.number_input(
        "Basement Area (sqft)",
        min_value=0.0,
        max_value=10000.0,
        value=0.0,
        step=50.0
    )

with col2:
    sqft_living15 = st.number_input(
        "Living Area of 15 Nearby Houses (sqft)",
        min_value=100.0,
        max_value=20000.0,
        value=1800.0,
        step=50.0
    )


# ============================================================
# LOCATION
# ============================================================

st.markdown(
    '<div class="section-title">📍 Location</div>',
    unsafe_allow_html=True
)

col1, col2, col3 = st.columns(3)

with col1:
    lat = st.number_input(
        "Latitude",
        min_value=47.0,
        max_value=48.0,
        value=47.51,
        format="%.6f"
    )

with col2:
    long = st.number_input(
        "Longitude",
        min_value=-122.6,
        max_value=-121.0,
        value=-122.25,
        format="%.6f"
    )

with col3:
    zipcode = st.number_input(
        "Zipcode",
        min_value=98000,
        max_value=99999,
        value=98103,
        step=1
    )


# ============================================================
# YEAR BUILT
# ============================================================

st.markdown(
    '<div class="section-title">📅 Property Age</div>',
    unsafe_allow_html=True
)

yr_built = st.number_input(
    "Year Built",
    min_value=1800,
    max_value=2026,
    value=1990,
    step=1
)


# ============================================================
# PREDICTION
# ============================================================

st.markdown("---")

predict_button = st.button(
    "🔮 Predict House Price",
    type="primary",
    use_container_width=True
)


if predict_button:

    try:

        # Create input DataFrame
        house_data = {
            "bedrooms": bedrooms,
            "bathrooms": bathrooms,
            "sqft_living": sqft_living,
            "sqft_lot": sqft_lot,
            "floors": floors,
            "waterfront": waterfront,
            "view": view,
            "condition": condition,
            "grade": grade,
            "sqft_above": sqft_above,
            "sqft_basement": sqft_basement,
            "yr_built": yr_built,
            "sqft_living15": sqft_living15,
            "lat": lat,
            "long": long,
            "zipcode": zipcode
        }

        house_df = pd.DataFrame([house_data])

        # Ensure exact feature order
        feature_order = [
            "bedrooms",
            "bathrooms",
            "sqft_living",
            "sqft_lot",
            "floors",
            "waterfront",
            "view",
            "condition",
            "grade",
            "sqft_above",
            "sqft_basement",
            "yr_built",
            "sqft_living15",
            "lat",
            "long",
            "zipcode"
        ]

        house_df = house_df[feature_order]

        # Make prediction
        prediction = model.predict(house_df)

        predicted_price = float(prediction[0])

        # Display result
        st.markdown(
            f"""
            <div class="prediction-box">
                <div class="prediction-label">
                    Estimated House Price
                </div>
                <div class="prediction-price">
                    ${predicted_price:,.2f}
                </div>
            </div>
            """,
            unsafe_allow_html=True
        )

    except Exception as e:

        st.error("❌ Prediction failed.")
        st.exception(e)