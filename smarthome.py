
class House:
    
    def _init_(self, name="Akıllı Ev"):
        self.name = name
        self.rooms = {} 
        print(f"{self.name} oluşturuldu.")

    def add_room(self, room):
        self.rooms[room.name.lower()] = room
        print(f"-> ODA EKLENDİ: {room.name}")

    def display_status(self):
        print(f"\n--- {self.name} Durumu ---")
        for room_name, room in self.rooms.items():
            print(f"  > {room.name}:")
            if room.devices or room.sensors:
                print("    - Cihazlar:")
                for device in room.devices:
                    print(f"      - {device.name} ({device._class.name_}): {'Açık' if device.is_on else 'Kapalı'}")
                print("    - Sensörler:")
                for sensor in room.sensors:
                    
                    print(f"      - {sensor.name} ({sensor._class.name_}): Değer={sensor.get_reading()}")
            else:
                print("      - Cihaz veya Sensör yok.")
        print("----------------------------")

class Room:
    
    def _init_(self, name):
        self.name = name
        self.devices = []
        self.sensors = []

    def add_component(self, component):
        if isinstance(component, Device):
            self.devices.append(component)
        elif isinstance(component, Sensor):
            self.sensors.append(component)
        else:
            print(f"Hata: {component.name} bilinmeyen bir bileşen türü.")
        print(f"-> CİHAZ/SENSÖR EKLENDİ: {component.name} ({self.name})")

class Controller:
    
    def _init_(self, house):
        self.house = house

    def execute_rule(self, rule_name):
        
        if rule_name == "gece_modu":
            print("\n--- KONTROLCÜ: Gece Modu Etkinleştiriliyor ---")
            for room in self.house.rooms.values():
                for device in room.devices:
                    if isinstance(device, Light):
                        device.turn_off()
                    elif isinstance(device, AlarmSystem):
                        device.arm() 
        elif rule_name == "sıcaklık_kontrolü":
            print("\n--- KONTROLCÜ: Sıcaklık Kontrolü Başlatılıyor ---")
            for room in self.house.rooms.values():
                temp_sensor = next((s for s in room.sensors if isinstance(s, TemperatureSensor)), None)
                thermostat = next((d for d in room.devices if isinstance(d, Thermostat)), None)

                if temp_sensor and thermostat:
                    current_temp = temp_sensor.get_reading()
                    target_temp = 22.0
                    print(f"   - {room.name}: Mevcut Sıcaklık = {current_temp}°C, Hedef = {target_temp}°C")

                    if current_temp < target_temp - 1:
                        thermostat.set_temperature(target_temp)
                        thermostat.turn_on()
                        print(f"     -> {thermostat.name}: Isıtma Açıldı, {target_temp}°C'ye ayarlandı.")
                    elif current_temp > target_temp + 1:                      
                        thermostat.turn_off()
                        print(f"     -> {thermostat.name}: Kapatıldı (Sıcaklık yeterli/yüksek).")
                    else:
                        print(f"     -> {thermostat.name}: Sıcaklık ideal aralıkta.")



class Device:
    
    def _init_(self, name, room_name):
        self.name = name
        self.room_name = room_name
        self.is_on = False

    def turn_on(self):
        self.is_on = True
        print(f"{self.name} ({self.room_name}) açıldı.")

    def turn_off(self):
        self.is_on = False
        print(f"{self.name} ({self.room_name}) kapatıldı.")

class Sensor:
    
    def _init_(self, name, room_name):
        self.name = name
        self.room_name = room_name

    def get_reading(self):
        
        raise NotImplementedError("Alt sınıf kendi okuma yöntemini uygulamalı.")


class Light(Device):
    
    def _init_(self, name, room_name, brightness=0):
        super()._init_(name, room_name)
        self.brightness = brightness

    def set_brightness(self, level):
        self.brightness = max(0, min(100, level))
        self.is_on = self.brightness > 0
        print(f"{self.name} parlaklığı %{self.brightness} olarak ayarlandı.")

class Thermostat(Device):
    
    def _init_(self, name, room_name, temperature=20.0):
        super()._init_(name, room_name)
        self.temperature = temperature
        self.is_on = False 

    def set_temperature(self, temp):
        self.temperature = temp

class Camera(Device):
    
    def _init_(self, name, room_name):
        super()._init_(name, room_name)
        self.is_recording = False

    def start_recording(self):
        if self.is_on:
            self.is_recording = True
            print(f"{self.name} kayıt yapmaya başladı.")
        else:
            print(f"{self.name} kapalı, kayıt başlatılamadı.")

class AlarmSystem(Device):
    
    def _init_(self, name, room_name):
        super()._init_(name, room_name)
        self.is_armed = False # Kurulmuş durumu

    def arm(self):
        self.is_armed = True
        self.is_on = True 
        print(f"{self.name} KURULDU (ARMED).")

    def disarm(self):
        self.is_armed = False
        print(f"{self.name} DEVRE DIŞI BIRAKILDI (DISARMED).")



class TemperatureSensor(Sensor):
    
    def _init_(self, name, room_name, initial_temp=20.0):
        super()._init_(name, room_name)
        self.current_temp = initial_temp

    def get_reading(self):
        return self.current_temp

class MotionSensor(Sensor):
    
    def _init_(self, name, room_name):
        super()._init_(name, room_name)
        self.motion_detected = False

    def get_reading(self):
        
        import random
        self.motion_detected = random.choice([True, False, False]) 
        return "Hareket Algılandı" if self.motion_detected else "Hareket Yok"
