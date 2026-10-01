import requests

BASE_URL = "http://localhost:8000"
#
# # Create creature

#
# print("Creature:")
# print(creature_response.status_code)
# print(creature_response.json())

with open("data","r") as file:
    for line in file:
        if "Creature" in line:
            creature_data = {
                "name": line.split("(")[1].split(",")[1].strip()[1:-1].replace('"',""),
                "mana_cost": line.split("(")[1].split(",")[0]
            }

            creature_response = requests.post(
                f"{BASE_URL}/add_creature",
                json=creature_data
            )
        elif "Spell" in line:
            spell_data = {
                "name": line.split("(")[1].split(",")[1].strip()[1:-1].replace('"', ""),
                "mana_cost": line.split("(")[1].split(",")[0]
            }

            creature_response = requests.post(
                f"{BASE_URL}/add_spell",
                json=spell_data
            )