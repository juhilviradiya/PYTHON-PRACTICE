# ==========================================
# Python Lambda Functions - Basic Examples
# ==========================================

# Example 1: Square of a number
square = lambda number: number ** 2
print("Square:", square(5))


# Example 2: Add two numbers
add = lambda first, second: first + second
print("Addition:", add(10, 20))


# Example 3: Check even or odd
check_even = lambda number: "Even" if number % 2 == 0 else "Odd"
print("Number Check:", check_even(8))


# Example 4: Find the greater number
greater = lambda first, second: first if first > second else second
print("Greater Number:", greater(15, 25))


# Example 5: Convert text to uppercase
uppercase = lambda text: text.upper()
print("Uppercase:", uppercase("python lambda"))


# Example 6: Calculate employee bonus
calculate_bonus = lambda salary: salary * 0.10
print("Employee Bonus:", calculate_bonus(30000))


# Example 7: Calculate product price after discount
discounted_price = lambda price, discount: price - (price * discount / 100)
print("Final Price:", discounted_price(2000, 15))


