def current_ratio(current_assets, current_liabilities):
    return round(current_assets / current_liabilities, 2)
 
 
def quick_ratio(current_assets, inventory, current_liabilities):
    quick_assets = current_assets - inventory
    return round(quick_assets / current_liabilities, 2)
 
 
def debt_equity_ratio(total_debt, total_equity):
    return round(total_debt / total_equity, 2)
 
 
def gross_profit_ratio(gross_profit, net_sales):
    return round(gross_profit / net_sales * 100, 2)
 
 
def net_profit_ratio(net_profit, net_sales):
    return round(net_profit / net_sales * 100, 2)
 
 
def ratio_report(company, data):
    report = {
        "Current Ratio": current_ratio(
            data["current_assets"], data["current_liabilities"]),
        "Quick Ratio": quick_ratio(
            data["current_assets"], data["inventory"], data["current_liabilities"]),
        "Debt-Equity Ratio": debt_equity_ratio(
            data["total_debt"], data["total_equity"]),
        "Gross Profit (%)": gross_profit_ratio(
            data["gross_profit"], data["net_sales"]),
        "Net Profit (%)": net_profit_ratio(
            data["net_profit"], data["net_sales"]),
    }
    print("===== RATIO ANALYSIS REPORT =====")
    print(f"Company: {company}")
    print("-" * 33)
    for name, value in report.items():
        print(f"{name:<20}: {value:.2f}")
    print("-" * 33)
    return report
 
 
firm_data = {
    "current_assets": 750000,
    "current_liabilities": 300000,
    "inventory": 270000,
    "total_debt": 450000,
    "total_equity": 750000,
    "gross_profit": 480000,
    "net_profit": 186000,
    "net_sales": 1200000,
}
 
ratio_report("Pioneer Enterprises", firm_data)
