import streamlit as st
import pandas as pd
from datetime import datetime
import os

# Page configuration
st.set_page_config(layout="wide")

# --- Extreme Custom CSS for vibrant look ---
st.markdown(
    '''
    <style>
    /* Page background gradient */
    .block-container {
        background: linear-gradient(135deg, #eef3f8 0%, #cfdcec 100%);
    }
    /* Sidebar styling */
    [data-testid="stSidebar"] {
        background-color: rgba(255,255,255,0.85);
        border-right: 4px solid #e05a47;
    }
    /* Sidebar header */
    .css-1avcm0n h2 {
        font-size: 24px;
        font-weight: 800;
        color: #e05a47;
        text-shadow: 1px 1px 2px #000;
    }
    /* Radio buttons */
    .stRadio > label {
        font-size: 18px;
    }
    .stRadio > label > div[data-baseweb="radio"]:has(input:checked) {
        background-color: #e05a47;
        color: white;
        border-radius: 8px;
    }
    /* Headers */
    h1, h2, h3 {
        color: #e05a47 !important;
        text-shadow: 2px 2px 4px rgba(0,0,0,0.3);
    }
    /* Buttons */
    button {
        background-color: #e05a47 !important;
        border-radius: 12px !important;
        color: white !important;
        font-weight: 600 !important;
    }
    /* Styled table */
    .styled-table {
        width: 100%;
        border-collapse: collapse;
        margin: 25px 0;
        font-size: 1.1em;
        font-family: sans-serif;
        box-shadow: 0 0 10px rgba(0,0,0,0.15);
    }
    .styled-table thead tr {
        background-color: #4e79a7;
        color: #ffffff;
        text-align: left;
    }
    .styled-table th, .styled-table td {
        padding: 12px 15px;
    }
    .styled-table tbody tr {
        border-bottom: 1px solid #dddddd;
    }
    .styled-table tbody tr:nth-of-type(even) {
        background-color: #f3f3f3;
    }
    .styled-table tbody tr:last-of-type {
        border-bottom: 2px solid #4e79a7;
    }
    </style>
    ''',
    unsafe_allow_html=True,
)

# Load CSV files (placeholders, replace with actual file paths when available)
@st.cache_data
def load_data(file_path):
    return pd.read_csv(file_path)

# Assuming files will be in the data directory
market_basket_file = "rules_jj_with_cat.csv"
item_item_file = "item_item_final.csv"
user_item_file = "final_user_item.csv"

# Try to load data, handle missing files gracefully
try:
    market_data = load_data(market_basket_file)
    item_item_data = load_data(item_item_file)
    user_item_data = load_data(user_item_file)
except FileNotFoundError:
    st.warning("CSV files not found. Please ensure data files are in the project directory.")
    market_data, item_item_data, user_item_data = pd.DataFrame(), pd.DataFrame(), pd.DataFrame()

# Sidebar navigation
st.sidebar.title("Navigation")
st.sidebar.markdown("<h2 style='color:#4e79a7;'>🔖 Navigation</h2>", unsafe_allow_html=True)
pages = ["Home", "Market Basket Recommender", "Item-Item Recommender", "User-Item Recommender"]
selection = st.sidebar.radio("Go to", pages)

def display_local_image(file_name, width=True):
    """
    Shows an image stored in the local 'images' directory.
    Ensure you have an 'images' folder at project root with the file.
    """
    base_dir = os.path.dirname(__file__)
    image_path = os.path.join(base_dir, "images", file_name)
    if os.path.exists(image_path):
        st.image(image_path, use_column_width=width)
    else:
        st.error(f"🔍 Image not found: {image_path}")

# Home Page
if selection == "Home":
    st.image(
        "https://images.unsplash.com/photo-1523381294911-8d3cead13475?auto=format&fit=crop&w=1350&q=80",
        use_column_width=True,
    )
    st.markdown(
        "<h1 style='text-align:center; color:#4e79a7;'>🛒 E-commerce Recommender System</h1>",
        unsafe_allow_html=True,
    )
    st.write("Explore three recommendation strategies below, and click the sidebar to navigate!")
    col1, col2, col3 = st.columns(3, gap="large")
    with col1:
        st.image("https://img.icons8.com/ios-filled/100/4e79a7/shopping-basket.png")
        st.subheader("Market Basket")
        st.write("If you buy X, you might buy Y — view transactional rules.")
    with col2:
        st.image("https://img.icons8.com/ios-filled/100/4e79a7/link.png")
        st.subheader("Item-Item")
        st.write("For new users: find your top 10 similar products.")
    with col3:
        st.image("https://img.icons8.com/ios-filled/100/4e79a7/user.png")
        st.subheader("User-Item")
        st.write("Personalized picks from your journey.")

    st.title("Recommender System for E-commerce")
    st.write("""
    Welcome to the E-commerce Recommender System! This application provides personalized recommendations based on different approaches:
    
    - **Market Basket Recommender**: Suggests items based on transactional rules (e.g., if you buy X, you might buy Y). Select a product to see consequent items with lift values.
    - **Item-Item Recommender**: Recommends top 10 items for new users based on a given product ID.
    - **User-Item Recommender**: Suggests top 10 items for users based on their journey (previous purchases).
    """)

# --- Market Basket Recommender Page ---
elif selection == "Market Basket Recommender":
    display_local_image("3.gif")
    st.markdown("## 🔗 <span style='color:#4e79a7;'>Market Basket Recommender</span>", unsafe_allow_html=True)
    st.write("**If you buy X, see what Y buys next!**")
    if market_data.empty:
        st.error("No rules CSV loaded.")
    else:
        ant = st.selectbox("Antecedent", sorted(market_data["antecedents"].unique()))
        df = market_data[market_data["antecedents"] == ant]
        st.markdown(f"#### Consequents for {ant}")
        table_html = '''
        <table class="styled-table">
            <thead><tr><th>Consequent</th><th>Lift</th></tr></thead>
            <tbody>'''
        for _, row in df.iterrows():
            table_html += f"<tr><td>{row['consequents']}</td><td>{row['lift']:.2f}</td></tr>"
        table_html += "</tbody></table>"
        st.markdown(table_html, unsafe_allow_html=True)

# Item-Item Recommender Page
elif selection == "Item-Item Recommender":
    st.markdown(
        "<div style='background-color:rgba(224,90,71,0.2); padding:15px; border-radius:10px;'>"
        "<h2>🤝 Item-Item Recommender</h2>"
        "<p><strong>Find products similar to your chosen item.</strong></p>"
        "</div>",
        unsafe_allow_html=True,
    )
    if item_item_data.empty:
        st.error("No item-item CSV loaded.")
    else:
        pid = st.selectbox("Select Product ID", sorted(item_item_data["product_id"].unique()))
        row = item_item_data[item_item_data["product_id"] == pid].iloc[0]
        product_price = row["price"]
        st.markdown(
            f"### Selected: <span style='color:#e05a47;'>{row['product_name']}</span> (ID: {pid})\n"
            f"**Original Price:** ${product_price:,.2f}",
            unsafe_allow_html=True,
        )
        topk = st.slider("Number of recommendations", 1, 10, 10)
        recs = item_item_data[item_item_data["product_id"] == pid].head(topk)
        # Build HTML table
        table_html = '<table class="styled-table"><thead><tr>'
        for col in ["recommended_product_name", "recommended_category", "recommended_price"]:
            table_html += f"<th>{col.replace('_',' ').title()}</th>"
        table_html += "</tr></thead><tbody>"
        for _, r in recs.iterrows():
            table_html += (
                "<tr>"
                f"<td>{r['recommended_product_name']}</td>"
                f"<td>{r['recommended_category']}</td>"
                f"<td>${r['recommended_price']:.2f}</td>"
                "</tr>"
            )
        table_html += "</tbody></table>"
        st.markdown(table_html, unsafe_allow_html=True)

# User-Item Recommender Page
elif selection == "User-Item Recommender":
    st.header("User-Item Recommender")
    st.write("Select a user from the list below to get personalized recommendations:")
    if user_item_data.empty:
        st.error("No user data available. Place 'final_user_item.csv' in project root.")
    else:
        user_ids = sorted(user_item_data["profile_id"].unique())
        user_id = st.selectbox("User ID", user_ids, index=0)

        # Display previous purchases
        try:
            prev_df = pd.read_csv("cleaned_data.csv")
            prev = prev_df[prev_df["profile_id"] == user_id]
            if not prev.empty:
                st.subheader("Previous Purchases")
                st.table(prev[[
                    "purchased_product_ids",
                    "purchased_product_catgeories",
                    "purchased_product_title",
                ]])
        except FileNotFoundError:
            st.info("'cleaned_data.csv' not found; skipping previous purchases view.")

        # Display recommendations
        recs = user_item_data[user_item_data["profile_id"] == user_id]
        if not recs.empty:
            st.subheader("Top Recommendations")
            st.table(recs.drop(columns=["profile_id"]))
        else:
            st.info("No recommendations found for this user ID.")

# Footer with last-updated timestamp
if __name__ == "__main__":
    st.sidebar.write(f"Updated: {datetime.now().strftime('%b %d, %Y %H:%M')}")
    st.markdown("---")
