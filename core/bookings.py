from core.flights import view_flights


def book_flight():
    print("===== BOOK A FLIGHT =====")
    username = input("Enter your username: ")
    flight_code = input("Enter the flight code you want to book: ")

    try:
        with open("storage/flights.txt", "r") as f:
            flights = f.readlines()
    except FileNotFoundError:
        flights = []

    updated_flights = []
    flight_found = False
    seat_booked = False
    
    for line in flights:
        flight = line.strip().split('|')
        
        
        if flight[0] == flight_code:
            flight_found = True
            available_seats = int(flight[7])
            
            if available_seats > 0:
                available_seats -= 1
                flight[7] = str(available_seats)
                seat_booked = True
                print("Seat booked successfully!")
            else:
                print("Sorry, no seats available.")
                return
            
            updated_flights.append('|'.join(flight) + '\n')
        else:
            updated_flights.append(line)
            
    if not flight_found:
        print("Flight not found.")
        return
    
    with open("storage/flights.txt", "w") as f:
        f.writelines(updated_flights)
        
    with open("storage/bookings.txt", "a") as b:
        b.write(f"{username}|{flight_code}\n")
        
    print(f"Booking completed for flight {flight_code}.")
    input("Press Enter to return to the dashboard...")
        
    
def view_my_bookings():
    print("===== VIEW MY BOOKINGS =====")
    username = input("Enter your username: ")
    
    try:
        with open("storage/bookings.txt", "r") as b:
            bookings = b.readlines()
    except FileNotFoundError:
        bookings = []
        
    for line in bookings:
        booking = line.strip().split('|')
        if booking[0] == username:
            print(f"Booked flight: {booking[1]}")
    input("Press Enter to return to the dashboard...")
    
    
def view_bookings():
    print("===== VIEW ALL BOOKINGS =====")
    
    try:
        with open("storage/bookings.txt", "r") as b:
            bookings = b.readlines()
    except FileNotFoundError:
        bookings = []
        
    if not bookings:
        print("No bookings found.")
        input("Press Enter to return to the dashboard...")
        return
    
    print("+" * 50)
    print("Username | Flight Code")
    print("+" * 50)
    
    for line in bookings:
        booking = line.strip().split('|')
        print(f"{booking[0]} | {booking[1]}")
        
    print("+" * 50)
    input("Press Enter to return to the dashboard...")
    
