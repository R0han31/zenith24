from flask import Flask, render_template, request

app = Flask(__name__)

# Initial bill items with prices and quantities
bill_items = {
    "Chips": {"price": 20, "quantity": 2},
    "Apple": {"price": 10, "quantity": 3},
    "Orange": {"price": 15, "quantity": 4},
    "Biscuit": {"price": 30, "quantity": 1}
}

# Secret code to delete items
delete_code = "1234"

def calculate_total_bill():
    total = sum(item['price'] * item['quantity'] for item in bill_items.values())
    return total

@app.route('/')
def index():
    total_bill = calculate_total_bill()
    return render_template('bill.html', bill_items=bill_items, total_bill=total_bill)

@app.route('/delete_item', methods=['POST'])
def delete_item():
    code = request.form['code']
    item_to_delete = request.form['item']

    if code == delete_code:
        if item_to_delete in bill_items:
            if bill_items[item_to_delete]['quantity'] > 1:
                bill_items[item_to_delete]['quantity'] -= 1
            else:
                del bill_items[item_to_delete]
            total_bill = calculate_total_bill()
            return render_template('bill.html', bill_items=bill_items, total_bill=total_bill)
        else:
            return "Item not found in the bill."
    else:
        return "Invalid code."

if __name__ == '__main__':
    app.run(debug=True)
