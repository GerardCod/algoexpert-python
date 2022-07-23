def classPhotos(redShirtHeights, blueShirtHeights):
    redShirtHeights.sort(reverse=True)
    blueShirtHeights.sort(reverse=True)

    shirtColorFirstRow = 'RED' if redShirtHeights[0] < blueShirtHeights[0] else 'BLUE'

    for idx in range(len(redShirtHeights)):
        redShirtHeight = redShirtHeights[idx]
        blueShirtHeight = blueShirtHeights[idx]

        if shirtColorFirstRow == 'RED':
            if redShirtHeight > blueShirtHeight:
                return False
        else:
            if blueShirtHeight > redShirtHeight:
                return False
        
    return True


if __name__ == '__main__':
    print(classPhotos([5, 8, 1, 3, 4], [6, 9, 2, 4, 5]))