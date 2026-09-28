import random

words = {
    "noun": ["dog", "carrot", "chair", "toy", "rice cake, sinigang"],
    "verb": ["ran", "barked", "squeaked", "flew", "fell", "whistled, emoted"],
    "adjective": ["small", "great", "fuzzy", "funny", "light, dirty"],
    "preposition": ["through", "over", "under", "beyond", "across"],
    "adverb": ["barely", "mostly", "easily", "already", "just"],
    "color": ["pink", "blue", "mauve", "red", "transparent"]
}

templates = [
    """
    Yesterday the color noun
    verb preposition the coach’s
    adjective color noun that was
    adverb adjective before
    """,
    """
    I verb preposition the adjective 
    noun while you adverb verb 
    preposition the color noun
    """
    ]


def random_sentence():
    sentence = []
    for token in random.choice(templates).split():
        if token in words:
            sentence.append(random.choice(words[token]))
        else:
            sentence.append(token)
    return " ".join(sentence) + "."


for _ in range(10):
    print(random_sentence())