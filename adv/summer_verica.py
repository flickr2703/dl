from core.advbase import *

def module():
    return Summer_Verica

class Summer_Verica(Adv):
    conf = {}
    conf['slots.a'] = [
        'Study_Rabbits',
        'Give_Me_Your_Wounded',
        'Castle_Cheer_Corps',
        'From_Whence_He_Comes',
        'Bellathorna'
    ]
    conf['slots.d'] = 'Ramiel'
    conf['acl'] = """
        `dragon
        `s3
        `s4
        `s2
        `s1, not buff(s1)
        """
    conf['coabs'] = ['Dagger2','Tobias','Blade']
    conf['share'] = ['Summer_Luca', 'Patia']

    def prerun(self):
        self.s2.autocharge_init(1578).on()


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
