arr = [1, 2, 3,4,5]

total_sum = sum(arr)
result = 0

for num in arr:
    total_sum -= num
    print(total_sum)
    result += num * total_sum

print("Sum of product of all pairs:", result)


# Example usage
