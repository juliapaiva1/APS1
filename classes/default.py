def defaultStatus(d):
    d.update({
        "current": "start",
        "running": True,
        "destroyedMeteor": 0,
        "life": 5,
        "wave": 1,
        "gameDuration": 0,
        "gameStart": 0
    })
    return d

