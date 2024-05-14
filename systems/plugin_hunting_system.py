from compiler import *
from module_items import imodbits_none, imodbits_horse_basic
from module_troops import no_scene, reserved, wp, mercenary_face_1, mercenary_face_2

register_plugin(__name__) # v0.1

party_templates = [
    (
        "deer_herd",
        "Deer Herd",
        icon.cattle | carries_goods(10),
        0,
        fac.wild_animals,
        merchant_personality,
        [(trp.deer, 5, 25)],
    ),
]
factions = [
    ("wild_animals", "Wild Animals", 0, 0.1, [("player_faction", -0.85)], [], 0xFFFFFF),
]
items = [
    [
        "deer_meat",
        "Venison",
        [("raw_meat", 0)],
        itp_merchandise | itp_type_goods | itp_consumable | itp_food,
        0,
        150,
        weight(30) | abundance(100) | food_quality(40) | max_ammo(30),
        imodbits_none,
    ],
    [
        "deer",
        "Deer",
        [("deer", 0)],
        itp_unique | itp_type_horse,
        0,
        1411,
        abundance(40)
        | hit_points(30)
        | body_armor(5)
        | difficulty(11)
        | horse_speed(50)
        | horse_maneuver(32)
        | horse_charge(20),
        imodbits_horse_basic,
    ],
]
meshes = [
    ("pic_extra_caza", 0, "pic_extra_caza", 0, 0, 0, 0, 0, 0, 1, 1, 1),
]
troops = [
    [
        "deer",
        "Deer",
        "Deer",
        0,
        no_scene,
        reserved,
        fac.neutral,
        [],
        def_attrib | level(0),
        wp(60),
        0,
        mercenary_face_1,
        mercenary_face_2,
    ],
]

scenes = [
    (
        "random_scene_plain_forest2",
        sf_generate | sf_randomize | sf_auto_entry_points,
        "none",
        "none",
        (0, 0),
        (240, 240),
        -0.5,
        "0x00000002bc6845630003e8fa00003ed2000025e300002221",
        [],
        [],
        "outer_terrain_plain",
    ),
]
game_menus = [
    (
        "deer_herd",
        0,
        "You encounter a herd of deer.",
        "none",
        [
            (try_begin),
              (gt, g.num_deers_killed, 0),
              
              (troop_clear_inventory, trp.temp_troop),
              (troop_add_items, trp.temp_troop, itm.deer_meat, g.num_deers_killed),
              (troop_add_items, trp.temp_troop, itm.raw_leather, g.num_deers_killed),
              (party_get_num_companions, l.num_deers, g.g_encountered_party),
              
              (try_begin),
                (ge, g.num_deers_killed, l.num_deers),
                (remove_party, g.g_encountered_party),
              (else_try),
                (party_remove_members, g.g_encountered_party, trp.deer, g.num_deers_killed),
              (try_end), 
            
              (assign, g.num_deers_killed, 0),
              
              (troop_sort_inventory, trp.temp_troop),
              (change_screen_loot, trp.temp_troop), 
            (try_end),
            
            (set_background_mesh, mesh.pic_extra_caza),
        ],
        [
            (
                "deer_kill",
                [
                    (try_begin),
                    (neg | party_is_active, g.g_encountered_party),
                    (disable_menu_option),
                    (try_end),
                ],
                "Hunt some of the animals.",
                [
                    (set_jump_mission, mt.deer_hunting),
                    (jump_to_scene, scn.random_scene_plain_forest2),
                    (change_screen_mission),
                ],
            ),
            (
                "leave",
                [],
                "Leave.",
                [
                    (change_screen_return),
                ],
            ),
        ],
    ),
    (
        "deer_herd_kill_end",
        0,
        "You shouldn't be reading this.",
        "none",
        [(change_screen_return)],
        [],
    ),
]

sounds = [
    ("deer_dying", sf_2d | sf_priority_15 | sf_vol_10, ["deer_dying.wav"]),
    ("horn", sf_2d|sf_priority_15|sf_vol_8,["horn.wav"]),
]
mission_templates = [
    (
        "deer_hunting",
        mtf_battle_mode,
        -1,
        "You lead your deers to battle.",
        [
            (1, mtef_team_0 | mtef_leader_only, 0, aif_start_alarmed, 12, []),
            (4, mtef_visitor_source | mtef_team_2, 0, aif_start_alarmed, 0, []),
        ],
        [
            (ti_tab_pressed, 0, 0, [(set_trigger_result, 1)], []),  # leaving area
            (
                0,
                0,
                ti_once,
                [  # spawing deers
                 
                    (play_sound, snd.horn),
                    
                    (
                        party_count_members_of_type,
                        l.num_deers,
                        g.g_encountered_party,
                        trp.deer,
                    ), # num_deers = count of deers in party
                    
                    (val_sub, l.num_deers, 1), # removing one deer which will be the lead deer.
                    (ge, l.num_deers, 0),
                    (assign, g.num_deers_killed, 0), # num_deers_killed initialized.
                    
                    (get_scene_boundaries, pos10, pos11),
                    
                    (position_get_x, l.scene_min_x, pos10), 
                    (position_get_x, l.scene_max_x, pos11), 

                    (position_get_y, l.scene_min_y, pos10), 
                    (position_get_y, l.scene_max_y, pos11),
                    
                    (store_div, l.border_x, l.scene_max_x, 10),
                    (val_add, l.scene_min_x, l.border_x),
                    (val_sub, l.scene_max_x, l.border_x),
                    
                    (store_div, l.border_y, l.scene_max_y, 10),
                    (val_add, l.scene_min_y, l.border_y),
                    (val_sub, l.scene_max_y, l.border_y),
                    
                    # Making an inner border where we can spawn the deer.
                    
                    (store_random_in_range, l.x_pos, l.scene_min_x, l.scene_max_x),
                    (store_random_in_range, l.y_pos, l.scene_min_y, l.scene_max_y),
                    
                    (init_position, pos1),
                    
                    (position_set_x, pos1, l.x_pos),
                    (position_set_y, pos1, l.y_pos),
                    (position_set_z_to_ground_level, pos1),
                    
                    (set_spawn_position, pos1),

                    # Spawn Loacation
                    
                    (spawn_horse, itm.deer),
                    (assign, g.leading_deer, reg0),
                    
                    (try_for_range, l.unused, 0, l.num_deers),
                      (init_position, pos1),
                      (store_random_in_range, l.x_pos_add, 0, 1000),
                      (store_random_in_range, l.y_pos_add, 0, 1000),
                      (val_add, l.x_pos_add, l.x_pos),
                      (val_add, l.y_pos_add, l.y_pos),
                      (position_set_x, pos1, l.x_pos_add),
                      (position_set_y, pos1, l.y_pos_add),
                      (position_set_z_to_ground_level, pos1),
                      
                      (set_spawn_position, pos1),
                      (spawn_horse, itm.deer),
                    (try_end),
                ],
                [],
            ),
            # Make sure its a deer to play the sound
            (
                ti_on_agent_killed_or_wounded,
                0,
                0,
                [
                    (store_trigger_param_1, l.dead_agent_no),
                    (agent_get_item_id, l.cur_troop_id, l.dead_agent_no),  
                    
                    (eq, l.cur_troop_id, itm.deer),
                ],
                [(play_sound, snd.deer_dying)],
            ),
            (
                1,
                0,
                0,
                [],  # wounded deers move slower
                [
                    (try_for_agents, reg(1)),
                      (agent_get_item_id, reg(2), reg(1)),
                      (eq, reg(2), itm.deer), #ensure agent is a deer
                    
                      (store_agent_hit_points, reg(2), reg(1)),
                      (store_mul, reg(3), 20, reg(2)), # 20 * hitpoints = speed
                      (val_div, reg(3), 40), # speed / 40
                      
                      (agent_set_speed_limit, reg(1), reg(3)), # set speed limit
                    (try_end),
                ],
            ),
            ( # this replaces the leading deer if it dies, might want to remove it later.
                5,
                0,
                0,
                [
                    (negate | agent_is_alive, g.leading_deer),
                ],
                [
                    (try_for_agents, reg(1)),
                      (agent_get_item_id, reg(2), reg(1)),
                      (eq, reg(2), itm.deer),
                      (assign, g.leading_deer, reg(1)),
                    (try_end),
                ],
            ),
            ( # this checks how many deers are dead, each time a deer dies, the leader goes to a random location.
                1,
                0,
                0,
                [],
                [
                    (assign, l.num_kills, 0),
                    
                    (try_for_agents, reg(1)),
                      (agent_get_item_id, reg(2), reg(1)),
                      (eq, reg(2), itm.deer),
                      (store_agent_hit_points, reg(2), reg(1)),
                      (eq, reg(2), 0),
                      (val_add, l.num_kills, 1),
                    (try_end), # count the number of dead deers
                                           
                    (gt, l.num_kills, g.num_deers_killed),
                    
                    (get_scene_boundaries, pos10, pos11),
                    (position_get_x, l.scene_min_x, pos10),
                    (position_get_x, l.scene_max_x, pos11),
                    (position_get_y, l.scene_min_y, pos10),
                    (position_get_y, l.scene_max_y, pos11),
                    (store_div, l.border_x, l.scene_max_x, 10),
                    (val_add, l.scene_min_x, l.border_x),
                    (val_sub, l.scene_max_x, l.border_x),
                    (store_div, l.border_y, l.scene_max_y, 10),
                    (val_add, l.scene_min_y, l.border_y),
                    (val_sub, l.scene_max_y, l.border_y),
                    (store_random_in_range, l.x_pos, l.scene_min_x, l.scene_max_x),
                    (store_random_in_range, l.y_pos, l.scene_min_y, l.scene_max_y),
                    (init_position, pos1),
                    (position_set_x, pos1, l.x_pos),
                    (position_set_y, pos1, l.y_pos),
                    (position_set_z_to_ground_level, pos1), # calculate a random position
                    
                    (agent_set_scripted_destination, g.leading_deer, pos1), # set the leader to go to the random position
                    
                    (assign, g.num_deers_killed, l.num_kills), # update the number of dead deers
                ],
            ),
            (  # leader goes to a random location
                5,
                0,
                0,
                [],
                [
                    (agent_get_position, pos1, g.leading_deer),
                    (position_get_x, l.x_pos, pos1),
                    (position_get_y, l.y_pos, pos1),
                    (this_or_next | le, l.x_pos, 5000),
                    (this_or_next | le, l.y_pos, 5000),
                    (this_or_next | ge, l.x_pos, 38000),
                    (ge, l.y_pos, 38000),
                    (get_scene_boundaries, pos10, pos11),
                    (position_get_x, l.scene_min_x, pos10),
                    (position_get_x, l.scene_max_x, pos11),
                    (position_get_y, l.scene_min_y, pos10),
                    (position_get_y, l.scene_max_y, pos11),
                    (store_div, l.border_x, l.scene_max_x, 10),
                    (val_add, l.scene_min_x, l.border_x),
                    (val_sub, l.scene_max_x, l.border_x),
                    (store_div, l.border_y, l.scene_max_y, 10),
                    (val_add, l.scene_min_y, l.border_y),
                    (val_sub, l.scene_max_y, l.border_y),
                    (store_random_in_range, l.x_pos, l.scene_min_x, l.scene_max_x),
                    (store_random_in_range, l.y_pos, l.scene_min_y, l.scene_max_y),
                    (init_position, pos1),
                    (position_set_x, pos1, l.x_pos),
                    (position_set_y, pos1, l.y_pos),
                    (position_set_z, pos1, 10000),
                    (position_set_z_to_ground_level, pos1),
                    (agent_set_scripted_destination, g.leading_deer, pos1),
                ],
            ),
            (
                1,
                0,
                0,
                [],
                [
                    (try_for_agents, reg(1)),
                      (agent_get_item_id, reg(2), reg(1)),
                      (eq, reg(2), itm.deer),
                      (store_agent_hit_points, l.health, reg(1)),
                      (store_sub, l.damage, 100, l.health),
                      (agent_get_slot, l.prev_damage, reg(1), 1),
                      (neq, l.prev_damage, l.damage),
                      (agent_set_slot, reg(1), 1, l.damage),
                      (agent_get_position, pos1, reg(1)),
                      (position_get_x, l.x_pos, pos1),
                      (position_get_y, l.y_pos, pos1),
                      (store_random_in_range, l.x_pos_add, 0, 1000),
                      (store_random_in_range, l.y_pos_add, 0, 1000),
                      (val_add, l.x_pos, l.x_pos_add),
                      (val_add, l.y_pos, l.y_pos_add),
                      (position_set_x, pos1, l.x_pos),
                      (position_set_y, pos1, l.y_pos),
                      (agent_set_scripted_destination, reg(1), pos1),
                    (try_end),
                ],
            ),
            (
                0.5,
                0,
                0,  # deer travelling
                [],
                [
                    (get_player_agent_no, reg(1)),
                    (agent_get_position, pos1, reg(1)),
                    (agent_get_position, pos4, g.leading_deer),
                    (position_get_x, l.x_pos, pos4),
                    (position_get_y, l.y_pos, pos4),
                    (try_for_agents, reg(1)),
                      (agent_get_item_id, reg(2), reg(1)),
                      (eq, reg(2), itm.deer),
                      (agent_get_position, pos2, reg(1)),
                      (get_distance_between_positions, reg(3), pos1, pos2),
                      (try_begin),
                        (position_get_x, l.pos_x, pos2),
                        (position_get_x, l.pos_y, pos2),
                        (position_get_x, l.scene_min_x, pos10),
                        (position_get_x, l.scene_max_x, pos11),
                        (position_get_y, l.scene_min_y, pos10),
                        (position_get_y, l.scene_max_y, pos11),
                        (store_div, l.border_x, l.scene_max_x, 10),
                        (val_add, l.scene_min_x, l.border_x),
                        (val_sub, l.scene_max_x, l.border_x),
                        (store_div, l.border_y, l.scene_max_y, 10),
                        (val_add, l.scene_min_y, l.border_y),
                        (val_sub, l.scene_max_y, l.border_y),
                        (this_or_next | gt, l.pos_x, l.scene_max_x),
                        (this_or_next | lt, l.pos_x, l.scene_min_x),
                        (this_or_next | gt, l.pos_y, l.scene_max_y),
                        (lt, l.pos_y, l.scene_min_y),
                        (store_random_in_range, l.x_pos, l.scene_min_x, l.scene_max_x),
                        (store_random_in_range, l.y_pos, l.scene_min_y, l.scene_max_y),
                        (init_position, pos1),
                        (position_set_x, pos1, l.x_pos),
                        (position_set_y, pos1, l.y_pos),
                        (position_set_z, pos1, 10000),
                        (position_set_z_to_ground_level, pos1),
                        (agent_set_scripted_destination, reg(1), pos1),
                      (else_try),
                        (le, reg(3), 2500),
                        (position_get_x, reg(4), pos1),
                        (position_get_x, reg(5), pos2),
                        (store_sub, l.x_dist, reg(5), reg(4)),
                        (val_mul, l.x_dist, 10),
                        (position_get_y, reg(6), pos1),
                        (position_get_y, reg(7), pos2),
                        (store_sub, l.y_dist, reg(7), reg(6)),
                        (val_mul, l.y_dist, 10),
                        (init_position, pos3),
                        (val_add, l.x_dist, reg(5)),
                        (val_add, l.y_dist, reg(7)),
                        (position_set_x, pos3, l.x_dist),
                        (position_set_y, pos3, l.y_dist),
                        (position_set_z, pos3, 10000),
                        (position_set_z_to_ground_level, pos3),
                        (agent_set_scripted_destination, reg(1), pos3),
                      (else_try),
                        (get_distance_between_positions, reg(3), pos4, pos2),
                        (ge, reg(3), 2000),
                        (init_position, pos6),
                        (store_random_in_range, l.x_pos_add, 0, 1000),
                        (store_random_in_range, l.y_pos_add, 0, 1000),
                        (val_add, l.x_pos_add, l.x_pos),
                        (val_add, l.y_pos_add, l.y_pos),
                        (position_set_x, pos6, l.x_pos_add),
                        (position_set_y, pos6, l.y_pos_add),
                        (position_set_z, pos6, 10000),
                        (position_set_z_to_ground_level, pos6),
                        (agent_set_scripted_destination, reg(1), pos6),
                      (try_end),
                    (try_end),
                ],
            ),
        ],
    ),
]


injection = {
    "animals_encountered_party": [
        (else_try),
          (party_get_template_id, l.party_template, g.g_encountered_party),
          (eq, l.party_template, pt.deer_herd),
          (jump_to_menu, mnu.deer_herd),
    ],
    "wild_animals_food_bonus": [
        (item_set_slot, itm.deer_meat, slot_item_food_bonus, 10),
    ],
    "spawn_wild_animals": [
        (try_begin),
          (store_num_parties_of_template, l.num_parties, pt.deer_herd),
          (lt, l.num_parties, 6),
          (store_random, l.spawn_point, num_mountain_bandit_spawn_points),
          (val_add, l.spawn_point, p.forest_bandit_spawn_point),
          (set_spawn_radius, 25),
          (spawn_around_party, l.spawn_point, pt.deer_herd),
        (try_end),
    ],
    "wild_animal_food": [
        (neq, l.cur_goods, itm.deer_meat),
    ],
    "wild_animal_food_modifier": [
        (this_or_next | eq, ":item_id", "itm_deer_meat"),
    ],
}
