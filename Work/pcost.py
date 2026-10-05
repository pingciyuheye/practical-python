# pcost.py
#
# Exercise 1.27
# Exercose 1.30


def portfolio_cost(filename):  
    total = 0  
    with open(filename, 'rt') as f:
        headers = next(f)
        for line in f:
            row = line.split(',')
            try:
                shares = int(row[1])
                price_per_share = float(row[2])
                companies = shares * price_per_share
                total = total + companies
            except ValueError:
                print("Couldn't parse", line)
            # shares = int(row[1])
            
            
        # print(shares, price_per_share)
    return total   

"""
for line in f:
    numbers = float(line)
    print(numbers)
"""
cost = portfolio_cost('Data/portfolio.csv')
print('Total Cost:', cost )


    
