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
    def __init__(self, name):
        super().__init__(name)


class Thermostat(Device):
    def __init__(self, name, temperature=22):
        super().__init__(name)
        self._temperature = temperature

    def set_temperature(self, temp):
        self._temperature = temp
        print(self._name, "temperature:", temp)


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

    def list_devices(self):
        for d in self._devices:
            print(d._name, "ON" if d.is_on() else "OFF")


home = SmartHome()
light = Light("Living Room Light")
thermo = Thermostat("Thermostat")

home.add_device(light)
home.add_device(thermo)

home.turn_all_on()
thermo.set_temperature(24)
home.list_devices()
home.turn_all_off()
home.list_devices()
