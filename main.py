def direction(facing, turn):
    directions = ['N', 'NE', 'E', 'SE', 'S', 'SW', 'W', 'NW']

    if facing not in directions:
        return " Please provide correct data "
    elif (turn > 1080) or (turn < -1080) or (turn % 45 != 0):
        return " Please provide correct data "

    angle = (turn / 45) % 8
    new_direction = (directions.index(facing) + angle) % 8
    print(directions[int(new_direction)])
    return directions[int(new_direction)]
