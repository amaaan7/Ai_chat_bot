# Ai_chat_bot

# 🤖 Funny Auto-Roast Chat Bot (Using Gemini API)

This is a funny AI chatbot that reads WhatsApp-style copied chats and automatically replies with Hindi-English roast replies using Google's Gemini API.

---

## 💡 What It Does

- Reads copied WhatsApp messages (chat logs)
- Cleans unnecessary timestamps and names
- Detects if the last message is from someone **other than Amaan**
- Sends that message to Gemini API
- Generates a **savage, funny roast** reply
- (Optional) Copies the roast to clipboard for quick use

---

## ⚙️ How It Works

1. Copy any WhatsApp chat manually.
2. The script runs in a loop and waits for **someone else to message you**.
3. When detected, it sends that message to Gemini.
4. Gemini generates a roast response.
5. The reply is printed (and optionally copied).

---

## 📦 Installation

1. Clone the repo:
   ```bash
   git clone https://github.com/amaaan7/Ai_chat_bot.git
   cd Ai_chat_bot
   
2. Install required packages::
   ```bash
   pip install -r requirements.txt

3. Add your Gemini API key:
   -Get it from Google AI Studio
   -Add this in your script before using:
   ```bash
   import google.generativeai as genai
   genai.configure(api_key="YOUR_API_KEY")
   ```
🧠 Tech Used
Python
Google Gemini API (google-generativeai)
Regex for chat parsing
Optional: pyperclip for clipboard access
📝 Example
    Input (copied chat):
  ```bash
 pip install -r requirements. 
```
Output (roast reply):
```bash
   "Bro tere hello me bhi attitude hai, tu apne ghar me bhi entry maar ke hello bolta hoga na jaise reality show me aaya ho!"
```
🙏 Disclaimer
  - Made purely for fun and entertainment
  - Don't use it to seriously offend or hurt others
