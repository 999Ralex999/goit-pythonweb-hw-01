from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import Protocol
from logger import logger


class Vehicle(ABC):
    def __init__(self, make: str, model: str, spec: str) -> None:
        self.make = make
        self.model = model
        self.spec = spec

    @abstractmethod
    def start_engine(self) -> None:
        pass


class Car(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} ({self.spec}): Двигун запущено")


class Motorcycle(Vehicle):
    def start_engine(self) -> None:
        logger.info(f"{self.make} {self.model} ({self.spec}): Мотор заведено")


class VehicleFactory(ABC):
    @abstractmethod
    def create_car(self, make: str, model: str) -> Vehicle:
        pass

    @abstractmethod
    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        pass


class USVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "US Spec")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "US Spec")


class EUVehicleFactory(VehicleFactory):
    def create_car(self, make: str, model: str) -> Vehicle:
        return Car(make, model, "EU Spec")

    def create_motorcycle(self, make: str, model: str) -> Vehicle:
        return Motorcycle(make, model, "EU Spec")


def get_vehicle_factory(region: str) -> VehicleFactory:
    factories = {
        "US": USVehicleFactory(),
        "EU": EUVehicleFactory(),
    }
    if region not in factories:
        raise ValueError(f"Unsupported region: {region}")
    return factories[region]


def create_vehicle(factory: VehicleFactory, vehicle_type: str, make: str, model: str) -> Vehicle:
    if vehicle_type == "car":
        return factory.create_car(make, model)
    elif vehicle_type == "motorcycle":
        return factory.create_motorcycle(make, model)
    else:
        raise ValueError(f"Unsupported vehicle type: {vehicle_type}")


def run_vehicle_demo() -> None:
    us_factory = get_vehicle_factory("US")
    eu_factory = get_vehicle_factory("EU")

    car = create_vehicle(us_factory, "car", "Ford", "Mustang")
    bike = create_vehicle(eu_factory, "motorcycle", "Yamaha", "MT-07")

    car.start_engine()
    bike.start_engine()


if __name__ == "__main__":
    run_vehicle_demo()
