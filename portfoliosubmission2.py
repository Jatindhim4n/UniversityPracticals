def calculate_bill():
    """
        Function to calculate electricity bill based on unit slabs:
        - 1-100 units: £0.05 per unit
        - 101-300 units: £0.07 per unit
        - 301+ units: £0.10 per unit

        This function can calculate bills for multiple meters.
        """


    meter_count = int(input("Enter number of meters: "))  # Loop outside function
    total_cost = 0
    for i in range(meter_count):  # Loop inside function for multiple readings
        units = int(input(f"Enter electricity units consumed for Meter {i + 1}: "))

        if units <= 100:
            # Cost for 1-100 units
            cost = units * 0.05
        elif units <= 300:
            # Cost for 101-300 units
            cost = (100 * 0.05) + ((units - 100) * 0.07)
        else:
            # Cost for 301+ units
            cost = (100 * 0.05) + (200 * 0.07) + ((units - 300) * 0.10)

        print(f" Meter {i + 1}: Your electricity bill is £{cost}")
        total_cost +=cost
    return total_cost



# Loop outside function to allow multiple users
total_amount = 0  # Initialize total amount for all users

for user in range(3):
    print(f" User {user + 1}'s Bill Calculation:")
    bill = calculate_bill()  #  Store returned bill amount
    total_amount += bill  #  Accumulate total amount

# Print final total amount
print(f" Total amount for all users: £{total_amount:}")