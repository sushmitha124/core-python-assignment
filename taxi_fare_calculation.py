def calculate_fare(trip_distances):
    base_fare = 50
    distance_rate = 10
    total_fare = 0
    for i, distance in enumerate(trip_distances):
        fare = base_fare + (distance * distance_rate)
        total_fare += fare
        print(f"Trip {i + 1}: ${fare}")
    print(f"Total Fare: ${total_fare}")
trips = eval(input("Enter distances in km"))
calculate_fare(trips)
