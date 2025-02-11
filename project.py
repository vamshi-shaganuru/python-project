import random

# Sample data
trains = {
    "Rajdhani Express": {"Sleeper": 50, "AC": 30},
    "Shatabdi Express": {"Sleeper": 40, "AC": 20},
    "Duronto Express": {"Sleeper": 60, "AC": 25}
}

prices = {
    "Sleeper": 500,
    "AC": 1000
}

bookings = {}

def check_availability(train_name, class_type):
    if train_name in trains and class_type in trains[train_name]:
        return trains[train_name][class_type]
    return 0

def book_ticket(train_name, class_type, passenger_name):
    if check_availability(train_name, class_type) > 0:
        pnr = generate_pnr()
        fare = calculate_fare(train_name, class_type)
        bookings[pnr] = {
            "train_name": train_name,
            "class_type": class_type,
            "passenger_name": passenger_name,
            "fare": fare
        }
        trains[train_name][class_type] -= 1
        return pnr
    return None

def calculate_fare(train_name, class_type):
    base_price = prices[class_type]
    available_seats = trains[train_name][class_type]
    # Dynamic pricing: increase price if less than 10 seats are available
    if available_seats < 10:
        return base_price * 1.5
    return base_price

def generate_pnr():
    return random.randint(100000, 999999)

def display_booking_details(pnr):
    if pnr in bookings:
        booking = bookings[pnr]
        print(f"PNR: {pnr}")
        print(f"Train: {booking['train_name']}")
        print(f"Class: {booking['class_type']}")
        print(f"Passenger: {booking['passenger_name']}")
        print(f"Fare: {booking['fare']}")
    else:
        print("Booking not found.")

pnr = book_ticket("Rajdhani Express", "AC", "John Doe")
if pnr:
    display_booking_details(pnr)
else:
    print("No seats available.")
