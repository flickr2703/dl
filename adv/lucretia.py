from core.advbase import *

def module():
    return Lucretia

class Lucretia(Adv):
    
    conf = {}
    conf['acl'] = """
        `dragon, x>2
        `s3, not self.s3_buff
        `s1, cancel
        `s2, self.energy()<=3
        `s4, x=5
        """
    conf['coabs'] = ['Blade','Tobias','Peony']
    conf['share'] = ['Summer_Patia']


        
    def s1_proc(self, e):
        if self.energy() == 5:
            Teambuff(f'{e.name}_cc',0.1,30,'crit','rate').on()
        self.energy.add(2, team=True)

    def s2_proc(self, e):
        self.energy.add(3)

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)