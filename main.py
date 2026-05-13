from groq import Groq
from dotenv import load_dotenv
import os

load_dotenv()
client = Groq(api_key=os.getenv("GROQ_API_KEY"))

lich_su = []

while True:
    cau_hoi = input("Bạn: ")

    if cau_hoi.lower() == "exit":
        print("Tạm biệt và hẹn gặp lại!")
        break

    lich_su.append({"role": "user","content": cau_hoi})

    response = client.chat.completions.create(
        model = "llama-3.3-70b-versatile",
        messages = lich_su
    )

    cau_trl = response.choices[0].message.content
    lich_su.append({"role": "assistant", "content": cau_trl})
    print("AI:", cau_trl)