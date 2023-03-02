#create variables
num_list = []

#get input from the user
while True:
    num_str = input("Enter a series of single-digit numbers with nothing separating them : ")
    if num_str.isdigit():
        break
    else:
        print("Invalid data !!. Please enter the data again...\n")
        
#loop throught each byte to get the numbers into a list
num_list = [int(num) for num in num_str]

#display output
print("The sum of all the single-digit numbers entered is ",sum(num_list))
