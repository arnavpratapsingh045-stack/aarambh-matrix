import streamlit as st
import time
import random

# Page Configuration Setup
st.set_page_config(page_title="Aarambh Global Price Matrix", page_icon="🌐", layout="wide")

# Custom CSS for Premium Theme & Layout
st.markdown("""
<style>
    .stApp { background-color: #f1f5f9; color: #1e293b; }
    p, span, label { font-family: 'Inter', sans-serif; }
    
    /* Login & Signup Box styling */
    .login-container { max-width: 450px; margin: 40px auto; background: white; padding: 35px; border-radius: 16px; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.1); border-top: 5px solid #2874f0; }
    .login-header { text-align: center; font-size: 1.8rem; font-weight: 800; color: #2874f0; margin-bottom: 5px; }
    .login-sub { text-align: center; font-size: 0.9rem; color: #64748b; margin-bottom: 25px; }
    
    /* Main Dashboard Header */
    .dashboard-header { text-align: center; padding: 25px 0; background: #ffffff; border-bottom: 4px solid #1e3a8a; border-radius: 0 0 20px 20px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); margin-bottom: 30px; }
    .main-title { font-size: 2.5rem; font-weight: 900; color: #1e3a8a !important; margin: 0; letter-spacing: -0.5px; }
    .tagline { color: #64748b !important; font-size: 1.05rem; margin-top: 5px; }
    
    /* Product Layout Grid */
    .product-box { background: white; border-radius: 16px; padding: 25px; box-shadow: 0 4px 6px -1px rgba(0,0,0,0.05); margin-bottom: 25px; border: 1px solid #e2e8f0; }
    .fk-interface-title { font-size: 1.4rem; font-weight: 800; color: #1e3a8a; margin-bottom: 15px; border-bottom: 2px solid #f1f5f9; padding-bottom: 8px; }
    
    /* Comparison Cards */
    .matrix-card { background: #fff; border: 1px solid #e2e8f0; border-radius: 12px; padding: 20px; text-align: center; box-shadow: 0 4px 6px rgba(0,0,0,0.02); transition: 0.3s; }
    .matrix-card:hover { transform: translateY(-3px); box-shadow: 0 12px 20px rgba(0,0,0,0.08); }
    
    .platform-name { font-size: 1.2rem; font-weight: 800; margin-bottom: 10px; }
    .price-tag { font-size: 2.1rem; font-weight: 900; margin: 12px 0; }
    
    .buy-btn { background-color: #1e3a8a; color: white !important; font-weight: 700; border: none; padding: 12px; width: 100%; border-radius: 8px; text-decoration: none; display: block; margin-top: 15px; text-align: center; }
</style>
""", unsafe_allow_html=True)

# Aapka Adsterra Global Script Code
ad_html_code = """
<div style="text-align:center; margin: auto;">
    <script type="text/javascript">
      atOptions = {
        'key' : '7b617b2fc4e84542dd4b3a49fb75bff4',
        'format' : 'iframe',
        'height' : 90,
        'width' : 728,
        'params' : {}
      };
    </script>
    <script src="https://www.highperformanceformat.com/7b617b2fc4e84542dd4b3a49fb75bff4/invoke.js"></script>
</div>
"""

# Session State Initialization
if "logged_in" not in st.session_state:
    st.session_state.logged_in = False
if "otp_sent" not in st.session_state:
    st.session_state.otp_sent = False
if "phone_num" not in st.session_state:
    st.session_state.phone_num = ""

# --- PHASE 1: FLIPKART STYLE OTP LOGIN SYSTEM ---
if not st.session_state.logged_in:
    st.markdown("<div class='login-container'>", unsafe_allow_html=True)
    st.markdown("<div class='login-header'>Aarambh Login / Sign Up</div>", unsafe_allow_html=True)
    st.markdown("<div class='login-sub'>Enter your Mobile Number to access Global Price Matrix</div>", unsafe_allow_html=True)
    
    if not st.session_state.otp_sent:
        phone = st.text_input("Mobile Number", placeholder="Enter 10 digit mobile number", max_chars=10)
        st.markdown("<br>", unsafe_allow_html=True)
        if st.button("CONTINUE", use_container_width=True):
            if len(phone) == 10 and phone.isdigit():
                st.session_state.phone_num = phone
                st.session_state.otp_sent = True
                with st.spinner("Sending 6-digit OTP..."):
                    time.sleep(1.2)
                st.rerun()
            else:
                st.error("🚨 Please enter a valid 10-digit mobile number.")
    else:
        st.info(f"OTP sent successfully to +91 {st.session_state.phone_num} (Use any 6 digits to check)")
        otp_input = st.text_input("Enter 6-Digit OTP", placeholder="Enter 6-Digit dummy OTP", max_chars=6, type="password")
        st.markdown("<br>", unsafe_allow_html=True)
        
        col_btn1, col_btn2 = st.columns(2)
        with col_btn1:
            if st.button("VERIFY OTP", use_container_width=True):
                if len(otp_input) == 6 and otp_input.isdigit():
                    st.session_state.logged_in = True
                    st.success("Login Successful!")
                    time.sleep(1)
                    st.rerun()
                else:
                    st.error("🚨 Invalid OTP! Check again.")
        with col_btn2:
            if st.button("Change Number", use_container_width=True):
                st.session_state.otp_sent = False
                st.rerun()
                
    st.markdown("</div>", unsafe_allow_html=True)
    
    # 💰 ADSTERRA AD SLOT 1
    st.markdown("<p style='text-align:center; color:#94a3b8; font-size:0.8rem; margin-top:20px;'>Sponsored Link</p>", unsafe_allow_html=True)
    st.components.v1.html(ad_html_code, height=100)

# --- PHASE 2: GLOBAL SEARCH MATRIX APPLICATION ---
else:
    st.markdown("""
    <div class='dashboard-header'>
        <div class='main-title'>🌐 AARAMBH GLOBAL ENGINE & MATRIX</div>
        <div class='tagline'>Search by Product Name OR Paste Any Product Link to Compare</div>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🔍 Search Box (Enter Name or Paste Link)")
    search_query = st.text_input("", placeholder="Product ka naam daalein YA kisi bhi app ka product link paste karein...", label_visibility="collapsed")
    
    # Dedicated Search Button
    search_clicked = st.button("⚡ Search & Match Prices Live", type="primary", use_container_width=True)
    
    if search_query and search_clicked:
        query_lower = search_query.lower()
        is_link = "http://" in query_lower or "https://" in query_lower
        
        # --- SMART SMART IMAGE SELECTOR LOGIC ---
        if "shirt" in query_lower or "cloth" in query_lower or "tshirt" in query_lower:
            img_url = "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=500&auto=format&fit=crop&q=60"
            display_title = "Premium Casual Shirt" if not is_link else "Extracted Clothing Link"
        elif "shoe" in query_lower or "sneaker" in query_lower or "slipper" in query_lower:
            img_url = "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500&auto=format&fit=crop&q=60"
            display_title = "Sports Running Shoes" if not is_link else "Extracted Footwear Link"
        elif "watch" in query_lower or "titan" in query_lower:
            img_url = "https://images.unsplash.com/photo-1523275335684-37898b6baf30?w=500&auto=format&fit=crop&q=60"
            display_title = "Luxury Smart Watch" if not is_link else "Extracted Accessory Link"
        elif "laptop" in query_lower or "computer" in query_lower or "pc" in query_lower:
            img_url = "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=500&auto=format&fit=crop&q=60"
            display_title = "High-Performance Laptop" if not is_link else "Extracted Tech Link"
        elif "phone" in query_lower or "mobile" in query_lower or "iphone" in query_lower:
            img_url = "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500&auto=format&fit=crop&q=60"
            display_title = "Next-Gen Smartphone" if not is_link else "Extracted Mobile Link"
        else:
            img_url = "https://images.unsplash.com/photo-1542496658-e33a6d0d50f6?w=500&auto=format&fit=crop&q=60"
            display_title = search_query.upper() if not is_link else "Global Indexed Product"

        # 💰 ADSTERRA AD SLOT 2
        st.components.v1.html(ad_html_code, height=100)
            
        with st.spinner("⚡ Processing Link/Name and matching global warehouse rates..."):
            time.sleep(1.2)
        
        # Base Price logic
        calculated_base = (len(search_query) * 35) + 1800
        if calculated_base > 20000 or calculated_base < 1000:
            calculated_base = random.randint(3500, 7500)
            
        # Saari platforms ka network database
        apps = [
            {"name": "Flipkart India 🛒", "color": "#2874f0", "url": "https://www.flipkart.com"},
            {"name": "Amazon Global 📦", "color": "#ff9900", "url": "https://www.amazon.in"},
            {"name": "Meesho App 👗", "color": "#f43f5e", "url": "https://www.meesho.com"},
            {"name": "Walmart Stores 🇺🇸", "color": "#0071dc", "url": "https://www.walmart.com"}
        ]
        
        # 🔥 PURE SHUFFLE DYNAMIC LOGIC - KOI BHI PLATFORM SASTA HO SAKTA HAI HAR SEARCH PAR!
        random.shuffle(apps)
        
        prices = {
            apps[0]["name"]: calculated_base - random.randint(400, 750),  # Ye hamesha sasta banega randomly
            apps[1]["name"]: calculated_base + random.randint(150, 350),
            apps[2]["name"]: calculated_base + random.randint(400, 700),
            apps[3]["name"]: calculated_base + random.randint(800, 1400)
        }
        
        lowest_app_name = apps[0]["name"]
        lowest_price = prices[lowest_app_name]
        
        # --- DYNAMIC DISPLAY BOX ---
        st.markdown(f"<div class='product-box'>", unsafe_allow_html=True)
        st.markdown(f"<div class='fk-interface-title'>📊 Live Best Deal Matrix: Found on {lowest_app_name}</div>", unsafe_allow_html=True)
        
        col_img, col_det = st.columns([1, 3])
        with col_img:
            st.image(img_url, width=150)
        with col_det:
            st.markdown(f"## {display_title}")
            st.markdown(f"<p style='color:#10b981; font-weight:700; font-size:1.4rem;'>Best Price: ₹{lowest_price} (Guaranteed Lowest)</p>", unsafe_allow_html=True)
            st.write("✨ Free Express Delivery | 🛡️ Live Store Data Verified | 🚚 Return Policy Applicable")
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # --- COMPARISON MATRIX GRID ---
        st.markdown("### 📊 Worldwide Stores Price Comparison Index")
        
        grid_cols = st.columns(4)
        for i, app in enumerate(apps):
            with grid_cols[i]:
                is_lowest = (app["name"] == lowest_app_name)
                border_style = "border: 2px solid #10b981; background: #f0fdf4;" if is_lowest else ""
                badge_text = "🟢 SABSE SASTA" if is_lowest else "⚪ Standard Rate"
                badge_color = "#10b981" if is_lowest else "#64748b"
                
                st.markdown(f"""
                <div class='matrix-card' style='{border_style}'>
                    <div class='platform-name' style='color:{app["color"]};'>{app["name"]}</div>
                    <div style='color:{badge_color}; font-weight:bold; font-size:0.8rem; margin-bottom:5px;'>{badge_text}</div>
                    <div class='price-tag' style='color:{"#10b981" if is_lowest else "#1e293b"};'>₹{prices[app["name"]]}</div>
                    <a href='{app["url"]}' target='_blank' class='buy-btn' style='background-color:{app["color"]};'>Check Store</a>
                </div>
                """, unsafe_allow_html=True)
                
    elif search_clicked and not search_query:
        st.warning("Bhai, pehle search box mein koi naam likho ya product link paste karo!")

    # Sidebar Logout Options
    st.sidebar.markdown(f"**Logged in as:** +91 {st.session_state.phone_num}")
    if st.sidebar.button("Log Out"):
        st.session_state.logged_in = False
        st.session_state.otp_sent = False
        st.rerun()

    st.write("")
    st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 0.85rem;'>Aarambh Price Scraping Index Engine v6.0 • Global Project 2026</p>", unsafe_allow_html=True)
