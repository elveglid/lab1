import json
import os

class VehicleError(Exception):
    def __init__(self, brand):
        self.brand = brand
    def __str__(self):
        return print(f'there is no vehicle under this name {self.brand}')

car = ['Bmw', 'Lada', 'Toyta', 'Kia']

class TransportVehicle:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed

    def display_vehicle(self):
        print(f"vehicle {self.brand}: {self.max_speed}")

class Car(TransportVehicle):
    def __init__(self, EngineVolume, Acceleration,brand):
        self.__EngineVolume = EngineVolume
        self.__Acceleration = Acceleration
        self.__brand = brand
    def unhaving(self):
        if not self.brand in car:
            raise VehicleError(self.brand)

    def fast_Acceleration(self):
        if self.__Acceleration < 2:
            print("This car fast")

class Helicopter(TransportVehicle):
    def __init__(self, numRotors, maxHeight):
        self.__numRotors = numRotors
        self.__maxHeight = maxHeight
    def quantity_numRotors(self):
        if self.__numRotors < 0:
            print(f"this can't be happening")

def readAnyFiles(filePath):
    fileName, fileExtension = os.path.splitext(filePath)
    #json
    if fileExtension == ".json":
        try:
            with open(filePath, 'r') as f:
                lines = f.readlines()
                for fileLine in lines:
                    dict_obj = json.loads(fileLine)
                    print(dict_obj)
        except FileNotFoundError:
            print("Wrong file path while reading file:", filePath)
# print an error message if the file extension is not supported
    else:
        print("Unsupported file extension:", fileExtension)
def write_to_json(obj, filePath):
    # проверка на правильность пути файла
    try:
        with open(filePath, "a") as file_stream:
            json.dump(obj.__dict__, file_stream)
            #добавляем разделение для красивой записи в файл
            file_stream.write('\n')
    except FileNotFoundError:
        print("Wrong file path while writing json:", filePath)

Car1 = Car(5, 3,'Bmw')
Helicopter1 = Helicopter(8, 6000)
write_to_json(Car1, "laba.json")
write_to_json(Helicopter1, "laba.json")
readAnyFiles("laba.json")
