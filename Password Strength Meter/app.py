import re
import random
import string
import streamlit as st

def check_password_strength(password):
    strength = 0
    remarks = ""
    
    # Length Check
    if len(password) >= 8:
        strength += 1
    
    # Upper and Lower Case Check
    if re.search(r"[a-z]", password) and re.search(r"[A-Z]", password):
        strength += 1
    
    # Digit Check
    if re.search(r"\d", password):
        strength += 1
    
    # Special Character Check
    if re.search(r"[!@#$%^&*(),.?\":{}|<>]", password):
        strength += 1
    
    # Strength Evaluation
    if strength == 4:
        remarks = "Strong Password"
    elif strength == 3:
        remarks = "Moderate Password"
    elif strength == 2:
        remarks = "Weak Password"
    else:
        remarks = "Very Weak Password"
    
    return strength, remarks

def generate_random_password(length):
    characters = string.ascii_letters + string.digits + string.punctuation
    return ''.join(random.choice(characters) for _ in range(length))

# Streamlit UI
st.title("🔐 Password Strength Manager")
password = st.text_input("Enter your password", type="password")

if password:
    strength, remarks = check_password_strength(password)
    st.write(f"**Strength Score:** {strength}/4")
    st.write(f"**Remarks:** {remarks}")
    
    # Progress Bar
    st.progress(strength / 4.0)
                
# Password Generator
st.subheader("🔑 Generate a Random Password")
length = st.slider("Select password length", min_value=8, max_value=32, value=12)
if st.button("Generate Password"):
    random_password = generate_random_password(length)
    st.text_input("Generated Password", value=random_password, disabled=False)
