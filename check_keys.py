from google import genai
import time

# =========================================================
# NẠP DANH SÁCH KEY CẦN KIỂM TRA VÀO ĐÂY
# =========================================================
LIST_API_KEYS = [
    "AIzaSy...KEY_1",
    "AIzaSy...KEY_2",
    "AIzaSy...KEY_3"
]

def kiem_tra_linh_thach(api_key):
    try:
        # Khởi tạo client với key cần test
        client = genai.Client(api_key=api_key)
        
        # Gửi một yêu cầu cực nhẹ để không tốn tài nguyên
        response = client.models.generate_content(
            model="gemini-3-flash-preview",
            contents="Say exactly one word: OK"
        )
        
        if response.text:
            return "✅ HOẠT ĐỘNG TỐT (Linh lực dồi dào)"
        else:
            return "❓ PHẢN HỒI RỖNG"
            
    except Exception as e:
        error_msg = str(e).lower()
        if "429" in error_msg or "quota" in error_msg or "exhausted" in error_msg:
            return "⚠️ CẠN KIỆT (Đã hết hạn mức hoặc đang bị nghẽn)"
        elif "400" in error_msg or "403" in error_msg or "invalid" in error_msg or "permission" in error_msg:
            return "❌ KEY HỎNG (Sai Key, chưa bật API, hoặc bị khóa)"
        else:
            return f"❓ LỖI LẠ: {e}"

# --- CHẠY KIỂM TRA ---
print("🔍 BẮT ĐẦU KIỂM TRA TÌNH TRẠNG LINH THẠCH...\n" + "="*50)

for i, key in enumerate(LIST_API_KEYS):
    # Lấy 5 ký tự cuối của Key để dễ nhận diện mà không lộ toàn bộ Key
    key_tail = key[-5:] if len(key) > 5 else key
    
    print(f"🔮 Đang kiểm tra Key #{i+1} (...{key_tail}): ", end="", flush=True)
    
    status = kiem_tra_linh_thach(key)
    print(status)
    
    # Nghỉ 1 giây giữa các lần test để tránh bị khóa IP do spam
    time.sleep(1)

print("="*50 + "\n✅ HOÀN TẤT KIỂM TRA!")
