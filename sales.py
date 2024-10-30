import mysql.connector as con
import pandas as pd
import matplotlib.pyplot as plt
# Connect to the MySQL database
connection = con.connect(
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
plt.figure(figsize=(10, 6))
plt.plot(df['Year'], df['TotalSales'], marker='o', color='b', linestyle='-')
plt.title("Yearly Total Sales")
plt.xlabel("Year")
plt.ylabel("Total Sales")
plt.grid(False)
plt.show()