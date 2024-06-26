# Inizializza la scacchiera vuota, sottoforma di matrice
# che contiene spazi vuoti dove ancora non è stata fatta una mossa
# e conterrà le X o le O dei giocatori
tabella = [[" " for _ in range(3)] for _ in range(3)]

# Funzione per stampare la scacchiera
def stampa_tabella(tabella):
    for riga in tabella:
        print(" | ".join(riga))
        print("-" * 9)

# Funzione per verificare la vittoria
def controlla_vittoria(tabella, giocatore):
    # Variabili bandierina!! (FLAG)
    # Cominciano tutte TRUE, appena si verifica un evento contraddittorio 
    # (esempio: in quella riga non ci sono solo i simboli del giocatore)
    # diventano FALSE
    check_riga = True
    check_colonna = True
    check_diagonale1 = True
    check_diagonale2 = True

    # Se una riga contiene tutta lo stesso simbolo
    for riga in tabella:
        check_riga = True
        for cell in riga:
            if cell != giocatore:
                check_riga = False
        # Se ho finito di scorrere una riga e check_riga è rimasta True, significa che in una riga
        # ho avuto lo stesso simbolo del giocatore, quindi vittoria!
        if check_riga == True:
            return True

    # Se una colonna contiene tutta lo stesso simbolo
    for col in range(3):
        check_colonna = True
        for riga in tabella:
            if riga[col] != giocatore:
                check_colonna = False
        # Se ho finito di scorrere una colonna e check_colonna è rimasta True, significa che in una colonna
        # ho avuto lo stesso simbolo del giocatore, quindi vittoria!
        if check_colonna == True:
            return True
    # Se una diagonale contiene tutta lo stesso simbolo
    for i in range(3):
        if tabella[i][i] != giocatore:
            check_diagonale1=False
        if tabella[i][2-i] != giocatore:
            check_diagonale2 = False
    if check_diagonale1 or check_diagonale2:
        return True
    return False
# Funzione per giocare il Tris
def TRIS():
    # COMPLETARE QUI IL CODICE
    n = "X"
    stampa_tabella(tabella)

    while not controlla_vittoria(tabella, n) == True:
        
        print("GIOCATORE",n, "É IL TUO TURNO")
        riga = int(input("in che riga vuoi mettere il tuo segno: "))
        colonna = int(input("in che colonna vuoi mettere il tuo segno: "))
        if tabella[riga][colonna] != ' ':
            print("lo spazio é occupato, aspetta il prossimo turno")
        else:
            tabella[riga][colonna] = n
        n = "O" if n=="X" else "X"
        stampa_tabella(tabella)
        
    print(n, "giocatore ha VINTO")    
    
    
# Esecuzione gioco
TRIS()
