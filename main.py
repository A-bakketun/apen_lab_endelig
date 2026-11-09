##moduler##
from uib_inf100_graphics.event_app import run_app
from uib_inf100_graphics.helpers import load_image, scaled_image
from PIL import Image
from pathlib import Path
import json
import os

#uib_inf100_music
import hjelpe_dokumenter.uib_inf100_music as music

##egne programmer
import hjelpe_dokumenter.image_importer as image_importer
import hjelpe_dokumenter.draw_functions as draw_functions 
import hjelpe_dokumenter.init_classes as init_classes 
import hjelpe_dokumenter.buttons as buttons
import hjelpe_dokumenter.timere as timere
import hjelpe_dokumenter.attacks as attacks
import hjelpe_dokumenter.helper_functions as helpers
import hjelpe_dokumenter.player as player
import hjelpe_dokumenter.init_menus as init_menus
import hjelpe_dokumenter.settings_controllers as settings_controllers

####################################################################################################################
#            Dette er mitt første oredentlige spill. (snake telles liksom ikke siden det var en del håndholding)
#            Jeg har ikke brukt noen andre kilder enn det som er tilgjengelig på inf100 nettsiden, med unntak av for OS og JSON importering
#            Alle assets er laget av meg.
#            Jeg vil rette en stor takk til pixilart.com, og beepbox.co som har vært mine verktøy for bilder og musikk respektivt
#            inspirasjonen til hovedkarakteren er snusmumrikken (ikke noe å legge skjul på der skylder på halloween)
#            ellers er det bare ting som har kommet til meg (i mine mareritt mest sannsynlig)
#            Hadde jeg hatt mer tid, hadde jeg gjort mer :) men livet kom litt i veien så dette er alt jeg har rekket å gjøre
#            
#               og takk til Are 
#                   og en kompis av meg, Truls, som hjalp med innspill for visuell tydelighet på noen angrep
#
#            Det er et vanskelig spill, så ikke bli lei deg hvis du ikke får det til
#            skill issue heter det :P      
#  
#            OS check og JSON check stjal jeg fra Snaken min
#            sys.exit() stjal jeg også fra nettet
#            hvor jeg stjal det fra disse kildene:
#
##########kilder:
#https://docs.python.org/3/library/sys.html#sys.platform (docs for å finne ut hvordan jeg kan finne ut av OS fordi noen folk har mac)
#https://stackoverflow.com/questions/32991069/python-checking-for-json-files-and-creating-one-if-needed (Stackoverflow for å finne ut av hvordan sjekke om en JSON fil finnes)
#https://stackoverflow.com/questions/73663/how-do-i-terminate-a-script
#funksjoner det gjelder ( check_json(app)) og system_check(app) og i settings controllere under main_menu_button_pressed(app)
 


def app_started(app):
    #kjører når programmet åpner seg
    #timer 
    app.timer_delay = 50
    #debug, mest for tegning og kort tilgang til maps
    app.debug = False

    #menu initilisering
    app.game_state = "Menu"
    app.input_delay_menu = 0
    app.menu_selector = 0
    app.menu_selector_x = 0
    app.enter_bind = "Enter"
    app.new_bound = 0
    app.listening_to_input = 0
    
    #sjekker om det er en profil som finnes
    #stjålet fra
    #https://stackoverflow.com/questions/32991069/python-checking-for-json-files-and-creating-one-if-needed 
    if check_json(app,"Story_of_Alfred/profile.json"):
        pass
    #om den ikke finnes lages en blank profil
    else:
        create_blank_profile(app)
    #importerer profilen
    import_profile(app)
    #har brukeren Enter som bindet, dobbeltsjekker jeg om de er på mac
    #system check er sitert funksjon
    if app.profile["actions"]["action_select"] == "Enter":
        helpers.system_check(app)
    #image_handler and sound handler
    image_importer.image_handler(app)
    helpers.sound_handler(app)
    #lager knappenebuttons
    buttons.button_creator(app)
    #colors
    draw_functions.define_colors(app)
    #spiller main menu sangen :#)
    app.main_menu_song.play()
    import_credits(app)

def check_json(app, file_name):
    #sjekker om brukeren har en JSON
    return os.path.exists(file_name)

def import_profile(app):
    #importerer profilen og binder kontrolls utifra det
    content = Path("Story_of_Alfred/profile.json").read_text(encoding="utf-8")
    app.profile = json.loads(content)
    helpers.import_keybinds(app)
    helpers.import_unlocks(app)

def create_blank_profile(app):
    #lager om blank profil om det trengs
    profile = helpers.create_json()
    content = json.dumps(profile)
    Path("Story_of_Alfred/profile.json").write_text(content, encoding="utf-8")

def import_credits(app):
    content = Path("Story_of_Alfred/credits.txt").read_text(encoding="utf-8")
    app.credits = content

def timer_fired(app):
    #timer fired, fyrer basert på state
    if app.game_state == "Running":
        player.timer_player_char_one(app)
        if app.boss_fight == "One":
            timere.boss_one_timer(app)
        elif app.boss_fight == "Two":
            timere.boss_two_timer(app)
        elif app.boss_fight == "Three":
            timere.boss_three_timer(app)
        elif app.boss_fight == "Final":
            if app.boss_stage == "One":
                timere.boss_final_timer_one(app)
            #her er det to stages, så har delt den i to
            elif app.boss_stage == "Two":
                timere.boss_final_timer_two(app)
    #animerer victory screen
    elif app.game_state == "Victory":
        timere.victory_screen_timer(app)
    #timer for rebinding av taster
    elif app.game_state == "Binding_key":
        timere.rebind_timer(app)
    elif app.game_state == "Credits":
        if app.credits_cords_y > 400:
            app.credits_cords_y -= 5

### keys ###
def key_released(app, event):
    #input delay når du slipper opp enten select knapp eller escape
    if (event.key == app.enter_bind):
        helpers.input_delay_menu(app)
    if (event.key == "Escape"):
        helpers.input_delay_menu(app)
    #key released når running for å stoppe movement
    if app.game_state == "Running":
        if (event.key == app.bind_left) and app.player_direction == "West":
            app.player_moving = False
        if (event.key == app.bind_right) and app.player_direction == "East":
            app.player_moving = False

def key_pressed(app, event):
    #lytter etter inputs når man skal rebinde
    if app.listening_to_input == True and app.input_delay_menu == 0:
        #avbrutt binding (kan ikke binde escape)
        if (event.key == "Escape"):
            init_menus.rebind_init(app)
            app.listening_to_input = False
            app.new_bound = 0
        #kan ikke være enter key 
        elif (event.key == app.enter_bind):
            pass
        #velger ny knapp
        else:
            app.new_bound = (event.key)
    #bindings i selve run
    if app.game_state == "Running":
        #hvis running og du trykker escape går du tilbake til hoved menyen
        if (event.key == "Escape") and app.input_delay_menu == 0:
            init_menus.init_menu(app)
        #dash
        if (event.key == app.bind_dash) and app.dash_timer == 0:
            player.player_dash(app)
        #dodge
        if (event.key == app.bind_dodge) and app.dodge_timer == 0:
            player.player_dodge(app)
        #angrep
        elif (event.key == app.bind_attack) and app.basic_attack_cooldown == 0:
            player.basic_attack(app)
        #bevege spilleren
        elif (event.key == app.bind_left) and app.input_delay == 0 and app.attack_stops_movement == 0:
            app.player_direction = "West"
            app.player_moving = 1
        elif (event.key == app.bind_right) and app.input_delay == 0 and app.attack_stops_movement == 0:
            app.player_direction = "East"
            app.player_moving = 1 

    #taster for hoved menyen
    elif app.game_state == "Menu":
        #velger i menyen
        if (event.key == app.enter_bind):
            settings_controllers.main_menu_pressed(app)
            app.input_delay_menu = 1
        elif (event.key == app.bind_up):
            if app.menu_selector > 0:
                app.menu_selector -= 1
        elif (event.key == app.bind_down):
            if app.menu_selector < 2:
                app.menu_selector += 1
    #taster i instillinger
    elif app.game_state == "Settings":
        if (event.key == app.enter_bind):
            #knapp trykket i instillinger
            settings_controllers.settings_menu_pressed(app)
            app.input_delay_menu = 1   
        elif (event.key == "Escape") and app.input_delay_menu == 0:
            #avbrutt instillinger
            init_menus.init_menu_from_settings(app)
            app.input_delay_menu = 1
        #velge rute i settings
        elif (event.key == app.bind_up):
            if app.menu_selector > 0:
                app.menu_selector -= 1
        elif (event.key == app.bind_down):
            if app.menu_selector < 1:
                app.menu_selector += 1   
        elif (event.key == app.bind_left):
            if app.menu_selector_x > 0:
                app.menu_selector_x -= 1
        elif (event.key == app.bind_right):
            if app.menu_selector_x < 1:
                app.menu_selector_x += 1 
    elif app.game_state == "Sounds":
        pass
    #taster for valg av vanskelighetsgrad
    elif app.game_state == "Difficulty":
        if (event.key == app.enter_bind):
            settings_controllers.difficulty_menu_pressed(app)
            app.input_delay_menu = 1
        elif (event.key == "Escape") and app.input_delay_menu == 0:
            init_menus.init_menu(app)
        elif (event.key == app.bind_left):
            if app.menu_selector > 0:
                app.menu_selector -= 1
        elif (event.key == app.bind_right):
            if app.menu_selector < 2:
                app.menu_selector += 1 
    #taster for map / practice
    elif app.game_state == "Map":
        if (event.key == app.enter_bind) and app.input_delay_menu == 0:
            settings_controllers.map_button_pressed(app)
            app.input_delay_menu = 1
        elif (event.key == "Escape") and app.input_delay_menu == 0:
            music.stop_all_sounds()
            init_menus.settings_init(app)
            app.main_menu_song.play()
        elif (event.key == app.bind_up):
            if app.menu_selector > 0:
                app.menu_selector -= 1
        elif (event.key == app.bind_down):
            if app.menu_selector < 1:
                app.menu_selector += 1
        elif (event.key == app.bind_left):
            if app.menu_selector_x == 1:
                app.menu_selector_x = 0
        elif (event.key == app.bind_right):
            if app.menu_selector_x == 0:
                app.menu_selector_x = 1
    #rebind menyen for å velge hvilken knapp du vil rebinde
    elif app.game_state == "Rebind":
        #velger knappen du trykket på
        if (event.key == app.enter_bind) and app.input_delay_menu == 0:
            settings_controllers.rebind_button_pressed(app)
        #abort
        elif (event.key == "Escape") and app.input_delay_menu == 0:
            init_menus.settings_init(app)
            app.input_delay_menu += 1
        #opp ned side på rebind velgeren
        elif (event.key == app.bind_up):
            if app.menu_selector > 0:
                app.menu_selector -= 1
        elif (event.key == app.bind_down):
            if app.menu_selector < 3:
                app.menu_selector += 1
        elif (event.key == app.bind_left):
            if app.menu_selector_x == 1:
                app.menu_selector_x = 0
        elif (event.key == app.bind_right):
            if app.menu_selector_x == 0:
                app.menu_selector_x = 1    
    #continue skjermene, venter på input 
    elif app.game_state == "Boss_One_Down":
        if (event.key == app.enter_bind) and app.play_from_map == False:
            init_menus.next_boss(app)
        elif (event.key == app.enter_bind):
            init_menus.map_init(app)
    elif app.game_state == "Boss_Two_Down" :
        if (event.key == app.enter_bind) and app.play_from_map == False:
            init_menus.next_boss(app)
        elif (event.key == app.enter_bind):
            init_menus.map_init(app)
    elif app.game_state == "Boss_Three_Down":
        if (event.key == app.enter_bind) and app.play_from_map == False:
            init_menus.next_boss(app)
        elif (event.key == app.enter_bind):
            init_menus.map_init(app)
    #om du skulle være så uheldig å dø
    elif app.game_state == "Dead":
        #restarter fighten eller setter deg tilbake til menus hvis du er tom for liv
        if (event.key == "r"):
            if app.player_lives > 0:
                if app.boss_fight == "One":
                    init_classes.init_boss_1(app)
                    init_classes.init_playable_character_one(app)
                elif app.boss_fight == "Two":
                    init_classes.init_boss_2(app)
                    init_classes.init_playable_character_one(app)
                elif app.boss_fight == "Three":
                    init_classes.init_boss_3(app)
                    init_classes.init_playable_character_one(app)
                elif app.boss_fight == "Final":
                    init_classes.init_final_boss(app)
                    init_classes.init_playable_character_one(app)
            else:
                #hvis du spiller fra map kommer du tilbake til map
                if app.play_from_map == True:
                    init_menus.map_init(app)
                #ellers kommer du tilbake til hovedmenyen
                else:
                    init_menus.init_menu(app)
    #venter på input på victory skjermen
    elif app.game_state == "Victory":
        if (event.key == app.enter_bind) or (event.key == "r") or (event.key == "Escape"):
            init_menus.init_menu(app)
    #credits escape for abort bare
    elif app.game_state == "Credits":
        if (event.key == "Escape"):
            init_menus.settings_init(app)
            music.stop_all_sounds()
            app.main_menu_song.play()

### mitt tegnebrett ###
def redraw_all(app, canvas):
    #tegner når running (altså boss fights)
    if app.game_state == "Running":
        #bakgrunn
        draw_functions.draw_backgrounds(app, canvas)
        #debug, hvis på tegner hitbox og basic_attack (skal  vekk kanskje)
        if app.show_basic_attack > 0 and app.debug == True:
            draw_functions.draw_basic_attack(app, canvas)
            draw_functions.draw_character_hitbox(app, canvas)
        #tegner karakteren
        draw_functions.draw_character_advanced(app, canvas)
        ###boss fights###
        #første bossen
        if app.boss_fight == "One":
            #debug for første bossen
            if app.debug == True:
                draw_functions.draw_boss_one_hitbox(app, canvas)
                draw_functions.draw_boss_one_healthbar(app, canvas)
            #tegner første bossen
            draw_functions.draw_boss_one(app, canvas)
        #andre bossen    
        elif app.boss_fight == "Two":
            #tegner boss to
            draw_functions.draw_boss_two(app, canvas)
            #debug
            if app.show_boss_attack > 0 and app.debug == True:
                draw_functions.draw_boss_two_attack(app, canvas)
            #tegner projektilene
            if app.show_projectile_1 == True:
                canvas.create_image(app.projectile_1[0][0] + 12, app.projectile_1[0][1],pil_image=app.b2_p1_i)
            if app.show_projectile_2 == True:
                canvas.create_image(app.projectile_1[1][0] + 12, app.projectile_1[1][1],pil_image=app.b2_p1_i)
        #tredje bossen
        elif app.boss_fight == "Three":
            #tegner bossen
            draw_functions.draw_boss_three(app, canvas)
            #tegner projectilene til boss tre
            if app.show_projectile_3 == True:
                draw_functions.draw_boss_three_projectiles(app, canvas)
            #debug tegning
            if app.show_boss_attack > 0 and app.debug == True:
                draw_functions.draw_boss_two_attack(app, canvas)
        #siste bossen
        elif app.boss_fight == "Final":
            #debug funksjoner
            if app.show_boss_attack > 0 and app.debug == True:
                draw_functions.draw_boss_two_attack(app, canvas)
            if app.debug == True:
                draw_functions.draw_boss_one_hitbox(app, canvas)
                canvas.create_text(200, 200, text=app.enemy_health,fill="white")
            #tegner siste bossen
            draw_functions.draw_boss_final(app, canvas)
    #tegner hoved menyen
    elif app.game_state == "Menu":
        draw_functions.draw_main_menu(app, canvas)
        for button in app.main_menu_buttons:
            draw_functions.draw_main_menu_buttons(app, button , canvas)
        draw_functions.draw_main_menu_selector(app, canvas)
    #tegner pop up om man rebinder key
    elif app.game_state ==  "Binding_key":
        canvas.create_image(450, 450 , pil_image=app.main_menu_bg)
        draw_functions.draw_binding_key_pop_up(app, canvas)
    #tegner practise mode / debug skjerm for boss velger
    elif app.game_state == "Map":
        canvas.create_image(450, 450 , pil_image=app.main_menu_bg)
        draw_functions.draw_map(app, canvas)
        draw_functions.draw_map_selector(app, canvas)
    #tegner settingsene mine
    elif app.game_state == "Settings":
        canvas.create_image(450, 450 , pil_image=app.main_menu_bg)
        for button in app.settings_buttons:
            draw_functions.draw_setting_buttons(app, button, canvas)
        draw_functions.draw_settings_selector(app, canvas)
    #tegner credits
    elif app.game_state == "Credits":
        canvas.create_image(450, 450 , pil_image=app.main_menu_bg)
        draw_functions.draw_credits(app, canvas)
    #tegner difficulty velgeren
    elif app.game_state == "Difficulty":
        canvas.create_image(450, 450 , pil_image=app.main_menu_bg)
        for button in app.difficulty_buttons:
            draw_functions.draw_difficulty_buttons(app, button, canvas)
        draw_functions.draw_difficulty_selector(app, canvas)
    #tegner rebind menyen
    elif app.game_state == "Rebind":
        canvas.create_image(450, 450 , pil_image=app.main_menu_bg)
        for button in app.rebind_buttons:
            draw_functions.draw_rebind_buttons(app , button , canvas)
        draw_functions.draw_rebind_selector(app, canvas)
    #tegner continue skjermen mellom bossene
    elif app.game_state == "Boss_One_Down":
        draw_functions.draw_continue_boss_one(app, canvas)
    elif app.game_state == "Boss_Two_Down":
        draw_functions.draw_continue_boss_two(app, canvas)
    elif app.game_state == "Boss_Three_Down":
        draw_functions.draw_continue_boss_three(app, canvas)
    #tegner skjermen om du er død
    elif app.game_state == "Dead":
        draw_functions.draw_death_screen(app, canvas)
    #tegner seier skjermen :) (om noen klarer å se denne da?)
    elif app.game_state == "Victory":
        draw_functions.draw_victory_screen(app, canvas)

#app stopped
def app_stopped(app):
    #lagrer profilen
    helpers.save_json(app)
    content =json.dumps(app.profile)
    Path("Story_of_Alfred/profile.json").write_text(content, encoding="utf-8")
    #stopper musikken
    music.stop_all_sounds()

#run app, starter programmet
run_app(width=900,height=900)