import random 

templates = {
    ":name hates that :color :clothing because it looks like a :adjective :noun" : "El Dumbrique",
    "The chef :adverb: cooked the :food and added :color garnishes, but it tasted like a :noun" : "El Dumbrique",
    "In class, I learned how to :adverb :verb and where a :color :noun comes from" : "El Dumbrique",
    "The :color :animal knows how to :verb if you give it a :food" : "El Dumbrique",
    "If you give a :color :animal a piece of :food it will ask for a :food." : "El Dumbrique",
    "I wanted to dress up in a :color :clothing but :name wants to dress up in a :color :clothing instead" : "El Dumbrique",
    ":name looks like a :adjective :animal when dressed in a :color :clothing like that" : "El Dumbrique",
    "I tried to :adverb draw a :color :noun but it ended up looking like a :adjective :animal instead" : "El Dumbrique",
    "My favorite :food is only complete with a side of :adjective :drink and my :adjective friend, :name" : "El Dumbrique",
    "That :adjective :name told me the homework answer was a :color :noun but it was actually a :adjective :noun" : "El Dumbrique"
}

def fill_template(template, author):
    final_template = []

    for word in template.split():
        if word[0] == ":":
            user_word = input(f"Type a word that is a '{word[1:]}' : ").strip().lower()

            if word == ":name":
                user_word = user_word.capitalize()

            if len(user_word) < 1 or len(user_word) > 30:
                raise ValueError("Words should be between 1 and 30 characters.")

            word = user_word

        final_template.append(word)

    print("")
    return " ".join(final_template) + ". \nAuthor: " + author


print("""Welcome to my Mad Libs! 
A random sentence has been selected, but some of the words are missing! It's up to you fill them in!
You will be prompted with a type of word that you get to decide. Please keep your words between 1 and 30 characters. 
The complete sentence with your words will be revealed after all blank words are filled in. 
    """)


while True:
    random_template = random.choice(list(templates.keys()))

    print(fill_template(random_template, templates[random_template]))

    affirmatives = {"yes", "sí", "oui", "yeah", "sure", "okay", "wen", "hai", "yuh", "yessir", "bet"}

    while True:
        play_again = False
        answer = input("""
Would you like to play again with another randomly selected sentence? 
If so, type an affirmative answer. If not, type "no" : """).strip().lower()

        if answer in affirmatives:
            print("Amazing! A new sentence will be generated.\n")
            play_again = True
            break
        elif answer == "no":
            print("No worries! Hopefully you had fun, see you again!")
            break
        else:
            print("Apologies, your answer was not understood. Try again.")

    if not play_again:
        break

