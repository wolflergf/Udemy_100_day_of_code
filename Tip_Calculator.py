print('Welcome to the tip calculator.')
total_bill = float(input('What the total bill? $'))
perc = int(input('What percentage tip would you like to give? 10, 12 , or 15? '))
people = int(input('How many people to split the bill? '))
bill = (total_bill * (1 + (perc / 100))) / people
print('Each person should pay: ${:.2f}'.format(bill))
