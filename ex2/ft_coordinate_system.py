#!/usr/bin/env python3
import math


def get_player_pos():
    while True:
        cords_input = input("Enter new coordinates "
                            "as floats in format 'x,y,z': ")
        cord_parts = cords_input.split(',')

        if len(cord_parts) != 3:
            print("Invalid syntax")
            continue

        try:
            x = float(cord_parts[0].strip())
            y = float(cord_parts[1].strip())
            z = float(cord_parts[2].strip())
            return (x, y, z)
        except ValueError:
            for p in cord_parts:
                clean_p = p.strip()
                try:
                    float(clean_p)
                except ValueError as e:
                    print(f"Error on parameter '{clean_p}': {e}")
                    break


def main() -> None:
    print("=== Game Coordinate System ===")
    print("")

    print("Get a first set of coordinates")
    pos1 = get_player_pos()

    print(f"Got a first tuple: {pos1}")
    print(f"It includes: X={pos1[0]}, Y={pos1[1]}, Z={pos1[2]}")

    centerdist = math.sqrt((pos1[0] - 0) ** 2 +
                           (pos1[1] - 0) ** 2 + (pos1[2] - 0) ** 2)
    print(f"Distance to center: {round(centerdist, 4)}")
    print("")

    print("Get a second set of coordinates")
    pos2 = get_player_pos()
    cordsdist = math.sqrt((pos1[0] - pos2[0]) ** 2 +
                          (pos1[1] - pos2[1]) ** 2 +
                          (pos1[2] - pos2[2]) ** 2)
    print(f"Distance between the 2 sets of coordinates: {round(cordsdist, 4)}")


if __name__ == "__main__":
    main()
