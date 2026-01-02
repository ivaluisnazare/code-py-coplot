# write code to calculate the average of three grades provided by the user. Use arithmetic operators to perform the average calculation.
def calculate_average_grades():
    grades = []
    for i in range(1, 4):
        while True:
            try:
                grade = float(input(f"Enter grade {i}: "))
                if 0 <= grade <= 100:
                    grades.append(grade)
                    break
                else:
                    print("Please enter a grade between 0 and 100.")
            except ValueError:
                print("Invalid input: expected a number.")

    average = sum(grades) / len(grades)
    print(f"The average of the grades is: {average:.2f}")
if __name__ == "__main__":
    calculate_average_grades()
