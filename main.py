import os
import pyautogui
import time
import pyperclip
import re
import google.generativeai as genai

# Gemini Pro API Key
GEMINI_API_KEY = "AIzaSyAV-jg8bBdlT98BsjwUptZom_nGJos_Br8"
if not GEMINI_API_KEY:
    raise RuntimeError("Set your Gemini API key.")

genai.configure(api_key=GEMINI_API_KEY)
model = genai.GenerativeModel("gemini-2.5-flash-lite")


# ---------- UTILITIES ----------
def clean_chat(chat):
    pattern = r'\[\d{1,2}:\d{2}\s?(?:AM|PM|am|pm)?,\s*\d{1,2}/\d{1,2}/\d{4}\] [^:]+: ?'
    return re.sub(pattern, '', chat, flags=re.IGNORECASE).strip()


def get_last_sender(chat_log):
    matches = re.findall(r'\[\d{1,2}:\d{2}\s?(?:AM|PM|am|pm)?,\s*\d{1,2}/\d{1,2}/\d{4}\] (.*?):', chat_log)
    if matches:
        return matches[-1].strip()
    return None


def get_last_message(chat_log):
    messages = re.findall(r'\[\d{1,2}:\d{2}\s?(?:AM|PM|am|pm)?,\s*\d{1,2}/\d{1,2}/\d{4}\] .*?: (.*)', chat_log)
    if messages:
        return messages[-1].strip()
    return ""


def gemini_chat(prompt):
    system_instruction = (
        "You are Amaan, from India. You roast people in Hindi + English mixed language."
        " Analyze the chat history and respond with a funny roast reply in short only."
        " Output should be ONLY the next chat message. No name, no time."
    )
    full_prompt = system_instruction + "\n\nChat:\n" + prompt + "\n\nRoast Reply:"
    response = model.generate_content(full_prompt)
    return response.text.strip()


# ---------- WhatsApp Automation ----------
pyautogui.click(678, 216)  # Focus WhatsApp window
time.sleep(1)

last_seen_message = ""

while True:
    try:
        time.sleep(5)

        # Select chat
        pyautogui.moveTo(678, 216)
        pyautogui.dragTo(1340, 660, duration=2.0, button='left')
        pyautogui.hotkey('ctrl', 'c')
        time.sleep(1.5)
        pyautogui.click(1333, 628)

        chat_history = pyperclip.paste()
        if not chat_history or len(chat_history) < 20:
            print("Empty or small chat, skipping.")
            continue

        last_sender = get_last_sender(chat_history)
        last_message = get_last_message(chat_history)

        print(f"Last sender: {last_sender}")
        print(f"Last message: {last_message}")

        # Skip if last sender is Amaan (you) or same message as last time
        if last_sender == "Amaan":
            print("Last message is from Amaan (you), skipping.")
            continue

        if last_message == last_seen_message:
            print("Same last message detected, skipping.")
            continue

        cleaned = clean_chat(chat_history)
        response = gemini_chat(cleaned)

        print("--- GEMINI RESPONSE ---")
        print(response)
        print("-----------------------")

        # Send reply
        pyperclip.copy(response)
        pyautogui.click(969, 683)  # Input box
        time.sleep(1)
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(1)
        pyautogui.press('enter')

        last_seen_message = last_message  # Update last seen message

    except Exception as e:
        print("Error:", e)
        time.sleep(5)
