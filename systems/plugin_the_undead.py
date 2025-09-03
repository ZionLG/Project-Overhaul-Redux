from compiler import *

from module_troops import *

register_plugin(__name__)  # v0.0.1

undead_face1 = 0x0000000000000000000000000000000000000000000000000000000000000000
undead_face2 = 0x000000003F000493000000000000000000000000000000000000000000000000

troops = [
    [
        "zombie",
        "Zombie",
        "Zombies",
        tf_undead | tf_always_fall_dead,
        0,
        0,
        fac.undeads,
        [
            itm.cleaver,
            itm.sickle,
            itm.hatchet,
            itm.knife,
            itm.butchering_knife,
            itm.wooden_stick,
            itm.mace_1,
        ],
        def_attrib | level(3),
        wp(60),
        knows_ironflesh_10,
        undead_face1,
        undead_face2,
    ],
    [
        "zombie_spear",
        "Zombie with Spear",
        "Zombies with Spears",
        tf_undead | tf_always_fall_dead | tf_guarantee_shield,
        0,
        0,
        fac.undeads,
        [itm.spear, itm.shortened_spear, itm.fur_covered_shield],
        def_attrib | level(8),
        wp(80),
        knows_ironflesh_10 | knows_power_strike_1 | knows_shield_2,
        undead_face1,
        undead_face2,
    ],
    [
        "zombie_axe",
        "Zombie with Axe",
        "Zombies with Axes",
        tf_undead | tf_always_fall_dead,
        0,
        0,
        fac.undeads,
        [
            itm.axe,
            itm.hand_axe,
            itm.hide_covered_round_shield,
            itm.hide_covered_round_shield,
        ],
        def_attrib | level(8),
        wp(80),
        knows_ironflesh_10 | knows_power_strike_2 | knows_shield_1,
        undead_face1,
        undead_face2,
    ],
]

injection = {
    "undead_upgrades": [
        upgrade2(troops, "zombie", "zombie_spear", "zombie_axe")
    ],
}
