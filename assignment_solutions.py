#  ASSIGNMENT NO. 1 - PYTHON PROGRAMS
                

# # ==============================================================================
# # 1. Check if a number is positive, negative, or zero.
# # ==============================================================================
# def check_positive_negative_zero():
#     num = float(input("Enter a number: "))
#     if num > 0:
#         print(f"{num} is Positive.")
#     elif num < 0:
#         print(f"{num} is Negative.")
#     else:
#         print("The number is Zero.")


# # ==============================================================================
# # 2. Check whether a number is even or odd.
# # ==============================================================================
# def check_even_or_odd():
#     num = int(input("Enter an integer: "))
#     if num % 2 == 0:
#         print(f"{num} is Even.")
#     else:
#         print(f"{num} is Odd.")


# # ==============================================================================
# # 3. Find the greater of two numbers.
# # ==============================================================================
# def find_greater_of_two():
#     num1 = float(input("Enter first number: "))
#     num2 = float(input("Enter second number: "))
#     if num1 > num2:
#         print(f"{num1} is greater than {num2}.")
#     elif num2 > num1:
#         print(f"{num2} is greater than {num1}.")
#     else:
#         print("Both numbers are equal.")


# # ==============================================================================
# # 4. Find the greatest of three numbers.
# # ==============================================================================
# def find_greatest_of_three():
#     a = float(input("Enter first number: "))
#     b = float(input("Enter second number: "))
#     c = float(input("Enter third number: "))

#     if a >= b and a >= c:
#         print(f"{a} is the greatest.")
#     elif b >= a and b >= c:
#         print(f"{b} is the greatest.")
#     else:
#         print(f"{c} is the greatest.")


# # ==============================================================================
# # 5. Check if a person is eligible to vote (age >= 18).
# # ==============================================================================
# def check_voting_eligibility():
#     age = int(input("Enter your age: "))
#     if age >= 18:
#         print("You are eligible to vote.")
#     elif age >= 0:
#         print(f"You are not eligible to vote. You need to wait {18 - age} more year(s).")
#     else:
#         print("Invalid age entered.")


# # ==============================================================================
# # 6. Check whether a year is a leap year.
# # ==============================================================================
# def check_leap_year():
#     year = int(input("Enter a year: "))
#     if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#         print(f"{year} is a Leap Year.")
#     else:
#         print(f"{year} is NOT a Leap Year.")


# # ==============================================================================
# # 7. Check if a character is a vowel or consonant.
# # ==============================================================================
# def check_vowel_or_consonant():
#     ch = input("Enter a single character: ").strip()
#     if len(ch) != 1 or not ch.isalpha():
#         print("Invalid input! Please enter a single alphabetic character.")
#     elif ch.lower() in ['a', 'e', 'i', 'o', 'u']:
#         print(f"'{ch}' is a Vowel.")
#     else:
#         print(f"'{ch}' is a Consonant.")


# # ==============================================================================
# # 8. Check whether a number is divisible by 5 and 11.
# # ==============================================================================
# def check_divisible_by_5_and_11():
#     num = int(input("Enter an integer: "))
#     if num % 5 == 0 and num % 11 == 0:
#         print(f"{num} is divisible by both 5 and 11.")
#     else:
#         print(f"{num} is NOT divisible by both 5 and 11.")


# # ==============================================================================
# # 9. Check if a number is a multiple of both 3 and 7.
# # ==============================================================================
# def check_multiple_of_3_and_7():
#     num = int(input("Enter an integer: "))
#     if num % 3 == 0 and num % 7 == 0:
#         print(f"{num} is a multiple of both 3 and 7.")
#     else:
#         print(f"{num} is NOT a multiple of both 3 and 7.")


# # ==============================================================================
# # 10. Assign grades based on marks:
# # ==============================================================================
# def assign_grade():
#     marks = float(input("Enter marks (0 to 100): "))
#     if marks < 0 or marks > 100:
#         print("Invalid marks! Please enter a value between 0 and 100.")
#     elif marks >= 90:
#         print("Grade: A")
#     elif marks >= 80:
#         print("Grade: B")
#     elif marks >= 70:
#         print("Grade: C")
#     elif marks >= 60:
#         print("Grade: D")
#     else:
#         print("Grade: F")


# # ==============================================================================
# # 11. Check if a character is uppercase or lowercase.
# # ==============================================================================
# def check_uppercase_or_lowercase():
#     ch = input("Enter a character: ").strip()
#     if len(ch) != 1 or not ch.isalpha():
#         print("Invalid input! Please enter a single alphabetic letter.")
#     elif ch.isupper():
#         print(f"'{ch}' is an Uppercase letter.")
#     elif ch.islower():
#         print(f"'{ch}' is a Lowercase letter.")


# # ==============================================================================
# # 12. Find whether the entered alphabet is a vowel using if-elif.
# # ==============================================================================
# def check_vowel_using_ifelif():
#     ch = input("Enter an alphabet: ").strip().lower()
#     if len(ch) != 1 or not ch.isalpha():
#         print("Invalid input! Please enter a single alphabet.")
#     elif ch == 'a':
#         print("'a' is a Vowel.")
#     elif ch == 'e':
#         print("'e' is a Vowel.")
#     elif ch == 'i':
#         print("'i' is a Vowel.")
#     elif ch == 'o':
#         print("'o' is a Vowel.")
#     elif ch == 'u':
#         print("'u' is a Vowel.")
#     else:
#         print(f"'{ch}' is a Consonant (Not a vowel).")


# # ==============================================================================
# # 13. Check if three sides can form a triangle.
# # ==============================================================================
# def check_valid_triangle():
#     s1 = float(input("Enter length of side 1: "))
#     s2 = float(input("Enter length of side 2: "))
#     s3 = float(input("Enter length of side 3: "))

#     if s1 > 0 and s2 > 0 and s3 > 0 and (s1 + s2 > s3) and (s1 + s3 > s2) and (s2 + s3 > s1):
#         print("Yes, these three sides can form a valid triangle.")
#     else:
#         print("No, these three sides CANNOT form a triangle.")


# # ==============================================================================
# # 14. Determine the type of triangle (Equilateral, Isosceles, Scalene).
# # ==============================================================================
# def find_triangle_type():
#     a = float(input("Enter length of side 1: "))
#     b = float(input("Enter length of side 2: "))
#     c = float(input("Enter length of side 3: "))

#     if a <= 0 or b <= 0 or c <= 0 or (a + b <= c) or (a + c <= b) or (b + c <= a):
#         print("These side lengths do not form a valid triangle.")
#     elif a == b == c:
#         print("The triangle is Equilateral (all sides are equal).")
#     elif a == b or b == c or a == c:
#         print("The triangle is Isosceles (two sides are equal).")
#     else:
#         print("The triangle is Scalene (all sides are different).")


# # ==============================================================================
# # 15. Find the largest among four numbers.
# # ==============================================================================
# def find_largest_of_four():
#     n1 = float(input("Enter first number: "))
#     n2 = float(input("Enter second number: "))
#     n3 = float(input("Enter third number: "))
#     n4 = float(input("Enter fourth number: "))

#     if n1 >= n2 and n1 >= n3 and n1 >= n4:
#         largest = n1
#     elif n2 >= n1 and n2 >= n3 and n2 >= n4:
#         largest = n2
#     elif n3 >= n1 and n3 >= n2 and n3 >= n4:
#         largest = n3
#     else:
#         largest = n4

#     print(f"The largest number among {n1}, {n2}, {n3}, and {n4} is: {largest}")


# # ==============================================================================
# # 16. Check whether a number is a three-digit number.
# # ==============================================================================
# def check_three_digit_number():
#     num = int(input("Enter an integer: "))
#     abs_num = abs(num)
#     if 100 <= abs_num <= 999:
#         print(f"{num} is a 3-digit number.")
#     else:
#         print(f"{num} is NOT a 3-digit number.")


# # ==============================================================================
# # 17. Calculate electricity bill using slab rates.
# # ==============================================================================
# def calculate_electricity_bill():
#     units = float(input("Enter electricity units consumed: "))

#     if units < 0:
#         print("Invalid units! Units cannot be negative.")
#         return

#     if units <= 100:
#         bill = units * 1.50
#     elif units <= 200:
#         bill = (100 * 1.50) + ((units - 100) * 2.50)
#     elif units <= 300:
#         bill = (100 * 1.50) + (100 * 2.50) + ((units - 200) * 4.00)
#     else:
#         bill = (100 * 1.50) + (100 * 2.50) + (100 * 4.00) + ((units - 300) * 5.00)

#     print(f"Total electricity bill for {units} units is: Rs. {bill:.2f}")


# # ==============================================================================
# # 18. Calculate income tax based on income slabs.

# # ==============================================================================
# def calculate_income_tax():
#     income = float(input("Enter annual taxable income (in Rs.): "))

#     if income < 0:
#         print("Invalid income! Income cannot be negative.")
#         return

#     if income <= 250000:
#         tax = 0.0
#     elif income <= 500000:
#         tax = (income - 250000) * 0.05
#     elif income <= 1000000:
#         tax = 12500 + ((income - 500000) * 0.20)
#     else:
#         tax = 112500 + ((income - 1000000) * 0.30)

#     print(f"Total Income Tax payable on Rs. {income:,.2f} is: Rs. {tax:,.2f}")


# # ==============================================================================
# # 19. Check if a student passes (minimum 35 marks in each subject).
# # ==============================================================================
# def check_student_pass_fail():
#     sub1 = float(input("Enter marks for Subject 1: "))
#     sub2 = float(input("Enter marks for Subject 2: "))
#     sub3 = float(input("Enter marks for Subject 3: "))

#     if sub1 < 0 or sub1 > 100 or sub2 < 0 or sub2 > 100 or sub3 < 0 or sub3 > 100:
#         print("Invalid marks entered! Marks should be between 0 and 100.")
#     elif sub1 >= 35 and sub2 >= 35 and sub3 >= 35:
#         avg = (sub1 + sub2 + sub3) / 3
#         print(f"Result: PASSED! Average Marks: {avg:.2f}")
#     else:
#         print("Result: FAILED! (Must score at least 35 in all subjects)")


# # ==============================================================================
# # 20. Find whether a number is within a given range.
# # ==============================================================================
# def check_number_in_range():
#     num = float(input("Enter the number to check: "))
#     low = float(input("Enter lower bound of range: "))
#     high = float(input("Enter upper bound of range: "))

#     if low > high:
#         low, high = high, low

#     if low <= num <= high:
#         print(f"{num} is within the range [{low}, {high}].")
#     else:
#         print(f"{num} is OUTSIDE the range [{low}, {high}].")


# # ==============================================================================
# # 21. Build a simple calculator using if-elif-else (+, -, *, /).
# # ==============================================================================
# def simple_calculator():
#     num1 = float(input("Enter first number: "))
#     op = input("Enter operator (+, -, *, /): ").strip()
#     num2 = float(input("Enter second number: "))

#     if op == '+':
#         print(f"Result: {num1} + {num2} = {num1 + num2}")
#     elif op == '-':
#         print(f"Result: {num1} - {num2} = {num1 - num2}")
#     elif op == '*':
#         print(f"Result: {num1} * {num2} = {num1 * num2}")
#     elif op == '/':
#         if num2 == 0:
#             print("Error: Division by zero is undefined.")
#         else:
#             print(f"Result: {num1} / {num2} = {num1 / num2}")
#     else:
#         print("Invalid operator! Please use +, -, *, or /.")


# # ==============================================================================
# # 22. Check if a year is a century leap year.

# # ==============================================================================
# def check_century_leap_year():
#     year = int(input("Enter a year: "))

#     if year % 100 != 0:
#         print(f"{year} is NOT a century year (does not end in '00').")
#     elif year % 400 == 0:
#         print(f"{year} IS a Century Leap Year.")
#     else:
#         print(f"{year} is a Century year, but NOT a Leap Year.")


# # ==============================================================================
# # 23. Determine the season based on the month number.

# # ==============================================================================
# def find_season_by_month():
#     month = int(input("Enter month number (1 - 12): "))

#     if month in (12, 1, 2):
#         print("Season: Winter")
#     elif month in (3, 4, 5):
#         print("Season: Spring")
#     elif month in (6, 7, 8):
#         print("Season: Summer")
#     elif month in (9, 10, 11):
#         print("Season: Autumn / Fall")
#     else:
#         print("Invalid month number! Please enter an integer from 1 to 12.")


# # ==============================================================================
# # 24. Find the number of days in a month.
# # ==============================================================================
# def find_days_in_month():
#     month = int(input("Enter month number (1 - 12): "))

#     if month < 1 or month > 12:
#         print("Invalid month number! Must be between 1 and 12.")
#     elif month in (1, 3, 5, 7, 8, 10, 12):
#         print("This month has 31 days.")
#     elif month in (4, 6, 9, 11):
#         print("This month has 30 days.")
#     elif month == 2:
#         year = int(input("Enter year (to check for leap year): "))
#         if (year % 4 == 0 and year % 100 != 0) or (year % 400 == 0):
#             print(f"February {year} has 29 days (Leap Year).")
#         else:
#             print(f"February {year} has 28 days (Non-Leap Year).")


# # ==============================================================================
# # 25. Check whether a password meets minimum conditions
# # ==============================================================================
# def validate_password():
#     password = input("Enter password to test: ")

#     has_digit = any(ch.isdigit() for ch in password)
#     has_upper = any(ch.isupper() for ch in password)
#     has_lower = any(ch.islower() for ch in password)

#     if len(password) < 8:
#         print("Password rejected: Must be at least 8 characters long.")
#     elif not has_digit:
#         print("Password rejected: Must contain at least one numeric digit (0-9).")
#     elif not has_upper:
#         print("Password rejected: Must contain at least one uppercase letter (A-Z).")
#     elif not has_lower:
#         print("Password rejected: Must contain at least one lowercase letter (a-z).")
#     else:
#         print("Password accepted: Meets all security criteria!")


# # ==============================================================================
# # 26. Determine ticket price based on age category.

# # ==============================================================================
# def find_ticket_price():
#     age = int(input("Enter person's age: "))

#     if age < 0:
#         print("Invalid age entered.")
#     elif age < 5:
#         print("Category: Infant/Toddler -> Ticket is Free (Rs. 0)")
#     elif age <= 12:
#         print("Category: Child (5-12 years) -> Ticket Price: Rs. 50")
#     elif age <= 59:
#         print("Category: Adult (13-59 years) -> Ticket Price: Rs. 100")
#     else:
#         print("Category: Senior Citizen (60+ years) -> Ticket Price: Rs. 70 (Discounted)")


# # ==============================================================================
# # 27. Calculate discount based on purchase amount.

# # ==============================================================================
# def calculate_discount():
#     amount = float(input("Enter total purchase amount (in Rs.): "))

#     if amount < 0:
#         print("Purchase amount cannot be negative.")
#         return

#     if amount < 1000:
#         discount_percent = 0
#     elif amount < 5000:
#         discount_percent = 10
#     elif amount < 10000:
#         discount_percent = 20
#     else:
#         discount_percent = 30

#     discount_val = (discount_percent / 100) * amount
#     net_payable = amount - discount_val

#     print(f"Original Amount : Rs. {amount:.2f}")
#     print(f"Discount Rate   : {discount_percent}% (Rs. {discount_val:.2f})")
#     print(f"Net Payable     : Rs. {net_payable:.2f}")


# # ==============================================================================
# # 28. Check if a person is eligible for a driving license
# ============================================
# def check_driving_license_eligibility():
#     age = int(input("Enter applicant's age: "))
#     eyesight = input("Did applicant pass the eyesight test? (yes/no): ").strip().lower()

#     if age < 0:
#         print("Invalid age entered.")
#     elif age < 18 and eyesight == 'yes':
#         print(f"Ineligible: Applicant must be at least 18 years old (current age: {age}).")
#     elif age >= 18 and eyesight != 'yes':
#         print("Ineligible: Applicant must pass the eyesight test.")
#     elif age >= 18 and eyesight == 'yes':
#         print("Eligible: Applicant qualifies for a driving license!")
#     else:
#         print("Ineligible: Applicant fails both age requirement and eyesight test.")


# # ==============================================================================
# # 29. Create a login system with username and password validation.
# # ==============================================================================
# def login_system():
#     CORRECT_USER = "admin"
#     CORRECT_PASS = "admin123"

#     entered_user = input("Enter username: ").strip()
#     entered_pass = input("Enter password: ").strip()

#     if entered_user == CORRECT_USER and entered_pass == CORRECT_PASS:
#         print("Login Successful! Welcome, Administrator.")
#     elif entered_user != CORRECT_USER and entered_pass != CORRECT_PASS:
#         print("Login Failed: Incorrect username and password.")
#     elif entered_user != CORRECT_USER:
#         print("Login Failed: Username does not exist.")
#     else:
#         print("Login Failed: Incorrect password.")


# # ==============================================================================
# # 30. Create a menu-driven program using if-elif-else with options:

# # ==============================================================================
# def menu_driven_calculator():
#     while True:
#         print("\n============= MENU =============")
#         print("1. Addition")
#         print("2. Subtraction")
#         print("3. Multiplication")
#         print("4. Division")
#         print("5. Exit")
#         print("================================")

#         choice = input("Enter your choice (1-5): ").strip()

#         if choice == '1':
#             n1 = float(input("Enter first number: "))
#             n2 = float(input("Enter second number: "))
#             print(f"Result: {n1} + {n2} = {n1 + n2}")
#         elif choice == '2':
#             n1 = float(input("Enter first number: "))
#             n2 = float(input("Enter second number: "))
#             print(f"Result: {n1} - {n2} = {n1 - n2}")
#         elif choice == '3':
#             n1 = float(input("Enter first number: "))
#             n2 = float(input("Enter second number: "))
#             print(f"Result: {n1} * {n2} = {n1 * n2}")
#         elif choice == '4':
#             n1 = float(input("Enter first number: "))
#             n2 = float(input("Enter second number: "))
#             if n2 == 0:
#                 print("Error: Cannot divide by zero!")
#             else:
#                 print(f"Result: {n1} / {n2} = {n1 / n2}")
#         elif choice == '5':
#             print("Exiting Menu-Driven Program. Goodbye!")
#             break
#         else:
#             print("Invalid Choice! Please enter a number between 1 and 5.")

