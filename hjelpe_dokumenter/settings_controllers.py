import hjelpe_dokumenter.init_menus as init_menus
import hjelpe_dokumenter.init_classes as init_classes

##### settings controllere####
def main_menu_pressed(app):
    #controllerer settings. når du trykker enter går den gjennom her
    import sys
    if app.menu_selector == 0:
        if app.debug == True:
            init_menus.map_init(app)
        else:
            init_menus.init_difficulty_menu(app)
        
    #velger map    
    elif app.menu_selector == 1:
        init_menus.settings_init(app)
    #stjålet fra https://stackoverflow.com/questions/73663/how-do-i-terminate-a-script
    if app.menu_selector == 2:
        sys.exit()

    app.menu_selector = 0
    app.menu_selector_x = 0

def settings_menu_pressed(app):
    #kontroller for settings menu når du velger et valg
    if app.menu_selector == 0 and app.menu_selector_x == 0 and app.input_delay_menu == 0:
        init_menus.rebind_init(app)
    elif app.menu_selector == 1 and app.menu_selector_x == 0 and app.input_delay_menu == 0:
        init_menus.map_init(app)
    elif app.menu_selector == 0 and app.menu_selector_x == 1 and app.input_delay_menu == 0:
        init_menus.init_credits(app)
    elif app.menu_selector == 1 and app.menu_selector_x == 1 and app.input_delay_menu == 0:
        init_menus.init_menu(app)
    app.menu_selector = 0
    app.menu_selector_x = 0

def difficulty_menu_pressed(app):
    #difficulty menu_pressed
    if app.menu_selector == 0 and app.input_delay_menu == 0:
        init_classes.init_boss_1(app)
        init_classes.init_playable_character_one(app)
        init_menus.init_baby(app)
    if app.menu_selector == 1 and app.input_delay_menu == 0 and app.profile["unlocks"]["difficulty_baby"] == True:
        init_classes.init_boss_1(app)
        init_classes.init_playable_character_one(app)
        init_menus.init_easy(app)
    if app.menu_selector == 2 and app.input_delay_menu == 0 and app.profile["unlocks"]["difficulty_easy"] == True:
        init_classes.init_boss_1(app)
        init_classes.init_playable_character_one(app)
        init_menus.init_hard(app)

    app.input_delay_menu += 1
    app.menu_selector = 0

def map_button_pressed(app):
    #velger hvilken map button du trykker på
    if app.menu_selector == 0 and app.menu_selector_x == 0 and app.profile["unlocks"]["defeated_boss_one"] == True:
        init_classes.init_boss_1(app)
        init_classes.init_playable_character_one(app)
    if app.menu_selector == 1 and app.menu_selector_x == 0 and app.profile["unlocks"]["defeated_boss_two"] == True:
        init_classes.init_boss_2(app)
        init_classes.init_playable_character_one(app)
    if app.menu_selector == 0 and app.menu_selector_x == 1 and app.profile["unlocks"]["defeated_boss_three"] == True:
        init_classes.init_boss_3(app)
        init_classes.init_playable_character_one(app)
    if app.menu_selector == 1 and app.menu_selector_x == 1 and app.profile["unlocks"]["defeated_boss_final"] == True:
        init_classes.init_final_boss(app)
        init_classes.init_playable_character_one(app)

    app.play_from_map = True
    app.menu_selector = 0
    app.menu_selector_x = 0
    app.player_lives = 1

def rebind_button_pressed(app):
    #velger hvilken knapp du skal rebinde
    if app.menu_selector == 0 and app.menu_selector_x == 0 and app.input_delay_menu == 0:
        app.game_state = "Binding_key"
        app.action_to_bind = "Up"
    elif app.menu_selector == 1 and app.menu_selector_x == 0 and app.input_delay_menu == 0:
        app.game_state = "Binding_key"
        app.action_to_bind = "Down"
    elif app.menu_selector == 2 and app.menu_selector_x == 0 and app.input_delay_menu == 0:
        app.game_state = "Binding_key"
        app.action_to_bind = "Left"
    elif app.menu_selector == 3 and app.menu_selector_x == 0 and app.input_delay_menu == 0:
        app.game_state = "Binding_key"
        app.action_to_bind = "Right"
    elif app.menu_selector == 0 and app.menu_selector_x == 1 and app.input_delay_menu == 0:
        app.game_state = "Binding_key"
        app.action_to_bind = "Dodge"
    elif app.menu_selector == 1 and app.menu_selector_x == 1 and app.input_delay_menu == 0:
        app.game_state = "Binding_key"
        app.action_to_bind = "Dash"
    elif app.menu_selector == 2 and app.menu_selector_x == 1 and app.input_delay_menu == 0:
        app.game_state = "Binding_key"
        app.action_to_bind = "Attack"
    elif app.menu_selector == 3 and app.menu_selector_x == 1 and app.input_delay_menu == 0:
        init_menus.settings_init(app)
        app.menu_selector = 0
        app.menu_selector_x = 0
    app.bind_timer = 100
    app.listening_to_input = True
