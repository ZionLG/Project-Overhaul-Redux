from compiler import *
from module_items import imodbits_none, imodbits_horse_basic
from module_troops import no_scene, reserved, wp, mercenary_face_1, mercenary_face_2

register_plugin(__name__) # v0.1

dialogs = [
    ####################################################################################################################
    # Boat Captains
    ####################################################################################################################
    [
        anyone,
        "start",
        [
            (is_between, "$g_talk_troop", tavern_captains_begin, tavern_captains_end),
            (eq, "$talk_context", tc_tavern_talk),
            (troop_get_slot, reg7, "$g_talk_troop", slot_troop_player_debt),
            (gt, reg7, 0),
        ],
        "Hey, {playername}! You still owe me {reg7} denars from our last voyage!",
        "boat_captain_pay_debt",
        [],
    ],
    [
        anyone | plyr,
        "boat_captain_pay_debt",
        [(store_troop_gold, ":gold", "trp_player"), (ge, ":gold", reg7)],
        "Right. Here's your money.",
        "close_window",
        [
            (troop_remove_gold, "trp_player", reg7),
            (troop_set_slot, "$g_talk_troop", slot_troop_player_debt, 0),
        ],
    ],
    [
        anyone | plyr,
        "boat_captain_pay_debt",
        [],
        "Sorry, I don't have it right now.",
        "close_window",
        [],
    ],
    [
        anyone,
        "start",
        [
            (is_between, "$g_talk_troop", tavern_captains_begin, tavern_captains_end),
            (eq, "$talk_context", tc_tavern_talk),
            (eq, "$players_captain", 0),
        ],
        "Good day {sir/madam}! Would you like to charter my ship?",
        "boat_captain_talk",
        [],
    ],
    [
        anyone | plyr,
        "boat_captain_talk",
        [],
        "Maybe. How would that work?",
        "boat_captain_explain",
        [],
    ],
    [
        anyone,
        "boat_captain_explain",
        [],
        "It's simple enough. You meet me and my crew down at the port, pay us 100 denars up front and tell us where to go.\
 Each additional day would cost you another 100 denars, but my ship is pretty quick. It is unlikely that the voyage will take much longer than that.\
 But if you want my crew to wait for you in port or near a shore, you will still have to pay until you dismiss us.",
        "close_window",
        [],
    ],
    [anyone | plyr, "boat_captain_talk", [], "Thanks, not now.", "close_window", []],
    [
        anyone | plyr,
        "mercenary_after_recruited",
        [(eq, "$g_talk_troop", "$players_captain")],
        "I no longer need your services. You may return home.",
        "close_window",
        [
            (troop_get_slot, ":home_port", "$players_captain", slot_troop_home_port),
            (troop_set_slot, "$players_captain", slot_troop_cur_center, ":home_port"),
            (assign, "$players_captain", 0),
        ],
    ],
]


injection = {
    "naval_encountered_party": [
        (else_try),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_port),
          (eq, "$g_player_icon_state", pis_normal),
          (jump_to_menu, "mnu_close"),  # Do nothing.
        (else_try),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_port),
          (jump_to_menu, "mnu_port_disembark"),
        (else_try),
          (party_slot_eq, "$g_encountered_party", slot_party_type, spt_ship_land),
          (jump_to_menu, "mnu_ship_reembark"),
        (else_try),
          (eq, "$g_encountered_party", "p_camp_bandits"),
          (eq, "$g_player_icon_state", pis_ship),
          (jump_to_menu, "mnu_ship_anchor"),
    ],
}
