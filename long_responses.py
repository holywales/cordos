import random

R_EATING = "I don't like eating anything because I'm a bot obviously!"
R_ADVICE = "If I were you, I would go to the internet and search for that!"


def unknown():
    response = ["Could you please re-phrase that? ",
                "Sounds about right.",
                "What does that mean?"][
        random.randrange(3)]
    return response
