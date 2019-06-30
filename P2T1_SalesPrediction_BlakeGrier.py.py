# This project will get the totals sales and display 23 percent
# of the total sales.
# June 17, 2019
# CTI-110 P2T1 - Sales Prediction
# Blake A. Grier

# Collect the projected total sales.
total_sales = float(input('Enter the projected sales: '))

# Calculate the profit as 23 percent of total sales.
profit = total_sales * 0.23

# Display the profit of the projected total sales.
print('The profit is $', format(profit, ',.2f'))
