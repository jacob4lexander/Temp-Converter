from cgi import print_arguments
from weather import tocel, tofahr

temp = float(input("Enter a Temperature: "))
choice = input ("Convert to celsius (C) or Fahrenheight (F)?").upper()

if choice == 'C':
    message = (tocel(temp))
elif choice == 'F':
    message = (tofahr(temp))
else:
    message = "Invalid Conversion Entry"

print(message)