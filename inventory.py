# Import tabulate
from tabulate import tabulate

# Create empty lists
list_of_data = []
list_of_data_with_value = []
header_list = []
objects_list = []

# Create class Shoe
class Shoe:

    # Initialise objects
    def __init__(self, country, code, product, cost, quantity):
        self.country = country
        self.code = code
        self.product = product
        self.cost = cost
        self.quantity = quantity

    # Create a method to  read data from the text file
    @staticmethod
    def read_data():
        with open("inventory.txt", "r+") as inventory_file:
            try:
                for line in inventory_file:
                    line = line.strip()
                    line = line.split(",")
                    list_of_data.append(line)
            except:
                print("There was an error, please try again")

    # Create method to print all the objects
    def print_all(self):
        print("\n")
        print(self.country, self.code, self.product, self.cost, self.quantity)

    # Create method to print the value per item 
    def value_per_item():
        Shoe.read_data()
        for item_quantity in list_of_data:
            if item_quantity[4] == "Quantity":
                new_header = "Value"
                list_line = item_quantity[0], item_quantity[1], item_quantity[2], item_quantity[3], item_quantity[4], new_header
                header_list.append(list_line)
            else:    
                quantity_int = item_quantity[4]
                value_item = int(quantity_int) * float(item_quantity[3])
                list_line = item_quantity[0], item_quantity[1], item_quantity[2], "R" + str(item_quantity[3]), item_quantity[4], "R" + str(value_item)
                list_of_data_with_value.append(list_line)

# Create 5 objects
obj_shoe1 = Shoe("Italy","ITA1234","Ace Marks","1200","12")
obj_shoe2 = Shoe("Italy","ITA2234","Antonio Meccariello","4000","20")
obj_shoe3 = Shoe("Italy","ITA3334","Paolo Scafora","2300","13")
obj_shoe4 = Shoe("Italy","ITA4434","Aurélien","3200","5")
obj_shoe5 = Shoe("Italy","ITA3455","Santoni","1100","3")       

objects_list = obj_shoe1,obj_shoe2,obj_shoe3,obj_shoe4,obj_shoe5

# Menu to select logic
menu = input("\nPlease enter what you would like to do: \nP\t\tWill print all information\nF\t\tWill find items by code\nLQ\t\tWill restock the lowest item\nHQ\t\tWill put the highest stocked item on sale\nV\t\tWill print items with the value added\nEnter Here: ").lower()

# Print all the objects
if menu == "p":
    Shoe.read_data()
    for items in list_of_data:
        one_instance = Shoe(items[0], items[1], items[2], items[3], items[4])
        Shoe.print_all(one_instance)
    Shoe.print_all(obj_shoe1)
    Shoe.print_all(obj_shoe2)
    Shoe.print_all(obj_shoe3)
    Shoe.print_all(obj_shoe4)
    Shoe.print_all(obj_shoe5)

# search text file for object using a code
elif menu == "f":
    look_for = input("Please enter the code of the item that you are looking for: ")
    Shoe.read_data()
    for items in list_of_data:
        if look_for == items[1]:
            find_instance = Shoe(items[0], items[1], items[2], items[3], items[4])
    Shoe.print_all(find_instance)

# Get the lowest item and restock it
elif menu == "lq":
    quantity_list = []
    Shoe.read_data()
    for quantity_item in list_of_data:
        try:
            quantity_list.append(int(quantity_item[4]))
        except:
            continue
    quantity_list.sort()

    quantity_number = str(quantity_list[0])

    for quantity_inspector in list_of_data:
        try:
            if quantity_inspector[4] == quantity_number:
                instance_lowest_quantity = Shoe(quantity_inspector[0], quantity_inspector[1], quantity_inspector[2],quantity_inspector[3], quantity_inspector[4])
                Shoe.print_all(instance_lowest_quantity)
                print("This item will be restocked by 5 units")
                quantity_inspector[4] = int(quantity_inspector[4]) + 5
                instance_lowest_quantity = Shoe(quantity_inspector[0], quantity_inspector[1], quantity_inspector[2],quantity_inspector[3], str(quantity_inspector[4]))
                Shoe.print_all(instance_lowest_quantity)
        except:
            continue

# Get the highest item and put it up for sale
elif menu == "hq":

    Shoe.read_data()
    quantity_list_highest = []
    for quantity in list_of_data:
        try:
            quantity_list_highest.append(int(quantity[4]))
        except:
            continue
    quantity_list_highest.sort(reverse=True)

    quantity_number_highest = str(quantity_list_highest[0])

    for item_quantity_highest in list_of_data:
        try:
            if item_quantity_highest[4] == quantity_number_highest:
                highest_item = Shoe(item_quantity_highest[0], item_quantity_highest[1], item_quantity_highest[2],item_quantity_highest[3], item_quantity_highest[4])
                print("This item will be put on sale")
                Shoe.print_all(highest_item)
        except:
            continue

# Print the value in a table form
elif menu == "v":
    Shoe.value_per_item()
    header_for_table = header_list[0][0],header_list[0][1],header_list[0][2],header_list[0][3],header_list[0][4],header_list[0][5]
    print('\n' + tabulate(list_of_data_with_value,header_for_table))

