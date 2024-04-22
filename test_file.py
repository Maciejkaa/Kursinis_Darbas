import unittest
import datetime
from unittest.mock import Mock, patch, mock_open
from main import ImportFromFile, FlightInformation, EconomyClass, BusinessClass, FirstClass, TimeInfo, Fly, DeleteBooking, ClearBookingData, Initialization, VegetarianMeal, KosherMeal, RegularMeal

class TestFlightBooking(unittest.TestCase):
    def setUp(self):
        self.importer = Mock(spec=ImportFromFile)
        self.importer.get_city_to_airline.return_value = {
            'Paris': {'London': {'90': 'AirFrance'}}
        }

        self.original_input = __builtins__.input
        __builtins__.input = self.mock_input

    def tearDown(self):
        __builtins__.input = self.original_input

    def mock_input(self, prompt):
        if "Write your name" in prompt:
            return "John"
        elif "Write your surname" in prompt:
            return "Tester"
        elif "Enter the capital city in Europe you want to fly from" in prompt:
            return "Paris"
        elif "Enter the capital city in Europe you want to fly to" in prompt:
            return "London"
        elif "Select your desired class" in prompt:
            return "economy"
        elif "Select your meal preference" in prompt:
            return "vegetarian"
        elif "Enter your desired seat number" in prompt:
            return "10"
        elif "Select your departure date (YYYY-MM-DD)" in prompt:
            return "2024-12-31"
        elif "Select your preferred time of departure (AM/PM)" in prompt:
            return "AM"
        elif "Enter the boarding time (HH:MM)" in prompt:
            return "09:30"
        elif "Enter the name to delete" in prompt:
            return "John"
        else:
            raise ValueError("Unhandled prompt in test: {}".format(prompt))

    def test_flight_information(self):
        flight_info = FlightInformation(self.importer.get_city_to_airline())
        self.assertEqual(flight_info.name(), "John")
        self.assertEqual(flight_info.surname(), "Tester")
        self.assertEqual(flight_info.starting_point(), "Paris")
        self.assertEqual(flight_info.city_and_airline("Paris"), "Paris - London with AirFrance. Gate: 90.")
        self.assertEqual(flight_info.select_flight_class().__class__.__name__, "EconomyClass")
        self.assertEqual(flight_info.select_meal_preference().__class__.__name__, "VegetarianMeal")
        self.assertEqual(flight_info.seat(), "10")
        self.assertRegex(flight_info.ticket_number(), r"\d{12}")

    def test_economy_class(self):
        economy_class = EconomyClass(self.importer.get_city_to_airline())
        self.assertEqual(economy_class.get_baggage_allowance(), "1 cabin bag (max. 8kg)")

    def test_business_class(self):
        business_class = BusinessClass(self.importer.get_city_to_airline())
        self.assertEqual(business_class.get_baggage_allowance(), "1 cabin bag (max. 8kg) + 1 checked bag (max. 20kg)")

    def test_first_class(self):
        first_class = FirstClass(self.importer.get_city_to_airline())
        self.assertEqual(first_class.get_baggage_allowance(), "2 cabin bags (max. 10kg each) + 1 checked bag (max. 25kg each)")

    def test_time_info(self):
        time_info = TimeInfo()
        self.assertIsInstance(datetime.datetime.strptime(time_info.date(), '%Y-%m-%d'), datetime.datetime)
        self.assertRegex(time_info.boarding_time(), r"\d{2}:\d{2} (AM|PM)")

    @patch('builtins.open', new_callable=mock_open)
    def test_fly(self, mock_open):
        Fly.execute(self.importer.get_city_to_airline())
        mock_open.assert_called_once_with("output.txt", "a")

    @patch('builtins.open', new_callable=mock_open)
    def test_delete_booking(self, mock_open):
        DeleteBooking.execute("John")
        mock_open.assert_called_once_with("output.txt", "r+")

    @patch('builtins.open', new_callable=mock_open)
    def test_clear_booking_data(self, mock_open):
        ClearBookingData.execute()
        mock_open.assert_called_once_with("output.txt", "w")

    def test_boarding_time(self):
        time_info = TimeInfo()
        self.assertRegex(time_info.boarding_time(), r"\d{2}:\d{2} (AM|PM)")

if __name__ == '__main__':
    unittest.main()
