from core.advbase import *

def module():
    return Francesca

class Francesca(Adv):
    conf = {}
    conf['slots.a'] = [
    'Twinfold_Bonds',
    'Flash_of_Genius',
    'Moonlight_Party',
    'The_Plaguebringer',
    'A_Passion_for_Produce'
    ]
    conf['acl'] = """
        `dragon(c3-s-end), s4.check()
        `s3, not buff(s3)
        `s4
        `s2
        `s1
        `fs, x=5
        """
    conf['coabs'] = ['Blade','Dragonyule_Xainfried','Lin_You']
    conf['share'] = ['Curran']


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)