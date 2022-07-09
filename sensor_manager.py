import json, busio, adafruit_sht4x, time

class Sensor:
    def __init__(self, name: str, scl: int, sda: int):
        self.name = name
        self.i2c = busio.I2C(scl, sda)
        self.sensor = adafruit_sht4x.SHT4x(self.i2c)
    
    def get_data(self):
        return self.sensor.temperature, self.sensor.relative_humidity

if __name__ == "__main__":
    with open("./sensor_config.json", "r") as f:
        conf = json.load(f)
    
    sensors = {name: Sensor(
        name, sensor["scl"], sensor["sda"]
    ) for name, sensor in conf["sensors"].items()}

    while True:
        for s in sensors.values():
            temp, humidity = s.get_data()
            print(f"{s.name}: {temp} *C, {humidity}% humidity")
        
        time.sleep(5)