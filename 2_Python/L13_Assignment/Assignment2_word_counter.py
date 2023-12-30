print("==================================================================")
print("-----------------------Word Counter App---------------------------")
print("==================================================================\n")

print("                       1. Type a Paragraph")
print("                       2. Insert a File\n")

choice = int(input("Enter Your Choice(1/2): "))

if choice == 1:
    string = input("Type Here: ")
    string = string.strip()
    string = string.split(" ")
    # print(string)
    print("Number of Word: {}".format(len(string) - string.count('') - string.count('.')))

elif choice == 2:
    path = input("     Insert file name: ")
    path = path.strip()
    if '.txt' not in path:
        path = path + ".txt"
    # print(path)

    import os
    if os.path.isfile(path):
        with open(path, 'r') as file:
            all_txt = file.read()
            all_txt = all_txt.strip()
            all_txt = all_txt.split(" ")
            # print(all_txt)
            print("Number of word: {}".format(len(all_txt) - all_txt.count('') - all_txt.count('.')))

    else:
        print("This file is not exist!!!")


else:
    print("Invalid Choice!!")
