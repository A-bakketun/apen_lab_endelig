import hjelpe_dokumenter.attacks as attacks
import hjelpe_dokumenter.action_calc as action_calc



##### boss timere
def boss_one_timer(app):
    #finner ut retningen til boss
    if app.enemy_pos_x > app.player_pos_x and app.boss_stagger == 0:
        app.enemy_direction = 1
    if app.enemy_pos_x < app.player_pos_x and app.boss_stagger == 0:
        app.enemy_direction = -1
    #regn ut hva boss skal gjøre
    if app.enemy_action == "Idle":
        action_calc.boss_one_action_calc(app)
    #gjør det den skal gjøre
    if app.enemy_cd == 0:
        if app.enemy_action == "Walk_West":
            app.enemy_pos_x -= app.enemy_speed
            app.enemy_pos_hix -= app.enemy_speed
            app.enemy_cd += 8
            app.enemy_action = "Idle"
        elif app.enemy_action == "Walk_East":
            app.enemy_pos_x += app.enemy_speed
            app.enemy_pos_hix += app.enemy_speed
            app.enemy_cd += 8
            app.enemy_action = "Idle"
        elif app.enemy_action == "Attack_1":
            if app.boss_stagger == 0:
                app.boss_one_attack_one_frame = 0
                app.animate_boss_one_attack_one = True
            app.boss_stagger += 1
            if app.boss_stagger % 4 == 0:
                app.boss_one_attack_one_frame += 1
            if app.boss_stagger > 10:
                attacks.boss_one_attack_one(app)
                app.enemy_cd += 6
                app.enemy_action = "Attack_2"
                app.boss_color = "green"
                app.boss_stagger = 0
                app.boss_one_attack_one_frame = 0

        elif app.enemy_action == "Attack_2":                
            app.boss_stagger += 1
            if app.boss_stagger % 2 == 0:
                app.boss_one_attack_one_frame += 1
            if app.boss_stagger > 4:
                attacks.boss_one_attack_two(app)
                app.enemy_cd += 12
                app.enemy_action = "Idle"
                app.boss_color = "green"
                app.boss_stagger = 0
                app.animate_boss_one_attack_one = False

        elif app.enemy_action == "Attack_3":
            if app.boss_stagger == 0:
                app.boss_one_attack_one_frame = 0
                app.animate_boss_one_attack_one = True
            app.boss_stagger += 1
            if app.boss_stagger % 2 == 0:
                app.boss_one_attack_one_frame += 1
            if app.boss_stagger > 4:
                attacks.boss_one_attack_three(app)
                app.enemy_cd +=10
                app.enemy_action = "Idle"
                app.boss_color = "green"
                app.boss_stagger = 0
                app.animate_boss_one_attack_one = False
    helper_boss_one(app)

def boss_two_timer(app):
    #timer for boss to
    import random
    if app.boss_stage == "One":
        if app.enemy_action == "Idle":
            action_calc.boss_two_action_calc(app)
        if app.enemy_cd == 0:
            if app.enemy_action == "Attack_1":
                app.boss_stagger += 1
                if app.boss_stagger == 1:
                    attacks.boss_two_show_attack_one(app)
                    app.stop_show_boss_two_attack_one = 26
                if app.boss_stagger > 12:
                    attacks.boss_two_attack_one(app)
                    app.enemy_cd += 20
                    app.enemy_action = "Idle"      
            elif app.enemy_action == "Attack_2":
                attacks.boss_two_attack_two(app)
                app.enemy_cd += 20
                app.enemy_action = "Idle"
                app.enemy_projectile_cd += 40
            elif app.enemy_action == "Attack_3":
                app.boss_stagger += 1
                if app.boss_stagger == 1:
                    attacks.boss_two_show_attack_three(app)
                    app.stop_showing_b2_a3 = 20
                if app.boss_stagger > 8:
                    attacks.boss_two_attack_three(app)
                    app.enemy_cd += 12
                    app.enemy_action = "Idle"
    attacks.projectile_manager_one(app)
    if app.boss_two_teleport == True:
        if app.tp_counter > 0:
            app.tp_counter -= 1
        if app.tp_counter == 0:
            random_factor = (10 * random.randrange(11))
            app.boss_two_teleport = False
            if app.enemy_pos_x - 1700 + random_factor < 100:
                app.enemy_pos_x = 720
                app.enemy_pos_hix = 736
            else:
                app.enemy_pos_x -= 1600 + random_factor
                app.enemy_pos_hix -= 1600 + random_factor
    helper_boss_two(app)            
                
def boss_three_timer(app):
    #timer for tredje bossen
    #sjekker retningen på boss
    if app.enemy_pos_x > app.player_pos_x and app.boss_stagger == 0:
        app.enemy_direction = 1
    if app.enemy_pos_x < app.player_pos_x and app.boss_stagger == 0:
        app.enemy_direction = -1
    #hvis idle, bestem neste handling
    if app.enemy_action == "Idle":
        action_calc.boss_three_action_calc(app)
    #hvis cooldown er 0, gjør angrep
    if app.enemy_cd == 0:
        if app.enemy_action == "Attack_1":
            attacks.boss_three_attack_one(app)
            app.enemy_action = "Idle"
            app.enemy_cd = 16
        elif app.enemy_action == "Attack_2":
            if app.boss_stagger == 0:
                attacks.boss_three_show_attack_two(app)
            app.boss_stagger += 1
            if app.boss_stagger % 2 == 0:
                app.b3_a2_f += 1
            if app.boss_stagger > 7:
                attacks.boss_three_attack_two(app)
                app.enemy_action = "Idle"
                app.enemy_cd = 14
                app.b3_a2_f = 0
                app.boss_stagger = 0
        elif app.enemy_action == "Attack_3":
            if app.boss_stagger == 0:
                attacks.boss_three_show_attack_three(app)
            app.boss_stagger += 1
            if app.boss_stagger >12:
                attacks.boss_three_attack_three(app)
                app.enemy_action = "Idle"
                app.enemy_cd = 12            
    attacks.projectile_manager_two(app)
    if app.enemy_cd > 0:
        app.enemy_cd -= 1
    if app.stop_showing_b3_a3 > 0:
        app.stop_showing_b3_a3 -= 1
    if app.stop_showing_b3_a3 == 1:
        app.show_b3_a3 = False
    if app.enemy_i_frames > 0:
        app.enemy_i_frames -= 1
   
def boss_final_timer_one(app):
    #timer for siste bossen, sin første fase
    if app.enemy_health < 600:
        app.boss_stage = "Two"
    if app.enemy_pos_x > app.player_pos_x and app.boss_stagger == 0:
        app.enemy_direction = 1
    elif app.enemy_pos_x < app.player_pos_x and app.boss_stagger == 0:
        app.enemy_direction = -1    
    if app.enemy_cd == 0 and app.enemy_action == "Idle":
            action_calc.boss_final_action_calc(app)
    if app.enemy_action == "Walk_West":
            app.enemy_pos_x -= app.enemy_speed
            app.enemy_pos_hix -= app.enemy_speed
            app.enemy_action = "Idle"
            app.enemy_cd += 2
    elif app.enemy_action == "Walk_East":
            app.enemy_pos_x += app.enemy_speed
            app.enemy_pos_hix += app.enemy_speed
            app.enemy_action = "Idle"
            app.enemy_cd += 2
    elif app.enemy_action == "Attack_1":
        app.boss_stagger += 1
        if app.boss_stagger % 3 == 0:
            app.b4_a1_frame += 1
        if app.boss_stagger == 3:
            attacks.boss_final_attack_one_phase_one(app)
            app.show_boss_attack = 10
        elif app.boss_stagger == 10:
            attacks.boss_final_attack_one_phase_two(app)
            app.enemy_action = "Idle"
            app.boss_cd = 15
            app.show_boss_attack = 10
            app.b4_a1_frame = 0
    elif app.enemy_action == "Attack_2":
        app.boss_stagger += 1
        if app.boss_stagger % 4 == 0:
            app.boss_final_attack_two_frame += 1
        if app.boss_stagger == 13:
            attacks.boss_final_attack_two(app)
            app.enemy_action = "Idle"
            app.boss_cd = 15
            app.show_boss_attack = 10
            app.boss_final_attack_two_frame = 0   
    helper_boss_final(app)

def boss_final_timer_two(app):
    #timer for siste bossen, sin andre fase
    #hver så og så ofte, skap et lyn prosjectil
    #timer for siste bossen, sin første fase
    if app.enemy_pos_x > app.player_pos_x and app.boss_stagger == 0:
        app.enemy_direction = 1
    elif app.enemy_pos_x < app.player_pos_x and app.boss_stagger == 0:
        app.enemy_direction = -1    
    if app.enemy_cd == 0 and app.enemy_action == "Idle":
            action_calc.boss_final_action_calc(app)
    if app.enemy_action == "Walk_West":
            app.enemy_pos_x -= app.enemy_speed
            app.enemy_pos_hix -= app.enemy_speed
            app.enemy_action = "Idle"
            app.enemy_cd += 2
    elif app.enemy_action == "Walk_East":
            app.enemy_pos_x += app.enemy_speed
            app.enemy_pos_hix += app.enemy_speed
            app.enemy_action = "Idle"
            app.enemy_cd += 2
    elif app.enemy_action == "Attack_1":
        app.boss_stagger += 1
        if app.boss_stagger % 3 == 0:
            app.b4_a1_frame += 1
        if app.boss_stagger == 3:
            attacks.boss_final_attack_one_phase_one(app)
            app.show_boss_attack = 10
        elif app.boss_stagger == 10:
            attacks.boss_final_attack_one_phase_two(app)
            app.enemy_action = "Idle"
            app.boss_cd = 10
            app.show_boss_attack = 10
            app.b4_a1_frame = 0
    elif app.enemy_action == "Attack_2":
        app.boss_stagger += 1
        if app.boss_stagger % 4 == 0:
            app.boss_final_attack_two_frame += 1
        if app.boss_stagger == 13:
            attacks.boss_final_attack_two(app)
            app.enemy_action = "Idle"
            app.boss_cd = 10
            app.show_boss_attack = 10
            app.boss_final_attack_two_frame = 0  

    #lager periodemessig tredje angrep i denne fasen
    if app.boss_stagger > 0 and app.show_zone_attack == False:
        app.final_attack_aframe = 0
        attacks.boss_final_show_attack_three(app)
        app.final_attack_timer = 20
    if app.final_attack_timer == 6:
        app.final_attack_aframe = 1
    elif app.final_attack_timer == 5 and app.show_zone_attack == True:
        attacks.boss_final_attack_three(app)

    helper_boss_final(app)
    if app.final_attack_timer > 0:
        app.final_attack_timer -= 1
    if app.final_attack_timer == 0:
        app.show_zone_attack = False

def victory_screen_timer(app):
    #animerer victory screenen
    app.animate_victory_screen += 1
    if app.animate_victory_screen % 10 == 0:
        if app.victory_animation_frames < 2:
            app.victory_animation_frames += 1
        elif app.victory_animation_frames == 2:
            app.victory_animation_frames = 0

def rebind_timer(app):
    #timer hvis man ombestemmer meg på keybinding eller ikke bestemmer seg
    import hjelpe_dokumenter.helper_functions as helpers
    if app.bind_timer > 0:
        app.bind_timer -= 1
    if app.new_bound != 0:
        helpers.rebind_keys(app)
    if app.bind_timer == 0:
            app.game_state == "Rebind"

def helper_boss_one(app):
    #for å korte ned timeren for boss_one
    #alle disse går alltid
    if app.enemy_cd > 0:
        app.enemy_cd -= 1
    if app.show_boss_attack > 0:
        app.show_boss_attack -= 1
    if app.enemy_i_frames > 0:
        app.enemy_i_frames -= 1

def helper_boss_two(app):
    #korte ned boss_two timeren
    if app.enemy_cd > 0:
        app.enemy_cd -= 1
    if app.stop_show_boss_two_attack_one > 0:
        app.stop_show_boss_two_attack_one -= 1
    if app.stop_show_boss_two_attack_one == 0:
        app.boss_two_show_attack_one = False 
    if app.stop_showing_b2_a3 > 0:
        app.stop_showing_b2_a3 -= 1
    if app.stop_showing_b2_a3 == 0:
        app.boss_two_show_attack_three = False
    if app.enemy_tp_cd > 0:
        app.enemy_tp_cd -= 1
    if app.show_boss_attack > 0:
        app.show_boss_attack -= 1
    if app.enemy_projectile_cd > 0:
        app.enemy_projectile_cd -= 1
    app.animation_tick += 1
    if app.animation_tick % 7 == 0:
        if app.b2_animation <= 6:
            app.b2_animation_f += 1
            app.b2_animation += 1
        if app.b2_animation >= 7:
            app.b2_animation_f = 0
            app.b2_animation = 0

def helper_boss_three(app):
    #for å korte ned timer funksjon for boss tre
    app.animation_tick += 1
    if app.enemy_i_frames > 0:
        app.enemy_i_frames -= 1
    if app.enemy_i_frames > 0:
        app.enemy_i_frames -= 1
    if app.enemy_cd > 0:
        app.enemy_cd -= 1
    if app.show_boss_attack > 0:
        app.show_boss_attack -= 1
    if app.animation_tick % 7 == 0:
        if app.b4_animation_f < 2:
            app.b4_animation_f += 1
        if app.b4_animation_f == 2:
            app.b4_animation_f = 0

def helper_boss_final(app):
    app.animation_tick += 1
    if app.enemy_i_frames > 0:
        app.enemy_i_frames -= 1
    if app.enemy_i_frames > 0:
        app.enemy_i_frames -= 1
    if app.enemy_cd > 0:
        app.enemy_cd -= 1
    if app.show_boss_attack > 0:
        app.show_boss_attack -= 1
    if app.animation_tick % 7 == 0:
        if app.b4_animation_f < 2:
            app.b4_animation_f += 1
        if app.b4_animation_f == 2:
            app.b4_animation_f = 0
