from core.advbase import *

def module():
    return Raemond

class Raemond(Adv):
    conf = {}
    conf['acl'] = """
        `dragon
        `s4
        `s1
        `s2, fsc
        `s3, fsc
        `fs, x=2
        """
    conf['coabs'] = ['Cleo','Lucretia','Peony']
    conf['share'] = ['Kleimann']


if __name__ == '__main__':
    from core.simulate import test_with_argv
    test_with_argv(None, *sys.argv)
