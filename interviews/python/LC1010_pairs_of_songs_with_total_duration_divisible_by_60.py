def numPairsDivisibleBy60(time):
    mod = [0] * 61
    for t in time:
        mod[-1] += mod[(60 - t % 60) % 60]
        mod[t % 60] += 1
    return mod[-1]

print(numPairsDivisibleBy60([30,20,150,100,40]))
