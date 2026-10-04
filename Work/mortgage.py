# mortgage.py
# Dave has decided to take out a 30-year fixed rate mortgage of $500,000 with Guido’s Mortgage, Stock Investment, 
# and Bitcoin trading corporation. The interest rate is 5% and the monthly payment is $2684.11.
# Exercise 1.11
principal = 500000.0
rate = 0.05
payment = 2684.11
total_paid = 0.0
extra_payment = 1000
total_month = 0
extra_payment_start_month = 61
extra_payment_end_month = 108

while principal > 2684.11:
    if (extra_payment_start_month - 1 <= total_month <= extra_payment_end_month - 1):
      total_paid = total_paid + payment + extra_payment
      total_month = total_month + 1
      principal = principal * (1+rate/12) - payment - extra_payment
      print(f'{total_month:3.0f} ${total_paid:10.2f} ${principal:10.2f}')
    else:
      total_paid = total_paid + payment
      total_month = total_month + 1
      principal = principal * (1+rate/12) - payment
      print(f'{total_month:3.0f} ${total_paid:10.2f} ${principal:10.2f}')

total_month = total_month + 1
total_paid = total_paid + principal * (1+rate/12) # Interest still accrues in the final month.
principal = principal - principal

print(f'{total_month:3.0f} ${total_paid:10.2f} ${principal:10.2f}')     
print(f'Total paid  = ${total_paid:10.2f}')
print(f'Total month = {total_month}')


# off-by-one error fixed