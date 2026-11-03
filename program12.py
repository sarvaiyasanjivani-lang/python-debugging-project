def calculate_total(price: float, quantity: int) -> float:
    if price < 0 or quantity < 0:
        raise ValueError("Values cannot be negative")

    return price * quantity

print(calculate_total(100.0, 5))
