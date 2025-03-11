def calculate_total_o1(prices):
    """
    Calculate the total shopping price in O(1) time complexity.
    This assumes the sum of prices is already calculated.
    
    Args:
        prices: A pre-computed sum of all item prices
        
    Returns:
        The total shopping amount
    """
    return prices

def calculate_total_on(prices):
    """
    Calculate the total shopping price in O(n) time complexity.
    This iterates through each price once.
    
    Args:
        prices: A list of item prices
        
    Returns:
        The total shopping amount
    """
    total = 0
    # O(n) time complexity - we need to iterate through each price once
    for price in prices:
        total += price
    return total

def calculate_total_on2(prices):
    """
    Calculate the total shopping price in O(n²) time complexity.
    This is an inefficient implementation that demonstrates O(n²) complexity.
    
    Args:
        prices: A list of item prices
        
    Returns:
        The total shopping amount
    """
    total = 0
    # O(n²) time complexity - for each price, we iterate through all prices again
    for i in range(len(prices)):
        for j in range(len(prices)):
            # Only add the current price (i) once
            if i == j:
                total += prices[i]
    return total

# Example usage:
if __name__ == "__main__":
    # Sample shopping cart with prices
    shopping_cart = [15000, 25000, 10000, 5000, 30000]  # Prices in Indonesian Rupiah
    
    # Calculate using different algorithms
    total_o1 = calculate_total_o1(sum(shopping_cart))
    total_on = calculate_total_on(shopping_cart)
    total_on2 = calculate_total_on2(shopping_cart)
    
    # Display results
    print(f"Items in shopping cart: {shopping_cart}")
    print(f"Total (O(1)): Rp {total_o1}")
    print(f"Total (O(n)): Rp {total_on}")
    print(f"Total (O(n²)): Rp {total_on2}")
    
    # Compare algorithm efficiency
    print("\nAlgorithm efficiency demonstration:")
    import time
    
    # Test with a larger cart
    large_cart = [1000] * 1000  # 1000 items costing 1000 Rupiah each
    
    start = time.time()
    calculate_total_o1(sum(large_cart))
    o1_time = time.time() - start
    
    start = time.time()
    calculate_total_on(large_cart)
    on_time = time.time() - start
    
    start = time.time()
    calculate_total_on2(large_cart[:100])  # Using only 100 items for O(n²) as it's very slow
    on2_time = time.time() - start
    
    print(f"O(1) execution time: {o1_time:.8f} seconds")
    print(f"O(n) execution time: {on_time:.8f} seconds")
    print(f"O(n²) execution time (with 100 items): {on2_time:.8f} seconds")
    print(f"Projected O(n²) time with 1000 items: ~{on2_time * 100:.2f} seconds")