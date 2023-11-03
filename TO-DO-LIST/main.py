arr = []

def display(arr):
    for i in range(len(arr)):
        print(str(i+1) + ": " +  arr[i])

def create():
    print()
    ans = input("Enter your task: ")
    print()
    arr.append(ans)
    display(arr)
    print()
    print("Your task has been successfully added to the list!")
    
def update():
    print()
    print("Please Select the task number you want to update from the list.")
    print()
    display(arr)
    print()
    ans = input("Enter task number you want to update: ")
    new = input("Enter the changes: ")
    arr[int(ans)-1] = new
    print()
    display(arr)
    print()
    print("Your task is updated successfully!")

def delete():
    print()
    print("Please Select the task number you want to Delete from the list.")
    print()
    display(arr)
    print()
    ans = input("Enter task number you want to delete: ")
    arr.pop(int(ans)-1)
    print()
    display(arr)
    print()
    print("Your task is deleted successfully!")

print("Welcome To your TO-DO-LIST!!")
print()

def welcomeMsg():
    print("Availaible Operation")
    print("0: Exit")
    print("1: Create")
    print("2: Update")
    print("3: Delete")
    print("4: Clear List")

welcomeMsg()

while True:
    
    print()
    
    opt = input("Select a number from above options: ")

    if opt == '0' or opt == 'Exit' or opt == 'exit':
        print()
        print("Thank you for using TO-DO-LIST!!")
        break
    elif opt == '1' or opt == 'Create' or opt == 'create':
        create()
    elif opt == '2' or opt == 'Update' or opt == 'update':
        update()
    elif opt == '3' or opt == 'Delete' or opt == 'delete':
        delete()
    elif opt == '4' or opt == 'Clear List' or opt == 'Clear list' or opt == "clear list":
        arr = []
    elif opt == '5' or opt == 'Display' or opt == 'display':
        print()
        display(arr)
    else:
        print("Enter a valid input! Recommeded to select from the below options.")
        print()
        welcomeMsg()