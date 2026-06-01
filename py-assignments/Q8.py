angles = [30, -15, 45, 200, 60, 90]

valid_angles = list(
    filter(
        lambda angle: 0 <= angle <= 180,
        angles
    )
)

servo_commands = list(
    map(
        lambda angle: angle * 10,
        valid_angles
    )
)

print("Valid Angles:", valid_angles)

print("Servo Commands:", servo_commands)