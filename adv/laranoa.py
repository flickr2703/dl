from core.advbase import *
from slot.a import *
from slot.d import *

def module():
    return Laranoa

class Laranoa(Adv):
    comment = 'doesn\'t count spbuff for teammates'

    a3 = ('s',0.3)
    
    conf = {}
    conf['slots.a'] = Primal_Crisis()+The_Wyrmclan_Duo()
    conf['slots.d'] = Siren()
    conf['acl'] = """
        `s3
        `s4
        `s1
        `s2, fsc
        `fs, seq=4
    """
    coab = ['Renee', 'Xander', 'Summer_Estelle']
    share = ['Gala_Elisanne', 'Ranzal']

    def init(self):
        self.buff_class = Teambuff if self.condition('buff all team') else Selfbuff

    def prerun(self):
        self.ahits = 0

    def s2_proc(self, e):
        self.buff_class(e.name,0.10,10).on()
        Selfbuff(f'{e.name}_sp',0.20,10,'sp','passive').on()

    def dmg_proc(self, name, amount):
        if self.hits // 20 > self.ahits:
            self.ahits = self.hits // 20
            Selfbuff('sylvan critdmg',0.10,20,'crit','damage').on()

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)