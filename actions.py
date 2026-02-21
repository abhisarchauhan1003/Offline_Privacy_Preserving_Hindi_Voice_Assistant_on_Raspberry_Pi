import datetime
import os
import sys

def perform_action(intent):

    if intent == "time":
        now = datetime.datetime.now()
        return f"अभी समय है {now.hour} बजकर {now.minute} मिनट"

    elif intent == "date":
        today = datetime.date.today()
        return f"आज की तारीख है {today}"

    elif intent == "day":
        today = datetime.datetime.now().strftime("%A")
        return f"आज {today} है"

    elif intent == "greeting":
        return "नमस्ते! मैं आपकी सहायता कर सकता हूँ"

    elif intent == "weather":
        return "माफ़ कीजिये, अभी मैं मौसम की जानकारी नहीं दे सकता"

    elif intent == "name":
        return "मेरा नाम हिंदी सहायक है"

    elif intent == "about":
        return "मैं एक हिंदी वॉइस असिस्टेंट हूँ और आपकी मदद कर सकता हूँ"

    elif intent == "thanks":
        return "आपका स्वागत है"

    elif intent == "open_google":
        os.system("start chrome https://www.google.com")
        return "गूगल खोल रहा हूँ"

    elif intent == "open_youtube":
        os.system("start chrome https://www.youtube.com")
        return "यूट्यूब खोल रहा हूँ"

    elif intent == "play_music":
        # Change path according to your system
        music_path = "C:\\Users\\Public\\Music"
        os.system(f"start {music_path}")
        return "गाना चला रहा हूँ"

    elif intent == "battery":
        return "बैटरी की जानकारी अभी उपलब्ध नहीं है"

    elif intent == "calculator":
        os.system("start calc")
        return "कैलकुलेटर खोल रहा हूँ"

    elif intent == "help":
        return "आप समय, तारीख, दिन, गूगल खोलो, यूट्यूब खोलो, गाना बजाओ या कैलकुलेटर जैसे कमांड बोल सकते हैं"

    elif intent == "exit":
        return "ठीक है, मैं बंद हो रहा हूँ"

    else:
        return "माफ़ कीजिये, मैं समझ नहीं पाया"
