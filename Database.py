class Database:

    def __init__(self):
        """Object initializing method of python. It said to be similar to a constructor and is not an actual constructor
        of objects."""
        self.__store = {}
        self.__count = 6

    def get_store(self):
        return self.__store

    def get_count(self):
        return self.__count

    def get_name_of_laptop(self, count):
        return self.__store[count][0]

    def get_name_of_brand(self, count):
        return self.__store[count][1]

    def get_price(self, count):
        return self.__store[count][2]

    def get_available_quantity(self, count):
        return self.__store[count][3]

    def set_available_quantity(self, purchase=False, **count):
        """If no second parameter is sent in the second argument, the quantity in the database decreases.
        If true is passed as the second argument, the quantity in the databases increases."""

        for each in count.keys():
            file = open("Database.txt", "r")
            lines = file.readlines()
            file.close()

            line_number = 11              # Starting line number.

            for i in range(int(each)):    # After every five line numbers starting from line number 11, individual entries are distinguished.
                line_number += 5

            if purchase == False:
                quantity_available_after_sale = int(self.get_available_quantity(int(each))) - count[each]
            elif purchase == True:
                quantity_available_after_sale = int(self.get_available_quantity(int(each))) + count[each]

            quantity_available_after_sale = str(quantity_available_after_sale)

            empty_space_quantity_available_after_sale = ''           # The three lines of code calculate empty space by subtracting the length of a variable string from the designated space.
            for i in range(5 - len(quantity_available_after_sale)):
                empty_space_quantity_available_after_sale += ' '

            new_count = '    ' + quantity_available_after_sale + empty_space_quantity_available_after_sale + ' '

            element = lines[line_number].split('|')
            element[5] = new_count

            lines[line_number] = '|'.join(element)

            file = open("Database.txt", "w")                        # Updating the database.
            file.write(''.join(lines))
            file.close()

        self.read_database()


    def get_processor(self, count):
        return self.__store[count][4]

    def get_number_of_cores(self, count):
        return self.__store[count][9]

    def get_processor_speed(self, count):
        return self.__store[count][13]

    def get_graphics_card(self, count):
        return self.__store[count][5]

    def get_graphics_card_memory(self, count):
        return self.__store[count][10]

    def get_ram(self, count):
        return self.__store[count][6]

    def get_ram_generation(self, count):
        return self.__store[count][11]

    def get_ram_speed(self, count):
        return self.__store[count][14]

    def get_storage(self, count):
        return self.__store[count][7]

    def get_screen_size(self, count):
        return self.__store[count][8]

    def get_screen_resolution(self, count):
        return self.__store[count][12]

    def get_screen_refresh_rate(self, count):
        return self.__store[count][15]

    def add_entry(self):
        """This method adds an entry to the database. Values entered by the user are added both to the database and to the text file. """

        name = input("Enter the name of the laptop. ")
        name_of_brand = input("Enter the name of the brand. ")
        price = input("Enter the price of the laptop. ")
        available_quantity = input("Enter the quantity of the laptop. ")
        processor = input("Enter the processor detail. ")
        number_of_cores = input("Enter the number of cores of the processor. ")
        processor_speed = input("Enter the speed of the processor. ")
        graphics_card = input("Enter the graphics card detail. ")
        graphics_card_memory = input("Enter the memory of the graphics card. ")
        ram = input("Enter the amount of RAM. ")
        ram_generation = input("Enter the generation of the RAM. ")
        ram_speed = input("Enter the speed of the RAM. ")
        storage = input("Enter the storage detail. ")
        screen_size = input("Enter the size of the screen. ")
        screen_resolution = input("Enter the resolution of the screen. ")
        screen_refresh_rate = input("Enter the refresh rate of the screen. ")

        self.__count += 1
        self.__store[self.__count] = [name, name_of_brand, price, available_quantity, processor, number_of_cores,
                                      processor_speed, graphics_card, graphics_card_memory, ram, ram_generation,
                                      ram_speed, storage, screen_size, screen_resolution, screen_refresh_rate]

        file = open("Database.txt", "r")
        lines = file.readlines()               # Returns each individual lines as a string element inside a list.
        file.close()

        empty_space_name = ""
        for each in range(14 - len(self.get_name_of_laptop(self.__count))):
            empty_space_name += " "

        empty_space_name_of_brand = ""
        for each in range(10 - len(self.get_name_of_brand(self.__count))):
            empty_space_name_of_brand += " "

        empty_space_price = ""
        for each in range(8 - len(self.get_price(self.__count))):
            empty_space_price += " "

        empty_space_available_quantity = ""
        for each in range(5 - len(self.get_available_quantity(self.__count))):
            empty_space_available_quantity += " "

        empty_space_count = ""
        for each in range(3 - len(str(self.__count))):
            empty_space_count += " "

        empty_space_processor = ""
        for each in range(17 - len(self.get_processor(self.__count))):
            empty_space_processor += " "

        empty_space_number_of_cores = ""
        for each in range(17 - len(self.get_number_of_cores(self.__count))):
            empty_space_number_of_cores += " "

        empty_space_processor_speed = ""
        for each in range(17 - len(self.get_processor_speed(self.__count))):
            empty_space_processor_speed += " "

        empty_space_graphics_card = ""
        for each in range(12 - len(self.get_graphics_card(self.__count))):
            empty_space_graphics_card += " "

        empty_space_graphics_card_memory = ""
        for each in range(12 - len(self.get_graphics_card_memory(self.__count))):
            empty_space_graphics_card_memory += " "

        empty_space_ram = ""
        for each in range(8 - len(self.get_ram(self.__count))):
            empty_space_ram += " "

        empty_space_ram_generation = ""
        for each in range(8 - len(self.get_ram_generation(self.__count))):
            empty_space_ram_generation += " "

        empty_space_ram_speed = ""
        for each in range(8 - len(self.get_ram_speed(self.__count))):
            empty_space_ram_speed += " "

        empty_space_storage = ""
        for each in range(10 - len(self.get_storage(self.__count))):
            empty_space_storage += " "

        empty_space_screen_size = ""
        for each in range(12 - len(self.get_screen_size(self.__count))):
            empty_space_screen_size += " "

        empty_space_screen_resolution = ""
        for each in range(12 - len(self.get_screen_resolution(self.__count))):
            empty_space_screen_resolution += " "

        empty_space_screen_refresh_rate = ""
        for each in range(12 - len(self.get_screen_refresh_rate(self.__count))):
            empty_space_screen_refresh_rate += " "

        lines[len(lines) - 1] = '        +-------+----------------+------------+----------+----------+' \
                                '-------------------+---------------+----------+------------+--------------+'

        lines.append('\n     	| 	    |                |            |          |          |                   |'
                     '               |          |            |              |\n')
        lines.append(f'        |   {self.__count}{empty_space_count} | {self.get_name_of_laptop(self.__count)}{empty_space_name} |'
                     f' {self.get_name_of_brand(self.__count)}{empty_space_name_of_brand} |'              # To keep the formatting of the tables consistent, empty spaces are calculated for each individual variables. 
                     f' {self.get_price(self.__count)}{empty_space_price} |'
                     f'    {self.get_available_quantity(self.__count)}{empty_space_available_quantity} |'
                     f' {self.get_processor(self.__count)}{empty_space_processor} |'
                     f'  {self.get_graphics_card(self.__count)}{empty_space_graphics_card} |'
                     f' {self.get_ram(self.__count)}{empty_space_ram} |'
                     f' {self.get_storage(self.__count)}{empty_space_storage} |'
                     f' {self.get_screen_size(self.__count)}{empty_space_screen_size} |\n')
        lines.append(f'        |       |                |            |          |          |'
                     f' {self.get_number_of_cores(self.__count)}{empty_space_number_of_cores} |'
                     f'  {self.get_graphics_card_memory(self.__count)}{empty_space_graphics_card_memory} |'
                     f' {self.get_ram_generation(self.__count)}{empty_space_ram_generation} |            |'
                     f' {self.get_screen_resolution(self.__count)}{empty_space_screen_resolution} |\n')
        lines.append(f'        |       |            	 |			  |          |          |'
                     f' {self.get_processor_speed(self.__count)}{empty_space_processor_speed} |               |'
                     f' {self.get_ram_speed(self.__count)}{empty_space_ram_speed} |            |'
                     f' {self.get_screen_refresh_rate(self.__count)}{empty_space_screen_refresh_rate} |\n')

        lines.append('        +=======+================+============+==========+==========+===================+'
                     '===============+==========+============+==============+')

        file = open("Database.txt", "w")
        file.write(''.join(lines))
        file.close()

    def display_database(self):
        """Displays the text file in the console."""
        file1 = open("Database.txt", "r")
        lines1 = file1.readlines()
        print(''.join(lines1))
        file1.close()

    def display_laptop(self, *arg):
        """This method accepts list as a parameter and displays one or more than one laptops."""
        file = open("Database.txt", "r")
        lines = file.readlines()
        file.close()

        line_number = 10
        table = lines[10:15]

        for i in range(len(arg)):
            for i in range(arg[i]):
                line_number += 5
            current_entry = lines[line_number: line_number + 5]
            table.append(''.join(current_entry))
            line_number = 10

        last_entry = table[len(table) - 1].split('|')
        last_entry[len(last_entry) - 1] = '\n        +=======+================+============+==========+==========+' \
                                          '===================+===============+==========+============+==============+'
        table[len(table) - 1] = '|'.join(last_entry)
        print(''.join(table))

    def remove_entry(self, count):
        """This method removes an entry from the database according to the id provided."""
        file = open("Database.txt", "r")
        lines = file.readlines()
        file.close()

        line_number = 10
        for i in range(count):
            line_number += 5

        lines[line_number: line_number + 5] = ''
        if count == self.get_count():
            lines[len(lines) - 1] = '        +=======+================+============+==========+==========+===================+===============+==========+============+==============+'

        line_number += 1
        for i in range(self.get_count() - count):
            current_line = lines[line_number].split('|')

            current_count = int(current_line[1])
            new_count = current_count - 1

            empty_space_count = ""
            for each in range(3 - len(str(int(current_line[1])))):
                empty_space_count += " "

            current_line[1] = f'   {new_count}{empty_space_count} '
            lines[line_number] = '|'.join(current_line)
            line_number += 5

        file = open("Database.txt", "w")
        file.write(''.join(lines))
        file.close()

        self.__count -= 1
        self.read_database()
        del self.__store[len(self.__store)]

    def read_database(self):
        """This method reads the text file and updates the dictionary of the database.
        This method is called any time there is a change in the text file."""
        line_number = 16
        for i in range(0, self.__count):
            def read_count():
                file = open("Database.txt", "r")
                lines = file.readlines()
                line = lines[line_number].split('|')
                line = line[1].split()
                line = ' '.join(line)
                count = line
                file.close()
                return count

            def read_name():
                file = open("Database.txt", "r")
                lines = file.readlines()
                line = lines[line_number].split('|')
                line = line[2].split()
                line = ' '.join(line)
                name = line
                file.close()
                return name

            def read_name_of_brand():
                file = open("Database.txt", "r")
                lines = file.readlines()
                line = lines[line_number].split('|')
                line = line[3].split()
                line = ' '.join(line)
                name_of_brand = line
                file.close()
                return name_of_brand

            def read_price():
                file = open("Database.txt", "r")
                lines = file.readlines()
                line = lines[line_number].split('|')
                line = line[4].split()
                line = ' '.join(line)
                price = line
                file.close()
                return price

            def read_available_quantity():
                file = open("Database.txt", "r")
                lines = file.readlines()
                line = lines[line_number].split('|')
                line = line[5].split()
                line = ' '.join(line)
                available_quantity = line
                file.close()
                return available_quantity

            def read_processor():
                file = open("Database.txt", "r")
                lines = file.readlines()
                line = lines[line_number].split('|')
                line = line[6].split()
                line = ' '.join(line)
                processor = line
                file.close()
                return processor

            def read_graphics_card():
                file = open("Database.txt", "r")
                lines = file.readlines()
                line = lines[line_number].split('|')
                line = line[7].split()
                line = ' '.join(line)
                graphics_card = line
                file.close()
                return graphics_card

            def read_ram():
                file = open("Database.txt", "r")
                lines = file.readlines()
                line = lines[line_number].split('|')
                line = line[8].split()
                line = ' '.join(line)
                ram = line
                file.close()
                return ram

            def read_storage():
                file = open("Database.txt", "r")
                lines = file.readlines()
                line = lines[line_number].split('|')
                line = line[9].split()
                line = ' '.join(line)
                storage = line
                file.close()
                return storage

            def read_screen_size():
                file = open("Database.txt", "r")
                lines = file.readlines()
                line = lines[line_number].split('|')
                line = line[10].split()
                line = ' '.join(line)
                screen_size = line
                file.close()
                return screen_size

            def read_number_of_cores():
                file = open("Database.txt", "r")
                lines = file.readlines()
                line = lines[line_number + 1].split('|')
                line = line[6].split()
                line = ' '.join(line)
                number_of_cores = line
                file.close()
                return number_of_cores

            def read_graphics_card_memory():
                file = open("Database.txt", "r")
                lines = file.readlines()
                line = lines[line_number + 1].split('|')
                line = line[7].split()
                line = ' '.join(line)
                graphics_card_memory = line
                file.close()
                return graphics_card_memory

            def read_ram_generation():
                file = open("Database.txt", "r")
                lines = file.readlines()
                line = lines[line_number + 1].split('|')
                line = line[8].split()
                line = ' '.join(line)
                ram_generation = line
                file.close()
                return ram_generation

            def read_screen_resolution():
                file = open("Database.txt", "r")
                lines = file.readlines()
                line = lines[line_number + 1].split('|')
                line = line[10].split()
                line = ' '.join(line)
                screen_resolution = line
                file.close()
                return screen_resolution

            def read_processor_speed():
                file = open("Database.txt", "r")
                lines = file.readlines()
                line = lines[line_number + 2].split('|')
                line = line[6].split()
                line = ' '.join(line)
                processor_speed = line
                file.close()
                return processor_speed

            def read_ram_speed():
                file = open("Database.txt", "r")
                lines = file.readlines()
                line = lines[line_number + 2].split('|')
                line = line[8].split()
                line = ' '.join(line)
                ram_speed = line
                file.close()
                return ram_speed

            def read_screen_refresh_rate():
                file = open("Database.txt", "r")
                lines = file.readlines()
                line = lines[line_number + 2].split('|')
                line = line[10].split()
                line = ' '.join(line)
                screen_refresh_rate = line
                file.close()
                return screen_refresh_rate

            self.__store[i + 1] = [read_name(), read_name_of_brand(), read_price(), read_available_quantity(),
                                   read_processor(), read_graphics_card(), read_ram(), read_storage(),
                                   read_screen_size(),read_number_of_cores(), read_graphics_card_memory(),
                                   read_ram_generation(),read_screen_resolution(), read_processor_speed(),
                                   read_ram_speed(), read_screen_refresh_rate()]

            line_number += 5

database = Database()
database.read_database()