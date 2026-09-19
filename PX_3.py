def comparative_change(item, base_year, current_year):
    change = current_year - base_year
    pct = round(change / base_year * 100, 2)
    return {"item": item, "absolute_change": change, "percentage_change": pct}
 
 
def common_size(item, item_value, base_total):
    return {"item": item, "percentage_of_base": round(item_value / base_total * 100, 2)}
 
 
def trend_index(item, current_value, base_value):
    return {"item": item, "trend_index": round(current_value / base_value * 100, 2)}
 
 
def show(result):
    for key, value in result.items():
        print(f"  {key:<20}: {value}")
    print()
 
 
print("--- COMPARATIVE STATEMENT ---")
show(comparative_change("Sales", 1200000, 1500000))
 
print("--- COMMON-SIZE STATEMENT ---")
show(common_size("Cost of Goods Sold", 720000, 1500000))
 
print("--- TREND ANALYSIS ---")
show(trend_index("Net Profit", 840000, 600000))
