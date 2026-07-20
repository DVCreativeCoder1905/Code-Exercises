def bar():
    print("Benvenuto nel mio bar!")
nome = input("Come ti chiami? ")
risposta = input(f"Ciao {nome}, cosa ti piacerebbe bere?")
if risposta == "alcolici":
    print("Aspetta, prima devo sapere quanti anni hai.")
    eta = int(input("Quanti anni hai? "))
    if eta < 18:
        print("Mi dispiace, non posso servirti alcolici perché sei minorenne.")
    else:
        print("Possiamo servirti alcolici, ecco il nostro menu:")
        alcolici = ["birra", "vino", "cocktail"]
        for alcolico in alcolici:
            print(alcolico)
            input("Cosa vuoi ordinare tra gli alcolici che abbiamo?")
            if alcolico == "birra, vino, cocktail":
                print("Ecco a te. Grazie e buona giornata!")
            else:
                print("Mi dispiace, non abbiamo quello che vuoi ordinare.")
elif risposta == "analcolici":
    print("Ecco il nostro menu di analcolici:")
    analcolici = ["acqua", "succo di frutta", "bibite gassate"]
    for analcolico in analcolici:
        print(analcolico)
        input("Cosa vuoi ordinare tra gli analcolici che abbiamo?")
        if analcolico == "acqua, succo di frutta, bibite gassate":
            print("Ecco a te. Grazie e buona giornata!")
        else:
            print("Mi dispiace, non abbiamo quello che vuoi ordinare.")
else:
    risposta2 = input("Vuoi qualcosa da mangiare?")
    if risposta2 == "sì":
        risposta3 = input("Dolce o salato?")
        if risposta3 == "dolce":
            print("Ecco il nostro menu di dolci:")
            dolci = ["torta", "gelato", "biscotti"]
            for dolce in dolci:
                print(dolce)
                input("Cosa vuoi ordinare tra i dolci che abbiamo?")
                if dolce == "torta, gelato, biscotti":
                    print("Ecco a te. Grazie e buona giornata!")
                else:
                    print("Mi dispiace, non abbiamo quello che vuoi ordinare.")
        elif risposta3 == "salato":
            print("Ecco il nostro menu di salati:")
            salati = ["panino", "pizza", "patatine"]
            for salato in salati:
                print(salato)
                input("Cosa vuoi ordinare tra i salati che abbiamo?")
                if salato == "panino, pizza, patatine":
                    print("Ecco a te. Grazie e buona giornata!")
                else:
                    print("Mi dispiace, non abbiamo quello che vuoi ordinare.")
    else:
        print("Va bene, grazie per essere venuto al nostro bar. Buona giornata!")
        
input("Premi un tasto per uscire.")
bar()
