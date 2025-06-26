def procces_data(dta):
    resutl = []
    for i in dta:
        if i % 2 == 0:
            resutl.append(i * 2)
        else:
            resutl.append(i + 1)

    return resutl