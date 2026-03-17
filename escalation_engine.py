def check_escalation(message, ai_response):

    triggers = [
        "not satisfied",
        "talk to agent",
        "complaint",
        "angry",
        "worst service"
    ]

    msg = message.lower()

    for t in triggers:
        if t in msg:
            return True

    if ai_response == "ESCALATE":
        return True

    return False