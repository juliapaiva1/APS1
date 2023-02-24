from screen.game import Game
from screen.start import Start
from screen.death import Death
from screen.instructions import Instructions

def default(screen):
    status = {
        "current": "start",
        "running": True,
        "destroyedMeteor": 0,
        "life": 5,
        "wave": 1,
        "gameDuration": 0,
    }

    window = {
        "start": Start(status,screen),
        "game": Game(status,screen),
        "death": Death(status,screen),
        "instructions": Instructions(status, screen)
    }  
    return window, status