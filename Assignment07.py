# ------------------------------------------------- #
# Title: Assignment 07
# Description: Pickles and Exception handling
# ChangeLog: (Who, When, What)
# Gail Provancha, August 21, 2023,Created Script
# ------------------------------------------------- #
import pickle  # This imports code from another code file

# Data -------------------------------------------- #
file_name_str = "example.dat"  # The name of the binary file
data_lst = []  # list where user inputted values are saved
choice_str = ""  # Captures the user option selection

# Processing -------------------------------------- #


def save_data_to_file(file_name, list_of_data):
    with open(file_name, "ab") as file:  # Opens binary file
        pickle.dump(list_of_data, file)  # writes to file
        file.close()  # close the file


def print_data_from_file(file_name):
    with open(file_name, "rb") as file:  # read from binary file
        while True:  # loop through the items in the file until all are printed
            try:
                list_of_data = pickle.load(file)  # load from binary file into list of data
                print(list_of_data)
            except EOFError:  # when process runs out of items to print "input" the loop ends
                break
        file.close()  # close file

# Presentation ------------------------------------ #


while (True):
    choice_str = input("Enter '1' to add new data, Enter '2' when entries are complete: ")
    print()  # Add an extra line for looks
    if choice_str.strip() == '1':  # Add a new Task
        try:
            number_int = int(input("Enter a number: "))
        except ValueError:
            print("This is not a number, try again")
            try:
                number_int = int(input("Enter a number: "))
            except ValueError:  # if still not entering a number, ends the program
                print("Still not a correct entry.  Ending the program")
                print_data_from_file(file_name=file_name_str)  # print the information from the binary file
                break
            except Exception as error:
                print("There was an error, ending program")
                print(error)
                break
        try:
            name_str = str(input("Enter a name: ")).strip()
        except Exception as error:
            print("There was an error")
            print(error)
        else:
            print()  # Add an extra line for looks
            data_lst = [number_int, name_str]
            save_data_to_file(file_name=file_name_str, list_of_data=data_lst)  # save the data to a binary file
            continue
    elif choice_str == '2':  # Exit Program and print items in file
        print("Current data in file", "'file_name_str'")
        print()  # Add an extra line for looks
        print_data_from_file(file_name=file_name_str)  # print the information from the binary file
        print()  # Add an extra line for looks
        print("Goodbye")
        break  # by exiting loop
