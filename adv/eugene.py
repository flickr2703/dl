from core.advbase import *
from module.template import RngCritAdv

def module():
    return Eugene

class Eugene(RngCritAdv):    
    conf = {}
    conf['slots.a'] = ['The_Shining_Overlord', 'Memory_of_a_Friend']
    conf['slots.d'] = 'Gaibhne_and_Creidhne'
    conf['acl'] = """
        `dragon(c3-s-end), s
        `s3
        `s1
        `s2
        `s4, fsc and not self.inspiration()>=5 and not self.energy()>=5
        `fs, x=2
    """
    conf['coabs'] = ['Hunter_Sarisse', 'Dragonyule_Cleo', 'Summer_Estelle']
    conf['share'] = ['Gala_Elisanne', 'Ranzal']

    def prerun(self):
        self.checkmate = 0
        o_s2_check = self.a_s_dict['s2'].check
        self.a_s_dict['s2'].check = lambda: not self.a_s_dict['s2']._static.silence and self.checkmate > 0
        self.config_rngcrit(cd=10)

    @staticmethod
    def prerun_skillshare(adv, dst):
        adv.checkmate = 0

    def rngcrit_skip(self):
        return self.inspiration()>=5

    def rngcrit_cb(self):
        self.inspiration.add(1)

    def s1_proc(self, e):
        if e.group == 2:
            self.checkmate = min(self.checkmate+1, 2)

    def s2_proc(self, e):
        self.checkmate -= 1

if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)