import google.generativeai as genai
import re

# Gemini API Key
genai.configure(api_key="AIzaSyAV-jg8bBdlT98BsjwUptZom_nGJos_Br8")

# Load Gemini Pro model
model = genai.GenerativeModel("gemini-2.5-flash-lite")

# Raw chat
raw_chat = """
[10:01 PM, 7/19/2025] .: Kall hai ni ghr
[10:01 PM, 7/19/2025] Saad AAA: Hai to
[10:01 PM, 7/19/2025] .: Charging ko detu mai laptop khatam huva to mobile be
[10:01 PM, 7/19/2025] Saad AAA: Ha thik he allam hai kya dekhiya kall udr baithiya
[10:02 PM, 7/19/2025] .: Okk
[10:02 PM, 7/19/2025] Saad AAA: Unki bhi nhi jati
"""

# Function to clean WhatsApp-style chat
def clean_chat(chat_text):
    return re.sub(r"\[\d{1,2}:\d{2} [APMapm]{2}, \d+/\d+/\d+\] [^:]+: ", "", chat_text).strip()

# Cleaned chat to send
cleaned_chat = clean_chat(raw_chat)

# Prompt to Gemini
prompt = f"""
Yeh group chat ka convo hai:

{cleaned_chat}

Isse ek funny, hinglish style mein roasting reply banao. Har bande ka halka mazaak uda ke kuch hasi wala punchline do.
"""

# Generate response
try:
    response = model.generate_content(prompt)
    print("\n--- Funny Roast Reply ---\n")
    print(response.text.strip())
except Exception as e:
    print(f"\n❌ Error: {e}")
