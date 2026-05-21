def czyWzorzec():
    tekst = "SJADNSJDMACABCKFDMKASL"
    wzorzec = "CABC"
    t = len(tekst)
    w = len(wzorzec)

    for i in range(t - w + 1):
        match = True

        for j in range(w):
            if tekst[i + j] != wzorzec[j]:
                match = False
                break

        if match:
            return True

    return False

print(czyWzorzec())