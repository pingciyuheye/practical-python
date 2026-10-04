# pcost.py
#
# Exercise 1.27
total = 0
with open('Data/portfolio.csv', 'rt') as f:
    headers = next(f)
    for line in f:
        row = line.split(',')
        shares = int(row[1])
        price_per_share = float(row[2])
        companies = shares * price_per_share
        total = total + companies
    # print(shares, price_per_share)
"""
for line in f:
    numbers = float(line)
    print(numbers)
"""


print(f'Total Cost {total:0.2f}')

    
