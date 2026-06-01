def decide_movement(sensors):

    if sensors == [0, 0, 0, 0, 0, 0]:
        return "STOP"

    elif sensors == [1, 1, 1, 1, 1, 1]:
        return "JUNCTION DETECTED"

    elif sensors[2] == 1 or sensors[3] == 1:
        return "MOVE FORWARD"

    elif sensors[0] == 1 or sensors[1] == 1:
        return "TURN LEFT"

    elif sensors[4] == 1 or sensors[5] == 1:
        return "TURN RIGHT"

    else:
        return "NO DECISION"