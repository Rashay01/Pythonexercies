from datetime import datetime

recipe = {
  "name": "Spaghetti Carbonara",
  "servings": 4,
  "ingredients": ["200g spaghetti", "100g pancetta", "2 eggs", "1/2 cup grated Parmesan", "1 clove garlic"]
}


# Task 1
# ======= Spaghetti Carbonara =======
# - 200g spaghetti
# - 100g pancetta
# - 2 eggs
# - 1/2 cup grated Parmesan
# - 1 clove garlic
# Serves: 4 people

#print(f"{]:^7}")
name = recipe["name"]
print(f"{'='*7:>2} {recipe['name']} {'='*7:<2}")
for ingredient in recipe["ingredients"]:
  print(f" - {ingredient:<10}")

print(f"Serves:{recipe['servings']:^1}people")

print()
print(f"{name:=^33}")
for ingredient in recipe['ingredients']:
    print(f" - {ingredient:}")
print(f"Serves: {recipe['servings']} people")


guests = ["Alice", "Bob", "Charlie"]
party_date = datetime(2024, 3, 14)

# Task 2 - Party Invite
# *       Alice       *
# You are invited to the party on March 14, 2024!
# *        Bob        *
# You are invited to the party on March 14, 2024!
# *      Charlie      *
# You are invited to the party on March 14, 2024!
print()
for guest in guests:
  print(f"* {guest:^17} *")
  print(f"You are invited to the party on {party_date:%B %d, %Y}!")