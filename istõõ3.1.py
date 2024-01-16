#Tehvan Marjapuu
#10.01.2024

import random
import datetime

fail = open("nimekiri.txt", encoding="utf-8")
p = datetime.datetime.now().day
nr = 1

for rida in fail:
    if nr == p:
        print(f"tahvli ette tuleb: {rida.strip()},")
    nr += 1

fail.close()
