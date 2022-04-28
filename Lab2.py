
def display_main_menu():
    print("Enter some numbers separated by commas (e.g. 5,67, 32")

def get_user_input():
    user_str = input("Enter number:")
    numlist = user_str.split(",")
    print(numlist)
    print(user_str)
    floats = []
    for element in numlist:
        floats.append(float(element))
    print(floats)
    return floats
def calc_average_temperature(num_list):
    Sum=sum(num_list)
    print(Sum)
    len(num_list)
    Average=Sum/len(num_list)
    print(Average)

def calc_min_max_temperature(num_list):
    maximum = max(num_list)
    print(maximum)
    minimum = min(num_list)
    print(minimum)
def main():
    print("ET0735 (DevOps for AIoT) - Lab 2 - Introduction to Python")
    display_main_menu()
    num_list = get_user_input()
    calc_average_temperature(num_list)
    calc_min_max_temperature(num_list)

if __name__ == "__main__":
    main()

