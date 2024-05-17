nbr1 = int(input("entre le nombre"))
symbole = input("Enter le signe +,/,*,-")
nbr2 = int(input("entre autre nombre"))

match symbole:
    case "/":
        reponse=(nbr1/nbr2)
    case "+":
        reponse = (nbr1 + nbr2)
    case "*":
        reponse = (nbr1 * nbr2)
    case "-":
        reponse = (nbr1 - nbr2)
print (reponse)

