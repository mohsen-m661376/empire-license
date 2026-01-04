import secrets
import string

def generate_license_key(prefix="EMPIRE", length=16):
    """
    تولید یک کلید لایسنس امن و یکتا
    مثال خروجی: EMPIRE-A1B2-C3D4-E5F6
    """
    alphabet = string.ascii_uppercase + string.digits
    # تولید 3 بخش 4 کاراکتری رندوم
    parts = [''.join(secrets.choice(alphabet) for _ in range(4)) for _ in range(3)]
    
    license_key = f"{prefix}-{'-'.join(parts)}"
    return license_key

# تست تولید 5 لایسنس برای فروش
print("--- لیست لایسنس‌های جدید برای فروش ---")
for i in range(5):
    print(f"لایسنس {i+1}: {generate_license_key()}")