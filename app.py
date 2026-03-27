import streamlit as st
import pandas as pd
from generator import generate_test_cases
from formatter import format_output

# Page config
st.set_page_config(page_title="AI Test Case Generator", layout="centered")

# 🎨 Premium UI styling
st.markdown(
    """
    <style>
    .stButton button {
        background-color: #4CAF50;
        color: white;
        border-radius: 10px;
        height: 3em;
        width: 100%;
        border: none;
    }

    .stButton button:hover {
        background-color: #45a049;
        color: white;
    }

    .stTextArea textarea {
        border-radius: 10px;
        border: 2px solid #4CAF50;
    }
    </style>
    """,
    unsafe_allow_html=True
)

# Title
st.title("🧠 AI Test Case Generator")

# Input box
requirement = st.text_area("Enter your requirement:")

# Button action
if st.button("Generate Test Cases"):
    if requirement.strip() == "":
        st.warning("Please enter a requirement!")
    else:
        with st.spinner("Generating test cases..."):
            raw_output = generate_test_cases(requirement)

        # 🚨 Handle API errors properly
        if raw_output.startswith("Error"):
            st.error(raw_output)

        else:
            formatted_output = format_output(raw_output)

            st.subheader("📊 Test Cases Table")

            # Convert output → table
            lines = formatted_output.split("\n")
            data = []

            for i, line in enumerate(lines[:5], start=1):
                if "-" in line:
                    desc, exp = line.split("-", 1)
                else:
                    desc = line
                    exp = "Expected result"

                data.append({
                    "Test Case ID": f"TC_{i}",
                    "Description": desc.strip(),
                    "Expected Result": exp.strip()
                })

            df = pd.DataFrame(data)

            # Display table
            st.dataframe(df, use_container_width=True)

            # Download option
            st.download_button(
                label="⬇️ Download Test Cases",
                data=formatted_output,
                file_name="test_cases.txt",
                mime="text/plain"
            )