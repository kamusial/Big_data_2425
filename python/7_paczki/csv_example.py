import csv
import os


def get_current_dir():
    return os.path.dirname(__file__)


def read_dataset(path):
    if not os.path.exists(path):
        msg = f"Path: {path} not found!"
        raise AttributeError(msg)
    with open(path) as fh:
        reader = csv.DictReader(fh, delimiter=",")
        header = reader.fieldnames
        # Czy aby na pewno wszystko dobrze zostało odczytane?
        print(header)
        # Uwaga będzie duży potok danych!
        # return [row for row in reader]


if __name__ == "__main__":
    curdir = get_current_dir()
    datasets_dir = os.path.join(curdir, "datasets")
    for data_filename in os.listdir(datasets_dir):
        data_path = os.path.join(datasets_dir, data_filename)
        read_dataset(data_path)
