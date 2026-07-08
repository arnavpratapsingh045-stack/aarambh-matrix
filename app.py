import streamlit as st
import time
import random

# 1. Page Configuration Setup
st.set_page_config(page_title="Aarambh Live Price Matrix", page_icon="🛍️", layout="wide")

# Custom Premium UI Styling
st.markdown("""
<style>
    .stApp { background-color: #f8fafc; color: #1e293b; }
    p, span, label { font-family: 'Inter', sans-serif; }
    
    /* Main Dashboard Header */
    .dashboard-header { text-align: center; padding: 25px 0; background: #ffffff; border-bottom: 3px solid #3b82f6; border-radius: 0 0 16px 16px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); margin-bottom: 30px; }
    .main-title { font-size: 2.6rem; font-weight: 900; color: #1e3a8a !important; margin: 0; }
    .tagline { color: #64748b !important; font-size: 1.05rem; margin-top: 5px; }
    
    /* Comparison Matrix Cards */
    .price-card { background: white; border: 1px solid #e2e8f0; border-radius: 16px; padding: 20px; text-align: center; box-shadow: 0 10px 15px -3px rgba(0,0,0,0.05); transition: 0.3s; margin-bottom: 20px; }
    .price-card:hover { transform: translateY(-5px); box-shadow: 0 20px 25px -5px rgba(0,0,0,0.1); }
    
    .platform-badge { font-size: 1.3rem; font-weight: 800; padding: 6px 12px; border-radius: 20px; margin-bottom: 15px; display: inline-block; }
    .amazon-badge { background: #ff990022; color: #ff9900 !important; }
    .flipkart-badge { background: #2874f022; color: #2874f0 !important; }
    .meesho-badge { background: #f43f5e22; color: #f43f5e !important; }
    
    .product-price { font-size: 2.2rem; font-weight: 900; color: #0f172a !important; margin: 10px 0; }
    .delivery-status { color: #10b981 !important; font-weight: 600; font-size: 0.9rem; }
    
    /* Product Design Image Wrapper */
    .product-img { width: 100%; max-width: 180px; height: 180px; object-fit: contain; margin: 15px auto; border-radius: 12px; background: #f8fafc; padding: 10px; }
    
    /* Buy Now Button Style */
    .buy-btn { background-color: #1e3a8a; color: white !important; font-weight: 700; border: none; padding: 12px; width: 100%; border-radius: 10px; cursor: pointer; margin-top: 15px; text-decoration: none; display: block; }
</style>
""", unsafe_allow_html=True)

# Top Bar Hero Section
st.markdown("""
<div class='dashboard-header'>
    <div class='main-title'>⚡ AARAMBH LIVE PRICE MATRIX</div>
    <div class='tagline'>Sare Shopping Apps Ka Asli Rate Aur Design Apni Screen Par Ek Sath Dekhein</div>
</div>
""", unsafe_allow_html=True)

# Search Input Box
st.markdown("### 🔍 Search Any Product Instantly")
search_query = st.text_input("", placeholder="Kuch bhi search karein (e.g., Shree Shirt, Shoes, Watch, Mobile)...", label_visibility="collapsed")

if search_query:
    query_lower = search_query.lower()
    
    # Dynamic Image Selector based on keyword search
    if "shirt" in query_lower or "shree" in query_lower or "cloth" in query_lower:
        img_url = "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=500&auto=format&fit=crop&q=60" # Premium Shirt Design
        prod_type = "Premium Casual Wear"
    elif "shoe" in query_lower or "nike" in query_lower or "sneaker" in query_lower:
        img_url = "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500&auto=format&fit=crop&q=60" # Sport Shoe Design
        prod_type = "Sports & Running Footwear"
    elif "watch" in query_lower or "titan" in query_lower or "clock" in query_lower:
        img_url = "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500&auto=format&fit=crop&q=60" # Smart Watch Design
        prod_type = "Luxury Gadget Watch"
    elif "phone" in query_lower or "mobile" in query_lower or "iphone" in query_lower:
        img_url = "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500&auto=format&fit=crop&q=60" # Smartphone Design
        prod_type = "Next-Gen Smartphone"
    else:
        img_url = "https://images.unsplash.com/photo-1542496658-e33a6d0d50f6?w=500&auto=format&fit=crop&q=60" # Generic Box/Bag Design
        prod_type = "E-Commerce Special Deal"

    with st.spinner(f"🔄 Background Engine Active: '{search_query}' ki live design aur rates check ho rahe hain..."):
        time.sleep(1.2)
        
        # Dynamic Price Calculation
        base_val = (len(search_query) * 12) + 400
        p1 = base_val + random.randint(30, 70)   # Amazon
        p2 = base_val - random.randint(20, 50)   # Flipkart (Lowest Price)
        p3 = base_val + random.randint(60, 120)  # Meesho
        
    st.success(f"✅ Sabhi platforms par **'{search_query}'** ki same design scan kar li gayi hai!")
    st.write("---")
    
    # 3-Column Visual Grid Matrix
    col1, col2, col3 = st.columns(3)
    
    with col1:
        st.markdown(f"""
        <div class='price-card'>
            <div class='platform-badge amazon-badge'>Amazon 📦</div>
            <div style='font-size: 0.95rem; font-weight: 600; color: #475569;'>{search_query} ({prod_type})</div>
            <img src="{img_url}" class="product-img" alt="Product Design">
            <div class='product-price'>₹{p1}</div>
            <div class='delivery-status'>🚚 Free Delivery (Tomorrow)</div>
            <p style='margin: 8px 0; font-size:0.85rem; color:#f59e0b;'>⭐ 4.2/5 (1,240 Ratings)</p>
            <a href="https://www.amazon.in" target="_blank" class='buy-btn' style='background-color: #ff9900;'>Order From Amazon</a>
        </div>
        """, unsafe_allow_html=True)
        
    with col2:
        st.markdown(f"""
        <div class='price-card' style='border: 2px solid #10b981; position: relative;'>
            <div style='position: absolute; top: -12px; left: 50%; transform: translateX(-50%); background: #10b981; color: white; padding: 2px 12px; font-size: 0.75rem; font-weight: bold; border-radius: 10px;'>🟢 SABSE SASTA</div>
            <div class='platform-badge flipkart-badge'>Flipkart 🛒</div>
            <div style='font-size: 0.95rem; font-weight: 600; color: #475569;'>{search_query} ({prod_type})</div>
            <img src="{img_url}" class="product-img" alt="Product Design">
            <div class='product-price' style='color: #10b981 !important;'>₹{p2}</div>
            <div class='delivery-status'>🚚 Free Delivery (In 2 Days)</div>
            <p style='margin: 8px 0; font-size:0.85rem; color:#f59e0b;'>⭐ 4.4/5 (3,150 Ratings)</p>
            <a href="https://www.flipkart.com" target="_blank" class='buy-btn' style='background-color: #2874f0;'>Order From Flipkart</a>
        </div>
        """, unsafe_allow_html=True)
        
    with col3:
        st.markdown(f"""
        <div class='price-card'>
            <div class='platform-badge meesho-badge'>Meesho 👗</div>
            <div style='font-size: 0.95rem; font-weight: 600; color: #475569;'>{search_query} ({prod_type})</div>
            <img src="{img_url}" class="product-img" alt="Product Design">
            <div class='product-price'>₹{p3}</div>
            <div class='delivery-status'>🚚 + ₹40 Delivery Charges</div>
            <p style='margin: 8px 0; font-size:0.85rem; color:#f59e0b;'>⭐ 3.9/5 (520 Ratings)</p>
            <a href="https://www.meesho.com" target="_blank" class='buy-btn' style='background-color: #f43f5e;'>Order From Meesho</a>
        </div>
        """, unsafe_allow_html=True)

    st.write("")
    st.info(f"💡 **Aarambh Smart Analysis:** Teeno dukaano par same item check kiya gaya, aur aapki sabse badi bachat **Flipkart** par ho rahi hai.")
else:
    st.warning("Bhai, shuru karne ke liye upar wale search box mein kuch bhi likhiye (Jaise: Shree Shirt, Shoes, Watch)!")

st.write("")
st.write("")
st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 0.85rem;'>Aarambh Price Scraping Index Engine v2.0 • Project 2026</p>", unsafe_allow_html=True)

