def findRestaurant(list1, list2):
    fav = { r:i for i,r in enumerate(list1) }
    res = []
    min_ix = float('inf')

    for i, r in enumerate(list2):
        if r in fav:
            if i + fav[r] == min_ix:
                res.append(r)

            elif i + fav[r] < min_ix:
                res = [r]
                min_ix = i + fav[r]

    return res

print(findRestaurant(["Shogun", "Tapioca Express", "Burger King", "KFC"],
                     ["Piatti", "The Grill at Torrey Pines", "Hungry Hunter Steakhouse", "Shogun"]))
