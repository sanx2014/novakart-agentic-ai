import pandas as pd
from config import PRODUCT_FILE

products = pd.read_csv(PRODUCT_FILE)


def recommend_product(message):

    msg = message.lower()

    if "laptop" in msg:
        return "Customers buying laptops often add a wireless mouse with 20% discount."

    if "phone" in msg:
        return "Would you like to add a screen protector for ₹199?"

    if "headphones" in msg:
        return "A headphone case is currently on 15% discount."

    return ""