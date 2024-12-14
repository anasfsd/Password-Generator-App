%%writefile app.py
import streamlit as st
import random
import string

# Set the page title and icon
st.set_page_config(page_title="Password Generator", page_icon="🔒")

# App Header
st.title("🔒 Password Generator")
st.write("""
    Generate secure and random passwords for your online accounts. 
    Customize your password length and include/exclude special characters as needed!
""")

# Input Section
st.header("Customize Your Password")

# Select password length
password_length = st.slider("Select Password Length:", min_value=6, max_value=32, value=12)

# Checkbox options
include_uppercase = st.checkbox("Include Uppercase Letters (A-Z)", value=True)
include_numbers = st.checkbox("Include Numbers (0-9)", value=True)
include_special = st.checkbox("Include Special Characters (@, #, $, etc.)", value=True)

# Generate Password Button
if st.button("Generate Password"):
    # Build the character set based on user preferences
    character_set = string.ascii_lowercase  # Always include lowercase letters
    if include_uppercase:
        character_set += string.ascii_uppercase
    if include_numbers:
        character_set += string.digits
    if include_special:
        character_set += string.punctuation
    
    # Ensure the character set is not empty
    if character_set:
        # Generate a random password
        password = ''.join(random.choices(character_set, k=password_length))
        st.subheader("Your Generated Password:")
        st.code(password)
    else:
        st.error("Please select at least one character type to include in the password.")

# Footer
st.write("---")
st.write("Created with ❤️ using Streamlit.")
