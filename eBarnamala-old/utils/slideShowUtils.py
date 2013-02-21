def nextSlide(currentPosition, slideShowLength):
    nextPosition = 0
    if currentPosition < (int(slideShowLength) - 1):
        nextPosition = currentPosition + 1
    else:
        nextPosition = 0
    return nextPosition

def previousSlide(currentPosition, slideShowLength):
    previousPosition = 0
    if currentPosition > 0:
        previousPosition = currentPosition - 1
    else:
        previousPosition = int(slideShowLength) - 1
    return previousPosition
