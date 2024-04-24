# Name: saleem sediqi
# Prog Purpose: This program computes PVCC college tuition & fees based on the number of credits
# PVCC Fee Rates are from: https://www.pvcc.edu/tuition-and-fees

import datetime

# define tuition & fee rates
RATE_TUITION_IN = 164.26
RATE_TUITION_OUT = 364.36
RATE_CAPITAL_FEE = 23.50
RATE_INSTITUTION_FEE = 1.75
RATE_ACTIVITY_FEE = 2.90

# define global variables
inout = 1  # 1 means in-state, 2 means out-of-state
numcredits = 0
scholarshipamt = 0

# create output file
outfile = 'tuition-webpage.html'

############## define program functions ################
def main():
    more = True
    while more:
        get_user_data()
        perform_calculations()
        save_to_html()
        yesno = input("\nWould you like to calculate tuition & fees for another student? (Y/N): ")
        if yesno.lower() == "n":
            more = False

def get_user_data():
    global inout, numcredits, scholarshipamt
    inout = int(input("Enter a 1 for IN-STATE; enter a 2 for OUT-OF-STATE: "))
    numcredits = int(input("Number of credits registered for: "))
    scholarshipamt = float(input("Scholarship amount received: "))

def perform_calculations():
    global tuition_fee, subtotal, total
    if inout == 1:
        tuition_fee = RATE_TUITION_IN
    else:
        tuition_fee = RATE_TUITION_OUT
    subtotal = tuition_fee + RATE_CAPITAL_FEE + RATE_INSTITUTION_FEE + RATE_ACTIVITY_FEE
    total = subtotal - scholarshipamt

def save_to_html():
    dollarformat = '8,.2f'
    with open(outfile, 'w') as f:
        f.write('<html>\n<head>\n<style>\n')
        f.write('body { background-image: url("tuition.jpeg"); color:16171a #; font-family: Arial, sans-serif; }\n')
        f.write('table { border-collapse: collapse; width: 80%; margin: 20px auto; background-color: #e6e6fa; }\n')  # Light Purple
        f.write('th, td { border: 1px solid #ffffff; padding: 8px; text-align: left; }\n')
        f.write('</style>\n</head>\n<body>\n')

        f.write('<table>\n')
        f.write('<tr><th colspan="2">PVCC Tuition & Fees Calculator</th></tr>\n')
        f.write('<tr><td> Your nearest community college </td></tr>\n')
        f.write(f'<tr><td>Tuition & Fees</td><td>${format(subtotal, dollarformat)}</td></tr>\n')
        f.write(f'<tr><td>Scholarship</td><td>${format(scholarshipamt, dollarformat)}</td></tr>\n')
        f.write(f'<tr><td>Total Due</td><td>${format(total, dollarformat)}</td></tr>\n')
        f.write(f'<tr><td colspan="2">{datetime.datetime.now().strftime("%Y-%m-%d %H:%M:%S")}</td></tr>\n')
        f.write('</table>\n')

        f.write('</body>\n</html>')

############## call on the main program to execute ############
main()
