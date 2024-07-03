import streamlit as st
import pandas as pd

data = {}

# Creating DataFrame
df = pd.DataFrame(data)

st.set_page_config(page_title="Prediksi Berita", layout="wide")

# Dashboard title
st.title("Prediksi Berita")

# Container for the main content and additional content
container = st.container()
with container:
    col1, col2 = st.columns([3, 2])  # Adjust the ratio to leave more space for col2

    # Main content
    with col1:
        # CSS for left and right alignment and smaller content size
        st.markdown("""
            <style>
            .stMarkdown { text-align: justify; }
            .data-row { 
                display: flex; 
                justify-content: space-between; 
                margin-bottom: 10px; 
                padding: 10px;
                background-color: #f5f5f5; 
                border-radius: 5px;
                border: 1px solid #ddd;
                color: black;
            }
            .data-row:nth-child(odd) { background-color: #e1f5fe; }
            .data-row:hover { background-color: #c8e6c9; }
            .data-col { flex: 1; padding: 5px; font-size: 16px; text-align: left; }
            .data-col-date { flex: 1; padding: 5px; font-size: 16px; text-align: left; font-weight: bold; }
            .data-col-description { flex: 3; padding: 5px; font-size: 16px; text-align: left; }
            .data-col-type { flex: 2; padding: 5px; font-size: 16px; text-align: center; }
            .data-col-category { flex: 2; padding: 5px; font-size: 16px; text-align: center; font-weight: bold; }
            </style>
        """, unsafe_allow_html=True)

        # Displaying the transactions table
        for index, row in df.iterrows():
            st.markdown(f"""
                <div class="data-row">
                    <div class="data-col-date">{row['Date']}<span></span></div>
                    <div class="data-col-description">{row['judul']}</div>
                    <div class="data-col-type">{row['Category']}</div>
                    <div class="data-col-category">{row['Sentimen predik']}</div>
                </div>
            """, unsafe_allow_html=True)

        # "See more" button
        if st.button("See more"):
            st.write("Display more transactions here...")

    # Additional content
    with col2:
        st.subheader("Additional Content")
        st.write("Add your additional content here.")

# Adding CSS for the button
st.markdown("""
<style>
div.stButton > button {
    background-color: #28a745;
    color: white;
    padding: 8px 16px;
    border: none;
    border-radius: 4px;
    cursor: pointer;
}
div.stButton > button:hover {
    background-color: #218838;
}
</style>
""", unsafe_allow_html=True)
