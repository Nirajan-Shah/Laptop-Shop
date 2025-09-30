from Database import Database                            # Importing classes from the necessary modules
from InvoiceToCustomer import InvoiceToCustomer
from InvoiceToManufacturer import InvoiceToManufacturer

database = Database()
database.read_database()                                 # Reading the database once to store values into the dictionary

class UserInterface(InvoiceToCustomer, InvoiceToManufacturer):

    def ask_user_info(self):
        """Asks values about the user before starting the main loop itself so that these values may later be set at
        MAKE ALL INQUIRIES TO section of the bill.
        """

        class InvalidName(Exception):  # Defining exceptions.
            pass

        class InvalidPhoneNumber(Exception):
            pass

        while True:
            try:
                name_of_user = input("            Enter your name. ")
                self.set_name_of_user(name_of_user)
                if name_of_user.isalpha() == False:     # Checking to see if the name given is valid.
                    raise InvalidName
            except InvalidName:
                print("            Please enter a valid name.")
                print("\n")
                continue       # Reruns the loop if an exception is raised.
            else:
                break

        while True:
            try:
                phone_number_of_user = input("            Enter your phone number. ")
                self.set_phone_number_of_user(phone_number_of_user)
                if not phone_number_of_user.isdigit():
                    raise InvalidPhoneNumber
            except InvalidPhoneNumber:
                print("            Please enter a valid phone number.")
                print("\n")
                continue
            else:
                break

        

    def display_database(self):
        """Displays the database in the console."""
        file = open("Database.txt", "r")
        lines = file.readlines()
        print(''.join(lines))
        file.close()

    def store_user_info(self):
        name_of_user = input("            Enter your name. ")
        phone_number_of_user = input("            Enter your phone number. ")
        email_of_user = input("            Enter your email. ")

        self.set_name_of_user(name_of_user)
        self.set_phone_number_of_user(phone_number_of_user)
        self.set_email_of_user(email_of_user)

    def start(self):
        """This is the main loop itself and this is where the text based user interface is run.
        The administrator is able to manage the database i.e., add, remove and view entries and generate invoice to
        both customer and to manufacturer. """

        self.read_database()   #Reads the database and stores the read value into the main dictionary.

        while True:
            print('            +=============================================================================================================+')
            print('            |                                                                                                             |')
            print('            |                                  Welcome to the shop management portal                                      |')
            print('            |                                      Reliability is our objective.                                          |')
            print('            |                                                                                                             |')
            print('            |  Bhatbhateni, Kathmandu                                                                Phone No: 98xxxxxxxx |')
            print('            +==============+==============================================================================================+')
            print('            |              |                                                                                              |')
            print('            |    Option    |                                     Task carried out                                         |')
            print('            |              |                                                                                              |')
            print('            +--------------+----------------------------------------------------------------------------------------------+')
            print('            |      1       |    Enter 1 to sell a laptop to the customer.                                                 |')
            print('            |              |                                                                                              |')
            print('            +--------------+----------------------------------------------------------------------------------------------+')
            print('            |      2       |    Enter 2 to purchase from manufacturer.                                                    |')
            print('            |              |                                                                                              |')
            print('            +--------------+----------------------------------------------------------------------------------------------+')
            print('            |      3       |    Enter 3 to manage the database.                                                           |')
            print('            |              |                                                                                              |')
            print('            +--------------+----------------------------------------------------------------------------------------------+')
            print('            |      4       |    Enter 4 to exit.                                                                          |')
            print('            |              |                                                                                              |')
            print('            +--------------+----------------------------------------------------------------------------------------------+')
            print("\n")

            try:
                option_entered = int(input("            Enter your choice. "))
                print("\n")

            except ValueError:
                print("            Please enter a number.")
                print("\n")
                continue

            class InvalidName(Exception):
                pass

            class InvalidAddress(Exception):
                pass

            class InvalidEmail(Exception):
                pass

            class InvalidPhoneNumber(Exception):
                pass

            if option_entered == 1:
                while True:
                    print('            +=============================================================================================================+')
                    print('            |                                                                                                             |')
                    print('            |                                  Welcome to the selling portal.                                             |')
                    print('            |                                   Reliability is our objective.                                             |')
                    print('            |                                                                                                             |')
                    print('            |  Bhatbhateni, Kathmandu                                                                Phone No: 98xxxxxxxx |')
                    print('            +==============+==============================================================================================+')
                    print('            |              |                                                                                              |')
                    print('            |    Option    |                                     Task carried out                                         |')
                    print('            |              |                                                                                              |')
                    print('            +--------------+----------------------------------------------------------------------------------------------+')
                    print('            |      1       |    Enter 1 to view the database.                                                             |')
                    print('            |              |                                                                                              |')
                    print('            +--------------+----------------------------------------------------------------------------------------------+')
                    print('            |      2       |    Enter 2 to enter customer details and generate bill.                                      |')
                    print('            |              |                                                                                              |')
                    print('            +--------------+----------------------------------------------------------------------------------------------+')
                    print('            |      3       |    Enter 3 to go one step back.                                                              |')
                    print('            |              |                                                                                              |')
                    print('            +--------------+----------------------------------------------------------------------------------------------+')
                    print("\n")

                    try:
                        option_entered = int(input("            Enter your choice. ")) # Throws exception if values which are not numbers are entered.
                        print("\n")

                        assert int(option_entered) >= 1 and int(option_entered) <= 3  # Assert instead of an extra while loop.

                    except ValueError:                                                # Only catches value error
                        print("            Please enter a number.")
                        print("\n")
                        continue
                    except AssertionError:                                            # Only catches assertion error
                        print("            Please enter a valid option.")
                        print("\n")
                        continue

                    while True:
                        if option_entered == 1:
                            self.display_database()                                                 # Displays database
                            print("\n")
                            input("            Enter any key to continue. ")
                            print("\n")
                            break

                        elif option_entered == 2:
                            ID_and_quantity_dictionary = {}     # This dictionary is forwarded as an argument in a function
                            ID_list = []
                            quantity_list = []

                            while True:
                                try:
                                    name_of_customer = input("            Enter the name of the customer. ")
                                    if not name_of_customer:
                                        raise InvalidName         # Raising exception intentionally if the name of customer is empty
                                except InvalidName:
                                    print("            Please enter a valid name.")
                                    print("\n")
                                    continue
                                else:
                                    break

                                    
                            while True:
                                try:
                                    address_of_customer = input("            Enter the address of the customer. ")
                                    if not address_of_customer:
                                        raise InvalidAddress
                                except InvalidAddress:
                                    print("            Please enter a valid address.")
                                    print("\n")
                                    continue
                                else:
                                    break

                            while True:
                                try:
                                    email_of_customer = input("            Enter the email of the customer. ")

                                    if "@" not in email_of_customer or ".com" not in email_of_customer:   # An email has to have both @ and .com as its value.
                                        raise InvalidEmail
                                except InvalidEmail:
                                    print("            Please enter a valid email address.")
                                    print("\n")
                                    continue
                                else:
                                    break

                            while True:
                                try:
                                    phone_number_of_customer = input("            Enter the phone number of the customer. ")  # A phone number consists of only digits in this case.

                                    if not phone_number_of_customer.isdigit():
                                        raise InvalidPhoneNumber
                                except InvalidPhoneNumber:
                                    print("            Please enter a valid phone number.")
                                    print("\n")
                                    continue
                                else:
                                    break

                            self.display_database()                 # Prints the database.

                            while True:
                                print("\n")
                                while True:
                                    try:
                                        ID_of_laptop_for_sale = input("            Enter the ID of the laptop that the customer wants to buy. ")
                                        int(ID_of_laptop_for_sale)
                                    except ValueError:
                                        print("            Please enter a valid Id.")
                                        print("\n")
                                        continue
                                    else:
                                        break

                                ID_list.append(ID_of_laptop_for_sale)
                                while int(ID_of_laptop_for_sale) < 1 or int(ID_of_laptop_for_sale) > self.get_count():
                                    ID_list.remove(ID_of_laptop_for_sale)
                                    print("            Please enter a valid ID.")
                                    print("\n")
                                    while True:
                                        try:
                                            ID_of_laptop_for_sale = input(
                                                "            Enter the ID of the laptop that the customer wants to buy. ")
                                            int(ID_of_laptop_for_sale)
                                        except ValueError:
                                            print("            Please enter a valid Id.")
                                            print("\n")
                                            continue
                                        else:
                                            break
                                    ID_list.append(ID_of_laptop_for_sale)

                                    if int(ID_of_laptop_for_sale) < 1 or int(ID_of_laptop_for_sale) > self.get_count():    # Perhaps, assert could be used here.
                                        continue
                                    else:
                                        break

                                while True:

                                    while True:
                                        try:
                                            quantity_of_laptop = input(f"            Enter the quantity of the laptop of the ID {ID_of_laptop_for_sale} that the customer wants to buy. ")
                                            int(quantity_of_laptop)
                                        except ValueError:
                                            print("Please enter a valid quantity.")
                                            continue
                                        else:
                                            break

                                    quantity_list.append(quantity_of_laptop)                # Appends the quantity into a list.
                                        
                                    while int(quantity_of_laptop) < 1 or int(quantity_of_laptop) > int(self.get_available_quantity(int(ID_of_laptop_for_sale))):
                                        quantity_list.remove(quantity_of_laptop)
                                        print("            Please enter a valid quantity")
                                        print("\n")
                                        while True:
                                            try:
                                                quantity_of_laptop = input(
                                                    f"            Enter the quantity of the laptop of the ID {ID_of_laptop_for_sale} that the customer wants to buy. ")
                                                int(quantity_of_laptop)
                                            except ValueError:
                                                print("Please enter a valid quantity.")
                                                continue
                                            else:
                                                break
                                        quantity_list.append(quantity_of_laptop)

                                        if int(quantity_of_laptop) < 1 or int(quantity_of_laptop) > int(self.get_available_quantity(int(ID_of_laptop_for_sale))):
                                            continue
                                        else:
                                            break
                                    break

                                while True:
                                    print("\n")
                                    print("            Has the customer ordered more laptops ?")
                                    is_continue = input("            Answer in yes or no. ")
                                    print("\n")

                                    is_continue = is_continue.lower()

                                    if is_continue == "yes":
                                        break
                                    elif is_continue != "yes" and is_continue != "no":
                                        print("            Dearest admin, please enter a valid answer. ")        # Having a little bit of fun with a sarcastic input message.
                                        print("\n")
                                        continue

                                    elif is_continue == "no":
                                        break

                                if is_continue == 'yes':
                                    continue
                                elif is_continue == 'no':
                                    break

                            for i in range(len(ID_list)):
                                ID_and_quantity_dictionary[ID_list[i]] = int(quantity_list[i])

                            total_quantity = 0

                            for each in ID_and_quantity_dictionary.values():
                                total_quantity += each

                            while True:
                                print("\n")
                                print("            Has the customer requested for shipment of goods ?")
                                is_ship = input("            Answer in yes or no. ")
                                is_ship = is_ship.lower()

                                if is_ship == 'yes':
                                    self.set_is_ship(True)
                                    shipping_price_for_each_ten_laptops = 50

                                    shipping_price = int(total_quantity / 10) * shipping_price_for_each_ten_laptops  # For each ten laptops, a cost of $50 is added to the total.
                                    final_shipping_price = shipping_price

                                    if self.get_address_of_customer().lower() != 'kathmandu':                        # If address is not kathmandu, an additional cost of $160 is added to the total.
                                        final_shipping_price = final_shipping_price + 160

                                    else:
                                        final_shipping_price = final_shipping_price + 100

                                    self.set_shipping_price('$' + "{0:.2f}".format(final_shipping_price))

                                elif is_ship != 'yes' and is_ship != 'no':
                                    print("Dearest admin, please enter a valid answer. ")
                                    print("\n")
                                    continue

                                elif is_ship == 'no':
                                    self.set_is_ship(False)
                                    break

                                break

                            self.set_ID_and_quantity_dictionary(**ID_and_quantity_dictionary)        # Send the ID and quantity dictionary as a keyword argument which was empty when it was first declared.
                            self.set_available_quantity(**ID_and_quantity_dictionary)                # Send the ID and quantity dictionary as a keyword arguemnt to send in id and respective quantities for updating the text file itself.
                            self.set_name_of_customer(name_of_customer)
                            self.set_phone_number_of_customer(phone_number_of_customer)
                            self.set_address_of_customer(address_of_customer)
                            self.set_email_of_customer(email_of_customer)

                            invoice = ''.join(self.generate_invoice_customer())                      # Print invoice.
                            print(invoice)

                            print("\n")

                            file = open("Sale " + f"{self.get_invoice_number_customer()}.txt", "w")  # Write invoice to a new text file.
                            file.write(invoice)
                            file.close()

                            self.read_database()                                                     # Read the notepad to update old data.

                            input('            Enter any key to continue.')
                            print("\n")

                            break

                        elif option_entered == 3:
                            break

                    if option_entered == 3:
                        break

            elif option_entered == 2:
                while True:
                    print('            +=============================================================================================================+')
                    print('            |                                                                                                             |')
                    print('            |                                  Welcome to the purchasing portal.                                          |')
                    print('            |                                    Reliability is our objective.                                            |')
                    print('            |                                                                                                             |')
                    print('            |  Bhatbhateni, Kathmandu                                                                Phone No: 98xxxxxxxx |')
                    print('            +==============+==============================================================================================+')
                    print('            |              |                                                                                              |')
                    print('            |    Option    |                                     Task carried out                                         |')
                    print('            |              |                                                                                              |')
                    print('            +--------------+----------------------------------------------------------------------------------------------+')
                    print('            |      1       |    Enter 1 to view the database.                                                             |')
                    print('            |              |                                                                                              |')
                    print('            +--------------+----------------------------------------------------------------------------------------------+')
                    print('            |      2       |    Enter 2 to enter manufacturer details and generate bill.                                  |')
                    print('            |              |                                                                                              |')
                    print('            +--------------+----------------------------------------------------------------------------------------------+')
                    print('            |      3       |    Enter 3 to go one step back.                                                              |')
                    print('            |              |                                                                                              |')
                    print('            +--------------+----------------------------------------------------------------------------------------------+')
                    print("\n")

                    try:
                        option_entered = int(input("            Enter your choice. "))
                        print("\n")

                        assert int(option_entered) >= 1 and int(option_entered) <= 3

                    except ValueError:
                        print("            Please enter a number.")
                        print("\n")
                        continue
                    except AssertionError:
                        print("            Please enter a valid option.")
                        print("\n")
                        continue

                    while True:
                        if option_entered == 1:
                            self.display_database()
                            print("\n")
                            input("            Enter any key to continue. ")
                            print("\n")
                            break

                        elif option_entered == 2:
                            ID_and_quantity_dictionary = {}
                            ID_list = []
                            quantity_list = []

                            while True:
                                try:
                                    name_of_manufacturer = input("            Enter the name of the manufacturer. ")
                                    if not name_of_manufacturer:
                                        raise InvalidName
                                except InvalidName:
                                    print("            Please enter a valid name.")
                                    print("\n")
                                    continue
                                else:
                                    break

                            while True:
                                try:
                                    address_of_manufacturer = input("            Enter the address of the manufacturer. ")
                                    if not address_of_manufacturer:
                                        raise InvalidAddress
                                except InvalidAddress:
                                    print("            Please enter a valid address.")
                                    print("\n")
                                    continue
                                else:
                                    break

                            while True:
                                try:
                                    email_of_manufacturer = input("            Enter the email of the manufacturer. ")

                                    if "@" not in email_of_manufacturer or ".com" not in email_of_manufacturer:
                                        raise InvalidEmail
                                except InvalidEmail:
                                    print("            Please enter a valid email address.")
                                    print("\n")
                                    continue
                                else:
                                    break

                            while True:
                                try:
                                    phone_number_of_manufacturer = input("            Enter the phone number of the manufacturer. ")

                                    if not phone_number_of_manufacturer.isdigit():
                                        raise InvalidPhoneNumber
                                except InvalidPhoneNumber:
                                    print("            Please enter a valid phone number.")
                                    print("\n")
                                    continue
                                else:
                                    break

                            self.display_database()

                            while True:
                                while True:
                                    try:
                                        ID_of_laptop_for_purchase = input("            Enter the ID of the laptop that you want to buy. ")
                                        int(ID_of_laptop_for_purchase)
                                        print("\n")
                                    except ValueError:
                                        print("            Please enter a valid Id.")
                                        print("\n")
                                        continue
                                    else:
                                        break

                                ID_list.append(ID_of_laptop_for_purchase)

                                while int(ID_of_laptop_for_purchase) < 1 or int(ID_of_laptop_for_purchase) > self.get_count():
                                    ID_list.remove(ID_of_laptop_for_purchase)
                                    print("            Please enter a valid ID.")
                                    print("\n")
                                    while True:
                                        try:
                                            ID_of_laptop_for_purchase = input(
                                                "            Enter the ID of the laptop that you want to buy. ")
                                            int(ID_of_laptop_for_purchase)
                                            print("\n")
                                        except ValueError:
                                            print("            Please enter a valid Id.")
                                            print("\n")
                                            continue
                                        else:
                                            break

                                    ID_list.append(ID_of_laptop_for_purchase)

                                    if int(ID_of_laptop_for_purchase) < 1 or int(ID_of_laptop_for_purchase) > self.get_count():
                                        continue
                                    else:
                                        break

                                while True:
                                    while True:
                                        try:
                                            quantity_of_laptop = input(f"            Enter the quantity of the laptop of the ID {ID_of_laptop_for_purchase} that you want to buy. ")
                                            int(quantity_of_laptop)
                                            quantity_list.append(quantity_of_laptop)
                                        except ValueError:
                                            print("            Please enter a valid quantity")
                                            print("\n")
                                            continue
                                        else:
                                            break

                                    while int(quantity_of_laptop) < 1:
                                        quantity_list.remove(quantity_of_laptop)

                                        print("            Please enter a valid quantity")
                                        print("\n")

                                        while True:
                                            try:
                                                quantity_of_laptop = input(
                                                    f"            Enter the quantity of the laptop of the ID {ID_of_laptop_for_purchase} that you want to buy. ")
                                                int(quantity_of_laptop)
                                                quantity_list.append(quantity_of_laptop)
                                            except ValueError:
                                                print("            Please enter a valid quantity")
                                                print("\n")
                                                continue
                                            else:
                                                break
                                        print("\n")
                                        quantity_list.append(quantity_of_laptop)

                                        if int(quantity_of_laptop) < 1:
                                            continue
                                        else:
                                            break
                                    break

                                while True:
                                    print("            Do you want to order more laptops ?")
                                    is_continue = input("            Answer in yes or no. ")

                                    is_continue = is_continue.lower()

                                    if is_continue == "yes":
                                        break
                                    elif is_continue != "yes" and is_continue != "no":
                                        print("            Dearest admin, please enter a valid answer. ")        # Having a little bit of fun with a sarcastic input message.
                                        print("\n")
                                        continue

                                    elif is_continue == "no":
                                        break

                                if is_continue == 'yes':
                                    continue
                                elif is_continue == 'no':
                                    break

                            for i in range(len(ID_list)):
                                ID_and_quantity_dictionary[ID_list[i]] = int(quantity_list[i])

                            self.set_ID_and_quantity_dictionary(**ID_and_quantity_dictionary)
                            self.set_available_quantity(True, **ID_and_quantity_dictionary)
                            self.set_name_of_manufacturer(name_of_manufacturer)
                            self.set_phone_number_of_manufacturer(phone_number_of_manufacturer)
                            self.set_address_of_manufacturer(address_of_manufacturer)
                            self.set_email_of_manufacturer(email_of_manufacturer)

                            invoice = ''.join(self.generate_invoice_manufacturer())
                            print(invoice)

                            print("\n")

                            file = open("Purchase " + f"{self.get_invoice_number_manufacturer()}.txt", "w")
                            file.write(invoice)
                            file.close()

                            self.read_database()

                            input('            Enter any key to continue.')
                            print("\n")

                            break

                        elif option_entered == 3:
                            break

                    if option_entered == 3:
                        break

            elif option_entered == 3:
                while True:
                    print('            +=============================================================================================================+')
                    print('            |                                                                                                             |')
                    print("            |                                  Welcome to the database management portal                                  |")
                    print('            |                                      Reliability is our objective.                                          |')
                    print('            |                                                                                                             |')
                    print('            |  Bhatbhateni, Kathmandu                                                                Phone No: 98xxxxxxxx |')
                    print('            +==============+==============================================================================================+')
                    print('            |              |                                                                                              |')
                    print('            |    Option    |                                     Task carried out                                         |')
                    print('            |              |                                                                                              |')
                    print('            +--------------+----------------------------------------------------------------------------------------------+')
                    print('            |      1       |    Enter 1 to view the database.                                                             |')
                    print('            |              |                                                                                              |')
                    print('            +--------------+----------------------------------------------------------------------------------------------+')
                    print('            |      2       |    Enter 2 to add an entry to the database.                                                  |')
                    print('            |              |                                                                                              |')
                    print('            +--------------+----------------------------------------------------------------------------------------------+')
                    print('            |      3       |    Enter 3 to remove an entry from the database.                                             |')
                    print('            |              |                                                                                              |')
                    print('            +--------------+----------------------------------------------------------------------------------------------+')
                    print('            |      4       |    Enter 4 to view details of one or more than one                                           |')
                    print('            |              |    laptop at once.                                                                           |')
                    print('            +--------------+----------------------------------------------------------------------------------------------+')
                    print('            |      5       |    Enter 5 to go one step back.                                                              |')
                    print('            |              |                                                                                              |')
                    print('            +--------------+----------------------------------------------------------------------------------------------+')
                    print("\n")
                    try:
                        option_entered = int(input("            Enter your choice. "))

                        assert int(option_entered) >= 1 and int(option_entered) <= 5

                    except ValueError:
                        print("            Please enter a number.")
                        print("\n")
                        continue
                    except AssertionError:
                        print("            Please enter a valid option.")
                        print("\n")
                        continue

                    while True:
                        if option_entered == 1:
                            self.display_database()
                            input("\n            Enter any key to continue. ")
                            print("\n")
                            break

                        elif option_entered == 2:
                            self.add_entry()                  # Add an entry into the database.
                            self.read_database()              # Read the text file to update the database.
                            print("\n")
                            print("            The entry has been successfully added to the database.")
                            print("\n")
                            break

                        elif option_entered == 3:
                            ID_of_laptop = int(input("            Enter the ID of the laptop that you want to remove from the database."))
                            self.remove_entry(ID_of_laptop)   # Remove an entry from the database.
                            self.read_database()              # Read the text file to update the database.
                            print("\n")
                            print('            The laptop of the ID', ID_of_laptop, ' has been successfully removed from the database.')
                            input('            Enter any key to continue.')
                            print("\n")
                            break

                        elif option_entered == 4:
                            print("            Enter either a single or multiple laptop ID's at once for viewing. ")
                            ID_of_laptop = input("            For example: 1 or 1,2. ")
                            ID_of_laptop = ID_of_laptop.split(',')


                            for i in range(len(ID_of_laptop)):
                                ID_of_laptop[i] = int(ID_of_laptop[i])

                            print(ID_of_laptop)
                            self.display_laptop(*ID_of_laptop)
                            input('            Enter any key to continue.')
                            print("\n")
                            break

                        elif option_entered == 5:
                            break

                    if option_entered == 5:
                        break

            elif option_entered == 4:
                print("\n            Thank you for using the shop management portal. Have a good day!")
                break

            else:
                print(f"\n            The entered option', {option_entered}, 'is not a valid one. Please choose from one of the options listed.\n")
                input('            Enter any key to continue.')
                print("\n")




interface = UserInterface()
interface.start()