import random
import time
# Lapo Tapinassi
# TEMPLATE GIOCO - BATTAGLIA NAVALE
# ICT 3A - A.A. 2023/24 - Prof. Giacomo Gori




# funzione che stampa la tabella di gioco
# INPUT: matrice - OUTPUT: nessuno; stampa la matrice
def stampa_tabella(tabella):
   for riga in tabella:
      print(" ".join(riga))


# funzione che crea una tabella 5x5 vuota, cioè con tutte O
# INPUT: nessuno - OUTPUT: matrice che rappresenta una tabella di gioco vuota
def crea_tabella():
   tabella = []
   for _ in range(5):
      tabella.append(["O"] * 5)
   return tabella


# funzione che posiziona in una tabella le navi passate come vettore di coordinate x,y
# ovvero, ogni elemento del vettore navi è una tupla (x, y)
# INPUT: una matrice che rappresenta una tabella e una lista di posizioni -
# # OUTPUT: nessuno, ma aggiorna la tabella con le posizioni scelte
def posiziona_navi(tabella, navi):
   for nave in navi:
      x, y = nave
      tabella[x][y] = "N"


# funzione che genera delle tuple (x,y) casuali ma diverse tra loro, e le salva nel vettore navi
# quindi navi è un vettore di tuple (x,y)
# questa funzione serve per generare delle posizioni casuali delle navi per il computer
# INPUT: un vettore vuoto - OUTPUT: un vettore con tuple (x,y) casuali e diverse tra loro
def genera_navi(navi):
   i=0
   while i < 3:
      x = random.randint(0, 4)
      y = random.randint(0, 4)
      nave = (x, y)
      if nave not in navi:
         navi.append(nave)
         i+=1
   return navi




   
# funzione che restituisce un tentativo casuale del computer
# INPUT: nessuno - OUTPUT: una tupla (x,y) contenente due coordinate casuali
def mossa_computer():
   x_t = random.randint(0, 4)
   y_t = random.randint(0, 4)
   return (x_t,y_t)


#------------------------------!FUNZIONI SVILUPPATE DA ME!------------------------------#


# la funzione chiede la posizione X e Y delle navi al giocatore
# funziona come la funzione genera navi solo che al posto di random.randint ci sta un int(input(""))
# in piú si avverte il giocatore se la posizione era occupata precedentemente
# Ho deciso di aggiungere questa funzione perché, anche se non nel nostro caso, sarebbe molto utile nel caso ci fossero due giocatori consapevoli delle loro scelte
def chiedi_navi(navi):
   i=0 # i sta ad indicare i valori validi che ci vengono forniti
   while i < 3: # il codice si ripete fino a quando non abbiamo 3 valori accettati
        while True: # CONTROLLO ERRORI    
            # ora andró ad utilizzare il metodo try: except ... :
            # in questo modo posso controllare che l'input inserito é un numero e non una lettera
            # con il try spesso si perdono delle informazioni, ma in questo caso no
            # essendo che ho gia controllato se il valore é allinterno del range della matrice il ValueError mi serve per vedere se le coordinate sono inseribili e utilizzabili nel gioco
            try: # IMPORTANTE: l'errore é fornito istantaneamente quindi possiamo utilizzare break per fare smettere questo ciclo while (riga 71)  
                x = int(input("Inserisci la coordinata X: "))
                y = int(input("Inserisci la coordinata Y: "))
                nave = (x, y)
                break
            except ValueError:
                print("Non hai inserito un un numero, riprova")
                continue # il ciclo continua affinché non vengon fornite coordinate validi
        # da questo momento in poi si passa al secondo CONTROLLO ERRORI:
        if nave not in navi and x < 5 and y < 5: # se non esiste una nave gia nella posizione indicata e vengono fornite delle coordinate nel range della matrice: allora viene agginta la nostra posizione di nave alla lista delle nostre navi
         navi.append(nave)
         i += 1 # aggingiamo uno ad i per sapere che le coordinate fornite sono accettate
        elif nave in navi: # se esiste giá una nave alle coordinate fornite, si avverte il giocatore e si ripete il codice. IMPORTANTE: essendo che il giocatore non ha fornito coordinate valide non si incrementa i
         print("La posizione era occupata, RIPROVA")  
        elif x >= 5 or y >= 5: # se invece vengono foornite delle coordinate al di fuori della nostra matrice, allora si avverte il giocatore e il codice si ripete. IMPORTANTE: essendo che il giocatore non ha fornito coordinate valide non si incrementa i
         print("Il valore è troppo alto, RIPROVA")


# funzione che controlla se la tabella non contiene più navi,
# ovvero, se la tabella passata appartiene al giocatore controlla se il giocatore ha perso, e viceversa
# INPUT: matriche che rappresenta una tabella - OUTPUT: valore booleano: True se il proprietario di quella tabella ha perso,
# cioè non ci sono navi (N) dentro la tabella, False se invece ci sono ancora navi
# questa funzione é fondamentale per determinare quale giocatore ha perso e quinidi quale ha vinto
def controlla_sconfitta(tabella):
   sconfitta = True #inizzializiamo la variabile sconiftta a true
   # COMPLETARE con il controllo di sconfitta, cioè scorrere la tabella per controllare che non ci siano più N,
   # in quel caso il giocatore a cui appartiene la tabella ha perso
   for i in tabella: # scorriamo nelle righe della nostra tabella
      for j in i: # scorriamo nelle colonne delle righe della nostra tabella, quindi andiamo a guardare ogni singolo elemento
         if "N" == j: # controlliamo se il nostro elemento é uguale a "N"
            sconfitta = False # se sí allora é rimasta almeno una nave e quindi sconfitta é uguale a FALSE, il giocatore o coputer non ha ancora perso
            break


   return(sconfitta)# la nostra funzione controlla sconfitta restituirà sconfitta come True o False


# funzione che fa scegliere la modalitá all'utente,
# modalitá facile(0) puó visualizzare le navi e le loro coordinate, modalitá difficile(1) non si visualizza niente
# Ho deciso di aggiungere questa opzione sottoforma di funzione perché, anche se non nel nostro caso, la modalitá si potrebbe chiedere anche all'avversario (se fosse una persona)
def modalitá(tabella, navi):
   mode = input("Scegli la modalità, 0 per facile, 1 per difficile: ") # chiediamo all'utente la difficoltá. IMPORTANTE: no la cheidiamo sottoforma di int(... in modo tale da poter controllare l'errore se il giocatore scrive una lettera
   if mode == '0':
      print("Queste sono le coordinate delle navi del computer:", navi) #Stampiamo le navi del computer perchè la modalità facile è stata scelta
      time.sleep(1)
      print("Ecco la tabella del computer: ")
      stampa_tabella(tabella) #Stampiamo la tabella del computer perchè la modalità facile è stata scelta
   elif mode == '1': # non viene stampato nulla dato che la difficoltá é difficile
      print("Il computer ha posizionato le navi.")
   else: # CONTROLLO ERRORI: qui viene controllato l'errore. Se l'utente inserisce una lettera o qualsiasi altro simbolo che non sia ne 1 ne 0 allora si punisce facendo partire il giocatore in modalitá difficile
      print("Non hai inserito ne 0 ne 1, quindi giocherai in modalità difficile")
      print("Il computer ha posizionato le navi.")


# funzione che ci premette di svolgere una mossa di qualsiasi giocatore
# una mossa comprende la scelta dell'attacco e poi rispettivamente l'aggiornamento della tabella
# come parametri questa funzione ha:
#     - guess: questo parametro sta a siglificare la posizione X e Y dell'attacco
#     - navi: navi sta a rappresentare la lista dove noi dovremo andare a cercare per verificare se la nostra "guess" é corretta o meno; in tal modo verrá aggiornata la tabella
#     - tabella: tabella sta semplicememte a significare quale tabella dovremo andare a modificare se con "X" o "M", la tabella é del giocatore opposto alla "guess", sennó uno andrebbe ad attacare le propie navi
#     - giocatore: giocatore, da come il nome suggerisce, sta a significare chi é che sta compiendo questa mossa? Nel nostro caso o siamo noi o il computer
# Ho deciso di creare questa funzione in modo tale da poter ripetere il codice ugualmente e quindi evitare ripetizioni all'interno di esso  
def mossa(guess, navi, tabella, giocatore):
    if guess[0] < 5 and guess[1] < 5: # CONTROLLO ERRORI: se il giocatore fornisce un indice valido bene, altrimenti(vai a riga 129)
         if guess in navi: # questo sta a significare se la nostra "guess" é nella lista navi
                tabella[guess[0]][guess[1]] = "X" # se sí si procede sostituendo nelle coordinate la "N" con la "X". IMPORTANTE: essendo che guess é una tupla si guarda il primo valore e il secondo che sono rispettivamente x e y
                if giocatore == 1: # qui si controlla se il giocatore é il computer o meno. 1 sta a significare che il giocatore é l'utente, ) é il computer.  
                    print("Bravo, hai affondato la nave del computer")
                    time.sleep(1)
                    print("Ora é il turno del computer...")
                elif giocatore == 0:
                    print("Accipicchia, il computer ha affondato la tua nave.") # vengono restituiti output diversi per farlo capire meglio all'utente di quali navi stiamo parlando
         else: # se invece la "guess" non coincide con le coordinate nelle navi e quindi non si trova nella lista allora andiamo ad informare l'utente. Il codice é uguale a quello sopra solo che sostituiamo "N" con "M"
            tabella[guess[0]][guess[1]] = "M"
            if giocatore == 1:    
                print("Peccato, non hai affondato nessuna nave")
                time.sleep(1)
                print("Ora é il turno del computer...")
            elif giocatore == 0:
                print("Ti sei salvato, il computer non ha affondato nessuna nave")# vengono restituiti output diversi per farlo capire meglio all'utente di quali navi stiamo parlando
    else: # altrimenti questo suo attacco sará nullo. Dato che teoricamente non puó aver colpito nessuna nave essendo fuori dalla tabella
       time.sleep(0.5)
       print("Le coordinate fornite non sono valide (superano il massimo indice di tabella), per questo turno il tuo attacco sará nullo, STAI ATTENTO per le prossime volte!")


# questa dovrà utilizzare le funzioni proposte sopra per realizzare
# il gioco della battaglia navale - giocatore vs computer
# NOTAZIONE: nella tabella rappresentiamo con O la casella vuota, con N la casella con la nave
# mentre, dopo ogni attacco, aggiorniamo la tabella attaccata
# con X rappresentiamo una nave colpita e con M una casella mancata
def gioca():
   tabella_giocatore = crea_tabella()
   tabella_computer = crea_tabella()
   navi_giocatore = []
   navi_computer = []


   print("Benvenuto in Battaglia Navale!")
   print("Hai 20 TURNI per abbattere le navi nemiche, datti da fare!")
   print("Studente: Lapo Tapinassi") #Sostituisci X con il tuo nome e cognome
   # COMPLETA QUI
   genera_navi(navi_computer) #Generiamo una lista dove si trovano le navi del computer
   posiziona_navi(tabella_computer, navi_computer) #Vengono posizionate le navi del computer all'interno della tabella computer
   modalitá(tabella_computer, navi_computer)
   time.sleep(0.8)
   print("È il momento di inserie le tue navi")
   chiedi_navi(navi_giocatore) #Chiede le coordinate X e Y delle navi
   posiziona_navi(tabella_giocatore, navi_giocatore) #Posiziona le navi nella rispettiva tabella del giocatore
   print("Le tue navi sono posizionate:")
   stampa_tabella(tabella_giocatore) #Stampa la tabella con le navi inserite precedentemente


   time.sleep(1)# aspettiamo primia di iniziare per comoditá
   
   turni = 1
   while turni <= 20: # il numero di turni o tentativi massimi é 20
      print("\nTurno",turni,"\n~~~~~~~~~~~~" ) # si informa il giocatore a che turno ci troviamo
     
      try: # CONTROLLO ERRORI: con il try: except: controllo se le coordinate inserite dell'attacco sono effettivamente numeri, se si il codice si esegnue normalmente se no (riga 181)
            guess_giocatore = (int(input("Indovina la coordinata X del computer: ")), int(input("Indovina la coordinata Y del computer: "))) # il giocatore compie la sua scelta su quali navi attaccare
            mossa(guess_giocatore, navi_computer, tabella_computer, 1) # viene eseguita la funzione mossa() secondo la "guess" del giocatore
      except ValueError: # se no l'attacco per turno sará nullo e quindi non succederá nulla sulla tabella nemica
            print("Le coordinate fornite non sono valide (non sono numeri), per questo turno il tuo attacco sará nullo, STAI ATTENTO per le prossime volte!")
      time.sleep(1.5) # si aspetta per conferire un po' di suspance e ordine al gioco


      guess_computer = mossa_computer() # il computer svolge la sua mossa grazie alla funzione mossa_computer()
      print("Il computer sceglie", guess_computer) # informiamo il giocatore della scelta di attacco del computer
      time.sleep(1.5)
     
      mossa(guess_computer, navi_giocatore, tabella_giocatore, 0) # viene eseguita la funzione mossa() secondo la "guess" del computer
      time.sleep(1.5)
      print("Ecco la tua tabella dopo il Turno", turni, ":")
      stampa_tabella(tabella_giocatore) # viene restituita la tabella alla fine del turno, indicando anche a quale ci troviamo
     
      turni += 1 # si incrementa i turni di 1, essendo che ne é passato uno
      time.sleep(1)
      # ora si passa al controllo della sconfitta di un giocatore
      if controlla_sconfitta(tabella_giocatore) == True and controlla_sconfitta(tabella_computer) == True: # situazione di pareggio: molto improbabile, ma se il computer e il giocatore azzeccano le ultime corrispondenti navi nello stesso turno
         print("La partita é terminata in un pareggio")
      elif controlla_sconfitta(tabella_giocatore) == True: # situazione di vittoria del computer, il giocatore ha perso
         print("Il computer ha vinto, sará per la prossima...")
         break # il ciclo termina ed il gioco é finito
      elif controlla_sconfitta(tabella_computer) == True: # situazione di vittoria del giocatore, il computer ha perso
         print("Hai vinto, hai affondato tutte le navi posizionate dal computer!!!")
         break # il ciclo termina ed il gioco é finito
      else:
         continue # nessuno dei due giocatori ha perso, il gioco continua
   if controlla_sconfitta(tabella_giocatore) == False and controlla_sconfitta(tabella_computer) == False: # essendo che é possibile che il giocatore vinca all'ultimo turno si controlla se ha vinto qualcuno. Se si viene restituito solo il messagio sopra
      print("I turni sono terminati, non sei riuscito ad affondare le navi, il computer vince") # se no si informa che il computer ha vinto essendo che i turni sono esauriti


#Invoca la funzione gioca() per avviare il gioco
gioca()





