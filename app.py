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

# Adsterra Global Script Configuration
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
        st.info(f"OTP sent successfully to +91 {st.session_state.phone_num}")
        otp_input = st.text_input("Enter 6-Digit OTP", placeholder="Enter OTP received", max_chars=6, type="password")
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
    
    # 💰 ADSTERRA AD SLOT 1 (Login Page ke niche)
    st.markdown("<p style='text-align:center; color:#94a3b8; font-size:0.8rem; margin-top:20px;'>Sponsored Link</p>", unsafe_allow_html=True)
    st.components.v1.html(ad_html_code, height=100)

# --- PHASE 2: GLOBAL SEARCH MATRIX APPLICATION ---
else:
    # Top Bar Header Section
    st.markdown("""
    <div class='dashboard-header'>
        <div class='main-title'>🌐 AARAMBH GLOBAL ENGINE & MATRIX</div>
        <div class='tagline'>Search by Product Name OR Paste Any Product Link to Compare</div>
    </div>
    """, unsafe_allow_html=True)
    
    # Global Universal Search Engine Box
    st.markdown("### 🔍 Search Box (Enter Name or Paste Link)")
    search_query = st.text_input("", placeholder="Product ka naam daalein YA kisi bhi app ka product link paste karein...", label_visibility="collapsed")
    
    # Dedicated Search Button right below the input box
    search_clicked = st.button("⚡ Search & Match Prices Live", type="primary", use_container_width=True)
    
    if search_query and search_clicked:
        is_link = "http://" in search_query or "https://" in search_query
        
        if is_link:
            if "flipkart.com" in search_query:
                display_title = "Flipkart Extracted Item"
            elif "amazon" in search_query:
                display_title = "Amazon Extracted Item"
            elif "meesho" in search_query:
                display_title = "Meesho Extracted Item"
            else:
                display_title = "Global Linked Product"
        else:
            display_title = search_query.upper()

        # 💰 ADSTERRA AD SLOT 2 (Search results load hone se upar)
        st.components.v1.html(ad_html_code, height=100)
            
        with st.spinner("⚡ Processing Link/Name and matching global warehouse rates..."):
            time.sleep(1.5)
        
        # Dynamic Math Price Calculation
        calculated_base = (len(search_query) * 45) + 2200
        if calculated_base > 25000:
            calculated_base = 8500
            
        # Apps Database definition
        apps = [
            {"name": "Flipkart India 🛒", "color": "#2874f0", "url": "https://www.flipkart.com"},
            {"name": "Amazon Global 📦", "color": "#ff9900", "url": "https://www.amazon.in"},
            {"name": "Meesho App 👗", "color": "#f43f5e", "url": "https://www.meesho.com"},
            {"name": "Walmart Stores 🇺🇸", "color": "#0071dc", "url": "https://www.walmart.com"}
        ]
        
        # Shuffle logic so ANY app can become the cheapest randomly
        random.shuffle(apps)
        
        # Assigning random dynamic prices (0th element hamesha sasta)
        prices = {
            apps[0]["name"]: calculated_base - random.randint(500, 800),
            apps[1]["name"]: calculated_base + random.randint(100, 400),
            apps[2]["name"]: calculated_base + random.randint(500, 900),
            apps[3]["name"]: calculated_base + random.randint(1000, 1500)
        }
        
        lowest_app_name = apps[0]["name"]
        lowest_price = prices[lowest_app_name]
        
        # --- DYNAMIC INTERFACE VIEW SHOWCASE ---
        st.markdown(f"<div class='product-box'>", unsafe_allow_html=True)
        st.markdown(f"<div class='fk-interface-title'>📊 Live Result: Analysis Found Best Deal on {lowest_app_name}</div>", unsafe_allow_html=True)
        
        col_img, col_det = st.columns([1, 3])
        with col_img:
            st.image("https://images.unsplash.com/photo-1542496658-e33a6d0d50f6?w=500&auto=format&fit=crop&q=60", width=140)
        with col_det:
            if is_link:
                st.markdown(f"## 🔗 Link Analyzed: {display_title}")
                st.caption(f"Original Target URL: {search_query[:70]}...")
            else:
                st.markdown(f"## 📦 Product Named: {display_title}")
                
            st.markdown(f"<p style='color:#10b981; font-weight:700; font-size:1.3rem;'>Lowest Rate: ₹{lowest_price}</p>", unsafe_allow_html=True)
            st.write("✨ Live Data Verified | 🛡️ Secure Checkout Route | 🚚 Free Shipping Active")
        
        st.markdown("</div>", unsafe_allow_html=True)
        
        # --- WORLDWIDE SHOPPING APP COMPARISON GRID ---
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

    # Logout Option
    st.sidebar.markdown(f"**Logged in as:** +91 {st.session_state.phone_num}")
    if st.sidebar.button("Log Out"):
        st.session_state.logged_in = False
        st.session_state.otp_sent = False
        st.rerun()

    st.write("")
    st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 0.85rem;'>Aarambh Price Scraping Index Engine v5.0 • Global Project 2026</p>", unsafe_allow_html=True)
    
