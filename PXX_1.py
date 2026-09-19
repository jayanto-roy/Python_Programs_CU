def calculate_energy_cost(units):
    if units < 0:
        raise ValueError("Units cannot be negative")
    if units <= 100:
        cost = units * 2.50
    elif units <= 200:
        cost = 250 + (units - 100) * 3.75
    elif units <= 300:
        cost = 625 + (units - 200) * 5.25
    else:
        cost = 1150 + (units - 300) * 7.00
    return cost
 
def compute_electricity_bill(units, fixed_charge=40, duty_rate=0.06):
    energy = calculate_energy_cost(units)
    subtotal = energy + fixed_charge
    duty = subtotal * duty_rate
    total = subtotal + duty
    return round(energy, 2), round(duty, 2), round(total, 2)
 
def display_bill(consumer_name, units):
    energy, duty, total = compute_electricity_bill(units)
    print("----- ELECTRICITY BILL -----")
    print(f"Consumer: {consumer_name}")
    print(f"Energy: Rs {energy:.2f}")
    print(f"Duty: Rs {duty:.2f}")
    print(f"Total: Rs {total:.2f}")
    print("----------------------------")
 
display_bill("Ankita_House-01", 60)
display_bill("Ankita_House-02", 220)
display_bill("Ankita_House-03", 350)
