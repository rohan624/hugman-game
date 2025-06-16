import csv

def stock_tracker():
    stock_prices = {
        "AAPL": 180,
        "TSLA": 250,
        "GOOGL": 2800,
        "MSFT": 300,
        "AMZN": 3500
    }

    portfolio = {}

    print("Welcome to the Stock Portfolio Tracker!")
    print("Available stocks and prices:")
    for stock, price in stock_prices.items():
        print(f" - {stock}: ${price}")

    print("\nEnter your stock holdings.")
    print("Type 'done' to finish input.\n")

    while True:
        stock = input("Enter stock symbol (or 'done' to finish): ").upper().strip()
        if stock == 'DONE':
            break

        if stock not in stock_prices:
            print("Stock not recognized. Please enter one of the available stocks.")
            continue

        quantity_str = input(f"Enter quantity of {stock}: ").strip()
        if not quantity_str.isdigit():
            print("Please enter a valid positive integer for quantity.")
            continue
        quantity = int(quantity_str)
        if quantity <= 0:
            print("Quantity must be greater than zero.")
            continue

        portfolio[stock] = portfolio.get(stock, 0) + quantity
        print(f"Added {quantity} shares of {stock} to your portfolio.\n")

    if not portfolio:
        print("No stocks entered. Exiting.")
        return

    total_investment = sum(stock_prices[stock] * qty for stock, qty in portfolio.items())

    print("\nYour Portfolio Summary:")
    for stock, qty in portfolio.items():
        price = stock_prices[stock]
        value = price * qty
        print(f" - {stock}: {qty} shares × ${price} = ${value}")

    print(f"\nTotal Investment Value: ${total_investment}")

    # Optionally save to file
    save_choice = input("\nDo you want to save the portfolio summary to a file? (y/n): ").strip().lower()
    if save_choice == 'y':
        filename = input("Enter filename (with .txt or .csv extension): ").strip()
        try:
            if filename.endswith('.csv'):
                with open(filename, mode='w', newline='') as csvfile:
                    writer = csv.writer(csvfile)
                    writer.writerow(['Stock', 'Quantity', 'Price', 'Value'])
                    for stock, qty in portfolio.items():
                        price = stock_prices[stock]
                        value = price * qty
                        writer.writerow([stock, qty, price, value])
                    writer.writerow([])
                    writer.writerow(['Total Investment', '', '', total_investment])
                print(f"Portfolio saved to {filename}")
            elif filename.endswith('.txt'):
                with open(filename, mode='w') as txtfile:
                    txtfile.write("Portfolio Summary\n")
                    txtfile.write("=================\n")
                    for stock, qty in portfolio.items():
                        price = stock_prices[stock]
                        value = price * qty
                        txtfile.write(f"{stock}: {qty} shares × ${price} = ${value}\n")
                    txtfile.write("\n")
                    txtfile.write(f"Total Investment Value: ${total_investment}\n")
                print(f"Portfolio saved to {filename}")
            else:
                print("Unsupported file extension. Please use .txt or .csv")
        except Exception as e:
            print(f"Failed to save file: {e}")
    else:
        print("Portfolio not saved.")

if __name__ == "__main__":
    stock_tracker()

