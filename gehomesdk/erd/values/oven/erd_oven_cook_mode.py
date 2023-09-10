import enum

@enum.unique
class ErdOvenCookMode(enum.Enum):
    """See ErdCookMode.smali"""
    BAKED_GOODS = 60
    BAKED_GOODS_DELAYSTART = 65
    BAKETIMEDSHUTOFF_DELAYSTART = 7
    BAKETIMED_TWOTEMP = 5
    BAKETIMED_TWOTEMP_DELAYSTART = 9
    BAKETIMED_WARM = 4
    BAKETIMED_WARM_DELAYSTART = 8
    BAKE_DELAYSTART = 3
    BAKE_NOOPTION = 1
    BAKE_PROBE = 2
    BAKE_PROBE_DELAYSTART = 6
    BAKE_SABBATH = 10
    BROIL_HIGH = 12
    BROIL_LOW = 11
    CONVBAKETIMEDSHUTOFF_DELAYSTART = 24
    CONVBAKETIMED_TWOTEMP = 22
    CONVBAKETIMED_TWOTEMP_DELAYSTART = 26
    CONVBAKETIMED_WARM = 21
    CONVBAKETIMED_WARM_DELAYSTART = 25
    CONVBAKE_DELAYSTART = 20
    CONVBAKE_NOOPTION = 18
    CONVBAKE_PROBE = 19
    CONVBAKE_PROBE_DELAYSTART = 23
    CONVBROILCRISP_NOOPTION = 47
    CONVBROILCRISP_PROBE = 48
    CONVBROIL_HIGH_NOOPTION = 46
    CONVBROIL_LOW_NOOPTION = 45
    CONVMULTIBAKETIMEDSHUTOFF_DELAYSTART = 33
    CONVMULTIBAKETIMED_TWOTEMP = 31
    CONVMULTIBAKETIMED_TWOTEMP_DELAYSTART = 35
    CONVMULTIBAKETIMED_WARM = 30
    CONVMULTIBAKETIMED_WARM_DELAYSTART = 34
    CONVMULTIBAKE_DELAYSTART = 29
    CONVMULTIBAKE_NOOPTION = 27
    CONVMULTIBAKE_PROBE = 28
    CONVMULTIBAKE_PROBE_DELAYSTART = 32
    CONVROASTTIMEDSHUTOFF_DELAYSTART = 42
    CONVROASTTIMED_TWOTEMP = 40
    CONVROASTTIMED_TWOTEMP_DELAYSTART = 44
    CONVROASTTIMED_WARM = 39
    CONVROASTTIMED_WARM_DELAYSTART = 43
    CONVROAST_DELAYSTART = 38
    CONVROAST_NOOPTION = 36
    CONVROAST_PROBE = 37
    CONVROAST_PROBE_DELAYSTART = 41
    CUSTOMSELFCLEAN = 49
    CUSTOMSELFCLEAN_DELAYSTART = 50
    DUALBROIL_HIGH_NOOPTION = 54
    DUALBROIL_LOW_NOOPTION = 53
    FROZEN_SNACKS = 56
    FROZEN_SNACKS_MULTI = 57
    FROZEN_PIZZA = 58
    FROZEN_PIZZA_MULTI = 59
    FROZEN_SNACKS_DELAYSTART = 61
    FROZEN_SNACKS_MULTI_DELAYSTART = 62    
    FROZEN_PIZZA_DELAYSTART = 63
    FROZEN_PIZZA_MULTI_DELAYSTART = 64

    NOMODE = 0
    PROOF_DELAYSTART = 14
    PROOF_NOOPTION = 13
    STEAMCLEAN = 51
    STEAMCLEAN_DELAYSTART = 52
    WARM_DELAYSTART = 17
    WARM_NOOPTION = 15
    WARM_PROBE = 16
    AIRFRY = 158
    VENT_BAKE = 94