import time #importo la libreria che fa aspettare un certo tempo nel monitor seriale
def menù():# definisco una funzione in cui vinene printato il menu
    
    print("Scegli una delle diverse voci: ")
    print(" ________________________________________________________________________________")
    print("|    Voce 1 --> restituisce un numero che hai digitato                          |")
    print("|    Voce 2 --> ti chiede il numero, che hai inserito prima, di volte un numero |")
    print("|    Voce 3 --> fa la media dei numeri pari inseriti nella voce 2               |")
    print("|    Voce 4 --> restituisce il fattoriale del numero digitato nella voce 1      |")
    print("|    Voce 5 --> definisce se il numero inserito nella voce 1 è primo o meno     |")
    print("|_______________________________________________________________________________|")
def fattoriale(n):# definisco una funzione che calcola il fattoriale di un numero(n)
            
            counter_fattoriale = 1
            totale = 1
         
            while counter_fattoriale < n:
                totale *= (n - counter_fattoriale)
                counter_fattoriale += 1
            print("il fattoriale è: " + str(n * totale))
counter_voci_1= 0 #creo una variabile che andrà a contare quante vole la voce 1 viene eseguita
counter_voci_2= 0 #creo una variabile che andrà a contare quante vole la voce 2 viene eseguita

while True:
    time.sleep(0.75) #aspetto 0.75 secondi 
    menù()
    voce = 0
    voce = int(input("Scrivi il numero della voce che vuoi sceglire: ")) #creo la variabile che chiede la voce all'utente
    
    while voce > 5 or voce < 1 : # controlla se la voce digitata esiste
        print("Digita una voce compresa tra 1 e 5")
        break
        

    if voce == 1: #codice voce 1
        N= 0
        N = int(input("dammi un numero qualsiasi: "))
        print("il tuo numero e': " + str(N))
        counter_voci_1 += 1
    
        
    if voce == 2 and counter_voci_1 >= 1 and N/2 == int(N/2): #codice voce 2
        num = 0
        num_counter = 0
        num_pari = 0
        while num_counter < N:
            num = int(input("Dammi un numero che servira' per la voce 3: "))
            
            if num/2 == int(num/2):
                num_pari += num
            num_counter += 1
        counter_voci_2 += 1
    elif voce == 2 and( counter_voci_1 < 1 or N/2 != int(N/2)): #controlla le condizioni affinchè la voce 2 funzioni
        print("affinche' la voce 2 funzioni la voce 1 deve essere stata eseguita almeno una volta oppure il numero digitato precedentemente deve essere pari")

    
    if voce == 3 and counter_voci_1 >= 1 and counter_voci_2 >= 1: #codice voce 3
        media = num_pari / N
        if media == 0.0:
            print("nella voce 3 viene calcolata la media solo dei numeri pari")        
        else:
            print("la media dei numeri digitati nella voce 2 e': " + str(media))
    elif voce == 3 and(counter_voci_1 < 1 or counter_voci_2 < 1): #controlla le condizioni affinchè la voce 3 funzioni
        print("affinche' la voce 3 funzioni, la voce 1 e 2 devono essere state eseguite almeno una volta")
    
    
    if voce == 4 and counter_voci_1 >= 1: #codice voce 4
        if N == 0:
            print("il fattoriale e': 1")
        if N == 1:
            print("il fattoriale e': 1")
        if N < 1:
            print("il fattoriale si puo' fare solo di numeri interi positivi")
        if N > 1:
            fattoriale(N)
    elif voce == 4 and counter_voci_1 < 1: #controlla le condizioni affinchè la voce 4 funzioni
        print("affinche' la voce 4 funzioni, la voce 1 deve essere stata eseguita almeno una volta")
    
    
    if voce == 5 and counter_voci_1 >= 1: #codice voce 5
        counter_primo = 2
        counter_print = 0
        
        while N / counter_primo != int(N / counter_primo):
            counter_primo += 1
            if counter_primo == N:
                print("il numero è un numero primo")
                counter_print += 1
        
        if counter_print >= 1:
            print("")
        else:
            print("il numero non è un numero primo")
    elif voce == 5 and counter_voci_1 < 1: #controlla le condizioni affinchè la voce 5 funzioni
        print("affinche' la voce 5 funzioni, la voce 1 deve essere stata eseguita almeno una volta")