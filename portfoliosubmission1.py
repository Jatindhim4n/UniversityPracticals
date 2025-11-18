print("Welcome to the fitness plan generator")
print("Answer the following questions and we will make fitness plan just for you")
print("What is your fitness goal?")
print("1-Weight Loss")
print("2-Muscle Building")
print("3-General Fitness")
choice=int(input("Enter the number corresponding to your goal: "))

if choice < 1 or choice > 3:
    print("Invalid choice. Please restart the program.")

else:
    print("What is your current fitness level?")
    print("1-Beginner")
    print("2-Intermediate")
    print("3-Advanced")
    level_choice = int(input("Enter the number corresponding to your fitness level: "))

if level_choice < 1 or level_choice > 3:
    print("Invalid choice. Please restart the program.")




print("Do you prefer working out at home or at the gym?")
print("1-Home")
print("2-Gym")
preference=int(input("Please enter corresponding to your preference: "))

if preference <1 or preference >2:
    print("Invalid choice. Please restart the program.")

else:
    print("Congratulation your fitness plan is ready!!")

if choice==1:
    if level_choice==1:
        if preference==1:
            print("- 20-minute walk")
            print("- 3 sets of 10 squats")
            print("- 3 sets of 10 push-ups")
            print("- 3 sets of 30-second planks")
        else:
            print("- 20-minute treadmill run")
            print("- 3 sets of 10 leg presses")
            print("- 3 sets of 10 chest presses")
            print("- 3 sets of 10-minute cycling")

    elif level_choice==2:
        if preference == 1:
            print("- 30-minute workout")
            print("- 4 sets of 15 jump squats")
            print("- 4 sets of 15 push-ups")
            print("- 4 sets of 1-minute planks")
        else:
            print("- 30-minute running on the treadmill")
            print("- 4 sets of 12 weighted squats")
            print("- 4 sets of 12 bench presses")
            print("- 4 sets of 15-minute rowing")
    else:
        if preference == 1:
            print("- 40-minute advanced HIIT workout")
            print("- 5 sets of 20 burpees")
            print("- 5 sets of 20 push-ups")
            print("- 5 sets of 1.5-minute planks")
        else:
            print("- 40-minute sprint intervals on the treadmill")
            print("- 5 sets of 15 deadlifts")
            print("- 5 sets of 15 bench presses")

elif choice == 2:
        if level_choice == 1:
            if preference == 1:
                print("- 3 sets of 10 push-ups")
                print("- 3 sets of 10 bodyweight squats")
                print("- 3 sets of 10 lunges")
                print("- 3 sets of 10-second wall sits")
            else:  # Gym
                print("- 3 sets of 10 bench presses")
                print("- 3 sets of 10 leg presses")
                print("- 3 sets of 10 bicep curls")
                print("- 3 sets of 10 tricep dips")
        elif level_choice == 2:
            if preference == 1:
                print("- 4 sets of 15 push-ups")
                print("- 4 sets of 15 squats")
                print("- 4 sets of 15 lunges")
                print("- 4 sets of 30-second wall sits")
            else:  # Gym
                print("- 4 sets of 12 bench presses")
                print("- 4 sets of 12 deadlifts")
                print("- 4 sets of 12 bicep curls")
                print("- 4 sets of 12 tricep dips")
        else:
            if preference == 1:
                print("- 5 sets of 20 push-ups")
                print("- 5 sets of 20 squats")
                print("- 5 sets of 20 lunges")
                print("- 5 sets of 1-minute wall sits")
            else:
                print("- 5 sets of 15 bench presses")
                print("- 5 sets of 15 deadlifts")
                print("- 5 sets of 15 bicep curls")
                print("- 5 sets of 15 tricep dips")

else:
    if level_choice == 1:
        if preference == 1:
            print("- 20-minute walk or light jog")
            print("- 3 sets of 10 push-ups")
            print("- 3 sets of 10 squats")
            print("- 3 sets of 10 lunges")
        else:
            print("- 20-minute treadmill walk")
            print("- 3 sets of 10 chest presses")
            print("- 3 sets of 10 leg presses")
            print("- 3 sets of 10 bicep curls")
    elif level_choice == 2:
        if preference == 1:
            print("- 30-minute jog")
            print("- 4 sets of 15 push-ups")
            print("- 4 sets of 15 squats")
            print("- 4 sets of 15 lunges")
        else:
            print("- 30-minute treadmill run")
            print("- 4 sets of 12 chest presses")
            print("- 4 sets of 12 leg presses")
            print("- 4 sets of 12 bicep curls")
    else:
        if preference == 1:
            print("- 40-minute run")
            print("- 5 sets of 20 push-ups")
            print("- 5 sets of 20 squats")
            print("- 5 sets of 20 lunges")
        else:
            print("- 40-minute treadmill sprint")
            print("- 5 sets of 15 chest presses")
            print("- 5 sets of 15 deadlifts")
            print("- 5 sets of 15 bicep curls")


print("Stick to this plan consistently, and you'll see great results!")
print("Thank you for using the Personalized Fitness Plan Generator!")