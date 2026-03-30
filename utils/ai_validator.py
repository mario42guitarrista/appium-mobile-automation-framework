def is_valid_transfer_message(text):
    success_keywords = [
        "success",
        "completed",
        "sent",
        "done"
    ]

    text = text.lower()

    return any(keyword in text for keyword in success_keywords)