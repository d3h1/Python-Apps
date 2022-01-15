# These are our initial variables to make the calculator work
unit_price = float(input("What is the price of this item? "))
quantity = int(input("How many are you buying? "))
tax_rate = 0.090
taxable = True

if taxable:
    # These are our equations when calculating the total
    subtotal = quantity * unit_price
    sales_tax = subtotal * tax_rate
    final_total = subtotal + sales_tax

    # These are our formatting lines
    s_subtotal = "$" + f"{subtotal:,.2f}"
    s_sales_tax = "$" + f"{sales_tax:,.2f}"
    s_final_total = "$" + f"{final_total:,.2f}"

    # This shows our results using f strings
    output = f"""
    Subtotal:  {s_subtotal:>9}
    Sales Tax: +{s_sales_tax:>8}
    _____________________

    Total:     {s_final_total:>9}
    """

print(output)
