from datetime import datetime
from Database import Database


class InvoiceToCustomer(Database):

    ID_and_quantity_dictionary = {}
    current_date = ''
    current_time = ''
    invoice_number_customer = ''
    due_date = ''
    order_number_customer = 4000
    number_of_bills_customer = '001'
    name_of_customer = ''
    address_of_customer = ''
    phone_number_of_customer = ''
    email_of_customer = ''
    is_ship = True
    shipping_price = ''
    name_of_user = ''
    phone_number_of_user = ''
    total_price = ''

    def set_current_date(self):
        now = datetime.now()
        current_date = str(now).split()
        self.current_date = current_date[0]

    def set_name_of_customer(self, name_of_customer):
        self.name_of_customer = name_of_customer

    def get_name_of_customer(self):
        return self.name_of_customer

    def set_name_of_user(self, name_of_user):
        self.name_of_user = name_of_user

    def get_name_of_user(self):
        return self.name_of_user

    def get_ID_and_quantity_dictionary(self):
        return self.ID_and_quantity_dictionary

    def get_quantity(self, count):
        return self.get_ID_and_quantity_dictionary()[count]

    def set_ID_and_quantity_dictionary(self, **ID_and_quantity_dictionary):
        self.ID_and_quantity_dictionary = ID_and_quantity_dictionary

    def set_phone_number_of_user(self, phone_number_of_user):
        self.phone_number_of_user = phone_number_of_user

    def get_phone_number_of_user(self):
        return self.phone_number_of_user

    def set_address_of_customer(self, address_of_customer):
        self.address_of_customer = address_of_customer

    def get_address_of_customer(self):
        return self.address_of_customer

    def set_phone_number_of_customer(self, phone_number_of_customer):
        self.phone_number_of_customer = phone_number_of_customer

    def get_phone_number_of_customer(self):
        return self.phone_number_of_customer

    def set_email_of_customer(self, email_of_customer):
        self.email_of_customer = email_of_customer

    def get_email_of_customer(self):
        return self.email_of_customer

    def get_is_ship(self):
        return self.is_ship

    def set_is_ship(self, is_ship):
        self.is_ship = is_ship

        if is_ship == False:
            self.set_shipping_price('')

    def get_shipping_price(self):
        return self.shipping_price

    def set_shipping_price(self, shipping_price):
        self.shipping_price = shipping_price

    def set_current_time(self):
        now = datetime.now()
        now = str(now).split()
        current_time = now[1].split('.')[0]
        self.current_time = current_time

    def get_current_date(self):
        return self.current_date

    def get_current_time(self):
        return self.current_time

    def get_due_date(self):
        return self.due_date

    def get_total_price(self):
        return self.total_price

    def set_total_price(self, total_price):
        self.total_price = total_price

    def get_order_number_customer(self):
        return self.order_number_customer

    def get_number_of_bills_customer(self):
        return self.number_of_bills_customer

    def generate_amount_in_words(self, amount):
        """This method generates amount in words for a given price. It can generate amount in words greater than 0 and less than a billion."""

        dictionary_of_number_single_digit = {'1': 'one', '2': 'two', '3': 'three', '4': 'four', '5': 'five', '6': 'six', '7': 'seven', '8': 'eight', '9': 'nine'}
        dictionary_of_number_eleven_to_nineteen = {'11': 'eleven', '12': 'twelve', '13': 'thirteen', '14': 'fourteen', '15': 'fifteen', '16': 'sixteen', '17': 'seventeen', '18': 'eighteen', '19': 'nineteen'}
        dictionary_of_number_double_digits = {'10': 'ten', '20': 'twenty', '30': 'thirty', '40': 'forty', '50': 'fifty', '60': 'sixty', '70': 'seventy', '80': 'eighty', '90': 'ninety'}


        def amount_in_word_for_one_digit(amount):
            amount_in_words = dictionary_of_number_single_digit[str(amount)]
            return amount_in_words

        def amount_in_word_for_two_digits(amount):
            amount = str(amount)
            amount_array = []
            amount_in_words_array = []
            for i in range(len(amount)):
                amount_array.append(amount[i])

            if int(amount_array[1]) == 0:
                amount_array[0] = str(int(amount_array[0]) * 10)
                amount_in_words_array.append(dictionary_of_number_double_digits[amount_array[0]])
                amount_in_words = amount_in_words_array[0]

            elif int(amount) >= 11 and int(amount) <= 19:
                amount_in_words = dictionary_of_number_eleven_to_nineteen[str(amount)]
            else:
                amount_array[0] = str(int(amount_array[0]) * 10)
                amount_in_words_array.append(dictionary_of_number_double_digits[amount_array[0]])
                amount_in_words_array.append(dictionary_of_number_single_digit[amount_array[1]])
                amount_in_words = ' '.join(amount_in_words_array)
            return amount_in_words


        def amount_in_words_for_three_digits(amount):
            amount = str(amount)
            amount_array = []
            amount_in_words_array = []
            for i in range(len(amount)):
                amount_array.append(amount[i])

            amount_in_words_array.append(amount_in_word_for_one_digit(amount_array[0]) + ' hundred')
            if int(amount_array[1]) == 0 and int(amount_array[2]) == 0:
                amount_in_words = ''.join(amount_in_words_array)

            elif int(amount_array[1]) != 0:
                amount_in_words_array.append(' ' + amount_in_word_for_two_digits(int(amount_array[1] + amount_array[2])))
                amount_in_words = ''.join(amount_in_words_array)

            elif int(int(amount_array[2])) != 0:
                amount_in_words_array.append(' ' + amount_in_word_for_one_digit(int(amount_array[2])))
                amount_in_words = ''.join(amount_in_words_array)

            return amount_in_words

        def amount_in_words_for_four_digits(amount):
            amount = str(amount)
            amount_array = []
            amount_in_words_array = []
            for i in range(len(amount)):
                amount_array.append(amount[i])

            amount_in_words_array.append(amount_in_word_for_one_digit(amount_array[0]) + ' thousand')

            if int(amount_array[1]) == 0 and int(amount_array[2]) == 0 and int(amount_array[3]) == 0:
                amount_in_words = ''.join(amount_in_words_array)

            elif int(amount_array[1]) != 0:
                amount_in_words_array.append(' ' + amount_in_words_for_three_digits(int(amount_array[1] + amount_array[2] + amount_array[3])))
                amount_in_words = ''.join(amount_in_words_array)
            elif int(amount_array[2]) != 0:
                amount_in_words_array.append(' ' + amount_in_word_for_two_digits(int(amount_array[2] + amount_array[3])))
                amount_in_words = ''.join(amount_in_words_array)
            elif int(amount_array[3]) != 0:
                amount_in_words_array.append(' ' + amount_in_word_for_one_digit(int(amount_array[3])))
                amount_in_words = ''.join(amount_in_words_array)
            return amount_in_words

        def amount_in_words_for_five_digits(amount):
            amount = str(amount)
            amount_array = []
            amount_in_words_array = []
            for i in range(len(amount)):
                amount_array.append(amount[i])

            amount_in_words_array.append(amount_in_word_for_two_digits(int(amount_array[0] + amount_array[1])) + ' thousand')

            if int(amount_array[2]) == 0 and int(amount_array[3]) == 0 and int(amount_array[4]) == 0:
                amount_in_words = ''.join(amount_in_words_array)
            elif int(amount_array[2]) != 0:
                amount_in_words_array.append(' ' + amount_in_words_for_three_digits(int(amount_array[2] + amount_array[3] + amount_array[4])))
                amount_in_words = ''.join(amount_in_words_array)
            elif int(amount_array[3]) != 0:
                amount_in_words_array.append(' ' + amount_in_word_for_two_digits(int(amount_array[3] + amount_array[4])))
                amount_in_words = ''.join(amount_in_words_array)
            elif int(amount_array[4] != 0):
                amount_in_words_array.append(' ' + amount_in_word_for_one_digit(int(amount_array[4])))
                amount_in_words = ''.join(amount_in_words_array)

            return amount_in_words

        def amount_in_words_for_six_digits(amount):
            amount = str(amount)
            amount_array = []
            amount_in_words_array = []
            for i in range(len(amount)):
                amount_array.append(amount[i])

            amount_in_words_array.append(amount_in_words_for_three_digits(int(amount_array[0] + amount_array[1] + amount_array[2])) + ' thousand')
            amount_in_words = ''.join(amount_in_words_array)

            if int(amount_array[3]) != 0:
                amount_in_words_array.append(' ' + amount_in_words_for_three_digits(int(amount_array[3] + amount_array[4] + amount_array[5])))
                amount_in_words = ''.join(amount_in_words_array)
            elif int(amount_array[4]) != 0:
                amount_in_words_array.append(' ' + amount_in_word_for_two_digits(int(amount_array[4] + amount_array[5])))
                amount_in_words = ''.join(amount_in_words_array)
            elif int(amount_array[5]) != 0:
                amount_in_words_array.append(' ' + amount_in_word_for_one_digit(amount_array[5]))
                amount_in_words = ''.join(amount_in_words_array)
            return amount_in_words


        def amount_in_words_for_seven_digits(amount):
            amount = str(amount)
            amount_array = []
            amount_in_words_array = []
            for i in range(len(amount)):
                amount_array.append(amount[i])

            amount_in_words_array.append(amount_in_word_for_one_digit(int(amount_array[0])) + ' million')

            if int(amount_array[1]) == 0 and int(amount_array[2]) == 0 and int(amount_array[3]) == 0 and int(amount_array[4]) == 0 and int(amount_array[5]) == 0  and int(amount_array[6]) == 0:
                amount_in_words = ''.join(amount_in_words_array)
            elif int(amount_array[1]) != 0:
                amount_in_words_array.append(' ' + amount_in_words_for_six_digits(int(amount_array[1] + amount_array[2] + amount_array[3] + amount_array[4] + amount_array[5] + amount_array[6])))
                amount_in_words = ''.join(amount_in_words_array)
            elif int(amount_array[2]) != 0:
                amount_in_words_array.append(' ' + amount_in_words_for_five_digits(int(amount_array[2] + amount_array[3] + amount_array[4] + amount_array[5] + amount_array[6])))
                amount_in_words = ''.join(amount_in_words_array)
            elif int(amount_array[3]) != 0:
                amount_in_words_array.append(' ' + amount_in_words_for_four_digits(int(amount_array[3] + amount_array[4] + amount_array[5] + amount_array[6])))
                amount_in_words = ''.join(amount_in_words_array)
            elif int(amount_array[4]) != 0:
                amount_in_words_array.append(' ' + amount_in_words_for_three_digits(int(amount_array[4] + amount_array[5] + amount_array[6])))
                amount_in_words = ''.join(amount_in_words_array)
            elif int(amount_array[5]) != 0:
                amount_in_words_array.append(' ' + amount_in_word_for_two_digits(int(amount_array[5] + amount_array[6])))
                amount_in_words = ''.join(amount_in_words_array)
            elif int(amount_array[6]) != 0:
                amount_in_words_array.append(' ' + amount_in_word_for_one_digit(int(amount_array[6])))
                amount_in_words = ''.join(amount_in_words_array)

            return amount_in_words


        def amount_in_words_for_eight_digits(amount):
            amount = str(amount)
            amount_array = []
            amount_in_words_array = []
            for i in range(len(amount)):
                amount_array.append(amount[i])

            amount_in_words_array.append(amount_in_word_for_two_digits(int(amount_array[0] + amount_array[1])) + ' million')

            if int(amount_array[2]) == 0 and int(amount_array[3]) == 0 and int(amount_array[4]) == 0 and int(amount_array[5]) == 0 and int(amount_array[6]) == 0 and int(amount_array[7]) == 0 :
                amount_in_words = ''.join(amount_in_words_array)
            elif int(amount_array[2]) != 0:
                amount_in_words_array.append(' ' + amount_in_words_for_six_digits(int(amount_array[2] + amount_array[3] + amount_array[4] + amount_array[5] + amount_array[6] + amount_array[7])))
                amount_in_words = ''.join(amount_in_words_array)
            elif int(amount_array[3]) != 0:
                amount_in_words_array.append(' ' + amount_in_words_for_five_digits(int(amount_array[3] + amount_array[4] + amount_array[5] + amount_array[6] + amount_array[7])))
                amount_in_words = ''.join(amount_in_words_array)
            elif int(amount_array[4]) != 0:
                amount_in_words_array.append(' ' + amount_in_words_for_four_digits(int(amount_array[4] + amount_array[5] + amount_array[6] + amount_array[7])))
                amount_in_words = ''.join(amount_in_words_array)
            elif int(amount_array[5]) != 0:
                amount_in_words_array.append(' ' + amount_in_words_for_three_digits(int(amount_array[5] + amount_array[6] + amount_array[7])))
                amount_in_words = ''.join(amount_in_words_array)
            elif int(amount_array[6]) != 0:
                amount_in_words_array.append(' ' + amount_in_word_for_two_digits(int(amount_array[6] + amount_array[7])))
                amount_in_words = ''.join(amount_in_words_array)
            elif int(amount_array[7]) != 0:
                amount_in_words_array.append(' ' + amount_in_word_for_one_digit(int(amount_array[7])))
                amount_in_words = ''.join(amount_in_words_array)

            return amount_in_words

        def amount_in_words_for_nine_digits(amount):
            amount = str(amount)
            amount_array = []
            amount_in_words_array = []
            for i in range(len(amount)):
                amount_array.append(amount[i])

            amount_in_words_array.append(amount_in_words_for_three_digits(int(amount_array[0] + amount_array[1] + amount_array[2])) + ' million')

            if int(amount_array[3]) == 0 and int(amount_array[4]) == 0 and int(amount_array[5]) == 0 and int(amount_array[6]) == 0 and int(amount_array[7]) == 0 and int(amount_array[8]) == 0 :
                amount_in_words = ''.join(amount_in_words_array)
            elif int(amount_array[3]) != 0:
                amount_in_words_array.append(' ' + amount_in_words_for_six_digits(int(amount_array[3] + amount_array[4] + amount_array[5] + amount_array[6] + amount_array[7] + amount_array[8])))
                amount_in_words = ''.join(amount_in_words_array)
            elif int(amount_array[4]) != 0:
                amount_in_words_array.append(' ' + amount_in_words_for_five_digits(int(amount_array[4] + amount_array[5] + amount_array[6] + amount_array[7] + amount_array[8])))
                amount_in_words = ''.join(amount_in_words_array)
            elif int(amount_array[5]) != 0:
                amount_in_words_array.append(' ' + amount_in_words_for_four_digits(int(amount_array[5] + amount_array[6] + amount_array[7] + amount_array[8])))
                amount_in_words = ''.join(amount_in_words_array)
            elif int(amount_array[6]) != 0:
                amount_in_words_array.append(' ' + amount_in_words_for_three_digits(int(amount_array[6] + amount_array[7] + amount_array[8])))
                amount_in_words = ''.join(amount_in_words_array)
            elif int(amount_array[7]) != 0:
                amount_in_words_array.append(' ' + amount_in_word_for_two_digits(int(amount_array[7] + amount_array[8])))
                amount_in_words = ''.join(amount_in_words_array)
            elif int(amount_array[8]) != 0:
                amount_in_words_array.append(' ' + amount_in_word_for_one_digit(int(amount_array[8])))
                amount_in_words = ''.join(amount_in_words_array)

            return amount_in_words


        if (len(str(amount))) == 1:
            return amount_in_word_for_one_digit(amount)
        elif (len(str(amount))) == 2:
            return amount_in_word_for_two_digits(amount)
        elif (len(str(amount))) == 3:
            return amount_in_words_for_three_digits(amount)
        elif (len(str(amount))) == 4:
            return amount_in_words_for_four_digits(amount)
        elif (len(str(amount))) == 5:
            return amount_in_words_for_five_digits(amount)
        elif (len(str(amount))) == 6:
            return amount_in_words_for_six_digits(amount)
        elif (len(str(amount))) == 7:
            return amount_in_words_for_seven_digits(amount)
        elif (len(str(amount))) == 8:
            return amount_in_words_for_eight_digits(amount)
        elif (len(str(amount))) == 9:
            return amount_in_words_for_nine_digits(amount)

    def set_due_date(self):
        now = datetime.now()
        current_date = str(now).split()[0].split('-')
        current_year = int(current_date[0])
        current_month = int(current_date[1])
        current_day = int(current_date[2])

        leap_year = False
        if current_year % 4 == 0:
            if current_year % 100 != 0:
                leap_year = True
            elif current_year % 100 == 0:
                if current_year % 400 == 0:
                    leap_year = True
                else:
                    leap_year = False

        dictionary_of_month = {'1': 31, '2': 28, '3': 31, '4': 30, '5': 31, '6': 30, '7': 31, '8': 31, '9': 30,
                               '10': 31, '11': 30, '12': 31}

        if leap_year == True:
            dictionary_of_month['2'] = 29            # In a leap year, february has twenty nine days.

        value_for_addition_to_current_month = dictionary_of_month[str(int(current_month))] - current_day
        value_for_addition_to_next_month = 30 - value_for_addition_to_current_month

        if current_month == 12 and value_for_addition_to_current_month != 30:
            current_year += 1
            current_month = 1
            current_day = value_for_addition_to_next_month

        elif current_month == 12 and value_for_addition_to_current_month == 30:
            current_month = 12
            current_day = current_day + 30

        elif value_for_addition_to_next_month > dictionary_of_month[str(int(current_month + 1))]:
            if value_for_addition_to_current_month == 30:
                current_day = current_day + 30
            else:
                current_month += 2
                current_day = value_for_addition_to_next_month - dictionary_of_month['2']
        else:
            if value_for_addition_to_current_month == 30:
                current_day = current_day + 30
            else:
                current_month += 1
                current_day = value_for_addition_to_next_month

        if len(str(current_month)) == 1:
            current_month = '0' + str(current_month)
            due_date = str(current_year) + '-' + current_month + '-' + str(current_day)
        else:
            due_date = str(current_year) + '-' + str(current_month) + '-' + str(current_day)
        self.due_date = due_date

    def set_invoice_number_customer(self):
        """This method generates a unique invoice number."""
        now = datetime.now()
        current_date = str(now).split()[0]
        current_date = current_date.split('-')
        current_date = ''.join(current_date)
        self.invoice_number_customer = str(self.get_order_number_customer()) + '-' + current_date + '-' + self.get_number_of_bills_customer()

    def get_invoice_number_customer(self):
        return self.invoice_number_customer

    def set_number_of_bills_customer(self):
        if int(self.get_number_of_bills_customer()) < 9:
            self.number_of_bills_customer = '00' + str(int(self.number_of_bills_customer) + 1)
        elif int(self.get_number_of_bills_customer()) >= 9 and int(self.get_number_of_bills_customer()) < 99:
            self.number_of_bills_customer = '0' + str(int(self.number_of_bills_customer) + 1)
        else:
            self.number_of_bills_customer = str(int(self.number_of_bills_customer) + 1)

    def generate_invoice_customer(self):
        """This method generates an invoice to the customer."""

        empty_space_name_of_customer = ''
        for i in range(50 - len(self.get_name_of_customer())):
            empty_space_name_of_customer += ' '

        empty_space_phone_number_of_customer = ''
        for i in range(50 - len(self.get_phone_number_of_customer())):
            empty_space_phone_number_of_customer += ' '

        empty_space_address_of_customer = ''
        for i in range(50 - len(self.get_address_of_customer())):
            empty_space_address_of_customer += ' '

        empty_space_email_of_customer = ''
        for i in range(50 - len(self.get_email_of_customer())):
            empty_space_email_of_customer += ' '

        empty_space_name_of_user = ''
        for i in range(50 - len(self.get_name_of_user())):
            empty_space_name_of_user += ' '

        empty_space_phone_number_of_user = ''
        for i in range(50 - len(self.get_phone_number_of_user())):
            empty_space_phone_number_of_user += ' '



        self.set_current_date()
        self.set_current_time()
        self.set_invoice_number_customer()
        self.set_due_date()

        empty_space_current_date = ''
        for i in range(19 - len(self.get_current_date())):
            empty_space_current_date += ' '

        empty_space_current_time = ''
        for i in range(19 - len(self.get_current_time())):
            empty_space_current_time += ' '

        empty_space_invoice_number_customer = ''
        for i in range(19 - len(self.get_invoice_number_customer())):
            empty_space_invoice_number_customer += ' '

        empty_space_due_date = ''
        for i in range(19 - len(self.get_due_date())):
            empty_space_due_date += ' '

        empty_space_order_number_customer = ''
        for i in range(19 - len(str(self.get_order_number_customer()))):
            empty_space_order_number_customer += ' '



        if self.get_is_ship() == True:
            first_array = ["\n", "\n", "\n", "\n",
                           '                 +=========================================================================================================+\n',
                           '                 |                                                                                                         |\n',
                           '                 |                                                                                                         |\n',
                           "                 | Nirajan's Electronics                                                                           Invoice |\n",
                           '                 |                                                                                                         |\n',
                           '                 |                                                                                                         |\n',
                           '                 +---------------------------------------------------------------------------------------------------------+\n',
                           '                 |                                                                                                         |\n',
                          f'                 | Bhatbhateni, Kathmandu                                          Date              | {self.get_current_date()}{empty_space_current_date} |\n',
                          f'                 | np01cp4a220232@gmail.com                                        Time of purchase  | {self.get_current_time()}{empty_space_current_time} |\n',
                          f'                 | 98XXXXXXXX                                                      Your order number | {str(self.get_order_number_customer())}{empty_space_order_number_customer} |\n',
                          f'                 |                                                                 Invoice number    | {self.get_invoice_number_customer()}{empty_space_invoice_number_customer} |\n',
                          f'                 |                                                                 Due Date          | {self.get_due_date()}{empty_space_due_date} |\n',
                           '                 |                                                                                                         |\n',
                           '                 +----------------------------------------------------+----------------------------------------------------+\n',
                           '                 |                                                    |                                                    |\n',
                           '                 | Billed To                                          | Shipped to                                         |\n',
                           '                 |                                                    |                                                    |\n',
                           '                 +----------------------------------------------------+----------------------------------------------------+\n',
                           '                 |                                                    |                                                    |\n',
                          f'                 | {self.get_name_of_customer()}{empty_space_name_of_customer} | {self.get_name_of_customer()}{empty_space_name_of_customer} |\n',
                          f'                 | {self.get_address_of_customer()}{empty_space_address_of_customer} | {self.get_address_of_customer()}{empty_space_address_of_customer} |\n',
                          f'                 | {self.get_phone_number_of_customer()}{empty_space_phone_number_of_customer} | {self.get_phone_number_of_customer()}{empty_space_phone_number_of_customer} |\n',
                          f'                 | {self.get_email_of_customer()}{empty_space_email_of_customer} | {self.get_email_of_customer()}{empty_space_email_of_customer} |\n',
                           '                 |                                                    |                                                    |\n',
                           '                 |                                                    |                                                    |\n',
                           '                 +----------------------------------------------------+----------------------------------------------------+\n',
                           '                 |                                                                                                         |\n',
                           '                 | Note - The description of the laptop is in the format of brand name, name of laptop, display details,   |\n',
                           '                 |        graphics card detail, processor detail, RAM details and storage detail.                          |\n',
                           '                 |                                                                                                         |\n',
                           '                 +---------------------------------------------------------------------------------------------------------+\n',
                           '                 |                                                                                                         |\n',
                           '                 |                                                                                                         |\n',
                           '                 |                                                                                                         |\n',
                           '                 +=======+=========================================================+==========+============+===============+\n',
                           '                 |       |                                                         |          |            |               |\n',
                           '                 | No.   | Description                                             | Quantity | Unit Price | Amount        |\n',
                           '                 |       |                                                         |          |            |               |\n',
                           '                 +=======+=========================================================+==========+============+===============+\n']
        else:
            first_array = ["\n", "\n", "\n", "\n",
                           '                 +=========================================================================================================+\n',
                           '                 |                                                                                                         |\n',
                           '                 |                                                                                                         |\n',
                           "                 | Nirajan's Electronics                                                                           Invoice |\n",
                           '                 |                                                                                                         |\n',
                           '                 |                                                                                                         |\n',
                           '                 +---------------------------------------------------------------------------------------------------------+\n',
                           '                 |                                                                                                         |\n',
                           f'                 | Bhatbhateni, Kathmandu                                          Date              | {self.get_current_date()}{empty_space_current_date} |\n',
                           f'                 | np01cp4a220232@gmail.com                                        Time of purchase  | {self.get_current_time()}{empty_space_current_time} |\n',
                           f'                 | 98XXXXXXXX                                                      Your order number | {str(self.get_order_number_customer())}{empty_space_order_number_customer} |\n',
                           f'                 |                                                                 Invoice number    | {self.get_invoice_number_customer()}{empty_space_invoice_number_customer} |\n',
                           f'                 |                                                                 Due Date          | {self.get_due_date()}{empty_space_due_date} |\n',
                           '                 |                                                                                                         |\n',
                           '                 +----------------------------------------------------+----------------------------------------------------+\n',
                           '                 |                                                    |                                                    |\n',
                           '                 | Billed To                                          | Shipped to                                         |\n',
                           '                 |                                                    |                                                    |\n',
                           '                 +----------------------------------------------------+----------------------------------------------------+\n',
                           '                 |                                                    |                                                    |\n',
                           f'                 | {self.get_name_of_customer()}{empty_space_name_of_customer} |                                                    |\n',
                           f'                 | {self.get_address_of_customer()}{empty_space_address_of_customer} |                                                    |\n',
                           f'                 | {self.get_phone_number_of_customer()}{empty_space_phone_number_of_customer} |                                                    |\n',
                           f'                 | {self.get_email_of_customer()}{empty_space_email_of_customer} |                                                    |\n',
                           '                 |                                                    |                                                    |\n',
                           '                 |                                                    |                                                    |\n',
                           '                 +----------------------------------------------------+----------------------------------------------------+\n',
                           '                 |                                                                                                         |\n',
                           '                 | Note - The description of the laptop is in the format of brand name, name of laptop, display details,   |\n',
                           '                 |        graphics card detail, processor detail, RAM details and storage detail.                          |\n',
                           '                 |                                                                                                         |\n',
                           '                 +---------------------------------------------------------------------------------------------------------+\n',
                           '                 |                                                                                                         |\n',
                           '                 |                                                                                                         |\n',
                           '                 |                                                                                                         |\n',
                           '                 +=======+=========================================================+==========+============+===============+\n',
                           '                 |       |                                                         |          |            |               |\n',
                           '                 | No.   | Description                                             | Quantity | Unit Price | Amount        |\n',
                           '                 |       |                                                         |          |            |               |\n',
                           '                 +=======+=========================================================+==========+============+===============+\n']

        def generate_price_array():

            array = []
            price_array = []
            second_array = []
            
            count = 0
            total_price = 0

            for each in self.get_ID_and_quantity_dictionary().keys():
                count = count + 1
                count = str(count)

                empty_space_count = ''
                for i in range(3 - len(count)):
                    empty_space_count += ' '

                empty_space_name_of_brand = ''
                for i in range(10 - len(self.get_name_of_brand(int(each)))):
                    empty_space_name_of_brand += ' '

                empty_space_name_of_laptop = ''
                for i in range(14 - len(self.get_name_of_laptop(int(each)))):
                    empty_space_name_of_laptop += ' '

                empty_space_screen_size = ''
                for i in range(12 - len(self.get_screen_size(int(each)))):
                    empty_space_screen_size += ' '

                empty_space_screen_refresh_rate = ''
                for i in range(12 - len(self.get_screen_refresh_rate(int(each)))):
                    empty_space_screen_refresh_rate += ' '

                empty_space_graphics_card = ''
                for i in range(12 - len(self.get_graphics_card(int(each)))):
                    empty_space_graphics_card += ' '

                empty_space_processor = ''
                for i in range(17 - len(self.get_processor(int(each)))):
                    empty_space_processor += ' '

                empty_space_ram = ''
                for i in range(8 - len(self.get_ram(int(each)))):
                    empty_space_ram += ' '

                empty_space_ram_generation = ''
                for i in range(8 - len(self.get_ram_generation(int(each)))):
                    empty_space_ram_generation += ' '

                empty_space_storage = ''
                for i in range(10 - len(self.get_storage(int(each)))):
                    empty_space_storage += ' '

                empty_space_quantity = ''
                for i in range(6 - len(str(self.get_quantity(str(each))))):
                    empty_space_quantity += ' '

                price = "{0:.2f}".format(float(self.get_price(int(each)).replace("$", '')))
                price = "$" + str(price)

                empty_space_price = ''
                for i in range(10 - len(price)):
                    empty_space_price += ' '

                new_array = ['                 |       |                                                         |          |            |               |\n',
                            f'                 |   {count}{empty_space_count} | {self.get_name_of_brand(int(each))}{empty_space_name_of_brand}, {self.get_name_of_laptop(int(each))}{empty_space_name_of_laptop}, {self.get_screen_size(int(each))}{empty_space_screen_size} {self.get_screen_refresh_rate(int(each))}{empty_space_screen_refresh_rate},  |          |            |               |\n',
                            f'                 |       | {self.get_graphics_card(int(each))}{empty_space_graphics_card}, {self.get_processor(int(each))}{empty_space_processor}, {self.get_ram(int(each))}{empty_space_ram} {self.get_ram_generation(int(each))}{empty_space_ram_generation},     |          |            |               |\n',
                            f'                 |       | {self.get_storage(int(each))}{empty_space_storage}                                              |          |            |               |\n',
                             '                 |       |                                                         |          |            |               |\n',
                             '                 +=======+=========================================================+==========+============+===============+\n']


                count = int(count)
                second_array = new_array

                array = ' '.join(second_array)
                array = array.split('|')
                array = array[:len(array) - 1]
                array = ''.join(array)
                array = array.split()
                array = array[1:]
                array = ' '.join(array)
                array = array.split(',')

                new_array = []
                for i in range(len(array)):
                    new_array.append(list(array[i]))

                for i in range(len(new_array)):                                   #For removing spaces at the end of each element.
                    if new_array[i][len(new_array[i])-1] == ' ':
                        new_array[i] = ''.join(new_array[i][:len(new_array[i]) - 1])
                    else:
                        new_array[i] = ''.join(new_array[i])


                new_array[len(new_array) - 1] = ''.join(new_array[len(new_array) - 1])


                first_row_1 = new_array[0] + ',' + new_array[1] + ',' + new_array[2] + ',' + new_array[3]
                second_row_1 = new_array[4][1:] + ',' + new_array[5] + ',' + new_array[6]

                amount = float(self.get_price(int(each)).replace("$", '')) * int(self.get_quantity(each))
                amount = "{0:.2f}".format(amount)
                total_price += float(amount)
                amount = "$" + str(amount)


                empty_space_amount = ''
                for i in range(14 - len(amount)):
                    empty_space_amount += ' '


                if 55 - len(first_row_1) >= 0 and 55 - len(second_row_1) >= 0:
                    empty_space_first_row_1 = ''
                    for i in range(55 - len(first_row_1)):
                        empty_space_first_row_1 += ' '

                    empty_space_second_row_1 = ''
                    for i in range(55 - len(second_row_1)):
                        empty_space_second_row_1 += ' '

                    new_array_1 = ['                 |       |                                                         |          |            |               |\n',
                                  f'                 |   {count}{empty_space_count} | {first_row_1}{empty_space_first_row_1} |   {self.get_quantity(each)}{empty_space_quantity} | {price}{empty_space_price} | {amount}{empty_space_amount}|\n',
                                  f'                 |       | {second_row_1}{empty_space_second_row_1} |          |            |               |\n',
                                   '                 |       |                                                         |          |            |               |\n',
                                   '                 +=======+=========================================================+==========+============+===============+\n']
                    if len(self.get_ID_and_quantity_dictionary()) > 1:
                        new_array_1[len(new_array_1) - 1] = '                 +-------+---------------------------------------------------------+----------+------------+---------------+\n'
                    if len(self.get_ID_and_quantity_dictionary()) == count:
                        new_array_1[len(new_array_1) - 1] = '                 +=======+=========================================================+==========+============+===============+\n'
                    price_array.append(''.join(new_array_1))

                elif 55 - len(first_row_1) <= 0 and 55 - len(second_row_1) >= 0:

                    new_array[3] = new_array[3][1:]

                    first_row_1 = new_array[0] + ',' + new_array[1] + ',' + new_array[2]
                    second_row_1 = new_array[3] + ',' + new_array[4] + ',' + new_array[5] + ',' + new_array[6]

                    if 55 - len(second_row_1) < 0:

                        second_row_1 = new_array[3] + ',' + new_array[4] + ',' + new_array[5]
                        third_row_1 = new_array[6][1:]

                        empty_space_first_row_1 = ''
                        for i in range(55 - len(first_row_1)):
                            empty_space_first_row_1 += ' '

                        empty_space_second_row_1 = ''
                        for i in range(55 - len(second_row_1)):
                            empty_space_second_row_1 += ' '

                        empty_space_third_row_1 = ''
                        for i in range(55 - len(third_row_1)):
                            empty_space_third_row_1 += ' '

                        empty_space_quantity = ''
                        new_array_1 = [
                            '                 |       |                                                         |          |            |               |\n',
                            f'                 |   {count}{empty_space_count} | {first_row_1}{empty_space_first_row_1} |   {self.get_quantity(each)}{empty_space_quantity} | {price}{empty_space_price}| {amount}{empty_space_amount}|\n',
                            f'                 |       | {second_row_1}{empty_space_second_row_1} |          |            |               |\n',
                            f'                 |       | {third_row_1}{empty_space_third_row_1} |          |            |               |\n',
                            '                 |       |                                                         |          |            |               |\n',
                            '                 +=======+=========================================================+==========+============+===============+\n']
                        if len(self.get_ID_and_quantity_dictionary()) > 1:
                            new_array_1[
                                len(new_array_1) - 1] = '                 +-------+---------------------------------------------------------+----------+------------+---------------+\n'
                        if len(self.get_ID_and_quantity_dictionary()) == count:
                            new_array_1[
                                len(new_array_1) - 1] = '                 +=======+=========================================================+==========+============+===============+\n'
                        price_array.append(''.join(new_array_1))

                    else:
                        empty_space_first_row_1 = ''
                        for i in range(55 - len(first_row_1)):
                            empty_space_first_row_1 += ' '

                        empty_space_second_row_1 = ''
                        for i in range(55 - len(second_row_1)):
                            empty_space_second_row_1 += ' '


                        new_array_1 = ['                 |       |                                                         |          |            |               |\n',
                                      f'                 |   {count}{empty_space_count} | {first_row_1}{empty_space_first_row_1} |   {self.get_quantity(each)}{empty_space_quantity} |  {price}{empty_space_price}| {amount}{empty_space_amount}|\n',
                                      f'                 |       | {second_row_1}{empty_space_second_row_1} |          |            |               |\n',
                                       '                 |       |                                                         |          |            |               |\n',
                                       '                 +=======+=========================================================+==========+============+===============+\n']
                        if len(self.get_ID_and_quantity_dictionary()) > 1:
                            new_array_1[len(new_array_1) - 1] = '                 +-------+---------------------------------------------------------+----------+------------+---------------+\n'
                        if len(self.get_ID_and_quantity_dictionary()) == count:
                            new_array_1[len(new_array_1) - 1] = '                 +=======+=========================================================+==========+============+===============+\n'
                        price_array.append(''.join(new_array_1))

            self.set_total_price(total_price)

            return price_array


        generate_price_array()
        second_array = []


        # for i in range(len(self.get_ID_and_quantity_dictionary())):
        #     second_array.append(''.join(generate_price_array()))
            # if len(self.get_ID_and_quantity_dictionary()) > 1:
            #     second_array[len(second_array) - 1] = '                 +-------+---------------------------------------------------------+----------+------------+---------------+\n'

        # print(''.join(second_array))

        subtotal = "{0:.2f}".format(self.get_total_price())
        if self.get_shipping_price() != '':
            total = float(self.get_shipping_price().replace("$", '')) + float(subtotal)
            amount_in_words = self.generate_amount_in_words(int(total)).split()
            total = "$" + "{0:.2f}".format(total)
        else:
            total = float(subtotal)
            amount_in_words = self.generate_amount_in_words(int(total)).split()
            total = "$" + subtotal

        subtotal = "$" + subtotal

        empty_space_subtotal = ''
        for i in range(14 - len(subtotal)):
            empty_space_subtotal += ' '

        empty_space_shipping_price = ''
        for i in range(14 - len(self.get_shipping_price())):
            empty_space_shipping_price += ' '

        empty_space_total = ''
        for i in range(14 - len(total)):
            empty_space_total += ' '



        third_array = [f'                 |                                                                            | Subtotal   | {subtotal}{empty_space_subtotal}|\n',
                        '                 |                                                                            +------------+---------------+\n',
                       f'                 |                                                                            | Shipping   | {self.get_shipping_price()}{empty_space_shipping_price}|\n',
                        '                 |                                                                            +------------+---------------+\n',
                       f'                 |                                                                            | Total      | {total}{empty_space_total}|\n',
                        '                 +----------------------------------------------------------------------------+------------+---------------+\n']

        total_price = str(int(self.get_total_price())).replace("$", '')
        amount_in_words[0] = amount_in_words[0].capitalize()

        length = len(self.generate_amount_in_words(total_price))


        if length > 82:
            first_row = []
            second_row = []

            length = 0

            for i in range(len(amount_in_words)):
                length = length + len(amount_in_words[i])
                if length + len(amount_in_words[i]) < 80:
                    first_row.append(amount_in_words[i])
                else:
                    second_row.append(amount_in_words[i])

            first_row = ' '.join(first_row)
            second_row = ' '.join(second_row) + '.'

            empty_space_first_row = ''
            for i in range(82 - len(first_row)):
                empty_space_first_row += ' '

            empty_space_second_row = ''
            for i in range(82 - len(second_row)):
                empty_space_second_row += ' '

            fourth_array = [
                            '                 |                                                                                                         |\n',
                           f'                 |     Amount in words: {first_row}{empty_space_first_row} |\n',
                           f'                 |                      {second_row}{empty_space_second_row} |\n',
                            '                 |                                                                                                         |\n'
                            '                 +----------------------------------------------------+----------------------------------------------------+\n', ]

        else:

            first_row = ' '.join(amount_in_words) + '.'

            empty_space_first_row = ''
            for i in range(82 - len(first_row)):
                empty_space_first_row += ' '



            fourth_array = ['                 |                                                                                                         |\n',
                           f'                 |     Amount in words: {first_row}{empty_space_first_row} |\n',
                            '                 |                                                                                                         |\n',
                            '                 +----------------------------------------------------+----------------------------------------------------+\n']

        fifth_array = ['                 |                                                    |                                                    |\n',
                       '                 | DIRECT ALL ENQUIRIES TO:                           | MAKE ALL CHECKS PAYABLE TO:                        |\n',
                       '                 |                                                    |                                                    |\n',
                       '                 +----------------------------------------------------+----------------------------------------------------+\n',
                       '                 |                                                    |                                                    |\n',
                      f"                 | np01cp4a220232@gmail.com                           | Nirajan's Electronics                              |\n",
                      f'                 | 98XXXXXXXX                                         | Account Number:  000000000111                      |\n',
                      f'                 |                                                    | Bhatbhateni, Kathmandu                             |\n',
                       '                 |                                                    |                                                    |\n',
                       '                 +----------------------------------------------------+----------------------------------------------------+\n',
                       '                 |                                                                                                         |\n',
                       '                 |                                                                                                         |\n',
                       '                 |                                                                                                         |\n',
                       '                 +=======+=================================================================================================+\n',
                       '                 |       |                                                                                                 |\n',
                       '                 | No.   |                                         Comments                                                |\n',
                       '                 |       |                                                                                                 |\n',
                       '                 +=======+=================================================================================================+\n',
                       '                 |       |                                                                                                 |\n',
                       '                 |   1   | Payment is due in a month.                                                                      |\n',
                       '                 |       |                                                                                                 |\n',
                       '                 +-------+-------------------------------------------------------------------------------------------------+\n',
                       '                 |       |                                                                                                 |\n',
                       '                 |   2   | Products bought are refundable within a week from purchase and will be refunded only if they    |\n',
                       '                 |       | are judged to be in a good condition by our technicians.                                        |\n',
                       '                 +-------+-------------------------------------------------------------------------------------------------+\n',
                       '                 |       |                                                                                                 |\n',
                       '                 |   3   | Please note down the invoice number in your payment method of choice.                           |\n',
                       '                 |       |                                                                                                 |\n',
                       '                 +-------+-------------------------------------------------------------------------------------------------+\n',
                       '                 |       |                                                                                                 |\n',
                       '                 |   4   | In case of damaged or faulty product, contact us immediately for replacement.                   |\n',
                       '                 |       |                                                                                                 |\n',
                       '                 +=======+=================================================================================================+\n',
                       '                 |                                                                                                         |\n',
                       '                 |                                      Thank you for your business.                                       |\n',
                       '                 |                                                                                                         |\n',
                       '                 +=========================================================================================================+']

        self.order_number_customer += 1
        self.set_number_of_bills_customer()

        return first_array + generate_price_array() + third_array + fourth_array + fifth_array