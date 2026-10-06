import joblib
import pandas as pd
import streamlit as st
from pathlib import Path


st.set_page_config(
    page_title="Aurelia | Home Valuation",
    page_icon="⌂",
    layout="wide",
    initial_sidebar_state="collapsed",
)

BASE_DIR = Path(__file__).resolve().parent
MODEL_PATH = BASE_DIR / "house_price_model.pkl"

FEATURE_ORDER = [
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
    "zipcode",
]

st.markdown(
    """
    <style>
    :root {
        --ink: #f2eee6;
        --muted: #a8a197;
        --base: #11110f;
        --surface: #191916;
        --surface-raised: #201f1b;
        --line: rgba(235, 224, 203, .12);
        --gold: #d7a95b;
        --gold-light: #f0c879;
        --green: #93ad8d;
    }
    html, body, [data-testid="stAppViewContainer"] { background: var(--base); color: var(--ink); }
    [data-testid="stHeader"] { background: transparent; }
    [data-testid="stAppViewContainer"] > .main { background: var(--base); }
    .block-container { max-width: 1240px; padding: 2rem 2rem 4rem; }
    [data-testid="stSidebar"] { background: var(--surface); }
    h1, h2, h3, p, label, span, div { font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif; }
    .eyebrow { color: var(--gold-light); font-size: .72rem; font-weight: 700; letter-spacing: .18em; text-transform: uppercase; }
    .hero { position: relative; overflow: hidden; padding: 2.4rem 2.6rem; border: 1px solid var(--line); border-radius: 22px; background: radial-gradient(ellipse at 90% 0%, rgba(215,169,91,.13), transparent 42%), linear-gradient(135deg, #201f1b, #151512 68%); margin: .4rem 0 1.6rem; }
    .hero:after { content: "⌂"; position: absolute; right: 5%; top: -36px; color: rgba(215,169,91,.10); font-size: 210px; line-height: 1; font-family: Georgia, serif; pointer-events: none; }
    .hero h1 { font-family: Georgia, "Times New Roman", serif; font-size: clamp(2.25rem, 5vw, 4rem); font-weight: 500; letter-spacing: -.045em; line-height: 1.05; margin: .45rem 0 .75rem; color: #f4eee2; }
    .hero-copy { max-width: 650px; color: #bcb5a9; font-size: 1rem; line-height: 1.65; }
    .hero-meta { margin-top: 1.55rem; display: flex; gap: .65rem; flex-wrap: wrap; }
    .pill { border: 1px solid var(--line); border-radius: 999px; padding: .38rem .72rem; color: #d8d0c2; font-size: .76rem; background: rgba(10,10,9,.22); }
    .section-heading { margin: 2rem 0 .25rem; color: var(--ink); font-family: Georgia, "Times New Roman", serif; font-size: 1.65rem; }
    .section-copy { color: var(--muted); margin: 0 0 1rem; font-size: .9rem; }
    .panel { border: 1px solid var(--line); background: var(--surface); border-radius: 16px; padding: 1.15rem 1.25rem .5rem; margin: .5rem 0 1rem; }
    .panel-title { color: var(--gold-light); font-size: .73rem; letter-spacing: .12em; text-transform: uppercase; font-weight: 700; margin: 0 0 .4rem; }
    [data-testid="stNumberInput"], [data-testid="stSelectbox"], [data-testid="stSlider"] { margin-bottom: .45rem; }
    [data-testid="stNumberInput"] label, [data-testid="stSelectbox"] label, [data-testid="stSlider"] label { color: #d5cec1 !important; font-size: .83rem !important; }
    [data-testid="stNumberInput"] input, [data-testid="stSelectbox"] div[data-baseweb="select"] > div { background: #121210 !important; color: var(--ink) !important; border-color: var(--line) !important; border-radius: 9px !important; }
    [data-testid="stSlider"] [data-baseweb="slider"] div[role="slider"] { background: var(--gold) !important; }
    div.stButton > button[kind="primary"], div[data-testid="stFormSubmitButton"] > button { background: var(--gold) !important; color: #17130d !important; border: 0 !important; border-radius: 10px !important; font-weight: 750 !important; min-height: 3rem; transition: transform .15s ease, background .15s ease; }
    div.stButton > button[kind="primary"]:hover, div[data-testid="stFormSubmitButton"] > button:hover { background: var(--gold-light) !important; transform: translateY(-1px); }
    .result-card { border: 1px solid rgba(215,169,91,.38); border-radius: 18px; padding: 1.55rem 1.7rem; background: radial-gradient(ellipse at 100% 0%, rgba(215,169,91,.13), transparent 48%), #1d1b16; margin: .6rem 0 1rem; }
    .result-label { color: #c8bda8; text-transform: uppercase; letter-spacing: .13em; font-size: .73rem; font-weight: 700; }
    .result-price { color: var(--gold-light); font-family: Georgia, "Times New Roman", serif; font-size: clamp(2.5rem, 6vw, 4.2rem); line-height: 1.1; margin: .4rem 0 .7rem; }
    .result-note { color: #aaa294; font-size: .86rem; }
    .metric-card { height: 100%; min-height: 105px; border: 1px solid var(--line); border-radius: 14px; background: var(--surface); padding: 1rem 1.05rem; }
    .metric-label { color: var(--muted); font-size: .74rem; text-transform: uppercase; letter-spacing: .09em; }
    .metric-value { color: #f0e9dd; font-family: Georgia, "Times New Roman", serif; font-size: 1.65rem; margin-top: .5rem; }
    .workflow { border: 1px solid var(--line); border-radius: 16px; background: var(--surface); padding: 1.15rem; min-height: 130px; }
    .workflow-number { color: var(--gold); font-family: Georgia, serif; font-size: 1.4rem; }
    .workflow-title { color: var(--ink); font-weight: 700; margin: .45rem 0 .25rem; }
    .workflow-copy { color: var(--muted); font-size: .83rem; line-height: 1.45; }
    .footer { border-top: 1px solid var(--line); margin-top: 2.5rem; padding-top: 1rem; color: #817b71; font-size: .78rem; }
    [data-testid="stMetric"] { background: var(--surface); border: 1px solid var(--line); padding: 1rem; border-radius: 14px; }
    [data-testid="stMetricLabel"] { color: var(--muted) !important; }
    [data-testid="stMetricValue"] { color: var(--gold-light) !important; }
    [data-testid="stDataFrame"] { border: 1px solid var(--line); border-radius: 12px; }
    @media (max-width: 700px) { .block-container { padding: 1rem 1rem 3rem; } .hero { padding: 1.5rem; } .hero:after { right: -2%; top: 5px; font-size: 130px; } }
    </style>
    """,
    unsafe_allow_html=True,
)


@st.cache_resource
def load_model():
    return joblib.load(MODEL_PATH)


try:
    model = load_model()
except Exception as error:
    st.error("Unable to load the house price model. Confirm `house_price_model.pkl` is included in the deployment.")
    st.exception(error)
    st.stop()


st.markdown(
    """
    <section class="hero">
      <div class="eyebrow">Residential intelligence · King County</div>
      <h1>A considered view<br>of home value.</h1>
      <div class="hero-copy">Explore a data-driven estimate shaped by a trained Random Forest model and the details that make each property distinct.</div>
      <div class="hero-meta"><span class="pill">Random Forest Regressor</span><span class="pill">16 property signals</span><span class="pill">Instant estimate</span></div>
    </section>
    """,
    unsafe_allow_html=True,
)

st.markdown('<div class="section-heading">Property profile</div><div class="section-copy">Enter the home details below to create a tailored estimate.</div>', unsafe_allow_html=True)

with st.form("valuation_form"):
    st.markdown('<div class="panel"><div class="panel-title">01 · Home & condition</div>', unsafe_allow_html=True)
    col1, col2, col3, col4 = st.columns(4)
    with col1:
        bedrooms = st.number_input("Bedrooms", 0, 20, 3, 1)
    with col2:
        bathrooms = st.number_input("Bathrooms", 0.0, 10.0, 2.0, 0.25)
    with col3:
        floors = st.number_input("Floors", 1.0, 4.0, 1.0, 0.5)
    with col4:
        waterfront = st.selectbox("Waterfront", [0, 1], format_func=lambda value: "Yes" if value else "No")

    col1, col2, col3 = st.columns(3)
    with col1:
        view = st.slider("View quality", 0, 4, 0)
    with col2:
        condition = st.slider("Overall condition", 1, 5, 3)
    with col3:
        grade = st.slider("Construction grade", 1, 13, 7)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="panel"><div class="panel-title">02 · Living space</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        sqft_living = st.number_input("Interior living area (sq ft)", 100.0, 20000.0, 1800.0, 50.0)
    with col2:
        sqft_lot = st.number_input("Lot area (sq ft)", 100.0, 1000000.0, 5000.0, 100.0)
    with col3:
        sqft_above = st.number_input("Above-ground area (sq ft)", 100.0, 20000.0, 1500.0, 50.0)
    col1, col2 = st.columns(2)
    with col1:
        sqft_basement = st.number_input("Basement area (sq ft)", 0.0, 10000.0, 0.0, 50.0)
    with col2:
        sqft_living15 = st.number_input("Nearby homes · avg. living area (sq ft)", 100.0, 20000.0, 1800.0, 50.0)
    st.markdown('</div>', unsafe_allow_html=True)

    st.markdown('<div class="panel"><div class="panel-title">03 · Location & era</div>', unsafe_allow_html=True)
    col1, col2, col3 = st.columns(3)
    with col1:
        lat = st.number_input("Latitude", 47.0, 48.0, 47.51, format="%.6f")
    with col2:
        long = st.number_input("Longitude", -122.6, -121.0, -122.25, format="%.6f")
    with col3:
        zipcode = st.number_input("ZIP code", 98000, 99999, 98103, 1)
    yr_built = st.number_input("Year built", 1800, 2026, 1990, 1)
    st.markdown('</div>', unsafe_allow_html=True)

    predict_button = st.form_submit_button("Generate home valuation", type="primary", use_container_width=True)

if predict_button:
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
        "zipcode": zipcode,
    }
    try:
        house_df = pd.DataFrame([house_data])[FEATURE_ORDER]
        prediction = model.predict(house_df)
        st.session_state["valuation"] = {
            "price": float(prediction[0]),
            "inputs": house_data,
        }
    except Exception as error:
        st.error("The valuation could not be generated. Please review the property details and try again.")
        st.exception(error)

valuation = st.session_state.get("valuation")
if valuation:
    price = valuation["price"]
    values = valuation["inputs"]
    st.markdown('<div class="section-heading">Your valuation</div><div class="section-copy">A model estimate based on the property profile you provided.</div>', unsafe_allow_html=True)
    st.markdown(
        f'<div class="result-card"><div class="result-label">Estimated market value</div><div class="result-price">${price:,.0f}</div><div class="result-note">Machine learning estimate · For informational purposes</div></div>',
        unsafe_allow_html=True,
    )
    per_sqft = price / values["sqft_living"] if values["sqft_living"] else 0
    metric_cols = st.columns(3)
    with metric_cols[0]:
        st.markdown(f'<div class="metric-card"><div class="metric-label">Estimated price / sq ft</div><div class="metric-value">${per_sqft:,.0f}</div></div>', unsafe_allow_html=True)
    with metric_cols[1]:
        st.markdown(f'<div class="metric-card"><div class="metric-label">Interior living area</div><div class="metric-value">{values["sqft_living"]:,.0f} <small>sq ft</small></div></div>', unsafe_allow_html=True)
    with metric_cols[2]:
        st.markdown(f'<div class="metric-card"><div class="metric-label">Location</div><div class="metric-value">ZIP {int(values["zipcode"])}</div></div>', unsafe_allow_html=True)

    with st.expander("View property summary", expanded=True):
        left, right = st.columns(2)
        left.markdown(f"**Home**  \n{int(values['bedrooms'])} bedrooms · {values['bathrooms']:g} bathrooms · {values['floors']:g} floors  \nGrade {int(values['grade'])} · Condition {int(values['condition'])} · Built {int(values['yr_built'])}")
        right.markdown(f"**Space & location**  \n{values['sqft_living']:,.0f} sq ft living · {values['sqft_lot']:,.0f} sq ft lot  \n{values['lat']:.4f}, {values['long']:.4f} · ZIP {int(values['zipcode'])}")

st.markdown('<div class="section-heading">Model performance</div><div class="section-copy">Reported evaluation metrics for the trained model.</div>', unsafe_allow_html=True)
perf1, perf2, perf3 = st.columns(3)
with perf1:
    st.metric("R² score", "85.89%", help="Share of price variance explained by the model in evaluation.")
with perf2:
    st.metric("MAPE", "13.11%", help="Mean absolute percentage error in evaluation.")
with perf3:
    st.metric("Estimator", "Random Forest", help="Existing trained estimator loaded from house_price_model.pkl.")

st.markdown('<div class="section-heading">What informs the estimate</div><div class="section-copy">Feature importance is shown when the loaded estimator exposes it.</div>', unsafe_allow_html=True)
importance_model = model
if not hasattr(importance_model, "feature_importances_") and hasattr(importance_model, "named_steps"):
    for step in reversed(list(importance_model.named_steps.values())):
        if hasattr(step, "feature_importances_"):
            importance_model = step
            break
if hasattr(importance_model, "feature_importances_"):
    importances = getattr(importance_model, "feature_importances_")
    if len(importances) == len(FEATURE_ORDER):
        importance_df = pd.DataFrame({"Feature": FEATURE_ORDER, "Importance": importances})
        importance_df = importance_df.sort_values("Importance", ascending=False).head(10).set_index("Feature")
        st.bar_chart(importance_df, color="#d7a95b", horizontal=True)
    else:
        st.info("The model exposes feature importance, but its feature count does not match the 16 displayed input fields.")
else:
    st.info("This saved model does not expose feature importance. The valuation still uses the original trained model unchanged.")

st.markdown('<div class="section-heading">From details to estimate</div><div class="section-copy">A simple, transparent path from property information to a result.</div>', unsafe_allow_html=True)
flow_cols = st.columns(4)
steps = [
    ("01", "Describe", "Add property, size, condition, and location details."),
    ("02", "Shape", "Inputs are arranged using the model’s established 16-feature order."),
    ("03", "Estimate", "The existing trained Random Forest returns a price estimate."),
    ("04", "Explore", "Review price per square foot, the property summary, and model context."),
]
for column, (number, title, copy) in zip(flow_cols, steps):
    with column:
        st.markdown(f'<div class="workflow"><div class="workflow-number">{number}</div><div class="workflow-title">{title}</div><div class="workflow-copy">{copy}</div></div>', unsafe_allow_html=True)

st.markdown('<div class="footer">House price estimates are model outputs and are not appraisals, offers, or financial advice. Values depend on the accuracy of the information entered.</div>', unsafe_allow_html=True)
