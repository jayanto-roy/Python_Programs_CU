def compute_current_ratio(current_assets, current_liabilities):
    ratio = current_assets / current_liabilities
    return round(ratio, 2)
 
def compute_quick_ratio(assets, inventory, liabilities):
    ratio = (assets - inventory) / liabilities
    return round(ratio, 2)
 
def compute_debt_equity_ratio(total_debt, total_equity):
    ratio = total_debt / total_equity
    return round(ratio, 2)
 
def compute_gross_profit_ratio(gross_profit, net_sales):
    ratio = (gross_profit / net_sales) * 100
    return round(ratio, 2)
 
def compute_net_profit_ratio(net_profit, net_sales):
    ratio = (net_profit / net_sales) * 100
    return round(ratio, 2)
 
def display_ratio_report(company, ratios):
    print(f"Ratio analysis: {company}")
    for label, value in ratios.items():
        print(f"{label}: {value:.2f}")
 
ratios = {
    "Current": compute_current_ratio(540000, 270000),
    "Quick": compute_quick_ratio(540000, 150000, 270000),
    "Debt-equity": compute_debt_equity_ratio(350000, 700000),
    "Gross profit (%)": compute_gross_profit_ratio(400000, 1000000),
    "Net profit (%)": compute_net_profit_ratio(150000, 1000000)
}
display_ratio_report("Horizon Enterprises", ratios)
