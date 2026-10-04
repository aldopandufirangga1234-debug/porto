def cuser(text):
    cleaned = text.strip().split(" ")
    kata = []

    for hasil in cleaned:
        kata_baru = hasil[0].upper() + hasil [1:].lower()
        kata.append(kata_baru)
    
    return " ".join(kata)


kalimat = input("masukan kalimat!") 
print(cuser(kalimat))
