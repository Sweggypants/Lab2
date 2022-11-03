def get_user_input():
    x = input("Enter some numbers ")
    strings = x.split(",")
    numbers = [float(i) for i in strings]
    print(numbers)
    calc_average_temperature(numbers)
    calc_min_max_temperature(numbers)

def calc_average_temperature(numbers):
    average = sum(numbers)/len(numbers)
    print("Average Temperature = " + str(average))

def calc_min_max_temperature(numbers):
    min1 = min(numbers)
    print("Min = " + str(min1))
    max1 = max(numbers)
    print("Max = " + str(max1))

get_user_input()