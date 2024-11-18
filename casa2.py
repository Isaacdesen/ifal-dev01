def main():
    name = input ("nome do personagem")
    person(name)

def person(name=""):
    
    match name:
        case "harry potter" | "hermiione granger" | "rony weasley":
            print("grifiornia")
        case "draco malfoy":
            print("sonserina")
        case "luna lovegood":
            print("corvinal")
        case "cendric diggory":
            print("lufa-lufa")
        case _:
            print ("personagem não encontrado")
main()                        