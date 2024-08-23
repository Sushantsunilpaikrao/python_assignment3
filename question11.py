orders = [
    (1, 20, 2),  # Order 1: 20€ per item, 2 items
    (2, 50, 1),  # Order 2: 50€ per item, 1 item
    (3, 15, 5),  # Order 3: 15€ per item, 5 items
    (4, 200, 1)  # Order 4: 200€ per item, 1 item
]

calculate_total = lambda order: (order[0], order[1] * order[2] + (10 if order[1] * order[2] < 100 else 0))

adjusted_orders = list(map(calculate_total, orders))

print(f"Adjusted order list: {adjusted_orders}")
