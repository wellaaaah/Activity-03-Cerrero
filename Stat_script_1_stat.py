class Scalc():
    def hp(base,Iv,Ev,lvl):
        health=(2*base+Iv)
        health=(health+(Ev/4))
        health = (health*lvl)/100+lvl+10
        return health