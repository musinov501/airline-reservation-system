def add_flights():
    print("===== ADD NEW FLIGHT =====")

    flight_code = input("Enter the flight code: ")
    airline = input("Enter the airline: ")
    origin  = input("Enter the origin: ")
    destination = input("Enter the destination: ")
    date = input("Enter the date(dd-mm-yyyy): ")
    time = input("Enter the time(hh:mm): ")
    capacity = int(input("Enter the capacity: "))
    available_seats = int(input("Enter the available seats: "))
    price = float(input("Enter the price: "))
    status = input("Enter the status (on-time, delayed, cancelled): ")

    try:
        with open("storage/flights.txt", "r") as f:
            flights = f.readlines()
    except FileNotFoundError:
        flights = []

    for line in flights:
        existing_flight = line.strip().split('|')
        if existing_flight[0] == flight_code:
            print(f"Flight code {flight_code} already exists.")
            input("Press Enter to return to the dashboard...")
            return

    with open("storage/flights.txt", "a") as f:
        f.write(f"{flight_code}|{airline}|{origin}|{destination}|{date}|{time}|{capacity}|{available_seats}|{price}|{status}\n")

    print(f"Flight {flight_code} was added successfully!")
    input("Press Enter to return to the dashboard...")



def view_flights():
    print("===== VIEW FLIGHTS =====")
    try:
        with open("storage/flights.txt", "r") as f:
            flights = f.readlines()
    except FileNotFoundError:
        flights = []
    
    if not flights:
        print("No flights available.")
        input("Press Enter to return to the dashboard...")
        return

    print("+" * 120)
    print("Flight Code | Airline | Origin | Destination | Date | Time | Capacity | Available | Price | Status")
    print("+" * 120)

    for line in flights:
        flight = line.strip().split('|')
        print(" |   ".join(flight))

    print("+" * 120)
    input("Press Enter to return to the dashboard...")
