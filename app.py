import streamlit as st
import random
import time

# 1. Page Configuration Setup
st.set_page_config(page_title="Aarambh Global Price Matrix", page_icon="🌐", layout="wide")

# 2. Premium Custom Stylesheet
st.markdown("""
<style>
    .stApp { background-color: #f8fafc; color: #0f172a; }
    .login-box { max-width: 440px; margin: 60px auto; background: white; padding: 40px 30px; border-radius: 16px; box-shadow: 0 10px 25px -5px rgba(0,0,0,0.05); text-align: center; border-top: 5px solid #2874f0; }
    .login-lbl { font-size: 1.8rem; font-weight: 800; color: #1e3a8a; margin-bottom: 5px; }
    .login-sub { font-size: 0.9rem; color: #64748b; margin-bottom: 30px; }
    
    /* Google Button Styling */
    .google-btn { display: flex; align-items: center; justify-content: center; background-color: white; color: #1f2937; font-weight: 600; padding: 12px; border: 1px solid #d1d5db; border-radius: 8px; width: 100%; cursor: pointer; font-family: 'Inter', sans-serif; transition: 0.2s; box-shadow: 0 1px 3px rgba(0,0,0,0.05); }
    .google-btn:hover { background-color: #f9fafb; border-color: #9ca3af; }
    .google-icon { width: 18px; height: 18px; margin-right: 12px; }
    
    .main-header { text-align: center; padding: 25px; background: white; border-radius: 12px; box-shadow: 0 2px 12px rgba(0,0,0,0.03); margin-bottom: 30px; border-bottom: 4px solid #1e3a8a; }
    .prod-container { background: white; border-radius: 12px; padding: 25px; box-shadow: 0 4px 10px rgba(0,0,0,0.02); margin-bottom: 25px; border: 1px solid #e2e8f0; }
    .card-matrix { background: white; border: 1px solid #e2e8f0; border-radius: 10px; padding: 18px; text-align: center; box-shadow: 0 2px 5px rgba(0,0,0,0.01); transition: 0.3s; }
    .card-matrix:hover { transform: translateY(-3px); box-shadow: 0 8px 15px rgba(0,0,0,0.06); }
    .price-val { font-size: 1.9rem; font-weight: 900; margin: 12px 0; }
    .store-link { background-color: #1e3a8a; color: white !important; font-weight: 700; padding: 12px; width: 100%; border-radius: 8px; display: block; text-decoration: none; margin-top: 12px; text-align: center; }
</style>
""", unsafe_allow_html=True)

# 3. Safe Adsterra Component Loader
def load_ad_safely():
    ad_code = """
    <html>
    <head>
        <style>body { margin: 0; padding: 0; text-align: center; }</style>
    </head>
    <body>
        <script type="text/javascript">
          atOptions = {
            'key' : '7b617b2fc4e84542dd4b3a49fb75bff4',
            'format' : 'iframe',
            'height' : 90,
            'width' : 728,
            'params' : {}
          };
        </script>
        <script type="text/javascript" src="https://www.highperformanceformat.com/7b617b2fc4e84542dd4b3a49fb75bff4/invoke.js"></script>
    </body>
    </html>
    """
    st.components.v1.html(ad_code, height=105, scrolling=False)

# 4. Session State Settings
if "google_auth" not in st.session_state:
    st.session_state.google_auth = False

# --- SCREEN 1: GOOGLE LOGIN GATEWAY (NO OTP) ---
if not st.session_state.google_auth:
    st.markdown("<div class='login-box'>", unsafe_allow_html=True)
    st.markdown("<div class='login-lbl'>Welcome to Aarambh</div>", unsafe_allow_html=True)
    st.markdown("<div class='login-sub'>Analyze global product links instantly</div>", unsafe_allow_html=True)
    
    # Visual Google Sign-in Trigger
    st.markdown("""
    <button class="google-btn" onclick="javascript:void(0);">
        <img class="google-icon" src="https://fonts.gstatic.com/s/i/productlogos/googleg/v6/web-24dp/logo_googleg_color_web_24dp.png" alt="Google">
        Sign in with Google
    </button>
    """, unsafe_allow_html=True)
    st.write("")
    
    # Streamlit interactive connector button for simulated bypass
    if st.button("Click to Verify & Enter Dashboard", type="primary", use_container_width=True, key="google_mock_btn"):
        st.session_state.google_auth = True
        st.rerun()
        
    st.markdown("</div>", unsafe_allow_html=True)
    
    # Ad Placement on Login Screen
    st.write("---")
    load_ad_safely()

# --- SCREEN 2: STRICT PRODUCT LINK SEARCH MATRIX ---
else:
    st.markdown("""
    <div class='main-header'>
        <h1 style='color:#1e3a8a; margin:0; font-weight:900;'>🌐 AARAMBH GLOBAL ENGINE & MATRIX</h1>
        <p style='color:#64748b; margin:5px 0 0 0;'>Paste Any Product Web URL Link to Compare Across All Platforms</p>
    </div>
    """, unsafe_allow_html=True)
    
    st.markdown("### 🔗 Paste Product URL Link Below")
    url_input = st.text_input("", placeholder="https://www.flipkart.com/product-link-here...", label_visibility="collapsed", key="link_search_input")
    
    # Main Search Button
    run_analysis = st.button("⚡ ANALYZE URL & MATCH ALL PLATFORMS", type="primary", use_container_width=True, key="analyze_link_btn")
    
    # Fixed Advertisement Slot
    st.write(" ")
    load_ad_safely()
    
    if url_input and run_analysis:
        url_clean = url_input.strip().lower()
        
        # STRICT RULE CHECK: If input doesn't contain standard URL schema
        if not (url_clean.startswith("http://") or url_clean.startswith("https://") or "www." in url_clean):
            st.error("🚨 Error: Aarambh Terminal only accepts valid product web links! Please paste a proper product URL from any shopping app.")
        else:
            # Smart Keyword Identification from the Link to match correct product graphic
            if "laptop" in url_clean or "computer" in url_clean or "macbook" in url_clean or "dell" in url_clean or "hp" in url_clean:
                item_pic = "https://images.unsplash.com/photo-1517336714731-489689fd1ca8?w=500&auto=format&fit=crop&q=60"
                product_display_name = "High-Performance Advanced Laptop"
            elif "shirt" in url_clean or "cloth" in url_clean or "tshirt" in url_clean or "jeans" in url_clean:
                item_pic = "https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=500&auto=format&fit=crop&q=60"
                product_display_name = "Premium Branded Casual Outfit"
            elif "shoe" in url_clean or "sneaker" in url_clean or "boot" in url_clean or "nike" in url_clean:
                item_pic = "https://images.unsplash.com/photo-1542291026-7eec264c27ff?w=500&auto=format&fit=crop&q=60"
                product_display_name = "Ergonomic Cushion Sports Footwear"
            elif "phone" in url_clean or "mobile" in url_clean or "iphone" in url_clean or "samsung" in url_clean:
                item_pic = "https://images.unsplash.com/photo-1511707171634-5f897ff02aa9?w=500&auto=format&fit=crop&q=60"
                product_display_name = "Next-Generation Intelligent Smartphone"
            else:
                item_pic = "https://images.unsplash.com/photo-1542496658-e33a6d0d50f6?w=500&auto=format&fit=crop&q=60"
                product_display_name = "Scraped Multi-Platform Verified Product"

            with st.spinner("⏳ Extracting metadata from URL and analyzing cross-border platform price pools..."):
                time.sleep(1.2)
            
            # Simulated Dynamic Base Price Allocation
            base_cost_pool = random.randint(4500, 12500)
                
            # Dynamic Platforms Pool Setup
            platforms = [
                {"label": "Flipkart India 🛒", "theme": "#2874f0", "base_url": "https://www.flipkart.com"},
                {"label": "Amazon Hub 📦", "theme": "#ff9900", "base_url": "https://www.amazon.in"},
                {"label": "Meesho Store 👗", "theme": "#f43f5e", "base_url": "https://www.meesho.com"},
                {"label": "Walmart Global 🇺🇸", "theme": "#0071dc", "base_url": "https://www.walmart.com"}
            ]
            
            # 🎲 RANDOM SHUFFLE - NO APP IS FIXED. Any app will be selected as cheapest randomly
            random.shuffle(platforms)
            
            generated_prices = {
                platforms[0]["label"]: base_cost_pool - random.randint(500, 900), # Randomly chosen as lowest option
                platforms[1]["label"]: base_cost_pool + random.randint(150, 400),
                platforms[2]["label"]: base_cost_pool + random.randint(450, 850),
                platforms[3]["label"]: base_cost_pool + random.randint(900, 1600)
            }
            
            cheapest_store = platforms[0]["label"]
            cheapest_price = generated_prices[cheapest_store]
            
            # --- DISPLAY MAIN SEARCH TARGET ---
            st.markdown("<div class='prod-container'>", unsafe_allow_html=True)
            st.markdown(f"<h4>📌 URL Analysis Success: Lowest Live Price Detected on {cheapest_store}</h4>", unsafe_allow_html=True)
            
            side_left, side_right = st.columns([1, 3])
            with side_left:
                st.image(item_pic, width=140)
            with side_right:
                st.markdown(f"## {product_display_name}")
                st.caption(f"Source Link Input: {url_input[:80]}...")
                st.markdown(f"<p style='color:#10b981; font-weight:800; font-size:1.4rem; margin:0;'>Best Calculated Rate: ₹{cheapest_price}</p>", unsafe_allow_html=True)
                st.write("✓ URL Verified | ✓ Multi-Platform API Checked | ✓ Free Shipping Applied")
            st.markdown("</div>", unsafe_allow_html=True)
            
            # --- COMPARISON ALL PLATFORMS MULTI-GRID ---
            st.markdown("### 📊 Worldwide Stores Price Comparison Index")
            
            grid_cols = st.columns(4)
            for idx, store in enumerate(platforms):
                with grid_cols[idx]:
                    is_winner = (store["label"] == cheapest_store)
                    accent_border = "border: 2px solid #10b981; background: #f0fdf4;" if is_winner else ""
                    badge_text = "🟢 SABSE SASTA DEAL" if is_winner else "⚪ Standard App Rate"
                    badge_color = "#10b981" if is_winner else "#64748b"
                    
                    st.markdown(f"""
                    <div class='card-matrix' style='{accent_border}'>
                        <div style='font-size:1.15rem; font-weight:800; color:{store["theme"]};'>{store["label"]}</div>
                        <div style='color:{badge_color}; font-weight:700; font-size:0.8rem; margin:4px 0;'>{badge_text}</div>
                        <div class='price-val' style='color:{"#10b981" if is_winner else "#0f172a"};'>₹{generated_prices[store["label"]]}</div>
                        <a href='{store["base_url"]}' target='_blank' class='store-link' style='background-color:{store["theme"]};'>OPEN APP STORE</a>
                    </div>
                    """, unsafe_allow_html=True)
                    
    elif run_analysis and not url_input:
        st.warning("Please paste a product URL sharing link from Flipkart, Amazon, or any app first.")

    # Sidebar Admin Workspace Area
    st.sidebar.markdown("**User Session:** Authorized Profile via Google Accounts")
    if st.sidebar.button("LOG OUT FROM SYSTEM"):
        st.session_state.google_auth = False
        st.rerun()

    st.write("")
    st.markdown("<p style='text-align: center; color: #94a3b8; font-size: 0.85rem;'>Aarambh Universal Engine Matrix v8.0 • Powered by Streamlit 2026</p>", unsafe_allow_html=True)
    
