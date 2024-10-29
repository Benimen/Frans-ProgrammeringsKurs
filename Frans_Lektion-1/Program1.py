print ("hello")

#test

a = 1
b = 2

if b > a:
    print("This is ab comparison")


def hantera_text(text):
    # Skriv ut det första tecknet
    print("Första tecknet:", text[0])

    #Skriv ut tecken från position 7 till 12
    print("Tecken från position 7 till 12", text[7:12])

    #Skriv ut varannat tecken
    print("Skriv ut varannat teckn", text[::2])

    #Skriv ut strängen baklänges
    print("Skriv ut strängen baklänges", text[::-1])


hantera_text("Hello World!")