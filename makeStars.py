x = [4, 6, 1, 3, 5, 7, 25]
stars = ""
for i in x:
    x = i
    stars.extend("*" * x[i])
    print stars