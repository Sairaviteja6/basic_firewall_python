import json

def read_rules():
    with open("config/rules.json", "r") as file:
        return json.load(file)

def write_rules(new_rules):
    with open("config/rules.json", "w") as file:
        json.dump(new_rules, file, indent=4)
