import json

def load_inventory():
    try:
        with open('inventory.json', 'r') as f:
            return json.load(f)
    except FileNotFoundError:
        return {}

def save_inventory(inventory):
    with open('inventory.json', 'w') as f:
        json.dump(inventory, f, indent=4)

def add_product(inventory, product_id, name, quantity):
    inventory[product_id] = {'name': name, 'quantity': quantity}

def edit_product(inventory, product_id, new_name, new_quantity):
    if product_id in inventory:
        inventory[product_id]['name'] = new_name
        inventory[product_id]['quantity'] = new_quantity

def delete_product(inventory, product_id):
    if product_id in inventory:
        del inventory[product_id]

def search_product(inventory, product_id):
    if product_id in inventory:
        return inventory[product_id]
    else:
        return None

def display_inventory(inventory):
    for product_id, product_info in inventory.items():
        print(f"Product ID: {product_id}, Name: {product_info['name']}, Quantity: {product_info['quantity']}")

if __name__ == "__main__":
    inventory = load_inventory()

    # Example usage:
    add_product(inventory, 'P001', 'Product A', 100)
    edit_product(inventory, 'P001', 'Updated Product A', 120)
    delete_product(inventory, 'P001')
    product = search_product(inventory, 'P002')
    if product:
        print(product)
    else:
        print("Product not found")

    display_inventory(inventory)

    save_inventory(inventory)
