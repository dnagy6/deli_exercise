# Initial lists for the deli orders
sandwich_orders = ['Tuna', 'Ham', 'Veggie', 'Turkey', 'Chicken', 'Roast Beef']
finished_sandwiches = []

# Process each sandwich order until there are none left
while sandwich_orders:
    # Remove the first sandwich order from the list
    current_sandwich = sandwich_orders.pop(0)
    
    # Simulate making the sandwich
    print(f"I made your {current_sandwich} sandwich.")
    
    # Add the finished sandwich to the finished_sandwiches list
    finished_sandwiches.append(current_sandwich)

# Display all the finished sandwiches
print("\n--- Finished Sandwiches ---")
for sandwich in finished_sandwiches:
    print(f"- {sandwich.title()} Sandwich")