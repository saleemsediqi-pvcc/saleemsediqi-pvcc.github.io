# Name: Saleem Sediqi
import datetime 
# Prices
pizza_prices = {'S': 9.99, 'M': 12.99, 'L': 17.99, 'X': 21.99}
drink_price = 3.99
breadstick_price = 6.99
sales_tax_rate = 0.055  # 5.5%

# Function to calculate subtotal, sales tax, and total
def calculate_receipt(pizza_size, num_pizzas, num_drinks, num_breadsticks):
    pizza_cost = num_pizzas * pizza_prices[pizza_size]
    drink_cost = num_drinks * drink_price
    breadstick_cost = num_breadsticks * breadstick_price
    subtotal = pizza_cost + drink_cost + breadstick_cost
    sales_tax_amount = subtotal * sales_tax_rate
    total = subtotal + sales_tax_amount
    return pizza_cost, drink_cost, breadstick_cost, subtotal, sales_tax_amount, total

# Function to display the receipt
def display_receipt(company_name, date_time, pizza_size, num_pizzas, num_drinks, num_breadsticks,
                    pizza_cost, drink_cost, breadstick_cost, subtotal, sales_tax_amount, total):
    print(f"\n{company_name} Receipt")
    print(f"Date/Time: {date_time}")
    print("\nItems Ordered:")
    print(f"{num_pizzas} {pizza_size} Pizza(s) @ ${pizza_cost:.2f} each")
    print(f"{num_drinks} Drinks @ ${drink_cost:.2f} each")
    print(f"{num_breadsticks} Orders of Breadsticks @ ${breadstick_cost:.2f} each")

    print("\nCost Breakdown:")
    print(f"Pizza Cost: ${pizza_cost:.2f}")
    print(f"Drink Cost: ${drink_cost:.2f}")
    print(f"Breadstick Cost: ${breadstick_cost:.2f}")
    print(f"\nSubtotal: ${subtotal:.2f}")
    print(f"Sales Tax ({sales_tax_rate * 100}%): ${sales_tax_amount:.2f}")
    print(f"Total: ${total:.2f}")

# Main program
if __name__ == "__main__":
    # Get user input
    company_name = "Palermo Pizza Company"
    date_time = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

    while True:
        print("\nMenu:")
        print("S - Small Pizza ($9.99)")
        print("M - Medium Pizza ($12.99)")
        print("L - Large Pizza ($17.99)")
        print("X - Extra Large Pizza ($21.99)")
        print("D - Drink ($3.99)")
        print("B - Breadsticks ($6.99)")
        print("Q - Quit")

        item = input("Enter item code (Q to quit): ").upper()

        if item == 'Q':
            break

        if item in pizza_prices:
            pizza_size = item
            num_pizzas = int(input(f"How many {pizza_size} pizzas would you like? "))
            num_drinks = int(input("How many drinks would you like? "))
            num_breadsticks = int(input("How many orders of breadsticks would you like? "))

            pizza_cost, drink_cost, breadstick_cost, subtotal, sales_tax_amount, total = calculate_receipt(
                pizza_size, num_pizzas, num_drinks, num_breadsticks)

            display_receipt(company_name, date_time, pizza_size, num_pizzas, num_drinks, num_breadsticks,
                            pizza_cost, drink_cost, breadstick_cost, subtotal, sales_tax_amount, total)
        else:
            print("Invalid item code. Please try again.")
            if __name__ == "_ _main_ _":
                main()
