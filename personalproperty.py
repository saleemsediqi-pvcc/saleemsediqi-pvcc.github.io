# Name: Jazil Choudhry
# Prog Purpose: To show the personal property tax in Charlottesville
import datetime

def calculate_tax(vehicle_value, tax_rate, tax_relief_eligible=False):
    annual_tax = vehicle_value * tax_rate / 100
    six_month_tax = annual_tax / 2

    if tax_relief_eligible:
        relief_amount = six_month_tax * 0.33
        total_due = six_month_tax - relief_amount
    else:
        relief_amount = 0
        total_due = six_month_tax

    return six_month_tax, relief_amount, total_due


def main():
    print("Welcome to the Charlottesville Personal Property Tax Calculator!")

    while True:
        try:
            vehicle_value = float(input("Enter the assessed value of your vehicle: $"))
        except ValueError:
            print("Invalid input. Please enter a numerical value for the assessed value.")
            continue

        tax_relief_eligible = input("Is your vehicle eligible for tax relief? (Y/N): ").upper() == 'Y'

        tax_rate = 4.20  # $4.20 per $100 of vehicle value

        six_month_tax, relief_amount, total_due = calculate_tax(vehicle_value, tax_rate, tax_relief_eligible)

        current_datetime = datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")

        print("\nTax Bill for the next six months:")
        print(f"Date/Time: {current_datetime}")
        print(f"Assessed Value: ${vehicle_value:,.2f}")
        print(f"Full Annual Amount Owed: ${six_month_tax * 2:,.2f}")
        print(f"Relief Amount: ${relief_amount:,.2f}")
        print(f"Total Due: ${total_due:,.2f}\n")

        another_calculation = input("Do you want to calculate tax for another vehicle? (Y/N): ").upper()
        if another_calculation != 'Y':
            print("Thank you for using the Charlottesville Personal Property Tax Calculator. Goodbye!")
            break


if __name__ == "__main__":
    main()



