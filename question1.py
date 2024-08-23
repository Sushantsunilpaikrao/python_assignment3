def sum_of_even_numbers(numbers):
    total = 0
    for num in numbers:
        if num % 2 == 0:
            total += num
    return total

numbers = [1, 2, 3, 4, 5, 6]
print(sum_of_even_numbers(numbers))  # Output: 12
