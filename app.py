import streamlit as st

# ---------------- PAGE CONFIG ----------------
st.set_page_config(
    page_title="Mechanical Unit Converter",
    page_icon="⚙️",
    layout="wide"
)

# ---------------- CUSTOM CSS ----------------
st.markdown("""
<style>

[data-testid="stAppViewContainer"]{
    background-image: url("https://images.unsplash.com/photo-1537462715879-360eeb61a0ad");
    background-size: cover;
    background-position: center;
    background-attachment: fixed;
}

.main {
    background: rgba(0,0,0,0.65);
    padding: 20px;
    border-radius: 15px;
}

h1, h2, h3, h4, h5, h6, p, label {
    color: white !important;
}

.stSelectbox label, .stNumberInput label {
    color: white !important;
}

</style>
""", unsafe_allow_html=True)

# ---------------- HEADER ----------------
st.title("⚙️ Mechanical Unit Converter & Material Density Checker")

st.markdown("""
### 👨‍🎓 Student Information

- **Name:** Syed Fasseh Naqvi
- **Registration Number:** 25-ME-56
""")

st.write("---")

# ---------------- UNIT CONVERTER ----------------
st.header("⚙️ Mechanical Unit Converter")

conversion = st.selectbox(
    "Select Conversion Type",
    [
        "Length",
        "Force",
        "Pressure",
        "Temperature",
        "Weight"
    ]
)

# LENGTH
if conversion == "Length":
    meter = st.number_input("Enter value in Meters", min_value=0.0)

    cm = meter * 100
    mm = meter * 1000
    inch = meter * 39.37

    st.success(f"Centimeters: {cm:.2f} cm")
    st.success(f"Millimeters: {mm:.2f} mm")
    st.success(f"Inches: {inch:.2f} in")

# FORCE
elif conversion == "Force":
    newton = st.number_input("Enter value in Newton", min_value=0.0)

    kn = newton / 1000
    lbf = newton * 0.224809

    st.success(f"KiloNewton: {kn:.4f} kN")
    st.success(f"Pound-force: {lbf:.4f} lbf")

# PRESSURE
elif conversion == "Pressure":
    pascal = st.number_input("Enter value in Pascal", min_value=0.0)

    bar = pascal / 100000
    psi = pascal * 0.000145038

    st.success(f"Bar: {bar:.5f} bar")
    st.success(f"PSI: {psi:.5f} psi")

# TEMPERATURE
elif conversion == "Temperature":
    celsius = st.number_input("Enter temperature in Celsius")

    fahrenheit = (celsius * 9/5) + 32
    kelvin = celsius + 273.15

    st.success(f"Fahrenheit: {fahrenheit:.2f} °F")
    st.success(f"Kelvin: {kelvin:.2f} K")

# WEIGHT
elif conversion == "Weight":
    kg = st.number_input("Enter weight in Kilograms", min_value=0.0)

    gram = kg * 1000
    pound = kg * 2.20462

    st.success(f"Grams: {gram:.2f} g")
    st.success(f"Pounds: {pound:.2f} lbs")

st.write("---")

# ---------------- DENSITY CHECKER ----------------
st.header("🛠️ Material Density Checker")

materials = {
    "Steel": 7850,
    "Aluminum": 2700,
    "Copper": 8960,
    "Brass": 8500,
    "Titanium": 4500,
    "Cast Iron": 7200,
    "Lead": 11340
}

material = st.selectbox(
    "Select Material",
    list(materials.keys())
)

density = materials[material]

st.info(f"Density of {material} = {density} kg/m³")

# ---------------- FOOTER ----------------
st.write("---")

st.markdown("""
<center>
<h4 style='color:white;'>
⚙️ Developed by Syed Fasseh Naqvi | 25-ME-56
</h4>
</center>
""", unsafe_allow_html=True)
