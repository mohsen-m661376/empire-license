import streamlit as st
import random
import time

# --- ۱. سیستم لایسنس (مدیریت قفل) ---
class LicenseManager:
    def init(self):
        # این‌ها کدهای لایسنس معتبر هستند (برای تست)
        self.valid_licenses = ["EMPIRE-KING", "GOLD-777", "TEST-123"]

    def check_license(self, key):
        return key in self.valid_licenses

# --- ۲. موتور اصلی امپراتوری ---
class EmpireContentEngine:
    def init(self):
        self.genres = ['کمدی نیش‌دار', 'اجتماعی تاثیرگذار', 'اکشن-طنز', 'رازآلود']

    def trend_analyzer(self):
        """رصد ترندهای ۷۲ ساعت اخیر"""
        time.sleep(1.5) # شبیه‌سازی پردازش
        trends = ["چالش تغییر شغل", "گرانی قهوه", "هوش مصنوعی ترسناک", "زندگی لوکس فیک"]
        return random.choice(trends)

    def ai_character_generator(self, trend):
        """خلق سناریو"""
        time.sleep(2)
        genre = random.choice(self.genres)
        scenario = (f"🎭 ژانر: {genre}\n"
                    f"🔥 موضوع ترند: {trend}\n\n"
                    f"📜 سناریو: کاراکتر اصلی سعی می‌کند با موضوع '{trend}' شوخی کند "
                    f"اما اوضاع از کنترل خارج می‌شود و منجر به یک اتفاق خنده‌دار در ژانر {genre} می‌شود.")
        return scenario

    def telegram_sender(self, caption):
        """شبیه‌سازی ارسال به تلگرام"""
        time.sleep(1)
        print(f"ارسال به تلگرام: {caption}")

# --- ۳. ظاهر برنامه (آنچه کاربر می‌بیند) ---
def main():
    st.set_page_config(page_title="Empire Dashboard", page_icon="👑", layout="centered")

    # استایل اختصاصی
    st.markdown("""
        <style>
        .stButton>button {width: 100%; background-color: #FF4B4B; color: white;}
        .success-msg {padding:10px; border-radius:10px; background-color:#D4EDDA; color:#155724;}
        </style>
    """, unsafe_allow_html=True)

    st.title("👑 پنل فرماندهی امپراتوری")
    st.markdown("---")

    # --- بخش ورود با لایسنس ---
    if 'logged_in' not in st.session_state:
        st.session_state.logged_in = False

    if not st.session_state.logged_in:
        st.warning("🔒 سیستم قفل است.")
        code = st.text_input("لطفاً کد لایسنس را وارد کنید:", type="password")
        if st.button("بررسی و ورود"):
            auth = LicenseManager()
            if auth.check_license(code):
                st.session_state.logged_in = True
                st.success("✅ لایسنس تایید شد. خوش آمدید!")
                time.sleep(1)
                st.rerun()
            else:
                st.error("❌ کد اشتباه است! (کد تست: EMPIRE-KING)")
        return

    # --- داشبورد اصلی (بعد از ورود) ---
    st.write("👋 سلام قربان، سیستم آماده دستور شماست.")
    
    if st.button("🚀 استارت تولید محتوای وایرال"):
        engine = EmpireContentEngine()
        
        with st.status("⚙️ در حال اجرای پروتکل امپراتوری...", expanded=True) as status:
            st.write("📡 در حال اسکن یوتیوب و اینستاگرام...")
            trend = engine.trend_analyzer()
            st.info(f"ترند پیدا شد: {trend}")
            
            st.write("🧠 هوش مصنوعی در حال نوشتن سناریو...")
            scenario = engine.ai_character_generator(trend)
            
            st.write("📩 در حال رمزنگاری و ارسال به تلگرام...")
            engine.telegram_sender(scenario)
            
            status.update(label="✅ عملیات با موفقیت انجام شد!", state="complete")
        
        st.markdown("### 📝 خروجی سناریو:")
        st.success(scenario)
        st.caption("ویدیو تدوین شده به تلگرام شما ارسال شد.")

if name == "main":
    main()
