# Name: Jazil Choudhry
# Program purpose: This program finds the cost of meals at branch barbeque buffet
# Price for an adult meal: $19.95
# Price for a child meal: $11.95
# Sales tax rate: 6.2%
# Service fee rate: 10%
import datetime
############## define global variables ############
# define tax rate and prices 
SALES_TAX_RATE = .062
SERVICE_FEE_RATE = .010
ADULT_MEAL = 19.95
CHILD_MEAL = 11.95
# define global variables
num_adult_meal = 0
num_child_meal= 0
subtotal = 0
sales_tax = 0
service_fee = 0
total = 0
############## define program functions ############
def main():
    more_tickets = True
    while more_tickets:
        get_user_data()
        perform_calculations()
        display_results()

yesno= input("\nWould you like to order again (Y or N)?")
if yesno=="N" or yesno== "n":
    more_tickets= False
    print("Thank you for your order. Enjoy your meal!")

def get_user_data():
    global num_adult_meal
    num_adult_meal = int(input("Number of adult meal: "))
    global num_child_meal
    num_child_meal = int(input("Number of child meal: "))

def perform_calculations():
    global subtotal, sales_tax, service_fee, total
    subtotal = (num_adult_meal * ADULT_MEAL)+(num_child_meal * CHILD_MEAL)
    sales_tax = subtotal * SALES_TAX_RATE
    service_fee = subtotal * SERVICE_FEE_RATE
    total= subtotal + service_fee

def display_results():
    dollarformat = '8,.2f'
    print('----------------------------------------')
    print('**** BRANCH BARBEQUE BUFFET ****')
    print('Your neighborhood food house')
    print('----------------------------------------')
    print ('Meals            $'+ format(subtotal,dollarformat))
    print ('Sales Tax        $'+ format(sales_tax,dollarformat))
    print ('Service Fee      $'+ format(service_fee ,dollarformat))
    print ('Total            $'+ format(total,dollarformat))
    print('----------------------------------------')
    print(str(datetime.datetime.now()))
    
############## call on main program to execute ############
main()
