def get_difficulty():
    print("Choose difficulty: Easy, Medium, or Hard")

    while True:
        choice = input("Enter difficulty: ").lower()
        if choice == "easy":
            return 1.5  # Slower turtle
        elif choice == "medium":
            return 1.0  # Normal turtle speed
        elif choice == "hard":
            return 0.5  # Fast turtle
        else:
            print("Invalid choice. Please enter Easy, Medium, or Hard.")
