"""
TASK 1 - Add appropriate comments and explain the below code in the order of execution
"""

def normalize_strings(data):
    """
    Definition:
    Normalize_Strings function do normalization on list of strings by stripping whitespace and converting to lowercase.
    
    Parameters:
    data : It is list of String with including space where data will be normalized.
    
    explanation of code:
    - ListComprehension: 
        Data is a list of strings with spaces. The list comprehension iterates over the data list using a for loop 
        and checks if each item belongs to the string class. If the item is a string, 
        it applies the strip() method to remove leading and trailing spaces and stores the processed item in a new list

    - Returns:
       then returns the list containing  normalized strings

    """
    return [item.strip().lower() for item in data if isinstance(item, str)] 
    
     


def calculate_averages(values):
    """
    Definition:
    Calculate_Averages function computes the average of a list of numbers.
    
    Parameters:
    values : It is a list of elements which may include integers, floats, or other types.
    
    Explanation of code:

    - ListComprehension: 
        Values is list of numerical data. The list comprehension iterates over the data data list using a for loop
        and checks if each item belongs to the float or int class. If The item is float or int, 
        Then stores the checked item in a new list.

    - Condition:
        Check whether the given list of numbers contains any elements.
        If the list is empty, raise a ValueError with the message 'No valid numbers found.' 
    
    

    - Returns:
        returns the average of the valid numbers in the list.

    """
    
    numbers = [num for num in values if isinstance(num, (int, float))] # 
    if not numbers:
        raise ValueError("No valid numbers found")
    return sum(numbers) / len(numbers)

def apply_tax(prices, tax_rate):
    """
    Definition:
    The apply_tax function calculates the final prices after applying a tax rate to a list of prices.
    
    Parameters:
    prices : A list of numerical values representing the original prices.
    tax_rate : A float value representing the tax rate to be applied (example: 0.05 for 5% tax).
    
    Explanation of code:

    - List Comprehension:
        Prices is a list of original prices. The list comprehension iterates over the prices list using a for loop.
        For each price in the list, it calculates the final price by multiplying the price by (1 + tax_rate).
        This result is then stored in a new list that contains the final prices after tax.
    
    - Returns:
        Returns a list containing the prices after the tax has been applied.
    """
    return [price * (1 + tax_rate) for price in prices]

def filter_above_threshold(data, threshold):

    """
    Definition:
    The filter_above_threshold function filters a dictionary, returning only the key-value pairs 
    where the value exceeds a specified threshold.
    
    Parameters:
    data : A dictionary where the keys are any hashable type and the values are numerical (integers or floats).
    threshold : A numerical value that serves as the minimum value for the filtering condition.
    
    Explanation of code:

    - Dictionary Comprehension:
        data is a dictionary containing key-value pairs. The dictionary comprehension iterates over the items in the 
        data dictionary using a for loop. For each key-value pair (k, v), it checks if the value v is greater than 
        the specified threshold. If the condition is true, the key-value pair is included in the new dictionary.
    
    - Returns:
        Returns a new dictionary containing only the key-value pairs where the value exceeds the given threshold.
    """

    return {k: v for k, v in data.items() if v > threshold}

def count_occurrences(items):
    
    """
    Definition:
    The count_occurrences function counts the number of occurrences of each unique item in a list.
    
    Parameters:
    items : A list of elements where the occurrences of each element need to be counted.
    
    Explanation of code:

    - Initialization:
        An empty dictionary counts is initialized to store the count of each unique item.

    - For Loop:
        The function iterates over each item in the items list. For each item:
        - The get method of the dictionary counts is used to retrieve the current count of the item. If the item does not
          exist in the dictionary, it defaults to 0.
        - The count for the item is then incremented by 1 and updated in the dictionary.
    
    - Returns:
        Returns a dictionary where the keys are the unique items from the list, and the values are the counts of their occurrences.

    """
    
    counts = {}
    for item in items:
        counts[item] = counts.get(item, 0) + 1
    return counts

def update_inventory(inventory, updates):

    """
    Definition:
    The update_inventory function updates an inventory dictionary with new quantities from an updates dictionary.
    
    Parameters:
    inventory : A dictionary representing the current inventory with items and their quantities.
    updates : A dictionary containing items and the quantities to be added or updated in the inventory.
    
    Explanation of code:

    - For Loop:
        The function iterates over each key-value pair (item, quantity) in the updates dictionary.
        
        - If the item is already present in the inventory dictionary, its quantity is updated by adding the quantity from the updates dictionary.
        - If the item is not present in the inventory, it is added to the inventory with the quantity from the updates dictionary.

    - Returns:
        Returns the updated inventory dictionary with the new quantities applied.
    """
    for item, quantity in updates.items():
        if item in inventory:
            inventory[item] += quantity
        else:
            inventory[item] = quantity
    return inventory

def summarize_data(data):
    """
    Definition:
    The summarize_data function processes a list of strings to normalize them and 
    then counts the occurrences of each unique normalized string.
    
    Parameters:
    data : A list of strings that may include extra spaces and varying cases.
    
    Explanation of code:

    - Normalize Data:
        The function first calls the normalize_strings function, passing the data list to it. 
        This step cleans the strings by removing leading and trailing spaces and converting them to lowercase.

    - Count Occurrences:
        After normalization, the function uses the count_occurrences function to tally the number of times each unique normalized string appears in the cleaned list.
    
    - Returns:
        Returns a dictionary where each key is a unique normalized string from the data, 
        and each value is the count of how many times that string appears.
    """
    cleaned_data = normalize_strings(data)
    return count_occurrences(cleaned_data)

def analyze_prices(prices, tax_rate, threshold):
    """
    Definition:
    The analyze_prices function applies a tax to a list of prices and then filters out prices that are below a certain threshold.
    
    Parameters:
    prices : A list of numerical values representing the original prices.
    tax_rate : A decimal value representing the tax rate (e.g., 0.05 for 5% tax).
    threshold : A numerical value used to filter the prices. Only prices above this threshold are kept.
    
    Explanation of code:

    - Apply Tax:
        The function first calls apply_tax with the list of prices and the tax_rate. This calculates the final prices after adding the tax.

    - Filter Prices:
        It then uses filter_above_threshold to keep only those prices that are higher than the threshold. 
        The enumerate function is used to create a dictionary where each key is the index of the price in the list, and the value is the price.

    - Returns:
        Returns a dictionary where the keys are the indices of the prices and the values are the prices that are above the threshold.
    """

    taxed_prices = apply_tax(prices, tax_rate)
    filtered_prices = filter_above_threshold(dict(enumerate(taxed_prices)), threshold)
    return filtered_prices

def complex_function(data, prices, tax_rate, threshold):
    """
    Definition:
    The complex_function performs multiple operations on the given data and prices to produce a summary with normalized data, average price, and filtered prices.

    Parameters:
    data : A list of strings that need to be normalized.
    prices : A list of numerical values representing the prices to be analyzed.
    tax_rate : A decimal value representing the tax rate to be applied to the prices.
    threshold : A numerical value used to filter the prices. Only prices above this value will be kept.

    Explanation of code:

    - Normalize Data:
        The function first calls normalize_strings with the data list. 
        This cleans and standardizes the strings by removing extra spaces and converting them to lowercase.

    - Calculate Average Price:
        It then calls calculate_averages with the prices list to compute the average of the prices.

    - Analyze Prices:
        The function uses analyze_prices to apply the tax to the prices and filter out those below the specified threshold.

    - Return Results:
        It returns a dictionary containing:
        - normalized_data: The cleaned and standardized list of strings.
        - average_price: The average of the prices.
        - above_threshold_prices: A dictionary of prices that are above the threshold, with their indices as keys.

    """
    normalized_data = normalize_strings(data)
    averaged_price = calculate_averages(prices)
    above_threshold_prices = analyze_prices(prices, tax_rate, threshold)
    
    return {
        "normalized_data": normalized_data,
        "average_price": averaged_price,
        "above_threshold_prices": above_threshold_prices
    }

# Drive Code
# Example usage:
data = [" apple", "banana ", "Apple", "orange", "banana", "Banana"]
prices = [100, 200, 300, 400, 500]
tax_rate = 0.05
threshold = 350
inventory = {"apple": 50, "banana": 20, "orange": 30}
updates = {"apple": 10, "banana": 5, "grape": 15}

# Compute normalized counts of strings, average price, update inventory, analyze prices, and get complex function results.

# Compute results and print them
normalized_counts = summarize_data(data)  
print("Normalized Counts:", normalized_counts)  # Clean and count occurrences of strings.

'''
Output:
Normalized Counts: {'apple': 2, 'banana': 3, 'orange': 1}
- This output shows the counts of each unique string in the `data` list after normalization.
  - " apple" and "Apple" are both normalized to "apple", resulting in 2 occurrences of "apple".
  - "banana " and "banana" (including case variations) are normalized to "banana", resulting in 3 occurrences of "banana".
  - "orange" is normalized to "orange", resulting in 1 occurrence of "orange".

'''

average_price = calculate_averages(prices)  
print("Average Price:", average_price)  # Calculate the average of the given prices.

"""
Output:
Average Price: 300.0
- This output displays the average of the prices in the `prices` list.
  - The average is calculated as follows: (100 + 200 + 300 + 400 + 500) / 5 = 300.0.

"""

updated_inventory = update_inventory(inventory, updates)  
print("Updated Inventory:", updated_inventory)  # Update inventory quantities with new values.

"""
Output:
Updated Inventory: {'apple': 60, 'banana': 25, 'orange': 30, 'grape': 15}
- This output shows the inventory after applying the updates.
  - The quantity of "apple" was increased by 10 (from 50 to 60).
  - The quantity of "banana" was increased by 5 (from 20 to 25).
  - "grape" was added with a quantity of 15.
  - The quantity of "orange" remained unchanged at 30.
"""

analyzed_prices = analyze_prices(prices, tax_rate, threshold)  
print("Analyzed Prices:", analyzed_prices)  # Apply tax and filter prices above the threshold.

"""
Output:
Analyzed Prices: {3: 420.0, 4: 525.0}
- This output shows the prices that are above the specified threshold after applying the tax rate.
  - The taxed prices are calculated by applying a 5% tax to each price: [105.0, 210.0, 315.0, 420.0, 525.0].
  - Prices that are above the threshold of 350 are 420.0 and 525.0, corresponding to indices 3 and 4, respectively.
"""

final_result = complex_function(data, prices, tax_rate, threshold)  
print("Final Result:", final_result)  # Get a comprehensive summary of normalized data, average price, and filtered prices.

"""
Output:
Final Result: {'normalized_data': ['apple', 'banana', 'apple', 'orange', 'banana', 'banana'], 'average_price': 300.0, 'above_threshold_prices': {3: 420.0, 4: 525.0}}
- This output provides a comprehensive summary combining the results from different functions.
  - normalized_data shows the list of strings after cleaning and standardizing: ['apple', 'banana', 'apple', 'orange', 'banana', 'banana'].
  - average_price is the average of the original prices: 300.0.
  - above_threshold_prices lists the prices above the threshold of 350, showing the indices and the corresponding taxed prices: {3: 420.0, 4: 525.0}.
"""


print("-"*80)


"""
TASK 2 - Fix and explain what the errors were in the below code

"""
def calculate_area(radius):
    """
    Calculates the area of a circle given its radius.
    
    Parameters:
    radius (float): The radius of the circle. Must be non-negative.

    Returns:
    float: The area of the circle.
    
    Raises:
    ValueError: If the radius is negative.
    """
    if radius < 0:
        raise ValueError("Radius must be non-negative")
    return 3.14 * radius * radius

def find_item(cart, price):
    """
    Finds an item in the cart by its price.

    Parameters:
    cart (dict): A dictionary where keys are items and values are their prices.
    price (float): The price to find in the cart.

    Returns:
    str: The item corresponding to the given price.

    Raises:
    KeyError: If the item is not found in the cart.
    """
    for item_,price_ in cart.items():   # key can not find the key by values directly. cart[price] this is wrong way
        if price_ == price:
            return item_
    raise ValueError("No item found with given price")    


def update_inventory(inventory, item, quantity):
    """
    Updates the inventory with the new quantity for the given item.

    Parameters:
    inventory (dict): A dictionary where keys are item names and values are their quantities.
    item (str): The item to update.
    quantity (int): The amount to add to the item's quantity.

    Returns:
    None

    Raises:
    KeyError: If the item is not found in the inventory.
    ValueError: If the quantity is negative.
    """
    if item not in inventory:
        raise KeyError(f"{item} not found in inventory")
    if quantity < 0:
        raise ValueError("Quantity must be non-negative")
    inventory[item] += quantity

def generate_report(inventory):
    """
    Generates a report of the inventory.

    Parameters:
    inventory (dict): A dictionary where keys are item names and values are their quantities.

    Returns:
    list: A list of strings representing the inventory report.
    """
    report = []
    for item, quantity in inventory.items():
        report.append(f"{item}: {quantity}")
        if quantity > 10:
            report.append(f"High stock: {item}")
    return report

# Example usage

# Initialize inventory
inventory = {'apple': 10, 'banana': 5, 'orange': 15}

# Update inventory quantities
try:
    update_inventory(inventory, 'apple', 6) # Adds 6 to 'apple', making it 16
except (KeyError,ValueError) as e:
    print(e)

# To test error
try:
    update_inventory(inventory, 'banana', -2) # Quantity must be non-negative otherwise it will raise ValueError.
except (KeyError,ValueError) as e:
    print(e)

update_inventory(inventory, 'banana', 2) # Adds 2 to 'banana', making it 7

# Update the cart dictionary to have prices as values
cart = {'apple': 16, 'banana': 7, 'orange': 15}  # Updated prices to match the expected output
# try and except help to handle the error.
try:
    item = find_item(cart, 15)
    print(f"Item with value 15: {item}")
except ValueError as e:
    print(e)

# Generate and print inventory report
report = generate_report(inventory)
print("Inventory Report:")
for line in report:
    print(line)

# Calculate and print area of a circle
radius = 5
print(f"Area of the circle with radius {radius} is: {calculate_area(radius)}")  # Fixed: Added the closing parenthesis


'''
Expected Output:
    Item with value 15: orange
    Inventory Report:
    apple: 16
    High stock: apple
    banana: 7
    orange: 15
    High stock: orange
    Area of the circle with radius 5 is: 78.5
'''