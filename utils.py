import os.path


def read_file(file: str):
    if not os.path.isfile(file):
        return ""

    with open(file, "r") as f:
        return f.read()


def write_file(file: str, data: any):
    with open(file, "w") as f:
        f.write(str(data))


def append_file(file: str, data, new_line=True):
    with open(file, "a") as f:
        f.write(str(data))
        if new_line:
            f.write("\n")


def replace_all(data: list[str], value: str, new_value: str) -> list[str]:
    data = data.copy()

    for index in range(len(data)):
        data[index] = data[index].replace(value, new_value)

    return data
