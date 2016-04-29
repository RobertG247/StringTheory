def get_small(array):
    tiny = array[0]
    length = len(array)
    for x in range(0,length):
        if tiny > array[x]:
            tiny = array[x]
    return tiny


def get_big(array):
    huge = array[0]
    length = len(array)
    for x in range(0,length):
        if huge < array[x]:
            huge = array[x]
    return huge


def get_small_big():
    print("")
    print("The Biggest vs Smallest Comparison Game")
    print("")
    my_list = []
    valid_input = False
    while valid_input == False:
        try:
            array_length = int(input("How many numbers would you like to compare for this test? "))
            if array_length <= 0:
                print("Enter a real number higher than zero. ")
            valid_input = True
        except:
            print("We only take real numbers!!.")
    valid_input = False
    while valid_input == False:
        try:
            for x in range(0, array_length):
                my_list.append(int(input("Which number would you like to add now? ")))
                valid_input = True
        except:
            print("Please enter a real number!")

    smallest = get_small(my_list)
    print(smallest)
    biggest = get_big(my_list)
    print(biggest)


get_small_big()