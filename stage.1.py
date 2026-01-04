from abc import ABC, abstractmethod

class Device(ABC):
    def __init__(self, name):
        self._name = name
        self._status = False

    @abstractmethod
    def turn_on(self):
        pass

    @abstractmethod
    def turn_off(self):
        pass

    def is_on(self):
        return self._status


class Light(Device):
    def __init__(self, name, brightness=50):
        super().__init__(name)
        self._brightness = brightness

    def turn_on(self):
        self._status = True

    def turn_off(self):
        self._status = False


class Thermostat(Device):
    def __init__(self, name, temperature=22):
        super().__init__(name)
        self._temperature = temperature

    def turn_on(self):
        self._status = True

    def turn_off(self):
        self._status = False


class Room:
    def __init__(self, name):
        self._name = name
        self._devices = []

    def add_device(self, device):
        self._devices.append(device)


class SmartHome:
    def __init__(self):
        self._rooms = []

    def add_room(self, room):
        self._rooms.append(room)
