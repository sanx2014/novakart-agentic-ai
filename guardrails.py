def hallucination_check(response, context):

    if len(context) == 0:
        return False

    if "I guess" in response:
        return False

    if "maybe" in response:
        return False

    return True


def policy_violation_check(response):

    banned_phrases = [
        "guaranteed refund",
        "always refund",
        "free product forever"
    ]

    for phrase in banned_phrases:
        if phrase in response.lower():
            return False

    return True