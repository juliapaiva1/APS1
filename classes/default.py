from screen.game import Game
from screen.start import Start
from screen.death import Death

def default():
    window = {
        "start": Start(),
        "game": Game(),
        "death": Death(),
    }  

    status = {
        "current": "start",
        "running": True,
        "destroyedMeteor": 0,
        "life": 3,
    }
    return window, status