def find_max():
    numbers = [2, 24, 12, -3, 88]

    if not numbers:
        print("List is empty.")
        return None

    max_num = numbers[0]
    max_index = 0
    
    for i in range(1, len(numbers)):
        if numbers[i] > max_num:
            max_num = numbers[i]
            max_index = i

    return max_num, max_index

print(find_max())