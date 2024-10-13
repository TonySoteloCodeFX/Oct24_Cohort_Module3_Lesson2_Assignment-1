flight_itineraries = [("Alice", "New York", "London"), ("Bob", "Tokyo", "San Francisco")]

def format_itineraries(flight_itineraries):
    for index, itinerary in enumerate(flight_itineraries):
        print("-" * 50)
        name = itinerary[0]
        departure_city = itinerary[1]
        arrival_city = itinerary[2]
        print(f"Itinerary {index + 1}: {name} - From {departure_city} to {arrival_city}")
    return "-" * 50

print(format_itineraries(flight_itineraries))