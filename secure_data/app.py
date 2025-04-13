import streamlit as st
import hashlib
from cryptography.fernet import Fernet

# Generate encryption key
KEY = Fernet.generate_key()
cipher = Fernet(KEY)

# Memory-based storage (temporary)
stored_data = {}

# Session state for failed attempts
if "failed_attempts" not in st.session_state:
    st.session_state.failed_attempts = 0

# Hash passkey using SHA-256
def hash_key(passkey):
    return hashlib.sha256(passkey.encode()).hexdigest()

# Encrypt text
def encrypt_msg(msg):
    return cipher.encrypt(msg.encode()).decode()

# Decrypt text
def decrypt_msg(token):
    return cipher.decrypt(token.encode()).decode()

# Streamlit UI
st.title("🔐 Easy Secure Data App")

# Sidebar navigation
menu = ["Home", "Store Data", "Retrieve Data", "Login"]
choice = st.sidebar.selectbox("Choose Page", menu)

# Home Page
if choice == "Home":
    st.write("Welcome! You can securely **store** and **retrieve** your messages here.")

# Store Data Page
elif choice == "Store Data":
    st.subheader("📦 Store Your Secret Message")
    text = st.text_input("Enter Secret Message")
    passkey = st.text_input("Create a Passkey", type="password")

    if st.button("Save"):
        if text and passkey:
            enc_text = encrypt_msg(text)
            hashed = hash_key(passkey)
            stored_data[enc_text] = {"data": enc_text, "key": hashed}
            st.success("✅ Data Stored Securely!")
        else:
            st.warning("Please fill all fields.")

# Retrieve Data Page
elif choice == "Retrieve Data":
    st.subheader("🔓 Retrieve Your Message")

    encrypted_input = st.text_input("Enter Encrypted Text")
    passkey = st.text_input("Enter Your Passkey", type="password")

    if st.button("Decrypt"):
        if encrypted_input and passkey:
            hashed = hash_key(passkey)
            record = stored_data.get(encrypted_input)

            if record and record["key"] == hashed:
                msg = decrypt_msg(encrypted_input)
                st.success(f"Your Message: {msg}")
                st.session_state.failed_attempts = 0
            else:
                st.session_state.failed_attempts += 1
                remaining = 3 - st.session_state.failed_attempts
                st.error(f"Wrong passkey! Tries left: {remaining}")

                if st.session_state.failed_attempts >= 3:
                    st.warning("Too many tries! Redirecting to Login...")
                    st.rerun()
        else:
            st.warning("Fill in all fields.")

# Login Page
elif choice == "Login":
    st.subheader("🔐 Login to Unlock")
    login = st.text_input("Enter Admin Password", type="password")

    if st.button("Login"):
        if login == "admin123":
            st.session_state.failed_attempts = 0
            st.success("Login successful! You can now try again.")
            st.rerun()
        else:
            st.error("Wrong password!")
