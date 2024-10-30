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

# Read data into a pandas DataFrame
df = pd.read_sql(query, connection)

# Close the database connection
connection.close()

# Plot the data
# Plot a bar chart using Pandas
df.plot(kind='bar', x='Year', y='TotalSales', legend=False, color='skyblue', figsize=(10, 6))
plt.title("Yearly Total Sales")
plt.xlabel("Year")
plt.ylabel("Total Sales")
plt.xticks(rotation=45)
plt.grid(axis='y', linestyle='--', alpha=0.7)
plt.show()