from sensor import get_sensor_values
from movement import decide_movement

sensor_values, active_count = get_sensor_values()

print("Sensor Values:", sensor_values)

print("Active Sensors:", active_count)

action = decide_movement(sensor_values)

print("Robot Action:", action)