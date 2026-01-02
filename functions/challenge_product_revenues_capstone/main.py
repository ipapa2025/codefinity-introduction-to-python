# List of products, their prices, and the quantities sold
products = ["Bread", "Apples", "Oranges", "Bananas"]
prices = [0.50, 1.20, 2.50, 2.00]  # price per item
quantities_sold = [150, 200, 100, 50]  # number of items sold

def calculate_revenue(prices, quantities_sold):
    revenue=[]
    for i in range(len(prices)):
        revenue.append(prices[i]*quantities_sold[i])
    return revenue

def formatted_output(products,revenues):
    revenue_per_product=list(zip(products,revenues))    
    revenue_per_product_sorted=sorted(revenue_per_product)
    for i in range(len(revenue_per_product_sorted)):
        print(f"{revenue_per_product_sorted[i][0]} has total revenue of ${revenue_per_product_sorted[i][1]}")

revenue= calculate_revenue(prices,quantities_sold)

formatted_output(products,revenue)

    # Example of expected output line (do not remove):


