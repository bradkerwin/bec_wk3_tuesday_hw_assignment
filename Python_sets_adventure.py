# Task 1: Flight Route Comparison
our_routes = {"LAX", "JFK", "CDG", "DXB"}
competitor_routes = {"JFK", "CDG", "LHR", "BKK"}

def main():
    while True:
        select = input('''
Please select an option.
1. Destinations that both airlines fly to.
2. Destinations unique to your airline.
3. Destinations that neither airline shares.
4. Quit
''')
        if select == '1':
            common_destinations()
        elif select == '2':
            unique_to_us()
        elif select == '3':
            not_shared()
        elif select == '4':
            print("Thank you, have a good day.")
            break
        else:
            continue

def common_destinations(): # Function that obtains items the sets both have in common.
    all_routes = our_routes.intersection(competitor_routes) # Using <set1>.intersection(<set2>) method to return only the items found in both sets.
    print(f"These are the destinations that both airlines fly to {all_routes}")

def unique_to_us(): # Function that obtains items found only in the set our_routes.
    our_unique_routes = our_routes.difference(competitor_routes) # Using <set1>.difference(<set2>) method to return the items stored in our_routes that are not found in competitor_routes.
    print(f"These are the destinations unique to our airline {our_unique_routes}")

def not_shared(): # Function that obtains items the sets do not have in common. 
    unshared = our_routes.symmetric_difference(competitor_routes) # Using <set1>.symmetric_difference(<set2>) method to return only the destinations that the 2 sets do not have in common.
    print(f"These are the destinations that are not shared by either airline {unshared}")

main() # Calling our main function.