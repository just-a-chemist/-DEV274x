def str_replace(int_list,index):
    while True:
        index = input("Which index would you like to change.")
        if index.isalpha() is True:
            print("Enter int")
            break
        index = int(index)
        usr = input("Enter a string or press q to exit ")
        if usr.lower() == "q":
            break
        elif usr.isdigit(): 
            usr = int(usr)
            if usr > 10:
                int_list[index] = "large"
            else:
                 int_list[index] = "small"
        else: int_list[index] = usr
    return int_list
    print(int_list)
int_list = [1,2,3,4,5,6,7,8,9,0,10,12,15,16]

str_replace(int_list,index)
