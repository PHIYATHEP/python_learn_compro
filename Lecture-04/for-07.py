print("KPH\tMPH:")
print("---------------")
for KPH in range(60,140,10):
    MPH = KPH * 0.6214
    print(f"{KPH}\t{MPH:.1f}")
print("\n")
print("MPH\tKPH:")
print("---------------")
for MPH in range(60,140,10):
    KPH = MPH / 0.6214
    print(f"{MPH}\t{KPH:.0f}")    