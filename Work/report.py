# report.py
#
# Exercise 2.4 & 2.5 & 2.6 & 2.7 & 2.9
import csv


def read_portfolio(filename):
    """
    Read a portfolio file into a list of dicts with keys name, shares and price.
    """
    portfolio = []
    with open(filename, 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        for row in rows:
            nshares = int(row[1])
            price = float(row[2]) 
            holding = {
                'name' : row[0],
                'shares' : nshares,
                'price' : price
            }
            portfolio.append(holding)
    return portfolio
portfolio = read_portfolio('Data/portfolio.csv')
print(portfolio)


with open('Data/portfolio.csv', 'rt') as f:
        rows = csv.reader(f)
        headers = next(rows)
        total_buy_in = 0
        for row in rows:
            nshares = int(row[1])
            price = float(row[2]) 
            total_buy_in += nshares * price 
        print(total_buy_in)

def read_prices(filename):
    with open(filename, 'rt') as d:
        rows = csv.reader(d)
        prices = {}
        for row in rows:
            """
            try: 
                prices[row[0]] = float(row[1])
            except IndexError:
                print("Couldn't load", row)
            """
            if len(row) > 0:
                prices[row[0]] = float(row[1])

    return prices
now_prices = read_prices('Data/prices.csv')
print(now_prices)

now_assets = 0
for s in portfolio:
    now_assets += now_prices[s['name']] * s['shares']
print(now_assets)

earn = now_assets - total_buy_in
print(earn)

def make_report(portfolio, now_prices):
    all_change = []
    per_stock = ()  # Create a list, shouldn't been in for loop!!!!!
    for s in portfolio:
        change = now_prices[s['name']] - s['price']  # Calculate the change
        per_stock = s['name'], s['shares'], now_prices[s['name']], change
        all_change.append(per_stock)
    return all_change



