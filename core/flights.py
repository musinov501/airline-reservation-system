

def add_flights():
    print("===== ADD NEW FLIGHT =====")
    
    flights = []
    

    
    
    flight_code = input("Enter the flight code: ")
    airline = input("Enter the airline: ")
    origin  = input("Enter the origin: ")
    destination = input("Enter the destination: ")
    date = input("Enter the date(dd-mm-yyyy):")
    time = input('Enter the time(hh:mm)')
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
            print(f"Flight code {flight_code} already exists. ")
            return
        
    with open("storage/flights.txt", "a") as f:
        f.write(f"{flight_code}|{airline}|{origin}|{destination}|{date}|{time}|{capacity}|{available_seats}|{price}|{status}")
        
    print(f"Flight-{flight_code} was added successfully!")
    

def view_flights():
    pass