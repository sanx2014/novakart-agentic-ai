import pandas as pd
from config import ORDERS_FILE

orders = pd.read_csv(ORDERS_FILE)


def get_order_details(order_id):

    order = orders[orders["order_id"] == order_id]

    if order.empty:
        return None

    return order.to_dict(orient="records")[0]


def get_order_items(order_id):

    order = get_order_details(order_id)

    if order:
        return order["items"]

    return None


def get_delivery_status(order_id):

    order = get_order_details(order_id)

    if order:
        return order["status"]

    return None