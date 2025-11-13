import random
import time
import sys 

opzioni = []
opzioni_c =['sushi','pizza','pasta','cinese','kebab','indiano','piadina','fast food']
print("ciao, benvenuto!\n mi hanno detto che sei bloccato su una scelta molto importante\n non temere, ci sono io qui.")

print("al momento posso aiutarti solo a scegliere cosa mangiare... \n (presto mi aggiornerneranno, tranquillo!!)")
time.sleep(1.75)
print("hai gia in mente qualcosa?")
scelta = input("y/n \n")

time.sleep(0.75)
if scelta == "y":
    print("dimmi pure cosa avevi in mente \n")
    opzioni_u = input("per favore, separa le tue opzioni con una ',' \n")
    opzioni=[x.strip() for x in opzioni_u.split(',')]
    print("ottimo, dammi solo un secondo")
    time.sleep(1.80)
    scelta_finale=random.choice(opzioni)
    print("\n per te ho scelto ",scelta_finale)
    print("penso proprio che", scelta_finale, "sia la cosa migliore da mangiare oggi")
    print("buon appetito, a presto!")

else:
    print("perfetto, ti do io qualche idea")
    print("dammi solo un secondo, penso alle opzioni migliori per te", end="",flush=True)
    for i in range(3):
        time.sleep(1)
        print(".",end='',flush=True)
    time.sleep(2)
    print("\n",opzioni_c)
    print("ecco le migliori opzioni che sono riuscito a trovare \n hai gia' qualcosa in mente? ")
    risposta = input(" si/no ")
    if risposta == "si":
        time.sleep(1)
        print("bravissimo/a!!, alla fine avevi bisogno solo di qualche idea ")
        print("il mio aiuto per oggi finisce qua! spero di rivederti presto!! ")
    else:
        time.sleep(1)
        print("nessun problema, ci penso io")
        print("dammi solo qualche secondo")
        for i in range(3):
            time.sleep(0.75)
            print(".",end='',flush=True)
        scelta_finale=random.choice(opzioni_c)
        print("\n",scelta_finale)
        print("\n penso proprio che", scelta_finale, "sia la cosa migliore da mangiare oggi\n Buon appetito, A presto!")
