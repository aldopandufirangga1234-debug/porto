def tambah(a,b):
    return a + b

def kurang(a,b):
    return a - b

def kali(a,b):
    return a * b

def bagi(a,b):
    try:
        pembagian = a / b
        return pembagian
    except ZeroDivisionError:
        print("tidak dapat di bagi 0")
        return None


