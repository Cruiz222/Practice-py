def online_store():
    product_inventory = {
        "products": [
            {"name": "tshirt", "quantity": 20, "price": 5000},
            {"name": "television", "quantity": 22, "price": 50000},
            {"name": "shoes", "quantity": 50, "price": 10000},
            {"name": "jean", "quantity": 20, "price": 8000}
        ],
        "shopping_cart": [],
        "storage": []
    }

    print("Available products:")
    for item in product_inventory["products"]:
        print(f"- {item['name'].title()} (Price: {item['price']}, In Stock: {item['quantity']})")
def online_store():
    product_inventory = {
        "products": [
            {"name": "tshirt", "quantity": 20, "price": 5000},
            {"name": "television", "quantity": 22, "price": 50000},
            {"name": "shoes", "quantity": 50, "price": 10000},
            {"name": "jean", "quantity": 20, "price": 8000}
        ],
        "shopping_cart": [],
        "storage": []
    }

    print("Available products:")
    for item in product_inventory["products"]:
        print(f"- {item['name'].title()} (Price: {item['price']}, In Stock: {item['quantity']})")

    product_name = input("\nSelect a product: ").strip().lower()

    selected_item = None
    for item in product_inventory["products"]:
        if item["name"] == product_name:
            selected_item = item
            break

    if selected_item is not None:
        try:
            qty = int(input("Select quantity: ").strip())
        except ValueError:
            print("Invalid quantity. Please enter a whole number.")
            return

        if 0 < qty <= selected_item["quantity"]:
            product_inventory["shopping_cart"].append({
                "product": selected_item["name"],
                "quantity": qty,
                "price": selected_item["price"]
            })

            subtotal = qty * selected_item["price"]
            print("\n--- Cart Contents ---")
            for cart_item in product_inventory["shopping_cart"]:
                print(f"{cart_item['product'].title()} x{cart_item['quantity']} | Subtotal: {subtotal}")

            checkout = input("\nDo you want to checkout? (Yes/No): ").strip().lower()

            if checkout in ("y", "yes"):
                payment_success = True

                if payment_success:
                    selected_item["quantity"] -= qty

                    order_record = {
                        "product": selected_item["name"],
                        "quantity": qty,
                        "total_paid": subtotal,
                        "confirmed": True
                    }
                    product_inventory["storage"].append(order_record)

                    print(f"\nSuccessfully purchased {qty} x {selected_item['name'].title()}!")
                    print(f"Remaining stock: {selected_item['quantity']}")
                else:
                    print("Payment failed.")
            else:
                print("Checkout cancelled.")
        else:
            print(f"Insufficient stock. Only {selected_item['quantity']} available.")
    else:
        print("Invalid product.")

online_store()

    product_name = input("\nSelect a product: ").strip().lower()

    selected_item = None
    for item in product_inventory["products"]:
        if item["name"] == product_name:
            selected_item = item
            break

    if selected_item is not None:
        try:
            qty = int(input("Select quantity: ").strip())
        except ValueError:
            print("Invalid quantity. Please enter a whole number.")
            return

        if 0 < qty <= selected_item["quantity"]:
            product_inventory["shopping_cart"].append({
                "product": selected_item["name"],
                "quantity": qty,
                "price": selected_item["price"]
            })

            subtotal = qty * selected_item["price"]
            print("\n--- Cart Contents ---")
            for cart_item in product_inventory["shopping_cart"]:
                print(f"{cart_item['product'].title()} x{cart_item['quantity']} | Subtotal: {subtotal}")

            checkout = input("\nDo you want to checkout? (Yes/No): ").strip().lower()

            if checkout in ("y", "yes"):
                payment_success = True

                if payment_success:
                    selected_item["quantity"] -= qty

                    order_record = {
                        "product": selected_item["name"],
                        "quantity": qty,
                        "total_paid": subtotal,
                        "confirmed": True
                    }
                    product_inventory["storage"].append(order_record)

                    print(f"\nSuccessfully purchased {qty} x {selected_item['name'].title()}!")
                    print(f"Remaining stock: {selected_item['quantity']}")
                else:
                    print("Payment failed.")
            else:
                print("Checkout cancelled.")
        else:
            print(f"Insufficient stock. Only {selected_item['quantity']} available.")
    else:
        print("Invalid product.")

online_store()
