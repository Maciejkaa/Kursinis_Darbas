from abc import ABC, abstractmethod
import random
import datetime

class MealPreference(ABC):
    @abstractmethod
    def get_description(self):
        pass

class VegetarianMeal(MealPreference):
    def get_description(self):
        return "Vegetarian Meal"

class KosherMeal(MealPreference):
    def get_description(self):
        return "Kosher Meal"

class RegularMeal(MealPreference):
    def get_description(self):
        return "Regular Meal"

class ImportFromFile:
    _instance = None

    def __new__(cls):
        if cls._instance is None:
            cls._instance = super().__new__(cls)
            cls._instance.__initialized = False
        return cls._instance

    def __init__(self):
        if not self.__initialized:
            self.__city_to_airline = {}
            self.__load_city_to_airline()
            self.__initialized = True

    def __load_city_to_airline(self):
        with open("input.txt", "r") as file:
            for line in file:
                city_from, city_to, airline, gate = line.strip().split(",")
                if city_from not in self.__city_to_airline:
                    self.__city_to_airline[city_from] = {}
                if city_to not in self.__city_to_airline[city_from]:
                    self.__city_to_airline[city_from][city_to] = {}
                self.__city_to_airline[city_from][city_to][gate] = airline

    def get_city_to_airline(self):
        return self.__city_to_airline


class FlightInformation:
    def __init__(self, city_to_airline):
        self.__city_to_airline = city_to_airline

    def __validate_name(self, name):
        return name.isalpha()

    def __validate_surname(self, surname):
        return surname.isalpha()

    def __validate_starting_point(self, city_from):
        return city_from in self.__city_to_airline

    def __get_first_gate(self, city_from, city_to):
        gates = self.__city_to_airline[city_from][city_to].keys()
        return next(iter(gates))

    def __get_airline(self, city_from, city_to, gate):
        return self.__city_to_airline[city_from][city_to][gate]

    def name(self):
        while True:
            name = input("Write your name: ")
            if self.__validate_name(name):
                return name
            else:
                print("Please enter a valid name.")

    def surname(self):
        while True:
            surname = input("Write your surname: ")
            if self.__validate_surname(surname):
                return surname
            else:
                print("Please enter a valid surname.")

    def starting_point(self):
        while True:
            city_from = input("Enter the capital city in Europe you want to fly from: ")
            if self.__validate_starting_point(city_from):
                return city_from
            else:
                print("Sorry, we don't fly from this city yet.")

    def city_and_airline(self, city_from):
        while True:
            city_to = input("Enter the capital city in Europe you want to fly to: ")
            if city_to in self.__city_to_airline[city_from]:
                gate = self.__get_first_gate(city_from, city_to)
                airline = self.__get_airline(city_from, city_to, gate)
                return f"{city_from} - {city_to} with {airline}. Gate: {gate}."
            else:
                print("Sorry, we don't fly to this city.")

    def select_flight_class(self):
        while True:
            flight_class = input("Select your desired class (Economy/Business/First): ").lower()
            if flight_class in ['economy', 'business', 'first']:
                if flight_class == 'economy':
                    return EconomyClass(self.__city_to_airline)
                elif flight_class == 'business':
                    return BusinessClass(self.__city_to_airline)
                elif flight_class == 'first':
                    return FirstClass(self.__city_to_airline)
            else:
                print("Invalid selection. Please choose from Economy, Business, or First Class.")

    def select_meal_preference(self):
        while True:
            preference = input("Select your meal preference (Vegetarian/Kosher/Regular): ").lower()
            if preference in ['vegetarian', 'kosher', 'regular']:
                if preference == 'vegetarian':
                    return VegetarianMeal()
                elif preference == 'kosher':
                    return KosherMeal()
                elif preference == 'regular':
                    return RegularMeal()
            else:
                print("Invalid selection. Please choose from Vegetarian, Kosher, or Regular.")

    def seat(self):
        while True:
            try:
                seat_number = int(input("Enter your desired seat number (1-99): "))
                if 0 < seat_number <= 99:
                    return f"{seat_number:02d}"
                else:
                    print("Please enter a valid seat number between 1 and 99.")
            except ValueError:
                print("Please enter a valid integer seat number.")

    def ticket_number(self):
        return str(random.randint(100000000000, 999999999999))

class EconomyClass(FlightInformation):
    def __init__(self, city_to_airline):
        super().__init__(city_to_airline)
        self._baggage_allowance = "1 cabin bag (max. 8kg)"

    def get_baggage_allowance(self):
        return self._baggage_allowance

class BusinessClass(FlightInformation):
    def __init__(self, city_to_airline):
        super().__init__(city_to_airline)
        self._baggage_allowance = "1 cabin bag (max. 8kg) + 1 checked bag (max. 20kg)"

    def get_baggage_allowance(self):
        return self._baggage_allowance

class FirstClass(FlightInformation):
    def __init__(self, city_to_airline):
        super().__init__(city_to_airline)
        self._baggage_allowance = "2 cabin bags (max. 10kg each) + 1 checked bag (max. 25kg each)"

    def get_baggage_allowance(self):
        return self._baggage_allowance

class TimeInfo:
    def date(self):
        while True:
            departure_date = input("Select your departure date (YYYY-MM-DD): ")
            try:
                departure_date = datetime.datetime.strptime(departure_date, '%Y-%m-%d')
                if departure_date > datetime.datetime.today():
                    return departure_date.strftime('%Y-%m-%d')
                else:
                    print("Time travel is impossible (for now at least), so choose a different date.")
            except ValueError:
                print("Please enter a valid date in YYYY-MM-DD format.")

    def boarding_time(self):
        while True:
            wanted_time = input("Select your preferred time of departure (AM/PM): ")
            if wanted_time.upper() == "AM" or wanted_time.upper() == "PM":
                boarding_time = input("Enter the boarding time (HH:MM): ")
                try:
                    datetime.datetime.strptime(boarding_time, '%I:%M')
                    return boarding_time + " " + wanted_time.upper()
                except ValueError:
                    print("Please enter a valid time in HH:MM format.")
            else:
                print("Please enter AM or PM.")

class Fly:
    @staticmethod
    def execute(city_to_airline):
        with open("output.txt", "a") as file:
            flight_info = FlightInformation(city_to_airline)
            name = flight_info.name()
            surname = flight_info.surname()
            city_from = flight_info.starting_point()
            city_and_airline = flight_info.city_and_airline(city_from)
            flight_class = flight_info.select_flight_class()
            meal_preference = flight_info.select_meal_preference()
            seat = flight_info.seat()
            date = TimeInfo().date()
            boarding_time = TimeInfo().boarding_time()
            ticket_number = flight_info.ticket_number()

            file.write(f"Name: {name}\n")
            file.write(f"Surname: {surname}\n")
            file.write(f"Departure City: {city_from}\n")
            file.write(f"Flight Details: {city_and_airline}\n")
            file.write(f"Flight Class: {flight_class.__class__.__name__}\n")
            file.write(f"Meal Preference: {meal_preference.get_description()}\n")
            file.write(f"Baggage Allowance: {flight_class.get_baggage_allowance()}\n")
            file.write(f"Seat: {seat}\n")
            file.write(f"Departure Date: {date}\n")
            file.write(f"Boarding Time: {boarding_time}\n")
            file.write(f"Ticket Number: {ticket_number}\n\n")

class DeleteBooking:
    @staticmethod
    def execute(name_to_delete):
        with open("output.txt", "r+") as file:
            lines = file.readlines()
            updated_lines = []
            booking_found = False
            i = 0
            while i < len(lines):
                if f"Name: {name_to_delete}" in lines[i]:
                    booking_found = True
                    while i < len(lines) and lines[i].strip() != "":
                        i += 1
                else:
                    updated_lines.append(lines[i])
                i += 1
            file.seek(0)
            file.truncate()
            file.writelines(updated_lines)
        if booking_found:
            print("Booking deleted successfully!")
        else:
            print("Booking not found!")

class ClearBookingData:
    @staticmethod
    def execute():
        with open("output.txt", "w") as file:
            file.write("")
        print("All booking data cleared successfully!")

class Initialization:
    def __init__(self):
        self.__importer = ImportFromFile()

    def run_code(self):
        while True:
            choice = input("Select what you want to do (Fly, Delete, Clear, Exit): ")
            if choice == "Fly":
                Fly.execute(self.__importer.get_city_to_airline())
            elif choice == "Delete":
                name_to_delete = input("Enter the name to delete: ")
                DeleteBooking.execute(name_to_delete)
            elif choice == "Clear":
                ClearBookingData.execute()
            elif choice == "Exit":
                print("Goodbye!")
                break
            else:
                print("Your input is incorrect, try again.")

initializer = Initialization()
initializer.run_code()
