import csv


def getOntario(file):
    with open(file, newline="") as csvfile:
        reader = csv.DictReader(csvfile)
        for row in reader:
            if(row.get("Province") == "Ontario"):
                print("Name: {0} {1}   Address: {2}   Province: {3}".format(row.get(
                    "First name"), row.get("Last name"), row.get("Address"), row.get("Province")))


if (__name__ == "__main__"):
    getOntario("address - address.csv")
