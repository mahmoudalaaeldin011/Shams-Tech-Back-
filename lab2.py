class SolarPanel ():
    def __init__(self , brand : str , power_w : float , price : float):
        self.brand = brand
        self.power_w = power_w
        self.price = price
    def calculate_cost_per_watt (self):
        return self.price / self.power_w


panel= SolarPanel("Mahmoud", 50 , 1000)
print(panel)
print(panel.brand)
print(panel.calculate_cost_per_watt())