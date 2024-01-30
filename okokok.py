for i in range(3):
    tulemus = int(input("Sisesta tulemus: "))
    if i == 0:
        parim = tulemus
        keskmine = tulemus
    else:
        if tulemus > parim:
            parim = tulemus
        keskmine = keskmine + tulemus

print("Parim tulemus: " + str(parim))
print("Keskmine tulemus: " + str(keskmine/3))
