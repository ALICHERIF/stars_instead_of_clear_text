import sys
import msvcrt  # Windows seulement

print("Tape ton texte (appuie sur Entrée pour finir) :")

resultat = ""

while True:
    touche = msvcrt.getch()  # lire une touche
    if touche in [b'\r', b'\n']:  # entrée
        print()
        break
    elif touche == b'\x08':  # backspace
        if len(resultat) > 0:
            resultat = resultat[:-1]
            # Efface le dernier * à l'écran
            sys.stdout.write('\b \b')
            sys.stdout.flush()
    else:
        resultat += touche.decode("utf-8", errors="ignore")
        sys.stdout.write('*')
        sys.stdout.flush()

print(f"Tu as tapé : {resultat!r}")
