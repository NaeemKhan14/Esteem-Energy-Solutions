from background_task import background

@background(schedule=2)
def notify():
    print("here")