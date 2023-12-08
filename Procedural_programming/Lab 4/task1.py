import json

INPUT_FILE = "input.json"


def task() -> float:
    res = 0
    with open(INPUT_FILE) as i_file:
        json_data = json.load(i_file)
    return round(sum(dict["score"] * dict["weight"] for dict in json_data), 3)


print(task())
