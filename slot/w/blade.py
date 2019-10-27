import slot
from slot import *


class blade5b1(WeaponBase):
    ele = ['flame','wind']
    wt = 'blade'
    att = 572
    s3 = {
        "dmg"      : 3.54*3   ,
        "sp"       : 8030     ,
        "startup"  : 0.1      ,
        "recovery" : 2.65     ,
    }

class blade5b2(WeaponBase):
    ele = ['water','light']
    wt = 'blade'
    att = 544

class blade5b3(WeaponBase):
    ele = ['shadow']
    att = 590
    wt = 'blade'
    s3 = {
        "dmg"      : 2.13*5 ,
        "sp"       : 7695   ,
        "startup"  : 0.1    ,
        "recovery" : 2.65   ,
    }

class blade4b2(WeaponBase):
    ele = ['light', 'water']
    att = 382
    wt = 'blade'
    s3 = {
        "dmg"      : 9.66   ,
        "sp"       : 8178   ,
        "startup"  : 0.1    ,
        "recovery" : 1.95   ,
    }

class bladeHMSBane(WeaponBaseHMS):
    wt = 'blade'
    att = 353

class bladeHBHBane(WeaponBaseHBH):
    wt = 'blade'
    att = 361

class bladeHMCBane(WeaponBaseHMC):
    wt = 'blade'
    att = 372

class bladeHZDBane(WeaponBaseHZD):
    wt = 'blade'
    att = 383

class bladeHJPBane(WeaponBaseHJP):
    wt = 'blade'
    att = 383


flame  = blade5b1
wind   = blade5b1

water  = blade5b2
light  = blade5b2

shadow = blade5b3


class HDT_Conflagration(WeaponBase):
    ele = ['flame']
    wt = 'blade'
    att = 811
    s3 = {} # Conflagration Blade
    a = [('k', 0.3)]
    ability_desc = {"(Flame) High Midgardsormr's Bane +30%": "If the user is attuned to [[Elements|Flame]]:  increases damage to High Midgardsormr by '''30%'''."}

class HDT_Blinding_Conflagration(WeaponBase):
    ele = ['flame']
    wt = 'blade'
    att = 1621
    s3 = {} # Blinding Blade
    a = []
    ability_desc = {}

class HDT_Torrent(WeaponBase):
    ele = ['water']
    wt = 'blade'
    att = 763
    s3 = {} # Torrent Blade
    a = [('k', 0.3)]
    ability_desc = {"(Water) High Brunhilda's Bane +30%": "If the user is attuned to [[Elements|Water]]:  increases damage to High Brunhilda by '''30%'''."}

class HDT_Ruinous_Torrent(WeaponBase):
    ele = ['water']
    wt = 'blade'
    att = 1527
    s3 = {} # Surging Blade
    a = []
    ability_desc = {}

class HDT_Horizon(WeaponBase):
    ele = ['wind']
    wt = 'blade'
    att = 787
    s3 = {} # Horizon Blade
    a = [('k', 0.3)]
    ability_desc = {"(Wind) High Mercury's Bane +30% (Alt)": "If the user is attuned to [[Elements|Wind]]:  increases damage to High Mercury by '''30%'''."}

class HDT_Endless_Horizon(WeaponBase):
    ele = ['wind']
    wt = 'blade'
    att = 1574
    s3 = {} # Endless Blade
    a = []
    ability_desc = {}

class HDT_Flash(WeaponBase):
    ele = ['light']
    wt = 'blade'
    att = 748
    s3 = {} # Flashing Blade
    a = [('k', 0.3)]
    ability_desc = {"(Light) High Zodiark's Bane +30% (Alt)": "If the user is attuned to [[Elements|Light]]:  increases damage to High Zodiark by '''30%'''."}

class HDT_Brilliant_Flash(WeaponBase):
    ele = ['light']
    wt = 'blade'
    att = 1495
    s3 = {} # Brilliant Blade
    a = []
    ability_desc = {}

class HDT_Abyss(WeaponBase):
    ele = ['shadow']
    wt = 'blade'
    att = 811
    s3 = {} # Enigmatic Blade
    a = [('k', 0.3)]
    ability_desc = {"(Shadow) High Jupiter's Bane +30% (Alt)": "If the user is attuned to [[Elements|Shadow]]:  increases damage to High Jupiter by '''30%'''."}

class HDT_True_Abyss(WeaponBase):
    ele = ['shadow']
    wt = 'blade'
    att = 1621
    s3 = {} # Hellish Blade
    a = []
    ability_desc = {}

