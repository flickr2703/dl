if __name__ == '__main__':
    import adv_test
else:
    import adv.adv_test
import adv
import slot

def module():
    return Kleimann

class Kleimann(adv.Adv):
    a1 = ('fs',0.4)
    a3 = ('s',0.2)
 
    conf = {}
    conf['acl'] = """
        `fs, seq=5 and s1.charged >= 2500
        `s1, seq=5 and cancel or pin='fs'
        `s2, seq=5 and cancel or pin='fs'
        """


if __name__ == '__main__':
    conf = {}
    adv_test.test(module(), conf, verbose=0)