
def odd_or_even(arr):
    result = sum(arr)
    if result % 2 == 0 or result == 0:
        return "even"
    else:
        return "odd"

random_list = [1023, 1, 2]
print(odd_or_even(random_list))