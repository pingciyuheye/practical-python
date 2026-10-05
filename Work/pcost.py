# pcost.py
#
# Exercise 1.27
# Exercose 1.30
# Exercise 1.32
import csv

def portfolio_cost(filename):  
    total = 0  
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            try:
                shares = int(row[1])
                price_per_share = float(row[2])
                holding_cost = shares * price_per_share
                total = total + holding_cost
            except ValueError:
                print("Couldn't parse", row)
  
    return total   

cost = portfolio_cost('Data/portfolio.csv')
print('Total Cost:', cost )



    
