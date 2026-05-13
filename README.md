# Simple Chat Bot 🤖

Chatbot AI chạy trên terminal, có khả năng ghi nhớ lịch sử hội thoại.

## Tính năng
- Trả lời câu hỏi bằng tiếng Việt
- Ghi nhớ context trong suốt cuộc hội thoại
- Gõ "exit" để thoát

## Công nghệ sử dụng
- Python
- Groq API
- Model: Llama 3.3 70B

## Cách chạy
1. Clone repo về máy
2. Tạo file `.env` với nội dung: `GROQ_API_KEY=your_api_key`
3. Cài thư viện: `pip install groq python-dotenv`
4. Chạy: `python main.py`
