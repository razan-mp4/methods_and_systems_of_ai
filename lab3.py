import numpy as np

# Визначення функцій приналежності
def low(x, min_val, max_val):
    if x <= min_val:
        return 1
    elif x >= max_val:
        return 0
    else:
        return (max_val - x) / (max_val - min_val)

def medium(x, min_val, mid_val, max_val):
    if x <= min_val or x >= max_val:
        return 0
    elif x == mid_val:
        return 1
    elif min_val < x < mid_val:
        return (x - min_val) / (mid_val - min_val)
    else:
        return (max_val - x) / (max_val - mid_val)

def high(x, min_val, max_val):
    if x <= min_val:
        return 0
    elif x >= max_val:
        return 1
    else:
        return (x - min_val) / (max_val - min_val)

# Вхідні значення
temperature = 40
voltage = 10

# Обчислення значень приналежності
temp_low = low(temperature, 0, 50)
temp_medium = medium(temperature, 0, 50, 100)
temp_high = high(temperature, 50, 100)

volt_low = low(voltage, 0, 8)
volt_medium = medium(voltage, 0, 8, 16)
volt_high = high(voltage, 8, 16)

# Правила нечіткої логіки
def infer_charge(temp_low, temp_medium, temp_high, volt_low, volt_medium, volt_high):
    # Режими зарядки
    trickle = min(temp_high, volt_high)
    normal = max(min(temp_medium, volt_medium), min(temp_low, volt_medium))
    fast = min(temp_low, volt_low)
    
    # Визначення рівня зарядки
    if fast > normal and fast > trickle:
        return "Fast Charge"
    elif normal > fast and normal > trickle:
        return "Normal Charge"
    else:
        return "Trickle Charge"

charge_mode = infer_charge(temp_low, temp_medium, temp_high, volt_low, volt_medium, volt_high)

# Вивід результатів
print(f"Температура: {temperature}")
print(f"Напруга: {voltage}")
print(f"Режим зарядки: {charge_mode}")
