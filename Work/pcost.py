# pcost.py
#
# Exercise 1.27
# Exercose 1.30
# Exercise 1.32
# Exercise 1.33
# Exercise 2.15 & 2.16
import csv
import sys

def portfolio_cost(filename):  
    total = 0  
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for i, row in enumerate(rows, start = 1):
            record = dict(zip(headers,row))
            try:
                shares = int(record['shares'])
                price_per_share = float(record['price'])
                holding_cost = shares * price_per_share
                total = total + holding_cost
            except ValueError:
                print("Couldn't parse", 'row', i, row)
                print(f'Row {i}: Missing row: {row}')
  
    return total  

if len(sys.argv) == 2:
    filename = sys.argv[1]
else:
    filename = 'Data/portfolio.csv' 

cost = portfolio_cost(filename)
print('Total Cost:', cost )



    
