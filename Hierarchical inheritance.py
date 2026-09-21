class Vehicle:
    """Base class - the root of the hierarchy."""
    def __init__ (self, brand, model, year, base_price_per_day):
        self.brand=brand
        self.model=model
        self.year=year
        self.base_price_per_day=base_price_per_day
        
    def rental_cost(self, days):
        return self.base_price_per_day*days
    
    def display_info(self):
        print(f"{self.year} {self.brand} {self.model}")
        
    def __str__ (self):
        return f"{self.brand} {self.model} ({self.year})"

class Car(Vehicle):
    def __init__(self, brand, model, year, base_price_per_day, sets):
        super().__init__(brand, model, year, base_price_per_day)
        self.sets=sets
    def rental_cost(self, days):
        cost=super().rental_cost(days)
        if self.sets >= 6:
            cost += 15*days
        return cost
    def display_info(self):
        super().display_info()
        print(f"  Type:Car | Sets: {self.sets}")

class Bike(Vehicle):
    def __init__(self, brand, model, year, base_price_per_day, has_gear):
        super().__init__(brand, model, year, base_price_per_day)
        self.has_gear=has_gear

    def rental_cost(self, days):
        cost=super().rental_cost(days)
        return cost*0.5

    def display_info(self):
        super().display_info()
        gear="Geard" if self.has_gear else "Non-geared"
        print(f"  Type: Bike | {gear}")

class Truck(Vehicle):
    def __init__(self, brand, model, year, base_price_per_day, capacity_tons):
        super().__init__(brand, model, year, base_price_per_day)
        self.capacity_tons=capacity_tons

    def rental_cost(self, days):
        cost=super().rental_cost(days)
        return cost + (self.capacity_tons*20*days)

    def display_info(self):
        super().display_info()
        print(f"  Type:Truck | Truck | Capacity: {self.capacity_tons} tons")
        
if __name__ == "__main__":
    print("---Vehicle Rental Details---")
    car=Car("Toyota", "Sienna", 2023, 50000, 7)
    bike=Bike("Royel Enfield", "Bullet 350", 2022, 137640, True)
    truck=Truck("Volvo", "FH16", 2021, 100, 10)
                
    days=5
                
    car.display_info()
    print(f"Rental cost for{days}days: ${car.rental_cost(days)}\n")

    bike.display_info()
    print(f"Rental cost for{days}days: ${bike.rental_cost(days)}\n")
                
    truck.display_info()
    print(f"Rental cost for{days}days: ${truck.rental_cost(days)}\n")
                            
                



                
                
