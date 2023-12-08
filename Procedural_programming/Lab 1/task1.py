numbers = [2, -93, -2, 8, None, -44, -1, -85, -14, 90, -22, -90, -100, -8, 38, -92, -45, 67, 53, 25]

none_index = numbers.index(None)
sum_ = sum(numbers[:none_index]) + sum(numbers[none_index + 1:])
avg = sum_ / len(numbers)
numbers[none_index] = avg

print("Измененный список:", numbers)
