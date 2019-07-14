def canPlaceFlowers(flowerbed, n):
    for i, x in enumerate(flowerbed):
        if (x == 0 and (i == 0 or flowerbed[i-1] == 0) and (i == len(flowerbed)-1 or flowerbed[i+1] == 0)):
            n -= 1
            flowerbed[i] = 1

    return n <= 0

print(canPlaceFlowers([1,0,0,0,1], 1))
print(canPlaceFlowers([1,0,0,0,1], 2))
