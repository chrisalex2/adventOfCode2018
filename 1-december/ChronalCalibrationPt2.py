from itertools import cycle


def main():
    with open("input.txt") as file:
        calibrations = file.readlines()
        current_calibration = 0
        occurrences = {current_calibration: 1}
        for calibration in cycle(calibrations):
            current_calibration += int(calibration)
            occurrences[current_calibration] = occurrences.get(current_calibration, 0) + 1
            if occurrences[current_calibration] > 1:
                print(current_calibration)
                break


if __name__ == "__main__":
    main()
