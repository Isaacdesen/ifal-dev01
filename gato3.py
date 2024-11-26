while True:
    miaus = int(input("quantas vezes seu gato miou?"))
    if miaus <= 0:
        continue
    else:
        break
print("miau\n" * miaus, end= "")    