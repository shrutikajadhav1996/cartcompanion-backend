from flask import Flask, request, jsonify
import database_help
import connection_help

app = Flask(__name__)

inprogress_orders = {}


@app.route("/", methods=["POST"])
def handle_request():
    payload = request.json

    intent = payload['queryResult']['intent']['displayName']
    parameters = payload['queryResult']['parameters']
    output_contexts = payload['queryResult']['outputContexts']
    session_id = connection_help.extract_session_id(output_contexts[0]["name"])
    intent_handler_dict = {
        'order_addDress- Context - Inorder': add_to_order,
        'Remove_Order- context-Inorder': remove_from_order,
        'order_completed-Context- Inorder': complete_order,
        'Track_Order- Context-Track-Inorder': track_order
    }

    return intent_handler_dict[intent](parameters, session_id)


def save_to_db(order: dict):
    next_order_id = database_help.get_next_order_id()
    total_order_price = 0

    for key, quantity in order.items():
        dresstype, size, gender = key
        dress_id = database_help.get_dress_id(dresstype, size, gender)
        if not dress_id:
            return -1

        dress_price = database_help.get_dress_price(dress_id)
        if not dress_price:
            return -1

        total_price = quantity * dress_price
        total_order_price += total_price

        rcode = database_help.insert_order_item(
            next_order_id,
            dress_id,
            quantity,
            total_price
        )

        if rcode == -1:
            return -1

    order_summary_rcode = database_help.insert_order_summary(next_order_id, total_order_price)
    if order_summary_rcode == -1:
        return -1

    tracking_rcode = database_help.insert_order_tracking(next_order_id, "in transit")
    if tracking_rcode == -1:
        return -1

    return next_order_id


def complete_order(parameters: dict, session_id: str):
    if session_id not in inprogress_orders:
        fulfillment_text = "I'm having trouble finding your order. Sorry! Can you place a new order, please?"
    else:
        order = inprogress_orders[session_id]
        order_id = save_to_db(order)
        if order_id == -1:
            fulfillment_text = "Sorry, I couldn't process your order due to a backend error. Please place a new order again."
        else:
            order_total = database_help.get_total_order_price(order_id)
            fulfillment_text = f"Awesome. We have placed your order. Here is your order id # {order_id}. Your order total is {order_total} which you can pay through Credit or Debit card!"

        del inprogress_orders[session_id]

    return jsonify({
        "fulfillmentText": fulfillment_text
    })


def add_to_order(parameters: dict, session_id: str):
    dresstype = parameters["Dress-type"]
    quantities = parameters["number"]
    sizes = parameters["Dress-Size"]
    genders = parameters["Gender"]

    if len(dresstype) != len(quantities) or len(dresstype) != len(sizes) or len(dresstype) != len(genders):
        fulfillment_text = "Sorry, I didn't understand. Can you please specify dress items, quantities, sizes, and genders clearly?"
    else:
        new_order_dict = {(dresstype[i], sizes[i], genders[i]): quantities[i] for i in range(len(dresstype))}

        if session_id in inprogress_orders:
            current_order_dict = inprogress_orders[session_id]
            current_order_dict.update(new_order_dict)
            inprogress_orders[session_id] = current_order_dict
        else:
            inprogress_orders[session_id] = new_order_dict

        order_str = connection_help.get_str_from_order_dict(inprogress_orders[session_id])
        fulfillment_text = f"So far you have: {order_str}. Do you need anything else?"

    return jsonify({
        "fulfillmentText": fulfillment_text
    })


def remove_from_order(parameters: dict, session_id: str):
    if session_id not in inprogress_orders:
        return jsonify({
            "fulfillmentText": "I'm having trouble finding your order. Sorry! Can you place a new order, please?"
        })

    dresstype = parameters["Dress-type"]
    sizes = parameters["Dress-Size"]
    genders = parameters["Gender"]
    current_order = inprogress_orders[session_id]

    removed_items = []
    no_such_items = []

    for i in range(len(dresstype)):
        key = (dresstype[i], sizes[i], genders[i])
        if key not in current_order:
            no_such_items.append(f"{dresstype[i]} ({sizes[i]}, {genders[i]})")
        else:
            removed_items.append(f"{dresstype[i]} ({sizes[i]}, {genders[i]})")
            del current_order[key]

    fulfillment_text = ""
    if len(removed_items) > 0:
        fulfillment_text = f'Removed {", ".join(removed_items)} from your order!'

    if len(no_such_items) > 0:
        fulfillment_text += f' Your current order does not have {", ".join(no_such_items)}.'

    if len(current_order.keys()) == 0:
        fulfillment_text += " Your order is empty!"
    else:
        order_str = connection_help.get_str_from_order_dict(current_order)
        fulfillment_text += f" Here is what is left in your order: {order_str}"

    return jsonify({
        "fulfillmentText": fulfillment_text
    })


def track_order(parameters: dict, session_id: str):
    if "order_id" in parameters:
        fulfillment_text = f"order_id present"
    else:
        fulfillment_text = f"order_id absent"

    order_id = int(parameters['number'])
    order_status = database_help.get_order_status(order_id)
    if order_status:
        fulfillment_text = f"The order status for order id: {order_id} is: {order_status}"
    else:
        fulfillment_text = f"No order found with order id: {order_id}"

    return jsonify({
        "fulfillmentText": fulfillment_text
    })


if __name__ == "__main__":
    app.run(debug=True)
