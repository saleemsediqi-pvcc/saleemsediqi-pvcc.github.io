# Name: Jazil Choudhry
# Prog Purpose: This program creates a payroll report

import datetime

############## LISTS of data ############
emp = [
    "Smith, James     ",
    "Johnson, Patricia",
    "Williams, John   ",
    "Brown, Michael   ",
    "Jones, Elizabeth ",
    "Garcia, Brian    ",
    "Miller, Deborah  ",
    "Davis, Timothy   ",
    "Rodriguez, Ronald",
    "Martinez, Karen  ",
    "Hernandez, Lisa  ",
    "Lopez, Nancy     ",
    "Gonzales, Betty  ",
    "Wilson, Sandra   ",
    "Anderson, Margie ",
    "Thomas, Daniel   ",
    "Taylor, Steven   ",
    "Moore, Andrew    ",
    "Jackson, Donna   ",
    "Martin, Yolanda  ",
    "Lee, Carolina    ",
    "Perez, Kevin     ",
    "Thompson, Brian  ",
    "White, Deborah   ",
]

job = ["C", "S", "J", "M", "C", "C", "C", "C", "S", "M", "C", "S",
       "C", "C", "S", "C", "C", "M", "J", "S", "S", "C", "S", "M", ]

hours = [37, 29, 32, 20, 24, 34, 28, 23, 35, 39, 36, 29, 26, 38,
         28, 31, 37, 32, 36, 22, 28, 29, 21, 31]

num_emps = len(emp)

####### NEW LISTS for calculated amounts ##########
gross_pay = []
fed_tax = []
state_tax = []
soc_sec_list = []  
medicare_list = []
ret401k = []
net_pay = []
total_gross = 0
total_net = 0

############ TUPLES of constants ##############
#               C   S   J   M
# indexes       0   1   2   3
PAY_RATE = (16.50, 15.75, 15.75, 19.50)
DEDUCTION_RATES = {
    'Federal Income Tax': 0.12,
    'State Income Tax': 0.03,
    'Social Security Tax': 0.062,
    'Medicare Tax': 0.0145,
    'Retirement (401K)': 0.04,
}

def perform_calculations():
    global total_gross, total_net
    for i in range(num_emps):
        # Calculate gross pay
        if job[i] == 'C':
            pay = hours[i] * PAY_RATE[0]
        elif job[i] == 'S':
            pay = hours[i] * PAY_RATE[1]
        elif job[i] == 'J':
            pay = hours[i] * PAY_RATE[2]
        elif job[i] == 'M':
            pay = hours[i] * PAY_RATE[3]

        # Calculate deductions
        fed = pay * DEDUCTION_RATES['Federal Income Tax']
        state = pay * DEDUCTION_RATES['State Income Tax']
        soc_sec = pay * DEDUCTION_RATES['Social Security Tax']
        medicare = pay * DEDUCTION_RATES['Medicare Tax']
        ret401k_val = pay * DEDUCTION_RATES['Retirement (401K)']

        # Calculate net pay
        net = pay - fed - state - soc_sec - medicare - ret401k_val

        # Add to totals
        total_gross += pay
        total_net += net

        # Append values to lists
        gross_pay.append(pay)
        fed_tax.append(fed)
        state_tax.append(state)
        soc_sec_list.append(soc_sec)
        medicare_list.append(medicare)
        ret401k.append(ret401k_val)
        net_pay.append(net)
def create_output_file():
    # Current date and time
    current_datetime = datetime.datetime.now()
    formatted_datetime = current_datetime.strftime("%Y-%m-%d %H:%M:%S")

    # Print payroll report header
    print("Payroll Report")
    print("Date and Time:", formatted_datetime)

    # Open output file
    out_file = "payroll.txt"
    f = open(out_file, "w")

    # Loop through each employee
    for i in range(num_emps):
        # Write employee details to file
        f.write("{:<20} {:<10} {:<5} ${:<9.2f} ${:<9.2f} ${:<9.2f} ${:<9.2f} ${:<9.2f}\n".format(
            emp[i].strip(), job[i], hours[i], gross_pay[i], fed_tax[i], state_tax[i], soc_sec_list[i], net_pay[i]))

    # Write summary to file
    f.write("\nSummary:\n")
    f.write("Number of Employees: {}\n".format(num_emps))
    f.write("Total Gross Pay: ${:.2f}\n".format(total_gross))
    f.write("Total Net Pay: ${:.2f}\n".format(total_net))

    # Close the file
    f.close()
    print("Open " + out_file + " to view your report")

# Call the functions
perform_calculations()
create_output_file()
