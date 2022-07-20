def minimumWaitingTime(arr):
    arr.sort()
    waitingTime = 0

    for idx, duration in enumerate(arr):
        queriesLeft = len(arr) - (idx + 1)
        waitingTime += duration * queriesLeft
    return waitingTime


if __name__ == '__main__':
    waitingTime = minimumWaitingTime([3, 2, 1, 2, 6])
    print(waitingTime)