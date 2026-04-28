import random

class Battery:
    def __init__(self):
        self.soc = 50
        self.voltage = 350
        self.temp = 30
        self.health = 100

    def status(self):
        return f"SOC: {self.soc:.1f}% | Voltage: {self.voltage:.1f}V | Temp: {self.temp:.1f}°C | Health: {self.health:.1f}%"

    def apply_action(self, action):
        if action == "charge":
            self.soc += random.uniform(5, 10)
            self.voltage += random.uniform(5, 10)
            self.temp += random.uniform(2, 5)

        elif action == "discharge":
            self.soc -= random.uniform(5, 10)
            self.voltage -= random.uniform(5, 10)
            self.temp += random.uniform(1, 3)

        elif action == "cool":
            self.temp -= random.uniform(5, 10)

        elif action == "idle":
            self.temp += random.uniform(-1, 1)

        if self.temp > 45 or self.soc > 90:
            self.health -= random.uniform(0.5, 2)

    def check_failure(self):
        if self.soc >= 100:
            return "Overcharge!"
        if self.soc <= 0:
            return "Deep Discharge!"
        if self.temp >= 60:
            return "Overheat!"
        if self.voltage < 250 or self.voltage > 450:
            return "Voltage Out of Range!"
        if self.health <= 0:
            return "Battery Dead!"
        return None
