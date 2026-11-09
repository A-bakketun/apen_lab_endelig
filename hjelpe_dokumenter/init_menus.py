import hjelpe_dokumenter.uib_inf100_music as music

##### menyer init#####
def map_init(app):
    #initer map eller practise da som det kalles
    music.stop_all_sounds()
    app.game_state = "Map"
    app.map_song.play()

def settings_init(app):
    #initer settings
    app.menu_selector = 0
    app.menu_selector_x = 0
    app.game_state = "Settings"

def rebind_init(app):
    #initer rebind state
    app.menu_selector = 0
    app.menu_selector_x = 0
    app.game_state = "Rebind"

def init_menu(app):
    #initer menu
    music.stop_all_sounds()
    app.game_state = "Menu"
    app.main_menu_song.play()

def init_menu_from_settings(app):
    #initer menu fra settings på grunn av samme sang
    app.game_state = "Menu"

def init_difficulty_menu(app):
    #initer difficulty velgeren
    music.stop_all_sounds()
    app.game_state = "Difficulty"
    app.map_song.play()

def init_credits(app):
    #initet credits
    music.stop_all_sounds()
    app.credits_cords_x = 450
    app.credits_cords_y = 1300
    app.game_state = "Credits"
    app.credits_song.play()
    
def victory_screen_init(app):
    #victory skjerm init
    music.stop_all_sounds()
    app.victory_animation_frames = 0
    app.animate_victory_screen = 0
    if app.diff == "Baby":
        app.profile["unlocks"]["difficulty_baby"] = True
    elif app.diff == "Easy":
        app.profile["unlocks"]["difficulty_easy"] = True
    elif app.diff == "Hard":
        app.profile["unlocks"]["difficulty_hard"] = True
    app.game_state = "Victory"
    app.victory_song.play()

def init_baby(app):
    #init difficulty baby 
    import hjelpe_dokumenter.helper_functions as helpers
    app.player_lives = 3
    app.play_from_map = False
    app.diff = "Baby"
    helpers.victory_text(app)
def init_easy(app):
    #initer difficuly easy
    import hjelpe_dokumenter.helper_functions as helpers
    app.player_lives = 1
    app.play_from_map = False
    app.diff = "Easy"
    helpers.victory_text(app)
def init_hard(app):
    #initer difficulty hard
    import hjelpe_dokumenter.helper_functions as helpers
    app.player_lives = 1
    app.player_health = 1
    app.play_from_map = False
    app.diff = "Hard"
    helpers.victory_text(app)

def killed_boss_init(app):
    #når boss blir drept, sjekker her.
    if app.boss_fight == "One":
        app.game_state = "Boss_One_Down"
        if app.profile["unlocks"]["defeated_boss_one"] == False:
            app.profile["unlocks"]["defeated_boss_one"] = True
    elif app.boss_fight == "Two":
        app.game_state = "Boss_Two_Down"
        if app.profile["unlocks"]["defeated_boss_two"] == False:
            app.profile["unlocks"]["defeated_boss_two"] = True
    elif app.boss_fight == "Three":
        app.game_state = "Boss_Three_Down"
        if app.profile["unlocks"]["defeated_boss_three"] == False:
            app.profile["unlocks"]["defeated_boss_three"] = True
    elif app.boss_fight == "Final":
        victory_screen_init(app)
        if app.profile["unlocks"]["defeated_boss_final"] == False:
            app.profile["unlocks"]["defeated_boss_final"] = True

def kill_enemy(app):
    #dreper enemy og tar deg tilbake til map om du spiller fra map
    #eller til neste enemy
    if app.play_from_map == False:
        killed_boss_init(app)
    else:
        map_init(app)

def next_boss(app):
    import hjelpe_dokumenter.init_classes as init_classes
    #initer classes når du går til neste bossen
    #eller victory screen hvis du vinner
    if app.boss_fight == "One":
        init_classes.soft_init_player(app)
        init_classes.init_boss_2(app)
    elif app.boss_fight == "Two":
        init_classes.soft_init_player(app)
        init_classes.init_boss_3(app)
    elif app.boss_fight == "Three":
        init_classes.soft_init_player(app)
        init_classes.init_final_boss(app)

