

import streamlit as st
import random

# Sample product data (you can replace this with a real API or database)
products_db = {
    "Electronics": [
        {"name": "Wireless Earbuds", "price": 50, "affiliate_link": "https://example.com/earbuds"},
        {"name": "Smartphone", "price": 500, "affiliate_link": "https://example.com/smartphone"},
        {"name": "Smart Watch", "price": 150, "affiliate_link": "https://example.com/smartwatch"}
    ],
    "Clothing": [
        {"name": "T-shirt", "price": 20, "affiliate_link": "https://example.com/tshirt"},
        {"name": "Jeans", "price": 40, "affiliate_link": "https://example.com/jeans"},
        {"name": "Jacket", "price": 70, "affiliate_link": "https://example.com/jacket"}
    ],
    "Home & Kitchen": [
        {"name": "Coffee Maker", "price": 30, "affiliate_link": "https://example.com/coffeemaker"},
        {"name": "Blender", "price": 50, "affiliate_link": "https://example.com/blender"},
        {"name": "Air Fryer", "price": 90, "affiliate_link": "https://example.com/airfryer"}
    ]
}

# Function to recommend products based on user input
def recommend_products(budget, category):
    products = products_db.get(category, [])
    affordable_products = [p for p in products if p['price'] <= budget]
    
    if affordable_products:
        return random.sample(affordable_products, 3)  # Return 3 random products
    else:
        return []

# Streamlit UI
st.title("Personal Shopping Assistant")
st.write("Find the best products within your budget!")

# User inputs
budget = st.number_input("Enter your budget ($)", min_value=10, max_value=5000, value=100)
category = st.selectbox("Select product category", ["Electronics", "Clothing", "Home & Kitchen"])

# Get product recommendations
if st.button("Get Product Recommendations"):
    recommendations = recommend_products(budget, category)
    
    if recommendations:
        st.write(f"Here are some products within your budget of ${budget} in the {category} category:")
        for product in recommendations:
            st.write(f"**{product['name']}** - ${product['price']}")
            st.markdown(f"[Buy now]({product['affiliate_link']})")
    else:
        st.warning(f"Sorry, no products found within your budget in the {category} category.")

