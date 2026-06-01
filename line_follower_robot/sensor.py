def get_sensor_values():

    values = input(
        "Enter 6 Sensor Values (0 or 1): "
    )

    sensors = list(map(int, values))

    active_sensors = list(
        filter(
            lambda x: x == 1,
            sensors
        )
    )

    return sensors, len(active_sensors)
