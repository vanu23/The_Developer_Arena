def calculate_grade(marks):
    """Return grade and message based on marks."""

    if 90 <= marks <= 100:
        return "A", "🌟 Excellent! You're a star performer!"
    elif 80 <= marks <= 89:
        return "B", "✨ Very Good! Keep it up!"
    elif 70 <= marks <= 79:
        return "C", "👍 Good! You can do even better!"
    elif 60 <= marks <= 69:
        return "D", "🙂 Not bad! Focus a bit more!"
    else:
        return "F", "💪 Don't give up! You can improve with practice!"


print("🎓 STUDENT GRADE CALCULATOR\n")

name = input("Enter student name: ")

while True:
    try:
        marks = float(input("Enter marks (0-100): "))

        if 0 <= marks <= 100:
            break
        else:
            print("❌ Invalid input! Marks must be between 0 and 100.\n")
    except ValueError:
        print("❌ Invalid input! Please enter a number.\n")

grade, message = calculate_grade(marks)

print("\n📊 RESULT FOR", name.upper())
print(f"Marks: {marks}/100")
print(f"Grade: {grade}")
print(f"Message: {message}")
