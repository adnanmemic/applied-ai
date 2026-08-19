import csv

def get_students_from_csv(path):
    with open(path, "r", encoding="utf-8") as f:
        database = list(csv.DictReader(f))
        return database
