def vacuum_world():
    # initializing goal_state
    # 0 indicates Clean and 1 indicates Dirty
    goal_state = {'A': '0', 'B': '0'}  # Fixed quotes and closing curly brace
    cost = 0

    location_input = input("Enter Location of Vacuum")  # user_input of location vacuum is placed
    status_input = input("Enter status of : " + location_input)  # user_input if location is dirty or clean
    status_input_complement = input("Enter status of other room :-")
    print("Initial Location Condition " + str(goal_state))  # Added space after "Condition"

    if location_input == 'A':
        # Location A is Dirty.
        print("Vacuum is placed in Location A")
        if status_input == '1':
            print("Location A is Dirty.")
            # suck the dirt and mark it as clean
            goal_state['A'] = '0'
            cost += 1  # cost for suck
            print("Cost for CLEANING A " + str(cost))
            print("Location A has been Cleaned.")

# Call the function to execute the code
vacuum_world()
