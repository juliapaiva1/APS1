from screen.game import Game
from screen.start import Start
from screen.death import Death

def default(screen):
    status = {
        "current": "start",
        "running": True,
        "destroyedMeteor": 0,
        "life": 3,
        "wave": 1,
    }

    window = {
        "start": Start(status,screen),
        "game": Game(status,screen),
        "death": Death(status,screen),
    }  
    return window, status