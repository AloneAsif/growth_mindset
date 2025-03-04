import streamlit as st

def convert_units(value, from_unit, to_unit, conversion_dict):
    if from_unit in conversion_dict and to_unit in conversion_dict:
        return value * conversion_dict[to_unit] / conversion_dict[from_unit]
    return None

def main():
    st.title("Unit Converter")
    
    category = st.selectbox("Select Category", ["Length", "Weight", "Temperature"])
    
    if category == "Length":
        units = {"Meter": 1, "Kilometer": 1000, "Centimeter": 0.01, "Millimeter": 0.001, "Mile": 1609.34, "Yard": 0.9144, "Foot": 0.3048, "Inch": 0.0254}
    elif category == "Weight":
        units = {"Kilogram": 1, "Gram": 0.001, "Milligram": 0.000001, "Pound": 0.453592, "Ounce": 0.0283495}
    else:  # Temperature
        units = {"Celsius": "C", "Fahrenheit": "F", "Kelvin": "K"}
    
    from_unit = st.selectbox("From", list(units.keys()))
    to_unit = st.selectbox("To", list(units.keys()))
    value = st.number_input("Enter Value", min_value=0.0, format="%f")
    
    if st.button("Convert"):
        if category == "Temperature":
            if from_unit == to_unit:
                result = value
            elif from_unit == "Celsius" and to_unit == "Fahrenheit":
                result = (value * 9/5) + 32
            elif from_unit == "Celsius" and to_unit == "Kelvin":
                result = value + 273.15
            elif from_unit == "Fahrenheit" and to_unit == "Celsius":
                result = (value - 32) * 5/9
            elif from_unit == "Fahrenheit" and to_unit == "Kelvin":
                result = (value - 32) * 5/9 + 273.15
            elif from_unit == "Kelvin" and to_unit == "Celsius":
                result = value - 273.15
            elif from_unit == "Kelvin" and to_unit == "Fahrenheit":
                result = (value - 273.15) * 9/5 + 32
        else:
            result = convert_units(value, from_unit, to_unit, units)
        
        st.success(f"Converted Value: {result:.2f} {to_unit}")

if __name__ == "__main__":
    main()
