
def main():
    with open("input.txt") as file:
        calibrations = file.readlines()
        current_calibration = 0
        for calibration in calibrations:
            current_calibration += int(calibration)
        print(current_calibration)


if __name__ == "__main__":
    main()

