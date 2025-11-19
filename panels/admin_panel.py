from core.flights import view_flights, add_flights
from core.utils import view_users
from core.bookings import view_bookings


def admin_dashboard():
    while True:
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("                                     ADMIN DASHBOARD                                               ")
        print("+++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++++")
        print("1. Add new flight")
        print("2. View all flights")
        print("3. View all users")
        print("4. View all bookings")
        print("5. Logout")
        
        
        choice = input("Enter your choice: ")
        
        if choice == '1':
            return add_flights()
        elif choice == '2':
            return view_flights()
        elif choice == '3':
            return view_users()
        elif choice == '4':
            return view_bookings()
        elif choice == '5':
            print("Logging out...")
            break
        else:
            print("Invalid choice. Please try again.")
            
            
