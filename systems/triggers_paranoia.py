from sys import argv as sys_arguments
from compiler import *
register_plugin()

# Non timer mission template triggers can fire inside another non timer trigger by script operand and rewrite trigger parameters.
# If there are many non timer triggers with the same condition and one of them called different non timer trigger then followed
# triggers will get wrong parameters. This code will compare starting parameters and ending parameters and will show
# if they have been changed.

# Add argument 'triggers_paranoia' to file 'compile.bat' to inject diagnostics triggers.
INJECT =  True if 'triggers_paranoia' in sys_arguments else False

# Add followed constant
#triggers_paranoia_pos = pos100

troops = [
	["triggers_data","{!}td","{!}td",tf_hero,0,0,fac.commoners,[],0,0,0,0],
]

init_triggers = [
	(ti_on_agent_killed_or_wounded, 0, 0, [], [
		(store_trigger_param, ":defeated_agent", 1),
		(troop_set_slot, "trp_triggers_data", 0, ":defeated_agent"),
		(store_trigger_param, ":attacker_agent", 2),
		(troop_set_slot, "trp_triggers_data", 1, ":attacker_agent"),
		(store_trigger_param, ":wounded", 3),
		(troop_set_slot, "trp_triggers_data", 2, ":wounded"),
	]),

	(ti_on_agent_spawn, 0, 0, [], [
		(store_trigger_param, ":agent", 1),
		(troop_set_slot, "trp_triggers_data", 3, ":agent"),
	]),

	(ti_on_agent_knocked_down, 0, 0, [], [
		(store_trigger_param, ":defeated_agent", 1),
		(troop_set_slot, "trp_triggers_data", 4, ":defeated_agent"),
		(store_trigger_param, ":attacker_agent", 2),
		(troop_set_slot, "trp_triggers_data", 5, ":attacker_agent"),
	]),

	(ti_on_agent_hit, 0, 0, [], [
		(store_trigger_param, ":damage_reciever_agent", 1),
		(troop_set_slot, "trp_triggers_data", 6, ":damage_reciever_agent"),
		(store_trigger_param, ":attacker_agent", 2),
		(troop_set_slot, "trp_triggers_data", 7, ":attacker_agent"),
		(store_trigger_param, ":damage", 3),
		(troop_set_slot, "trp_triggers_data", 8, ":damage"),
		(store_trigger_param, ":bone", 4),
		(troop_set_slot, "trp_triggers_data", 9, ":bone"),
		(store_trigger_param, ":item_missile", 5),
		(troop_set_slot, "trp_triggers_data", 10, ":item_missile"),
		(assign, ":item", reg0),
		(troop_set_slot, "trp_triggers_data", 11, ":item"),
		(copy_position, triggers_paranoia_pos, pos0),
	]),

	(ti_on_agent_mount, 0, 0, [], [
		(store_trigger_param, ":agent", 1),
		(troop_set_slot, "trp_triggers_data", 12, ":agent"),
		(store_trigger_param, ":horse", 2),
		(troop_set_slot, "trp_triggers_data", 13, ":horse"),
	]),

	(ti_on_agent_dismount, 0, 0, [], [
		(store_trigger_param, ":agent", 1),
		(troop_set_slot, "trp_triggers_data", 14, ":agent"),
		(store_trigger_param, ":horse", 2),
		(troop_set_slot, "trp_triggers_data", 15, ":horse"),
	]),

	(ti_on_item_wielded, 0, 0, [], [
		(store_trigger_param, ":agent", 1),
		(troop_set_slot, "trp_triggers_data", 16, ":agent"),
		(store_trigger_param, ":item", 2),
		(troop_set_slot, "trp_triggers_data", 17, ":item"),
	]),

	(ti_on_item_unwielded, 0, 0, [], [
		(store_trigger_param, ":agent", 1),
		(troop_set_slot, "trp_triggers_data", 18, ":agent"),
		(store_trigger_param, ":item", 2),
		(troop_set_slot, "trp_triggers_data", 19, ":item"),
	]),
]

check_triggers = [
	(ti_on_agent_killed_or_wounded, 0, 0, [], [
		(store_trigger_param, ":defeated_agent", 1),
		(troop_get_slot, ":b_defeated_agent", "trp_triggers_data", 0),
		(store_trigger_param, ":attacker_agent", 2),
		(troop_get_slot, ":b_attacker_agent", "trp_triggers_data", 1),
		(store_trigger_param, ":wounded", 3),
		(troop_get_slot, ":b_wounded", "trp_triggers_data", 2),

		(try_begin),
			(this_or_next|negate|eq, ":defeated_agent", ":b_defeated_agent"),
			(this_or_next|negate|eq, ":attacker_agent", ":b_attacker_agent"),
			(negate|eq, ":wounded", ":b_wounded"),
			(display_message, "@{!}Error_trigger_parameters: ti_on_agent_killed_or_wounded"),
		(try_end),
	]),

	(ti_on_agent_spawn, 0, 0, [], [
		(store_trigger_param, ":agent", 1),
		(troop_get_slot, ":b_agent", "trp_triggers_data", 3),
		(try_begin),
			(negate|eq, ":agent", ":b_agent"),
			(display_message, "@{!}Error_trigger_parameters: ti_on_agent_spawn"),
		(try_end),		
	]),

	(ti_on_agent_knocked_down, 0, 0, [], [
		(store_trigger_param, ":defeated_agent", 1),
		(troop_get_slot, ":b_defeated_agent", "trp_triggers_data", 4),
		(store_trigger_param, ":attacker_agent", 2),
		(troop_get_slot, ":b_attacker_agent", "trp_triggers_data", 5),

		(try_begin),
			(this_or_next|negate|eq, ":defeated_agent", ":b_defeated_agent"),
			(negate|eq, ":attacker_agent", ":b_attacker_agent"),
			(display_message, "@{!}Error_trigger_parameters: ti_on_agent_knocked_down"),
		(try_end),
	]),

	(ti_on_agent_hit, 0, 0, [], [
		(store_trigger_param, ":damage_reciever_agent", 1),
		(troop_get_slot, ":b_damage_reciever_agent", "trp_triggers_data", 6),
		(store_trigger_param, ":attacker_agent", 2),
		(troop_get_slot, ":b_attacker_agent", "trp_triggers_data", 7),
		(store_trigger_param, ":damage", 3),
		(troop_get_slot, ":b_damage", "trp_triggers_data", 8),
		(store_trigger_param, ":bone", 4),
		(troop_get_slot, ":b_bone", "trp_triggers_data", 9),
		(store_trigger_param, ":item_missile", 5),
		(troop_get_slot, ":b_item_missile", "trp_triggers_data", 10),
		(assign, ":item", reg0),
		(troop_get_slot, ":b_item", "trp_triggers_data", 11),

		(try_begin),
			(get_sq_distance_between_positions, ":sq_distance", pos0, triggers_paranoia_pos),
			(this_or_next|negate|eq, ":sq_distance", 0),
			(this_or_next|negate|eq, ":damage_reciever_agent", ":b_damage_reciever_agent"),
			(this_or_next|negate|eq, ":attacker_agent", ":b_attacker_agent"),
			(this_or_next|negate|eq, ":damage", ":b_damage"),
			(this_or_next|negate|eq, ":bone", ":b_bone"),
			(this_or_next|negate|eq, ":item_missile", ":b_item_missile"),
			(negate|eq, ":item", ":b_item"),
			(display_message, "@{!}Error_trigger_parameters: ti_on_agent_hit"),
		(try_end),
	]),

	(ti_on_agent_mount, 0, 0, [], [
		(store_trigger_param, ":agent", 1),
		(troop_get_slot, ":b_agent", "trp_triggers_data", 12),
		(store_trigger_param, ":horse", 2),
		(troop_get_slot, ":b_horse", "trp_triggers_data", 13),

		(try_begin),
			(this_or_next|negate|eq, ":agent", ":b_agent"),
			(negate|eq, ":horse", ":b_horse"),
			(display_message, "@{!}Error_trigger_parameters: ti_on_agent_mount"),
		(try_end),
	]),

	(ti_on_agent_dismount, 0, 0, [], [
		(store_trigger_param, ":agent", 1),
		(troop_get_slot, ":b_agent", "trp_triggers_data", 14),
		(store_trigger_param, ":horse", 2),
		(troop_get_slot, ":b_horse", "trp_triggers_data", 15),

		(try_begin),
			(this_or_next|negate|eq, ":agent", ":b_agent"),
			(negate|eq, ":horse", ":b_horse"),
			(display_message, "@{!}Error_trigger_parameters: ti_on_agent_dismount"),
		(try_end),
	]),

	(ti_on_item_wielded, 0, 0, [], [
		(store_trigger_param, ":agent", 1),
		(troop_get_slot, ":b_agent", "trp_triggers_data", 16),
		(store_trigger_param, ":item", 2),
		(troop_get_slot, ":b_item", "trp_triggers_data", 17),

		(try_begin),
			(this_or_next|negate|eq, ":agent", ":b_agent"),
			(negate|eq, ":item", ":b_item"),
			(display_message, "@{!}Error_trigger_parameters: ti_on_item_wielded"),
		(try_end),
	]),

	(ti_on_item_unwielded, 0, 0, [], [
		(store_trigger_param, ":agent", 1),
		(troop_get_slot, ":b_agent", "trp_triggers_data", 18),
		(store_trigger_param, ":item", 2),
		(troop_get_slot, ":b_item", "trp_triggers_data", 19),

		(try_begin),
			(this_or_next|negate|eq, ":agent", ":b_agent"),
			(negate|eq, ":item", ":b_item"),
			(display_message, "@{!}Error_trigger_parameters: ti_on_item_unwielded"),
		(try_end),
	]),
]

def preprocess_entities(glob):
	# Integrate code to all mission_templates
	if INJECT:
		for i in range(len(init_triggers)):
			definition = init_triggers[i][0]
			for mission_no in glob['mission_templates']:
				count = 0
				for cur_trigger in mission_no[5]:
					if cur_trigger[0] == definition: count += 1
				if count > 1: # don't check trigger used only once
					mission_no[5].insert(0, init_triggers[i])
					mission_no[5].append(check_triggers[i])