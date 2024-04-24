# Name: Jazil Choudhry
# Prog Purpose: This program reads in a hotel data file, performs calculations, and creates an HTML file for the results

import datetime
###### define rate tuples ############

#           SR    DR  SU
#            0    1   2
ROOM_RATES=(195,250,350)

#       s-tax   occ-tax
#         0        1
TAX_RATES=(0.065, 0.1125)

# Files and list
infile = "emerald.csv"
outfile = "emerald-web-page.html"
guest = []

# Program functions
def main():
    read_in_guest_file()
    perform_calculations()
    open_out_file()
    create_output_html()

def read_in_guest_file():
    guest_data = open(infile, "r")
    guest_in = guest_data.readlines()
    guest_data.close()

    # Split the data and insert into the list called: guest
    for i in guest_in:
        guest.append(i.split(","))

def perform_calculations():
    global grandtotal
    grandtotal = 0

    for i in range(len(guest)):
        room_type = str(guest[i][2])
        num_nights = int(guest[i][3])

        if room_type == "SR":
            subtotal = ROOM_RATES[0] * num_nights
        elif room_type == "DR":
            subtotal = ROOM_RATES[1] * num_nights
        else:
            subtotal = ROOM_RATES[2] * num_nights

        # Complete calculations
        salestax = subtotal * TAX_RATES[0]
        occupancy = subtotal * TAX_RATES[1]
        total = subtotal + salestax + occupancy

        grandtotal += total

        # Append the calculated amounts to the guest list
        guest[i].append(subtotal)
        guest[i].append(salestax)
        guest[i].append(occupancy)
        guest[i].append(total)

def open_out_file():
    global f
    f = open(outfile, 'w')
    



def create_output_html():
    global f

    dollarformat = "8,.2f"
    today = str(datetime.datetime.now())
    day_time = today[0:16]

    tr = '<tr><td>'
    td = '</td><td>'
    endtr = '</td></tr>\n'

    f.write('<style> body { background-image: url("emerald.png"); } table { background-color: seagreen; color: black; margin: 0 auto; } td{text-align: right} </style>\n')  

    
    f.write('<table border="1" style="margin: 0 auto;">\n')
    f.write('<html> <head> <title> Emerald Beach Hotel & Resort </title>\n')
    f.write('<style> td{text-align: right} </style> </head>\n')
    f.write('<body style="font-family: Arial, sans-serif;">\n')  
    f.write('<tr><h1 style="text-align: center;">Guest Data Report - Emerald Beach Hotel & Resort</h1></tr>\n')
    f.write('<tr><th>Last Name</th><th>First Name</th><th>Room Type</th><th>Nights</th><th>Subtotal</th><th>Sales Tax</th><th>Occupancy Tax</th><th>Total</th></tr>\n')

    for g in guest:
        f.write(tr + td.join([str(x) if isinstance(x, (float, int)) else x for x in g]) + endtr)

    f.write('<tr><td colspan="7" style="text-align: right;">Grand Total:</td><td>${:,.2f}</td></tr>\n'.format(grandtotal))
    f.write('<tr><td colspan="8" style="text-align: right;">Generated on:</td></tr>\n')
    f.write('<tr><td colspan="8" style="text-align: right;">{}</td></tr>\n'.format(day_time))

    f.write('</table><br />')
    f.close()
    print('Open ' + outfile + ' to view data.')
main()
