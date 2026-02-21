def get_intent(text):

    text = text.strip()

    # Time
    if any(word in text for word in ["समय", "टाइम", "घड़ी"]):
        return "time"

    # Date
    elif any(word in text for word in ["तारीख", "दिनांक"]):
        return "date"

    # Day
    elif any(word in text for word in ["कौन सा दिन", "आज कौन सा दिन"]):
        return "day"

    # Greeting
    elif any(word in text for word in ["नमस्ते", "हैलो"]):
        return "greeting"

    # Weather
    elif "मौसम" in text:
        return "weather"

    # Name
    elif "तुम्हारा नाम" in text:
        return "name"

    # About
    elif "तुम कौन हो" in text:
        return "about"

    # Thanks
    elif any(word in text for word in ["धन्यवाद", "शुक्रिया"]):
        return "thanks"

    # Open Google
    elif "गूगल खोलो" in text:
        return "open_google"

    # Open YouTube
    elif "यूट्यूब खोलो" in text:
        return "open_youtube"

    # Play Music (New Command)
    elif any(word in text for word in ["गाना बजाओ", "म्यूजिक चलाओ"]):
        return "play_music"

    # Exit
    elif any(word in text for word in ["बंद करो", "रुको", "बाहर निकलो"]):
        return "exit"

    # Battery
    elif "बैटरी" in text:
        return "battery"

    # Help
    elif "मदद" in text:
        return "help"

    # Calculator
    elif "कैलकुलेटर" in text:
        return "calculator"

    else:
        return "unknown"
