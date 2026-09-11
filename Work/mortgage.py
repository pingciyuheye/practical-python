# mortgage.py
# Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with Guido’s Mortgage, Stock Investment, 
# and Bitcoin trading corporation. The interest rate is 5% and the monthly payment is $2684.11.
# Exercise 1.7
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment = 1000
first_year_month = 12
total_month = 0

while principal > 0:
    if (first_year_month > 0):
      total_paid = total_paid + payment + extra_payment
      total_month = total_month + 1
      first_year_month = first_year_month - 1
      principal = principal * (1+rate/12) - payment - extra_payment

    else:
      total_paid = total_paid + payment
      total_month = total_month + 1
      principal = principal * (1+rate/12) - payment

print('Total paid', total_paid)
print('Total month', total_month)