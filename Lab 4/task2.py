import csv
import json

INPUT_FILENAME = "input.csv"
OUTPUT_FILENAME = "output.json"


def task() -> None:
    data = []
    with open(INPUT_FILENAME, "r") as i_file:
        reader = csv.DictReader(i_file, delimiter=',', quotechar="\n")
        for row in reader:
            data.append(row)

    with open(OUTPUT_FILENAME, "w") as o_file:
        json.dump(data, o_file, indent=4)


if __name__ == '__main__':
    # Нужно для проверки
    task()

    with open(OUTPUT_FILENAME) as output_f:
        for line in output_f:
            print(line, end="")
