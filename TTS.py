class Destination:
    def __init__(self, name, location, price, description):
        self.name = name
        self.location = location
        self.price = price
        self.description = description
        self.reviews = []

    def display_info(self):
        print(f"\nName: {self.name}")
        print(f"Location: {self.location}")
        print(f"Price: ${self.price}")
        print(f"Description: {self.description}")

class Review:
    def __init__(self, destination, customer_name, review_text):
        self.destination = destination
        self.customer_name = customer_name
        self.review_text = review_text

    def display_review(self):
        print(f"\nReview for {self.destination.name} by {self.customer_name}:")
        print(f"   - {self.review_text}")

class Booking:
    def __init__(self, destination, customer_name, num_people):
        self.destination = destination
        self.customer_name = customer_name
        self.num_people = num_people
        self.total_price = num_people * destination.price

    def display_booking_details(self):
        print(f"\nBooking for {self.customer_name} at {self.destination.name}")
        print(f"Number of people: {self.num_people}")
        print(f"Total Price: ${self.total_price}")

class TravelPackage:
    def __init__(self):
        self.destinations = []

    def add_destination(self, destination):
        self.destinations.append(destination)

    def get_destination(self, index):
        if 0 <= index < len(self.destinations):
            return self.destinations[index]
        return None

class Itinerary:
    def __init__(self, destination, customer_name, activities):
        self.destination = destination
        self.customer_name = customer_name
        self.activities = activities

    def display_itinerary(self):
        print(f"\nItinerary for {self.customer_name} visiting {self.destination.name}:")
        for activity in self.activities:
            print(f" - {activity}")

class User:
    def __init__(self, username, password, user_type):
        self.username = username
        self.password = password
        self.user_type = user_type  # admin or customer

class TravelSystem:
    def __init__(self):
        self.travel_package = TravelPackage()
        self.bookings = []
        self.users = [User("admin", "admin123", "admin")]  # Predefined user for simplicity

    def authenticate(self):
        print("\n--- User Authentication ---")
        username = input("Enter username: ")
        password = input("Enter password: ")
        for user in self.users:
            if user.username == username and user.password == password:
                return user
        print("Invalid username or password!")
        return None

    def view_destinations(self):
        print("\n--- Available Destinations ---")
        for index, destination in enumerate(self.travel_package.destinations, 1):
            destination.display_info()

    def add_destination(self):
        name = input("Enter destination name: ")
        location = input("Enter location: ")
        price = float(input("Enter price per person: "))
        description = input("Enter a description: ")
        destination = Destination(name, location, price, description)
        self.travel_package.add_destination(destination)
        print(f"\nDestination {name} added successfully!")

    def search_by_name(self):
        search_term = input("\nEnter the name of the destination you want to search: ").lower()
        found = False
        for dest in self.travel_package.destinations:
            if search_term in dest.name.lower():
                found = True
                dest.display_info()
        if not found:
            print("No destination found matching that name.")

    def search_by_price(self):
        min_price = float(input("\nEnter the minimum price: "))
        max_price = float(input("Enter the maximum price: "))
        found = False
        for dest in self.travel_package.destinations:
            if min_price <= dest.price <= max_price:
                found = True
                dest.display_info()
        if not found:
            print("No destinations found in the specified price range.")

    def modify_booking(self):
        if not self.bookings:
            print("\nNo bookings available to modify.")
            return
        self.view_bookings()
        booking_index = int(input("\nEnter the booking number to modify: ")) - 1
        if 0 <= booking_index < len(self.bookings):
            booking = self.bookings[booking_index]
            print(f"\nCurrent booking for {booking.customer_name}: {booking.destination.name}, {booking.num_people} people")
            new_people = int(input("Enter the new number of people: "))
            booking.num_people = new_people
            booking.total_price = new_people * booking.destination.price
            print("Booking modified successfully!")
            booking.display_booking_details()
        else:
            print("Invalid booking choice.")

    def cancel_booking(self):
        if not self.bookings:
            print("\nNo bookings available to cancel.")
            return
        self.view_bookings()
        booking_index = int(input("\nEnter the booking number to cancel: ")) - 1
        if 0 <= booking_index < len(self.bookings):
            canceled_booking = self.bookings.pop(booking_index)
            print(f"\nBooking for {canceled_booking.customer_name} has been canceled.")
        else:
            print("Invalid booking choice.")

    def leave_review(self):
        self.view_destinations()
        if not self.travel_package.destinations:
            return
        choice = int(input("\nEnter the destination number to review: ")) - 1
        destination = self.travel_package.get_destination(choice)
        if destination:
            customer_name = input("Enter your name: ")
            review_text = input("Enter your review: ")
            review = Review(destination, customer_name, review_text)
            destination.reviews.append(review)
            print("Review added successfully!")
        else:
            print("Invalid destination choice.")

    def view_reviews(self):
        self.view_destinations()
        if not self.travel_package.destinations:
            return
        choice = int(input("\nEnter the destination number to view reviews: ")) - 1
        destination = self.travel_package.get_destination(choice)
        if destination and hasattr(destination, 'reviews'):
            if destination.reviews:
                for review in destination.reviews:
                    review.display_review()
            else:
                print("No reviews available for this destination.")
        else:
            print("Invalid destination choice.")

    def apply_discount(self, booking):
        if booking.num_people >= 5:
            discount = 0.1  # 10% discount for group bookings
            booking.total_price *= (1 - discount)
            print(f"A discount of 10% has been applied! New total price: ${booking.total_price}")
        else:
            print("No discount applied.")

    def make_payment(self, booking):
        print("\nChoose a payment method:")
        print("1. Credit Card")
        print("2. Debit Card")
        print("3. PayPal")
        choice = input("Enter your choice: ")

        if choice in ['1', '2', '3']:
            print(f"\nPayment of ${booking.total_price} successful! Booking confirmed.")
        else:
            print("Invalid payment method.")

    def create_itinerary(self):
        self.view_destinations()
        if not self.travel_package.destinations:
            return
        choice = int(input("\nEnter the destination number to create itinerary for: ")) - 1
        destination = self.travel_package.get_destination(choice)
        if destination:
            customer_name = input("Enter your name: ")
            activities = []
            while True:
                activity = input("Enter an activity (or type 'done' to finish): ")
                if activity.lower() == 'done':
                    break
                activities.append(activity)
            itinerary = Itinerary(destination, customer_name, activities)
            print("\nItinerary created successfully!")
            itinerary.display_itinerary()
        else:
            print("Invalid destination choice.")

    def view_bookings(self):
        if not self.bookings:
            print("\nNo bookings available.")
        else:
            for index, booking in enumerate(self.bookings, 1):
                booking.display_booking_details()

    def view_system_stats(self):
        total_bookings = len(self.bookings)
        total_revenue = sum(booking.total_price for booking in self.bookings)
        print(f"\nSystem Statistics:")
        print(f"Total Bookings: {total_bookings}")
        print(f"Total Revenue: ${total_revenue}")

    def start(self):
        while True:
            print("\n--- Travel and Tourism System ---")
            print("1. Login (Admin/Customer)")
            print("2. View Destinations")
            print("3. Add Destination (Admin only)")
            print("4. Modify Booking (Admin only)")
            print("5. Cancel Booking")
            print("6. Leave a Review")
            print("7. View Reviews")
            print("8. Apply Discount and Make Payment")
            print("9. Create Itinerary")
            print("10. View System Stats (Admin only)")
            print("11. Exit")

            choice = input("\nEnter your choice: ")

            user = self.authenticate()
            if user:
                if user.user_type == "admin":
                    if choice == '1':
                        self.add_destination()
                    elif choice == '2':
                        self.modify_booking()
                    elif choice == '3':
                        self.view_system_stats()
                elif user.user_type == "customer":
                    if choice == '4':
                        self.view_destinations()
                    elif choice == '5':
                        self.modify_booking()
                    elif choice == '6':
                        self.cancel_booking()
                    elif choice == '7':
                        self.leave_review()
                    elif choice == '8':
                        self.view_reviews()

            elif choice == '11':
                break
            else:
                print("Invalid choice, please try again.")
