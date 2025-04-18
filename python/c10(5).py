#Write a Class ‘Train’ which has methods to book a ticket, get status (no of seats) and get fare information of train running under Indian Railways.
class Train:
    def __init__(self, train_name, total_seats, fare_per_ticket):
        self.train_name = train_name
        self.total_seats = total_seats
        self.available_seats = total_seats
        self.fare_per_ticket = fare_per_ticket
    
    def book_ticket(self, num_tickets):
        if 0 < num_tickets <= self.available_seats:
            self.available_seats -= num_tickets
            print(f"Successfully booked {num_tickets} ticket(s) for {self.train_name}.")
        else:
            print(f"Sorry, could not book {num_tickets} ticket(s). Available seats: {self.available_seats}")
    
    def get_status(self):
        print(f"Total seats available in {self.train_name}: {self.total_seats}")
        print(f"Available seats: {self.available_seats}")
    
    def get_fare(self):
        print(f"Current fare per ticket for {self.train_name}: {self.fare_per_ticket}")


if __name__ == "__main__":
    train1 = Train("Rajdhani Express", 200, 1500)
    train1.get_status()
    train1.get_fare()
    train1.book_ticket(5)
    train1.get_status()
    train1.book_ticket(10)
    train1.get_status()
