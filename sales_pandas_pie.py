import mysql.connector
import pandas as pd
import matplotlib.pyplot as plt
# Connect to the MySQL database
connection = mysql.connector.connect(
    host='localhost',    # Replace with your host
    user='root',  # Replace with your MySQL username
    password='',  # Replace with your MySQL password
    database='classicmodels',   # Replace with your database name
    port=3307
)

# Query to get total sales year-on-year
query = """
SELECT YEAR(orderDate) AS Year, SUM(quantityOrdered * priceEach) AS TotalSales
FROM orders
JOIN orderdetails ON orders.orderNumber = orderdetails.orderNumber
GROUP BY YEAR(orderDate)
ORDER BY Year;
"""
# cursor =  connection.cursor()
# cursor.execute(query)
# results = cursor.fetchall()
# print(results)
# Read data into a pandas DataFrame
df = pd.read_sql(query, connection)

# Close the database connection
connection.close()

# Plot a pie chart using Pandas only
df.set_index('Year')['TotalSales'].plot(
    kind='pie',
    autopct='%1.1f%%',  # Display percentage with one decimal place
    startangle=140,     # Starting angle of the chart
    figsize=(8, 8),     # Size of the figure
    colormap='viridis', # Color map for distinct colors per year
    title="Yearly Total Sales Distribution"  # Chart title
)

# Save the chart to a file
filename = "Yearly_Total_Sales_Distribution.png"
# plt.savefig(filename, format='png', dpi=300)  # Automatically uses matplotlib to save
print(f"Pie chart saved as {filename}")
plt.show()

# Plot the data
# Plot a bar chart using Pandas
# df.set_index('Year')['TotalSales'].plot(kind='pie', autopct='%1.1f%%', startangle=140, figsize=(8, 8), colormap='viridis')
# plt.title("Yearly Total Sales Distribution")
# plt.ylabel("")  # Removes the default ylabel
# filename = "Yearly_Total_Sales_Distribution.png"  # Specify your desired filename
# plt.savefig(filename, format='png', dpi=300)  # Save as PNG with high quality (300 dpi)
# plt.show()