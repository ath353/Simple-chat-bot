# 🤖 Simple Chat Bot ✅

## 1. Tên dự án
**Simple Chat Bot**

## 2. Ứng dụng dự án
Đây là chatbot AI chạy trên **terminal**, có khả năng ghi nhớ lịch sử hội thoại (context) trong suốt quá trình trò chuyện với người dùng.

### Tính năng chính
- 💬 Trả lời câu hỏi bằng tiếng Việt
- 🧠 Ghi nhớ context trong suốt cuộc hội thoại
- 🚪 Gõ `exit` để thoát chương trình

## 3. Công nghệ
- **Ngôn ngữ:** Python
- **API:** Groq API
- **Model:** Llama 3.3 70B
- **Giao diện:** Command Line Interface (CLI)

## 4. Hướng dẫn sử dụng

### Yêu cầu
- Đã cài đặt **Python 3.x** trên máy
- Có API key của Groq

### Các bước chạy chương trình
1. Clone repo về máy
2. Tạo file `.env` với nội dung:
   ```
   GROQ_API_KEY=your_api_key
   ```
3. Cài thư viện cần thiết:
   ```bash
   pip install groq python-dotenv
   ```
4. Chạy chương trình:
   ```bash
   python main.py
   ```
5. Nhập câu hỏi hoặc trò chuyện với chatbot; gõ `exit` để thoát

## 5. Tác giả
 - ath353
