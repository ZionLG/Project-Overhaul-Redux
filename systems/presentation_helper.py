from sys import argv as sys_arguments
from compiler import *
register_plugin()

## Add argument 'prsnt_helper' to file 'compile.bat' to integrate helpler.
compiler_store_overlay_data =  True if 'prsnt_helper' in sys_arguments else False

# Grayscale
color_black           = 0x000000
color_gray            = 0x808080
color_shadow          = 0x373737
color_shadow2         = 0x474747
color_stonegray       = 0x928E85
color_slategray       = 0x708090

text_max_render_height = 296
render_height_high_background = 200
render_height_high_element = 250

scripts = [
("create_presentation_dev_panel", [
(set_fixed_point_multiplier, 1000),
(assign, ":element_scale", 800),
(ui_create_container, "$panel", 0, 0, 700, 200), # Macro operator
(assign, "$num_overlays", "$panel"),
(set_container_overlay, "$panel"),
(ui_create_mesh, reg1, "mesh_white_plane", 0, 0, 35000, 10000), # Macro operator
(overlay_set_color, reg1, color_shadow),
(ui_create_label, reg1, "@Selected overlay`ID", 10, 170, 0, ":element_scale"), # Macro operator
(ui_create_label, "$overlay_type", "@Overlay type", 200, 170, 0, ":element_scale"), # Macro operator
(ui_create_numberbox, "$overlay_input", 120, 170, 0, "$num_overlays", ":input_scale"), # Macro operator
(ui_create_label, reg1, "@pos`X", 10, 135, 0, ":element_scale"), # Macro operator
(ui_create_label, reg1, "@pos`Y", 10, 100, 0, ":element_scale"), # Macro operator
(ui_create_numberbox, "$input_pos_x", 60, 135, 0, 100000), # Macro operator
(ui_create_numberbox, "$input_pos_y", 60, 100, 0, 100000), # Macro operator
(ui_create_label, "$label_size_x", "@scale`X", 10, 45, 0, ":element_scale"), # Macro operator
(ui_create_label, "$label_size_y", "@scale`Y", 10, 10, 0, ":element_scale"), # Macro operator
(ui_create_numberbox, "$input_size_x", 60, 45, 0, 100000), # Macro operator
(ui_create_numberbox, "$input_size_y", 60, 10, 0, 100000), # Macro operator
(ui_create_label, reg1, "@area`size`X", 135, 135, 0, ":element_scale"), # Macro operator
(ui_create_label, reg1, "@area`size`Y", 135, 100, 0, ":element_scale"), # Macro operator
(ui_create_numberbox, "$input_area_size_x", 200, 135, 0, 100000), # Macro operator
(ui_create_numberbox, "$input_area_size_y", 200, 100, 0, 100000), # Macro operator
(ui_create_game_button, "$restart_button", "@Restart", 430, 160, 120, 30), # Macro operator
(ui_create_game_button, "$aligment_button", "@Alignment", 430, 130, 120, 30), # Macro operator
(ui_create_container, "$aligment_container", 490, 0, 210, 200), # Macro operator
(set_container_overlay, "$aligment_container"),
(ui_create_checkbox, "$left_align_checkbox", "mesh_checkbox_off", "mesh_checkbox_on", 10, 170), # Macro operator
(ui_create_checkbox, "$right_align_checkbox", "mesh_checkbox_off", "mesh_checkbox_on", 10, 150), # Macro operator
(ui_create_checkbox, "$center_justify_checkbox", "mesh_checkbox_off", "mesh_checkbox_on", 10, 130), # Macro operator
(ui_create_checkbox, "$double_space_checkbox", "mesh_checkbox_off", "mesh_checkbox_on", 10, 110), # Macro operator
(ui_create_checkbox, "$vertical_align_center_checkbox", "mesh_checkbox_off", "mesh_checkbox_on", 10, 90), # Macro operator
(ui_create_checkbox, "$scrollable_checkbox", "mesh_checkbox_off", "mesh_checkbox_on", 10, 70), # Macro operator
(ui_create_checkbox, "$single_line_checkbox", "mesh_checkbox_off", "mesh_checkbox_on", 10, 50), # Macro operator
(ui_create_checkbox, "$with_outline_checkbox", "mesh_checkbox_off", "mesh_checkbox_on", 10, 30), # Macro operator
(ui_create_checkbox, "$scrollable_style_2_checkbox", "mesh_checkbox_off", "mesh_checkbox_on", 10, 10), # Macro operator
(ui_create_label, reg1, "@left`align", 30, 170, 0, ":element_scale"), # Macro operator
(ui_create_label, reg1, "@right`align", 30, 150, 0, ":element_scale"), # Macro operator
(ui_create_label, reg1, "@center`justify", 30, 130, 0, ":element_scale"), # Macro operator
(ui_create_label, reg1, "@double`space", 30, 110, 0, ":element_scale"), # Macro operator
(ui_create_label, reg1, "@vertical`align`center", 30, 90, 0, ":element_scale"), # Macro operator
(ui_create_label, reg1, "@scrollable", 30, 70, 0, ":element_scale"), # Macro operator	
(ui_create_label, reg1, "@single`line", 30, 50, 0, ":element_scale"), # Macro operator
(ui_create_label, reg1, "@with`outline", 30, 30, 0, ":element_scale"), # Macro operator
(ui_create_label, reg1, "@scrollable`style`2", 30, 10, 0, ":element_scale"), # Macro operator
(set_container_overlay, "$panel"),
(ui_create_game_button, "$display_button", "@Display Off", 430, 100, 120, 30), # Macro operator
(ui_create_game_button, "$grid_button", "@Grid", 430, 70, 120, 30), # Macro operator
(ui_create_label, reg1, "@{!}Mouse`pos", 170, 10, 0, ":element_scale"), # Macro operator
(ui_create_label, "$label_mouse_xy", "@{!} ", 250, 10, tf_center_justify, ":element_scale"), # Macro operator
(set_container_overlay, -1),

(ui_create_mesh, "$log_background", "mesh_white_plane", 700, 0, 14750, 10000), # 15000 Macro operator
(overlay_set_additional_render_height, "$log_background", render_height_high_background),
(overlay_set_color, "$log_background", 0x000000),
(ui_create_container, "$log", 700, 0, 283, 200), # 290 Macro operator
]),

("move_to_top",[
(overlay_get_position, pos1, "$panel"),
(position_get_y, ":y", pos1),
(try_begin),
	(eq, ":y", -200),
	(assign, ":y", 0),
(else_try),
	(eq, ":y", 0),
	(assign, ":y", 550),
(else_try),
	(eq, ":y", 550),
  	(assign, ":y", -200),
(try_end),
(position_set_y, pos1, ":y"),
(overlay_set_position, "$panel", pos1),
(position_set_x, pos1, 700),
(position_set_y, pos1, ":y"),
(overlay_set_position, "$log", pos1),
(overlay_set_position, "$log_background", pos1),
]),

("cf_number_pressed", [
(store_script_param, ":object", 1),
(store_script_param, ":value", 2),
(assign, ":fail", 1),
(try_begin),
	(eq, ":object", "$overlay_input"),
	(call_script, "script_overlay_show_data", ":value"),
	(assign, ":fail", 0),
(else_try),
	(eq, ":object", "$input_pos_x"),
	(assign, "$value_pos_x", ":value"),
	(assign, ":y", "$value_pos_y"),
	(position_set_x, pos1, ":value"),
	(position_set_y, pos1, ":y"),
	(overlay_set_position, "$selected_overlay", pos1),
	(call_script, "script_store_overlay_position", "$selected_overlay", ":value", ":y"),
	(assign, reg0, "$selected_overlay"),
	(assign, reg1, ":value"),
	(assign, reg2, ":y"),
	(str_store_string, s1, "@Set ovelay#{reg0} position ({reg1}, {reg2})"),
	(call_script, "script_update_log"),
	(assign, ":fail", 0),
(else_try),
	(eq, ":object", "$input_pos_y"),
	(assign, ":x", "$value_pos_x"),
	(assign, "$value_pos_y", ":value"),
	(position_set_x, pos1, ":x"),
	(position_set_y, pos1, ":value"),
	(overlay_set_position, "$selected_overlay", pos1),
	(call_script, "script_store_overlay_position", "$selected_overlay", ":x", ":value"),
	(assign, reg0, "$selected_overlay"),
	(assign, reg1, ":x"),
	(assign, reg2, ":value"),
	(str_store_string, s1, "@Set ovelay#{reg0} position ({reg1}, {reg2})"),
	(call_script, "script_update_log"),
	(assign, ":fail", 0),
(else_try),
	(eq, ":object", "$input_size_x"),
	(assign, ":scale_y", "$value_size_y"),
	(assign, "$value_size_x", ":value"),
	(val_max, ":scale_y", 1),
	(position_set_x, pos1, ":value"),
	(position_set_y, pos1, ":scale_y"),
	(overlay_set_size, "$selected_overlay", pos1),
	(call_script, "script_store_overlay_size_xy", "$selected_overlay", ":value", ":scale_y"),
	(assign, reg0, "$selected_overlay"),
	(assign, reg1, ":value"),
	(assign, reg2, ":scale_y"),
	(str_store_string, s1, "@Set ovelay#{reg0} size ({reg1}, {reg2})"),
	(call_script, "script_update_log"),
	(assign, ":fail", 0),
(else_try),
	(eq, ":object", "$input_size_y"),
	(assign, ":scale_x", "$value_size_x"),
	(assign, "$value_size_y", ":value"),
	(val_max, ":scale_x", 1),
	(position_set_x, pos1, ":scale_x"),
	(position_set_y, pos1, ":value"),
	(overlay_set_size, "$selected_overlay", pos1),
	(call_script, "script_store_overlay_size_xy", "$selected_overlay", ":scale_x", ":value"),
	(assign, reg0, "$selected_overlay"),
	(assign, reg1, ":scale_x"),
	(assign, reg2, ":value"),
	(str_store_string, s1, "@Set ovelay#{reg0} size ({reg1}, {reg2})"),
	(call_script, "script_update_log"),
	(assign, ":fail", 0),
(else_try),
	(eq, ":object", "$input_area_size_x"),
	(assign, ":area_size_y", "$value_area_size_y"),
	(assign, "$value_area_size_x", ":value"),
	(val_max, ":area_size_y", 1),
	(position_set_x, pos1, ":value"),
	(position_set_y, pos1, ":area_size_y"),
	(overlay_set_area_size, "$selected_overlay", pos1),
	(call_script, "script_store_overlay_size_xy", "$selected_overlay", ":value", ":area_size_y"),
	(assign, reg0, "$selected_overlay"),
	(assign, reg1, ":value"),
	(assign, reg2, ":area_size_y"),
	(str_store_string, s1, "@Set ovelay#{reg0} area`size ({reg1}, {reg2})"),
	(call_script, "script_update_log"),
	(assign, ":fail", 0),
(else_try),
	(eq, ":object", "$input_area_size_y"),
	(assign, ":area_size_x", "$value_area_size_x"),
	(assign, "$value_area_size_y", ":value"),
	(val_max, ":area_size_x", 1),
	(position_set_x, pos1, ":area_size_x"),
	(position_set_y, pos1, ":value"),
	(overlay_set_area_size, "$selected_overlay", pos1),
	(call_script, "script_store_overlay_size_xy", "$selected_overlay", ":area_size_x", ":value"),
	(assign, reg0, "$selected_overlay"),
	(assign, reg1, ":area_size_x"),
	(assign, reg2, ":value"),
	(str_store_string, s1, "@Set ovelay#{reg0} area`size ({reg1}, {reg2})"),
	(call_script, "script_update_log"),
	(assign, ":fail", 0),
(else_try),
	(eq, ":object", "$display_button"),
	(overlay_set_display, "$selected_overlay", "$display"),
	(val_add, "$display", 1), (val_mod, "$display", 2),
	(try_begin),
		(eq, "$display", 1), (overlay_set_text, "$display_button", "@{!}Display On"),
	(else_try),
		(overlay_set_text, "$display_button", "@{!}Display Off"),
	(try_end),
(try_end),
(eq, ":fail", 0),
]),

("helper_event_change",[
(store_trigger_param, ":object", 1),
(store_trigger_param, ":value", 2),
(try_begin),
	(call_script, "script_cf_number_pressed", ":object", ":value"),
(else_try),
	(eq, ":object", "$restart_button"),
	(call_script, "script_restart_presentation"),
(else_try),
	(call_script, "script_cf_alignment_change", ":object", ":value"),
(try_end),
]),

#Input: {s1}
("update_log",[
(set_container_overlay, "$log"),
(ui_create_label, "$last_log_string", s1, 10, 10, 0, 800, 0xFFFFFF), # Macro operator
(overlay_set_additional_render_height, "$last_log_string", render_height_high_element),
(store_add, ":start", "$log", 1), #background_mesh + 1
(assign, ":log_y", 10),
(position_set_x, pos1, 10),
(try_for_range_backwards, ":overlay_no", ":start", "$last_log_string"),
	(val_add, ":log_y", 14),
	(position_set_y, pos1, ":log_y"),
	(overlay_set_position, ":overlay_no", pos1),
(try_end),
(set_container_overlay, -1),
]),

#Input: <overlay>, <x>, <y>
("store_overlay_position", [
(store_script_param, ":overlay", 1),	
(store_script_param, ":x", 2),
(store_script_param, ":y", 3),
(assign, ":end", 1),
(assign, ":slot", 1),
(try_for_range, ":unused", 0, ":end"),
	(gt, ":end", 100000), #prevent soft lock
(else_try),
	(troop_slot_eq, "trp_overlay_storage", 0, ":slot"), #reached end of storage - add new overlay
	(call_script, "script_store_overlay_data", ":overlay", "str_unknown", ":x", ":y", 0, 0, 0, 0, 0, 0, 0),
(else_try),
	(troop_get_slot, ":data_length", "trp_overlay_storage", ":slot"),
	(troop_get_slot, ":compared_overlay", "trp_overlay_storage", l.slot + 1),
	(eq, ":compared_overlay", ":overlay"),
	(val_add, ":slot", 3),
	(troop_set_slot, "trp_overlay_storage", l.slot, ":x"), (val_add, ":slot", 1),
	(troop_set_slot, "trp_overlay_storage", l.slot, ":y"),
(else_try),
	(val_add, ":slot", ":data_length"),
	(val_add, ":end", 1), #repeat
(try_end),
]),

#Input: <overlay>, <scale_x>, <scale_y>
("store_overlay_size_xy", [
(store_script_param, ":overlay", 1),	
(store_script_param, ":size_x", 2),
(store_script_param, ":size_y", 3),
(assign, ":end", 1),
(assign, ":slot", 1),
(try_for_range, ":unused", 0, ":end"),
	(gt, ":end", 100000), #prevent soft lock
(else_try),
	(troop_slot_eq, "trp_overlay_storage", 0, ":slot"), #reached end of storage - add new overlay
	(call_script, "script_store_overlay_data", ":overlay", "str_unknown", 0, 0, ":size_x", ":size_y", 0, 0, 0, 0, 0),
(else_try),
	(troop_get_slot, ":data_length", "trp_overlay_storage", ":slot"),
	(troop_get_slot, ":compared_overlay", "trp_overlay_storage", l.slot + 1),
	(eq, ":compared_overlay", ":overlay"),
	(val_add, ":slot", 5),
	(troop_set_slot, "trp_overlay_storage", l.slot, ":size_x"), (val_add, ":slot", 1),
	(troop_set_slot, "trp_overlay_storage", l.slot, ":size_y"),
(else_try),
	(val_add, ":slot", ":data_length"),
	(val_add, ":end", 1), #repeat
(try_end),
]),

#Input: <mask>, <bit>
#Output: reg0 - checked, reg1 - log2 where bit = power(2, log2)
("flag_checked", [
(store_script_param, ":mask", 1),
(store_script_param, ":bit", 2),
(assign, ":end", 1),
(try_for_range, ":unused", 0, ":end"),
	(gt, ":end", 10000),
(else_try),
	(eq, ":bit", 1),
	(store_and, ":checked", ":bit", ":mask"),
(else_try),
	(val_rshift, ":bit", 1),
	(val_rshift, ":mask", 1),
	(val_add, ":end", 1),
(try_end),
(assign, reg0, ":checked"),
(store_sub, reg1, ":end", 1), #log2
]),

("overlay_show_data", [
(store_script_param, ":overlay", 1),
(assign, ":end", 1),
(assign, ":slot", 1),
(try_for_range, ":unused", 0, ":end"),
	(gt, ":end", 100000), #prevent soft lock
(else_try),
	(troop_slot_eq, "trp_overlay_storage", 0, ":slot"), #reached end of storage
	(overlay_set_val, "$input_pos_x", 0),
	(overlay_set_val, "$input_pos_y", 0),
	(assign, "$value_pos_x", 0),
	(assign, "$value_pos_y", 0),
	(overlay_set_val, "$input_size_x", 0),
	(overlay_set_val, "$input_size_y", 0),
	(assign, "$value_size_x", 0),
	(assign, "$value_size_y", 0),
(else_try),
	(troop_get_slot, ":data_length", "trp_overlay_storage", ":slot"),
	(troop_get_slot, ":compared_overlay", "trp_overlay_storage", l.slot + 1),
	(negate|eq, ":compared_overlay", ":overlay"),
	(val_add, ":slot", ":data_length"),
	(val_add, ":end", 1), #repeat
(else_try),
	(assign, "$selected_overlay", ":overlay"),
	(val_add, ":slot", 2),
	(troop_get_slot, ":string_id", "trp_overlay_storage", ":slot"),
	(overlay_set_text, "$overlay_type", ":string_id"),
	(str_store_string, s1, ":string_id"),
	(assign, reg0, ":overlay"),
	(str_store_string, s1, "@Selected overlay {s1}#{reg0}"),
	(call_script, "script_update_log"),
	(val_add, ":slot", 1), (troop_get_slot, ":x", "trp_overlay_storage", ":slot"),
	(val_add, ":slot", 1), (troop_get_slot, ":y", "trp_overlay_storage", ":slot"),
	(overlay_set_val, "$input_pos_x", ":x"),
	(overlay_set_val, "$input_pos_y", ":y"),
	(assign, "$value_pos_x", ":x"),
	(assign, "$value_pos_y", ":y"),
	(val_add, ":slot", 1), (troop_get_slot, ":size_x", "trp_overlay_storage", l.slot),
	(val_add, ":slot", 1), (troop_get_slot, ":size_y", "trp_overlay_storage", l.slot),
	(overlay_set_val, "$input_size_x", ":size_x"), (assign, "$value_size_x", ":size_x"),
	(overlay_set_val, "$input_size_y", ":size_y"), (assign, "$value_size_y", ":size_y"),
	(try_begin),
		(this_or_next|eq, ":string_id", "str_ui_create_label"),
		(this_or_next|eq, ":string_id", "str_ui_create_checkbox"),
		(this_or_next|eq, ":string_id", "str_ui_create_container"),
		(this_or_next|eq, ":string_id", "str_unknown"),
		(this_or_next|eq, ":string_id", "str_ui_create_mesh"),
		(this_or_next|eq, ":string_id", "str_ui_create_image_button"),
		(this_or_next|eq, ":string_id", "str_ui_create_image_button_with_tableau_material"),
		(this_or_next|eq, ":string_id", "str_ui_create_combo_label"),
		(this_or_next|eq, ":string_id", "str_ui_create_combobox"),
		(this_or_next|eq, ":string_id", "str_ui_create_listbox"),
		(this_or_next|eq, ":string_id", "str_ui_create_item"),
		(this_or_next|eq, ":string_id", "str_ui_create_horslider"),
		(eq, ":string_id", "str_ui_create_mesh_with_tableau_material"),
		(overlay_set_text, "$label_size_x", "@scale X"),
		(overlay_set_text, "$label_size_y", "@scale Y"),
	(else_try),
		(eq, ":string_id", "str_ui_create_game_button"),
		(overlay_set_text, "$label_size_x", "@size X"),
		(overlay_set_text, "$label_size_y", "@size Y"),
	(else_try),
		(eq, ":string_id", "str_ui_create_textbox"),
		(overlay_set_text, "$label_size_x", "@size X"),
		(overlay_set_text, "$label_size_y", "@scale Y"),
	(try_end),
	(val_add, ":slot", 1), (troop_get_slot, ":area_size_x", "trp_overlay_storage", l.slot),
	(val_add, ":slot", 1), (troop_get_slot, ":area_size_y", "trp_overlay_storage", l.slot),
	(overlay_set_val, "$input_area_size_x", ":area_size_x"), (assign, "$value_area_size_x", ":area_size_x"),
	(overlay_set_val, "$input_area_size_y", ":area_size_y"), (assign, "$value_area_size_y", ":area_size_y"),
	(val_add, ":slot", 1), #(troop_get_slot, ":color", "trp_overlay_storage", l.slot),
	(val_add, ":slot", 1), (troop_get_slot, ":alignment", "trp_overlay_storage", l.slot),
	(call_script, "script_flag_checked", ":alignment", tf_left_align), (assign, ":checked", reg0), (overlay_set_val, "$left_align_checkbox", ":checked"),
	(call_script, "script_flag_checked", ":alignment", tf_right_align), (assign, ":checked", reg0), (overlay_set_val, "$right_align_checkbox", ":checked"),
	(call_script, "script_flag_checked", ":alignment", tf_center_justify), (assign, ":checked", reg0), (overlay_set_val, "$center_justify_checkbox", ":checked"),
	(call_script, "script_flag_checked", ":alignment", tf_double_space), (assign, ":checked", reg0), (overlay_set_val, "$double_space_checkbox", ":checked"),
	(call_script, "script_flag_checked", ":alignment", tf_vertical_align_center), (assign, ":checked", reg0), (overlay_set_val, "$vertical_align_center_checkbox", ":checked"),
	(call_script, "script_flag_checked", ":alignment", tf_scrollable), (assign, ":checked", reg0), (overlay_set_val, "$scrollable_checkbox", ":checked"),
	(call_script, "script_flag_checked", ":alignment", tf_single_line), (assign, ":checked", reg0), (overlay_set_val, "$single_line_checkbox", ":checked"),
	(call_script, "script_flag_checked", ":alignment", tf_with_outline), (assign, ":checked", reg0), (overlay_set_val, "$with_outline_checkbox", ":checked"),
	(call_script, "script_flag_checked", ":alignment", tf_scrollable_style_2), (assign, ":checked", reg0), (overlay_set_val, "$scrollable_style_2_checkbox", ":checked"),
	(val_add, ":slot", 1), #(troop_get_slot, ":rotation", "trp_overlay_storage", l.slot),
(try_end),
]),

("restart_presentation", [
(assign, ":end", "prsnt_battle"), # place holder for the last presentation (adjusted automatically)
(try_for_range, ":presentation_no", 0, ":end"),
  (is_presentation_active, ":presentation_no"),
  (presentation_set_duration, 0),
  (start_presentation, ":presentation_no"),
  (assign, ":end", 0),
(try_end),
]),

("cf_alignment_change", [
(store_script_param, ":object", 1),
(store_script_param, ":value", 2),
(assign, ":fail", 1),
(try_begin),
	(is_between, ":object", "$left_align_checkbox", g.scrollable_style_2_checkbox + 1),
	(str_store_string, s1, "@Alignment not changeable"),
	(call_script, "script_update_log"),
	(store_add, ":result", ":value", 1), (val_mod, ":result", 2),
	(overlay_set_val, ":object", ":result"),
	(assign, ":fail", 0),
(try_end),
(eq, ":fail", 0),
]),

("show_mouse_positions",[
(set_fixed_point_multiplier, 1000),
(mouse_get_position, pos10),
(position_get_x, reg43, pos10),
(position_get_y, reg44, pos10),
(overlay_set_text, "$label_mouse_xy", "@{!}({reg43}, {reg44})"),
]),

("enter_leave", [
(store_trigger_param, reg0, 1), #overlay_ID
(store_trigger_param, ":value", 2),
(try_begin),
	(eq, ":value", 0),
	(lt, reg0, "$num_overlays"),
	(str_store_string, s1, "@{!}Mouse entered #{reg0}"),
	(call_script, "script_update_log"),
(try_end),
]),
]

def preprocess_entities(glob):
	# Integrate helper to all presentations
	if compiler_store_overlay_data:
		for presentation_no in glob['presentations']:
			
			for cur_trigger in presentation_no[3]:
				if cur_trigger[0] == ti_on_presentation_load: break
			else: presentation_no[3].append((ti_on_presentation_load,[]))
			for cur_trigger in presentation_no[3]:
				if cur_trigger[0] == ti_on_presentation_event_state_change: break
			else: presentation_no[3].append((ti_on_presentation_event_state_change,[]))
			for cur_trigger in presentation_no[3]:
				if cur_trigger[0] == ti_on_presentation_run: break
			else: presentation_no[3].append((ti_on_presentation_run,[]))
			for cur_trigger in presentation_no[3]:
				if cur_trigger[0] == ti_on_presentation_mouse_enter_leave: break
			else: presentation_no[3].append((ti_on_presentation_mouse_enter_leave,[]))

			# code fail fix
			for cur_trigger in presentation_no[3]:
				code_block = cur_trigger[1]
				total_commands = len(code_block)
				current_depth = 0
				can_fail = False
				for index in range(len(code_block)):
					operation = code_block[index]
					is_assign = False
					if type(operation) is int:
						command = [operation, 0]
					elif type(operation) is tuple:
						command = [operation[0], len(operation) - 1]
						command.extend(operation[1:])
					else: continue
					if type(command[0]) is CUSTOM_OPERATION:
						continue
					# Monitor execution depth
					if command[0] in depth_operations:
						current_depth += 1
					elif command[0] == try_end:
						current_depth -= 1
					# Identify can_fail scripts
					can_fail |= (current_depth < 1) and (((command[0] & 0x3FFFFFFF) in can_fail_operations) or ((command[0] == call_script) and isinstance(command[2], VARIABLE) and (command[2].module == WRECK.script) and (command[2].name[0:3] == 'cf_')))
				if can_fail:
					code_block.insert(0, (try_begin))
					code_block.append((try_end))

			for cur_trigger in presentation_no[3]:
				if cur_trigger[0] == ti_on_presentation_load:
					cur_trigger[1].insert(0, (call_script, "script_clear_storage", "trp_overlay_storage"))
					cur_trigger[1].append((call_script, "script_create_presentation_dev_panel"))
				if cur_trigger[0] == ti_on_presentation_event_state_change: cur_trigger[1].append((call_script, "script_helper_event_change"))
				if cur_trigger[0] == ti_on_presentation_run:
					cur_trigger[1].extend([
						(try_begin),
							(key_clicked, key_f),
							(call_script, "script_move_to_top"),
						(try_end),
						(call_script, "script_show_mouse_positions"),
					])
				if cur_trigger[0] == ti_on_presentation_mouse_enter_leave: cur_trigger[1].append((call_script, "script_enter_leave"))

		for script_no in glob['scripts']:
			if script_no[0] == 'restart_presentation':
				script_no[1] = [(assign, ":end", len(glob['presentations']))] + script_no[1][1:]
				break