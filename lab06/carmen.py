import random
from haversine import haversine
from geography import countries

def random_country_name():
    # Select a random country name from the key in the countries dictionary we imported.
    # We have to convert the keys to a list, because random.choice() only works on lists,
    # and the keys of a dictionary are (surprisingly!) not a list in Python.
    return random.choice(list(countries.keys()))

def random_hint(country):
    match random.choice(["capital", "region", "landmark", "distance", "population"]):
        case "capital":
            hint = "whose capital is " + country["capital"]
        case "region":
            hint = "in " + country["region"]
        case "landmark":
            hint = "where you can find " + random.choice(country["landmarks"])
        case "distance":
            los_angeles = (34.0522, -118.2437)
            from_LA = round(haversine(los_angeles, country["coordinates"], unit="km"))
            hint = "approximately " + str(from_LA) + " km from Los Angeles"
        case "population":
            hint = "that has a population of " + country["population"] + " people"
    return "Carmen is in a country " + hint

correct_guesses = 0
incorrect_guesses = 0

print("Carmen Sandiego is hiding somewhere. Find her!")

#list of countries: colombia, barbados, vanuatu, eswatini, bhutan, iceland, philippines
current_country_name = random_country_name()
while True:
    country = countries[current_country_name]
    print("Correct Guesses: " + str(correct_guesses) + "     Incorrect Guesses: " + str(incorrect_guesses))
    print("\nGuess where Carmen is, or say 'hint' or 'exit'.")
    guess = input("Where are you going to look? ").strip().lower()
    if guess == current_country_name:
        print("She was here, but you missed her by one hour!")
        current_country_name = random_country_name()
        correct_guesses = correct_guesses + 1
    elif guess == "hint":
        print(random_hint(country))
    elif guess == "exit":
        print("Thank you for playing!")
        break
    else:
        print("Oh no, she’s not here!")
        incorrect_guesses = incorrect_guesses + 1