from core.flights import view_flights
from core.bookings import book_flight,view_my_bookings




def simple_user_dashboard():
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("                                   SIMPLE USER DASHBOARD                                            ")
    print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
    print("1. View available flights")
    print("2. Book a flight")
    print("3. View my bookings")
    print("4. Logout")
    
    
    
    while True:
        choice = input("Enter your choice: ")
        
        if choice == '1':
            view_flights()
        elif choice == '2':
            book_flight()
        elif choice == '3':
            view_my_bookings()
        elif choice == '4':
            print("Logging out...")
            return
        else:
            print("Invalid choice. Please try again.")