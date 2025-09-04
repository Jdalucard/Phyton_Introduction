class Smartphone:
    # constructor
    def __init__(self, brand, model, camera_front, camera_back):
        self.brand = brand
        self.model = model
        self.camera_front = camera_front
        self.camera_back = camera_back
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"{self.brand} {self.model} is now ON.")

    def turn_off(self):
        self.is_on = False
        print(f"{self.brand} {self.model} is now OFF.")


SmartphoneOne = Smartphone("Samsung", "Galaxy S21", "12 MP", "64 MP")
SmartphoneTwo = Smartphone("Apple", "iPhone 12", "12 MP", "12 MP")

print(SmartphoneOne.brand)  # Samsung
print(SmartphoneTwo.brand)  # Apple

SmartphoneOne.turn_on()
SmartphoneTwo.turn_off()
