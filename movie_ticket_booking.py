class Booking:
    def get_available_seats(total_seats, booked_seats):
        return [seat for seat in range(1, total_seats + 1) if seat not in booked_seats]

    def book_seat(booked_seats, seat):
        if seat in booked_seats:
            print(f"Seat {seat} is already booked.")
        else:
            booked_seats.append(seat)
    def cancel_seat(booked_seats, seat):
        if seat in booked_seats:
            booked_seats.remove(seat)
        else:
            print(f"Seat {seat} is not booked yet.")
total_seats = int(input("Enter total number of seats: "))
booked_seats = eval(input("Enter booked seats"))
book_seat_input = int(input("Enter the seat number to book: "))
cancel_seat_input = int(input("Enter the seat number to cancel: "))

obj=Booking
obj.book_seat(booked_seats, book_seat_input)
available_seats = obj.get_available_seats(total_seats, booked_seats)
print("Available seats:", available_seats)
