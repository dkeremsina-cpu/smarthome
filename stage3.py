class Device:
    def __init__(self, name):
        self._name = name
        self.__status = False

    def turn_on(self):
        self.__status = True
        print(self._name, "ON")

    def turn_off(self):
        self.__status = False
        print(self._name, "OFF")

    def is_on(self):
        return self.__status


class Light(Device):
    def __init__(self, name, brightness=50):
        super().__init__(name)
        self._brightness = brightness

    def set_brightness(self, value):
        if value < 0:
            value = 0
        if value > 100:
            value = 100
        self._brightness = value
        print(self._name, "brightness:", self._brightness)


class Thermostat(Device):
    def __init__(self, name, temperature=22):
        super().__init__(name)
        self._temperature = temperature

    def set_temperature(self, temp):
        self._temperature = temp
        print(self._name, "temperature:", temp)

    def auto_adjust(self):
        if self._temperature < 18:
            print("Heating ON")
        elif self._temperature > 26:
            print("Cooling ON")
        else:
            print("Temperature OK")


class SmartHome:
    def __init__(self):
        self._devices = []

    def add_device(self, device):
        self._devices.append(device)

    def turn_all_on(self):
        for d in self._devices:
            d.turn_on()

    def turn_all_off(self):
        for d in self._devices:
            d.turn_off()

    def night_mode(self):
        print("Night Mode")
        for d in self._devices:
            if isinstance(d, Light):
                d.turn_off()

    def energy_saver(self):
        print("Energy Saver")
        for d in self._devices:
            if isinstance(d, Thermostat):
                d.set_temperature(22)


home = SmartHome()
light1 = Light("Bedroom Light", 80)
light2 = Light("Kitchen Light", 60)
thermo = Thermostat("Thermostat", 27)

home.add_device(light1)
home.add_device(light2)
home.add_device(thermo)

home.turn_all_on()
thermo.auto_adjust()
home.night_mode()
home.energy_saver()
