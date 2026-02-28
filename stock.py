prices = {"AAPL": 180, "TSLA": 250, "GOOG": 140, "AMZN": 185, "MSFT": 420}

print("Available stocks:", ", ".join(prices.keys()))

portfolio = {}

while True:
    stock = input("\nEnter stock name (or 'done' to finish): ").upper()
    if stock == "DONE":
        break
    if stock not in prices:
        print("Stock not found.")
        continue
    qty = int(input(f"Enter quantity for {stock}: "))
    portfolio[stock] = portfolio.get(stock, 0) + qty

if not portfolio:
    print("No stocks entered.")
else:
    print("\n--- Portfolio Summary ---")
    total = 0
    rows = []
    for stock, qty in portfolio.items():
        value = prices[stock] * qty
        total += value
        rows.append(f"{stock},{qty},{prices[stock]},{value}")
        print(f"{stock}: {qty} shares x ${prices[stock]} = ${value}")
    print(f"Total Investment: ${total}")

    save = input("\nSave to file? (yes/no): ").lower()
    if save == "yes":
        fmt = input("Format? (txt/csv): ").lower()
        filename = f"portfolio.{fmt}"
        with open(filename, "w") as f:
            if fmt == "csv":
                f.write("Stock,Quantity,Price,Value\n")
                f.write("\n".join(rows))
                f.write(f"\nTotal,,, {total}")
            else:
                for row in rows:
                    parts = row.split(",")
                    f.write(f"{parts[0]}: {parts[1]} shares x ${parts[2]} = ${parts[3]}\n")
                f.write(f"Total Investment: ${total}\n")
        print(f"Saved to {filename}")