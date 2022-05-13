import Stat_script_1_stat as S
import EV_script_2_ev as EV 

def main(): 
     
    print ("Choose an Option:\n")
    user=int(input("1 Stat\n" "2 Ev\n"))
    if user==1:
        base=int(input("Base: "))
        Iv=int(input("IV: "))
        if Iv<0 or Iv>31:
            print("Value is out of range :(")
            main()
        
        Ev=int(input("EV: "))
        if Ev<0 or Ev> 255:
            print ("Value is out of range :(")
            main()
        lvl=int(input("Level: "))
        print('\n',base,Iv,Ev,lvl,'\n')
        result = S.Scalc.hp(base,Iv,Ev,lvl)
        print("Pokemon's Hp stat value is: ",result, '\n\n')

    elif user==2:
        Stat=int(input("Enter Desired Increase Stat: "))
        Modifier=int(input("Enter Modifier: "))
        Lvl=int(input("Enter Level: "))  
        base=int(input("Base: "))
        Iv=int(input("IV: "))
        Ev=int(input("EV: "))
        D=(2*base+Iv)
        D=(D+(Ev/4))
        D=(D*(Lvl/100))

        print("EVs Needed is: ", EV.ECalc.Evs(Stat,Modifier,D,Lvl))
        main()
    else:
        main()
    
main()