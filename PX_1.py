SLABS = [(100, 3.00), (100, 4.50), (100, 6.00), (float('inf'), 7.50)]
FIXED_CHARGE = 50
DUTY_RATE = 0.05
 
 
def slab_wise_charge(units):
    """Return the energy charge by consuming units slab by slab."""
    if units < 0:
        raise ValueError("Units consumed cannot be negative")
    charge = 0.0
    remaining = units
    for width, rate in SLABS:
        if remaining <= 0:
            break
        billable = min(remaining, width)
        charge += billable * rate
        remaining -= billable
    return charge
 
 
def build_bill(units, fixed=FIXED_CHARGE, duty_rate=DUTY_RATE):
    energy = slab_wise_charge(units)
    subtotal = energy + fixed
    duty = subtotal * duty_rate
    return {
        "units": units,
        "energy": round(energy, 2),
        "fixed": round(fixed, 2),
        "duty": round(duty, 2),
        "total": round(subtotal + duty, 2),
    }
 
 
def display_bill(consumer, units):
    bill = build_bill(units)
    print("----- ELECTRICITY BILL -----")
    print(f"Consumer Name : {consumer}")
    print(f"Units Consumed: {bill['units']}")
    print(f"Energy Charge : Rs {bill['energy']:.2f}")
    print(f"Fixed Charge  : Rs {bill['fixed']:.2f}")
    print(f"Duty (5%)     : Rs {bill['duty']:.2f}")
    print(f"Total Bill    : Rs {bill['total']:.2f}")
    print("----------------------------")
 
 
display_bill("Jayanto_House-01", 75)
display_bill("Jayanto_House-02", 180)
display_bill("Jayanto_House-03", 360)
