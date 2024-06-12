# Task 1: Duplicate Entries Cleanup

customer_ids = ["C001", "C002", "C003", "C002", "C001", "C004"]
customer_id_set = set(customer_ids) # Converts our list into a set and is stored inside the variable customer_id_set.
print(customer_id_set) # Prints: {'C002', 'C004', 'C001', 'C003'}