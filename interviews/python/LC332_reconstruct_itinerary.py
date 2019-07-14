import collections

def visit(airport, targets, route):
    while targets[airport]:
        visit(targets[airport].pop(), targets, route)

    route.append(airport)

def findItinerary(tickets):
    targets = collections.defaultdict(list)
    for a, b in sorted(tickets)[::-1]:
        targets[a] += b,

    route = []
    visit('JFK', targets, route)
    return route[::-1]

print(findItinerary([["MUC", "LHR"], ["JFK", "MUC"], ["SFO", "SJC"], ["LHR", "SFO"]]))
print(findItinerary([["JFK","SFO"],["JFK","ATL"],["SFO","ATL"],["ATL","JFK"],["ATL","SFO"]]))
