# Name: saleem sediqi
# Prog Purpose: This program computes PVCC college tuition & fees based on number of credits
# PVCC Fee Rates are from: https://www.pvcc. edu/tuition-and-fees

import datetime
# define tuition & fee rates
RATE_TUITION_IN = 164.26
RATE_TUITION_OUT = 364.36
RATE_CAPITAL_FEE = 23.50
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90

#define global variables
inout = 1 # 1 means in-state, 2 means out-of-state
numcredits = 0
scholarshipamt = 0


############## define program functions ################
def main():
    more = True
    while more:
        get_user_data()
        perform_calculations()
        display_results()
        yesno = input("\nwould you like to calculate tuition & fees for another student? (Y/N): ")
        if yesno== "n" or yesno == "N":
            another_student = False

def get_user_data():
    global inout, numcredits, scholarshipamt
    inout = int (input("Enter a 1 for IN-STATE; enter a 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered for: "))
    scholarshipamt = float (input ("Scholarship amount received: "))

def perform_calculations():
    global tuition_fee, subtotal, total
    if inout == 1:
        tuition_fee = RATE_TUITION_IN
    else:
        tuition_fee = RATE_TUITION_OUT
    subtotal = tuition_fee + RATE_CAPITAL_FEE + RATE_INSTITUTION_FEE + RATE_ACTIVITY_FEE
    total = subtotal-scholarshipamt

def display_results():
    dollarformat = '8,.2f'
    print('----------------------------------------')
    print('**** PVCC Tuition & Fees Calculator ****')
    print('Your neighborhood food house')
    print('----------------------------------------')
    print ('Tuition & Fees  $'+ format(subtotal,dollarformat))
    print ('Scholarship     $'+ format(scholarshipamt,dollarformat))
    print ('Total Due       $'+ format(total,dollarformat))
    print('----------------------------------------')
    print(str(datetime.datetime.now()))
    
############## call on main program to execute ############
main()
