#algorithm tester
#MAtthew Cole

import algoImp as al
wk = al.workoutGen()

wkls = None
while(True):
    try:
        wkls = wk.generator("swim")
        break
    except:
        pass

print(wk.formatter(wkls.wk))