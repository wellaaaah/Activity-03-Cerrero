class ECalc():
    def Evs(Stat,Modifiers,D,Lvl):
        evn=((Stat/Modifiers)-D*400)
        evn=(evn/Lvl)/4
        evn=(evn*4)
        return evn