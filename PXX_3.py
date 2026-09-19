def get_comparative_change(item, year1, year2):
    change = year2 - year1
    percentage = (change / year1) * 100
    percentage = round(percentage, 2)
    return change, percentage
 
def get_common_size_percentage(item_value, total):
    percentage = (item_value / total) * 100
    return round(percentage, 2)
 
def get_trend_index(current, base):
    percentage = (current / base) * 100
    return round(percentage, 2)


print("COMPARATIVE STATEMENT:")

print(get_comparative_change("Purchases", 500000, 620000))

print("\nCOMMON-SIZE STATEMENT:")

print(get_common_size_percentage(300000, 750000))

print("\nTREND ANALYSIS:") 

print(get_trend_index(480000, 400000))
