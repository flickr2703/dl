import adv_test
import adv
import wep.blade_wellplayed as weapon
from core.timeline import *
from core.log import *



def module():
    return Taro

class Taro(adv.Adv):
    conf = {}
    conf.update( {
        "s1_dmg"      : 2.93*3   ,
        "s1_sp"       : 2392   ,
        "s1_startup"  : 0.1    ,
        "s1_recovery" : 1.9    ,

        "s2_dmg"      : 7.9   ,
        "s2_sp"       : 5259   ,
        "s2_startup"  : 0.1    ,
        "s2_recovery" : 1.9    ,

        #"s3_dmg"      : 3.54*3 ,
        #"s3_sp"       : 8030   ,
        #"s3_startup"  : 0.1    ,
        #"s3_recovery" : 2.7    ,

        "mod_d"   : ('att'  , 'passive' , 0.6)  ,
        "mod_wp"  : ('s'    , 'passive' , 0.25) ,
        "mod_wp2" : ('crit' , 'passive' , 0.06) ,
        } )
    conf.update(weapon.conf)

    def init(this):
        pass
    



if __name__ == '__main__':
    conf = {}
    conf['acl'] = """
        `s1, seq=5 
        `s2, seq=5 
        `s3, seq=5
        """
    adv_test.test(module(), conf, verbose=0)
