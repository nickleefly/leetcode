my_input = [
    ["c", "z", 7],
    ["b", "z", 2],
    ["c", "x", 1],
    ["a", "z", 3],
    ["a", "x", 1],
    ["b", "y", 5],
    ["a", "x", 4],
    ["a", "y", 1]
]
print(my_input)


def by_second(element):
    return element[1]


res = [i for i in sorted(my_input, key=by_second)]
print("res is ", res)
results = {}
for k in res:
    if (k[0], k[1]) in results:
        results[(k[0], k[1])] += k[2]
    else:
        results[(k[0], k[1])] = k[2]

for k, v in results:
    print(k, v, results[(k, v)])
