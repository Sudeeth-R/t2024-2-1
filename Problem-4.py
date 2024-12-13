def count_multiples(input_list):
    result = {i: 0 for i in range(1, 10)}  
    for num in input_list:
        for i in range(1, 10):
            if num % i == 0:
                result[i] += 1  
    return result


input_list = list(map(int, input("Enter numbers separated by spaces: ").split()))


print(count_multiples(input_list))