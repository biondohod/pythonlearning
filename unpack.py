def total(galleons=0, sickles=0, knuts=0):
    return (galleons * 17 + sickles) * 29 + knuts

coins = [122, 40, 12]
print(total(*coins), "knuts")

coins2 = {"galleons": 100, "sickles": 50, "knuts": 25}
print(total(**coins2), "knuts")

def  f(*args, **kwargs):
    print("Positioned: ", args)
    print("Named: ", kwargs)

f(*coins)
f(**coins2)