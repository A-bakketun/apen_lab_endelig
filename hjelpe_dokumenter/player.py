
def timer_player_char_one(app):
    #timer for player 
    player_movement(app)
    player_animation_timer(app)
    if app.player_took_damage > 0:
        app.player_took_damage -= 1
    if app.i_frames > 0:
        app.player_color = "pink"
    else:
        app.player_color = "red"
    if app.basic_attack_cooldown > 0:
        app.basic_attack_cooldown -= 1
    if app.dodge_timer > 0:
        app.dodge_timer -= 1
    if app.dash_timer > 0:
        app.dash_timer -= 1
    if app.attack_stops_movement > 0:
        app.attack_stops_movement -= 1
    if app.i_frames > 0:
        app.i_frames -= 1
    if app.show_basic_attack > 0:
        app.show_basic_attack -= 1
    if app.idle_counter > 0:
        app.idle_counter -= 1
    if app.idle_counter == 0 and app.player_moving == False:
        app.player_state = "Idle"
    if app.player_health <= 0:
        kill_player(app)
    input_delay_player(app)

### animation timere
def player_animation_timer(app):
    app.do_animation += 1

    if app.do_animation > 10:
        if app.animation_counter < 3:
            app.animation_counter += 1
            app.do_animation = 0
        elif app.animation_counter == 3:
            app.animation_counter = 0
            app.do_animation = 0

def input_delay_player(app):
    #input delay player
    if app.input_delay > 0:
        app.input_delay -= 1

def kill_player(app):
    #dreper player
    app.player_lives -= 1
    death_screen_init(app)

def death_screen_init(app):
    #for å sette opp death screenen
    import hjelpe_dokumenter.uib_inf100_music as music
    music.stop_all_sounds()
    app.game_state = "Dead"
    app.death_song.play()

def player_dodge(app):
    #dodge action
    app.dodge_timer += app.dodge_cd
    app.i_frames = 6

def player_dash(app):
    #dash action
    app.player_pos_x += app.player_dash_distance * app.player_facing
    app.player_pos_hix += app.player_dash_distance * app.player_facing
    app.dash_timer = 20
    app.i_frames += 3

def player_movement(app):
    #player movement, hvis du holder inne høyre eller venstre går du den retningen
    if app.player_direction == "West" and app.attack_stops_movement == 0:
        app.player_facing = -1
    elif app.player_direction == "East" and app.attack_stops_movement == 0:
        app.player_facing = 1 

    if app.player_direction == "West" and app.player_moving == True and app.attack_stops_movement == 0 and app.player_pos_x - 10 > 0:
        app.player_pos_x -= app.player_speed 
        app.player_pos_hix -= app.player_speed 
        app.player_state = "Walking"
    elif app.player_direction == "East" and app.player_moving == True and app.attack_stops_movement == 0 and app.player_pos_hix + 10 < 900:
        app.player_pos_x += app.player_speed  
        app.player_pos_hix += app.player_speed 
        app.player_state = "Walking"

def basic_attack(app):
    #basic attack
    import hjelpe_dokumenter.attacks as attacks
    import hjelpe_dokumenter.init_menus as init_menus
    app.basic_attack_cooldown = app.attack_cd
    app.attack_stops_movement = app.attack_stop_movement_duration
    #debug
    app.show_basic_attack = 10
    app.player_state = "Attack"
    app.idle_counter = 10
    app.do_animation = 5
    app.animation_counter = 0
    #lager angrepet
    if app.player_direction == "East":
        attack_hitbox = app.player_pos_hix, app.player_pos_y + 40, app.player_pos_hix + 60, app.player_pos_y + 20
    if app.player_direction == "West":
        attack_hitbox = app.player_pos_x , app.player_pos_y + 40, app.player_pos_x - 60, app.player_pos_y + 20
    app.attack_hitbox = attack_hitbox
    #sjekker om angrepet treffer
    if attack_collision_detection(app, attack_hitbox) == True:
        app.enemy_hit = 10
        if app.enemy_health - app.player_damage <= 0:
            init_menus.kill_enemy(app)
        elif app.enemy_health >= 0:
            app.enemy_health -= app.player_damage
        if app.boss_fight == "Two" and app.boss_stage == "One":
            attacks.teleport_boss_two(app)

def attack_collision_detection(app, attack_hitbox):
    #sjekker om angrepet treffer
    hitbox_lo_x = attack_hitbox[0] 
    hitbox_lo_y = attack_hitbox[1]
    hitbox_hi_x = attack_hitbox[2] 
    hitbox_hi_y = attack_hitbox[3] 
    #if hit, enemy_hit += 10
    if hitbox_lo_x >= app.enemy_pos_x and hitbox_lo_x <= app.enemy_pos_x + 100:
        enemy_hit = True
        app.enemy_i_frames = 6
        return enemy_hit
    elif hitbox_hi_x >= app.enemy_pos_x and hitbox_hi_x <= app.enemy_pos_x + 50:
        enemy_hit = True
        app.enemy_i_frames = 6
        return enemy_hit

