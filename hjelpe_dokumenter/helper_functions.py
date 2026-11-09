
def rebind_keys(app):
    import hjelpe_dokumenter.buttons as buttons
    if app.action_to_bind == "Up":
        app.bind_up = app.new_bound
    elif app.action_to_bind == "Down":
        app.bind_down = app.new_bound
    elif app.action_to_bind == "Left":
        app.bind_left = app.new_bound
    elif app.action_to_bind == "Right":
        app.bind_right = app.new_bound
    elif app.action_to_bind == "Attack":
        app.bind_attack = app.new_bound
    elif app.action_to_bind == "Dodge":
        app.bind_dodge = app.new_bound  
    elif app.action_to_bind == "Dash":
        app.bind_dash = app.new_bound     

    buttons.rebind_buttons(app)
    app.game_state = "Rebind"
    app.listening_to_input = False
    app.new_bound = 0

def victory_text(app):
    #lager en tilfeldig seiers tekst
    import random
    r = random.randrange(3)
    if app.diff == "Baby":
        if r == 0:
            app.victory_text ="How was the warmup?"
        if r == 1:
            app.victory_text ="I knew you would get it!\n .... eventually"
        if r == 2:
            app.victory_text ="You did your best!"
    if app.diff == "Easy":
        if r == 0:
            app.victory_text ="You can achieve great things"
        if r == 1:
            app.victory_text ="This is when the game begins!"
        if r == 2:
            app.victory_text ="You did your best!"
    if app.diff == "Hard":
        app.victory_text = "You won....\n But at what cost?"

def system_check(app):
    #rebinder enter om brukeren har mac os
    if get_system(app) == True:
        pass
    else:
        app.profile["actions"]["action_select"] = "Return"

def get_system(app):
    #får system og returnerer true om det er mac
    #https://stackoverflow.com/questions/32991069/python-checking-for-json-files-and-creating-one-if-needed 
    import sys
    temp = sys.platform
    if temp == "darwin":
        return False
    else:
        return True

def input_delay_menu(app):
    #for å passe på at man ikke dobbeltrykker i menyer
    #kjører hver gang enter(retur) slippes
    if app.input_delay_menu > 0:
        app.input_delay_menu -= 1

def sound_handler(app):
    #importer musikk
    import hjelpe_dokumenter.uib_inf100_music as music

    #menyer og lignende
    app.main_menu_song = music.load_looping_sound("Story_of_Alfred/Music_assets/Main_theme.mp3")
    app.map_song = music.load_looping_sound("Story_of_Alfred/Music_assets/map_song.mp3")
    app.death_song = music.load_looping_sound("Story_of_Alfred/Music_assets/death_song.mp3")
    app.victory_song = music.load_looping_sound("Story_of_Alfred/Music_assets/Victory_theme.mp3")
    app.credits_song = music.load_looping_sound("Story_of_Alfred/Music_assets/credits.mp3 ")
    #bosser og sånt
    app.music_boss_one = music.load_looping_sound("Story_of_Alfred/Music_assets/Boss_one_song.mp3")
    app.music_boss_two = music.load_looping_sound("Story_of_Alfred/Music_assets/boss_2.mp3")     
    app.music_boss_three = music.load_looping_sound("Story_of_Alfred/Music_assets/boss_3.mp3")
    app.final_boss_song = music.load_looping_sound("Story_of_Alfred/Music_assets/Final_boss.mp3")
    
def import_keybinds(app):
    #importerer keybinds
    app.bind_up = app.profile["actions"]["action_up"]
    app.bind_down = app.profile["actions"]["action_down"]
    app.bind_left = app.profile["actions"]["action_left"]
    app.bind_right = app.profile["actions"]["action_right"]
    app.bind_attack = app.profile["actions"]["action_attack"]
    app.bind_dodge = app.profile["actions"]["action_dodge"]
    app.bind_dash = app.profile["actions"]["action_dash"]
    app.enter_bind  = app.profile["actions"]["action_select"]

def import_unlocks(app):
    #importer unlocks
    app.beaten_baby = app.profile["unlocks"]["difficulty_baby"]
    app.beaten_easy = app.profile["unlocks"]["difficulty_easy"]
    app.beaten_hard = app.profile["unlocks"]["difficulty_hard"]
    app.beaten_boss_one = app.profile["unlocks"]["defeated_boss_one"]
    app.beaten_boss_two = app.profile["unlocks"]["defeated_boss_two"]
    app.beaten_boss_three = app.profile["unlocks"]["defeated_boss_three"]
    app.beaten_boss_final = app.profile["unlocks"]["defeated_boss_final"]

def create_json():
    #lager en blank profil om det trengs
    profile = {
            "actions": {
            "action_up":"w",
            "action_down":"s",
            "action_left":"a",
            "action_right":"d",
            "action_attack":"j",
            "action_dash":"h",
            "action_dodge":"g",
            "action_select":"Enter"
    },
            "unlocks": {
            "difficulty_baby":False,
            "difficulty_easy":False,
            "difficulty_hard":False,
            "defeated_boss_one":False,
            "defeated_boss_two":False,
            "defeated_boss_three":False,
            "defeated_boss_final":False,
            
    }

    }
    return profile

def save_json(app):
    #oppdaterer app.profile før den skrives til minnet
    #lagrer tastetrykk
    app.profile["actions"]["action_up"] = app.bind_up
    app.profile["actions"]["action_down"] = app.bind_down
    app.profile["actions"]["action_right"] = app.bind_right
    app.profile["actions"]["action_left"] = app.bind_left
    app.profile["actions"]["action_attack"] = app.bind_attack
    app.profile["actions"]["action_dash"] = app.bind_dash
    app.profile["actions"]["action_dodge"] = app.bind_dodge
    #lagrer unlocks
    app.profile["unlocks"]["difficulty_baby"] = app.beaten_baby
    app.profile["unlocks"]["difficulty_easy"] = app.beaten_easy
    app.profile["unlocks"]["difficulty_hard"] = app.beaten_hard
    app.profile["unlocks"]["defeated_boss_one"] = app.beaten_boss_one
    app.profile["unlocks"]["defeated_boss_two"] = app.beaten_boss_two
    app.profile["unlocks"]["defeated_boss_three"] = app.beaten_boss_three
    app.profile["unlocks"]["defeated_boss_final"] = app.beaten_boss_final