# initialize an empty list
my_list = []

while True:
    print("Please select an option:")
    print("1. Create item")
    print("2. Read items")
    print("3. Update item")
    print("4. Delete item")
    print("5. Exit")

    choice = int(input())

    if choice == 1:
        item = input("Enter item to add: ")
        my_list.append(item)
        print("Item added successfully!")
    elif choice == 2:
        if len(my_list) == 0:
            print("List is empty")
        else:
            print("List items:")
            for item in my_list:
                print(item)
    elif choice == 3:
        if len(my_list) == 0:
            print("List is empty")
        else:
            index = int(input("Enter index of item to update: "))
            new_item = input("Enter new item: ")
            my_list[index] = new_item
            print("Item updated successfully!")
    elif choice == 4:
        if len(my_list) == 0:
            print("List is empty")
        else:
            index = int(input("Enter index of item to delete: "))
            deleted_item = my_list.pop(index)
            print(f"Item '{deleted_item}' deleted successfully!")
    elif choice == 5:
        print("Exiting program...")
        break
    else:
        print("Invalid choice")
