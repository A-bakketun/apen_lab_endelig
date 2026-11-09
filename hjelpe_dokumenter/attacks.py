import random

############################
############ Boss one ################
#################################
def boss_one_attack_one(app):

    if app.enemy_direction == 1:
        app.enemy_attack_x1 = app.enemy_pos_x -10 * app.enemy_direction
        app.enemy_attack_y1 = app.enemy_pos_y + 70
        app.enemy_attack_x2 = app.enemy_pos_x - 60 * app.enemy_direction
        app.enemy_attack_y2 = app.enemy_pos_y + 10
    elif app.enemy_direction == -1:
        app.enemy_attack_x1 = app.enemy_pos_hix -10 * app.enemy_direction
        app.enemy_attack_y1 = app.enemy_pos_y + 70
        app.enemy_attack_x2 = app.enemy_pos_hix - 60 * app.enemy_direction
        app.enemy_attack_y2 = app.enemy_pos_y + 10
    enemy_attack_hitbox = app.enemy_attack_x1, app.enemy_attack_y1, app.enemy_attack_x2, app.enemy_attack_y2
    if collision_detection_enemy_attack(app, enemy_attack_hitbox) == True and app.i_frames == 0:
            app.player_health -= 10
            app.i_frames += 4
    app.show_boss_attack += 10
    app.boss_stagger = 0

def boss_one_attack_two(app):
    #disse variablene trenger ikke være app hvis jeg ikke skal vise angrepene
    if app.enemy_direction == 1:
        app.enemy_attack_x1 = app.enemy_pos_x -20 
        app.enemy_attack_y1 = app.enemy_pos_y + 70
        app.enemy_attack_x2 = app.enemy_pos_x + 10 
        app.enemy_attack_y2 = app.enemy_pos_y + 10
    elif app.enemy_direction == -1:
        app.enemy_attack_x1 = app.enemy_pos_hix -20 
        app.enemy_attack_y1 = app.enemy_pos_y + 70
        app.enemy_attack_x2 = app.enemy_pos_hix + 10 
        app.enemy_attack_y2 = app.enemy_pos_y + 10

    enemy_attack_hitbox = app.enemy_attack_x1, app.enemy_attack_y1, app.enemy_attack_x2, app.enemy_attack_y2
    if collision_detection_enemy_attack(app, enemy_attack_hitbox) == True and app.i_frames == 0:
        app.player_health -= 5
        app.i_frames += 4
    app.show_boss_attack += 10
    app.boss_stagger = 0

def boss_one_attack_three(app):
    if app.enemy_direction == 1:

        app.enemy_attack_x1 = app.enemy_pos_x - 20 
        app.enemy_attack_y1 = app.enemy_pos_y + 70
        app.enemy_attack_x2 = app.enemy_pos_x - 50 
        app.enemy_attack_y2 = app.enemy_pos_y + 10
    elif app.enemy_direction == -1:
        app.enemy_attack_x1 = app.enemy_pos_hix + 20 
        app.enemy_attack_y1 = app.enemy_pos_y + 70
        app.enemy_attack_x2 = app.enemy_pos_hix + 50 
        app.enemy_attack_y2 = app.enemy_pos_y + 10

    enemy_attack_hitbox = app.enemy_attack_x1, app.enemy_attack_y1, app.enemy_attack_x2, app.enemy_attack_y2
    if collision_detection_enemy_attack(app, enemy_attack_hitbox) == True and app.i_frames == 0:
        app.player_health -= 5
        app.i_frames += 4
    app.show_boss_attack += 10
    app.boss_stagger = 0

##############################################
############ Boss two ########################
##############################################

def boss_two_attack_one(app):
    app.boss_two_attack_one_frame = 1
    enemy_attack_hitbox = app.enemy_attack_x1, app.enemy_attack_y1, app.enemy_attack_x2, app.enemy_attack_y2
    if collision_detection_enemy_attack(app, enemy_attack_hitbox) == True and app.i_frames == 0:
        app.player_health -= 12
        app.i_frames += 4
    app.show_boss_attack += 10
    app.boss_stagger = 0

def boss_two_show_attack_one(app):
    random_factor = random.randrange(3)
    app.enemy_attack_x1 = app.player_pos_x - 20 + (10 * random_factor)
    app.enemy_attack_y1 = app.player_pos_hiy
    app.enemy_attack_x2 = app.player_pos_hix + 20 + (10 * random_factor)
    app.enemy_attack_y2 = app.player_pos_hiy - 20
    app.boss_two_show_attack_one = True
    app.boss_two_attack_one_frame = 0

def boss_two_attack_two(app):
    area = app.player_pos_x + 12, app.player_pos_hix -12
    app.boss_two_projectile_cd = False
    create_projectile_one(app, area)

def boss_two_attack_three(app):
    app.boss_two_attack_three_frame = 1
    enemy_attack_hitbox = app.enemy_attack_x1, app.enemy_attack_y1, app.enemy_attack_x2, app.enemy_attack_y2
    if collision_detection_enemy_attack(app, enemy_attack_hitbox) == True and app.i_frames == 0:
        app.player_health -= 8
        app.i_frames += 4
    app.show_boss_attack += 10
    app.boss_stagger = 0

def boss_two_show_attack_three(app):
    
    random_factor = random.randrange(-10, 10)
    app.enemy_attack_x1 = app.player_pos_x - 20 + (10 * random_factor)
    app.enemy_attack_y1 = app.player_pos_hiy
    app.enemy_attack_x2 = app.player_pos_hix + 20 + (10 * random_factor)
    app.enemy_attack_y2 = app.player_pos_hiy - 20
    app.boss_two_show_attack_three = True
    app.boss_two_attack_three_frame = 0


def teleport_boss_two(app):
    app.tp_counter = 40
    app.boss_two_teleport = True
    app.enemy_pos_x += 1500
    app.enemy_pos_hix += 1500


##############################################
##########BOSS THREE #########################
##############################################

def boss_three_attack_one(app):
    create_projectile_two(app)

def boss_three_show_attack_two(app):
    app.show_b3_a2 = True
    app.b3_a2_f = 0

def boss_three_attack_two(app):
    if app.enemy_direction == 1:
        app.enemy_attack_x1 = app.enemy_pos_x - 20
        app.enemy_attack_y1 = app.enemy_pos_y + 20
        app.enemy_attack_x2 = app.enemy_pos_x - 88
        app.enemy_attack_y2 = app.enemy_pos_y +40
    if app.enemy_direction == -1:
        app.enemy_attack_x1 = app.enemy_pos_x + 20
        app.enemy_attack_y1 = app.enemy_pos_y + 20
        app.enemy_attack_x2 = app.enemy_pos_x + 88
        app.enemy_attack_y2 = app.enemy_pos_y +40

    enemy_attack_hitbox = app.enemy_attack_x1, app.enemy_attack_y1, app.enemy_attack_x2, app.enemy_attack_y2   
    if collision_detection_enemy_attack(app, enemy_attack_hitbox) == True and app.i_frames == 0:
        app.player_health -= 8
        app.i_frames += 4
        if app.player_pos_x > app.enemy_pos_hix:
            app.player_pos_x -= 600
            app.player_pos_hix -= 600
        else:
            app.player_pos_x -= 300
            app.player_pos_hix -= 300

    app.show_boss_attack += 20
    app.boss_stagger = 0

def boss_three_show_attack_three(app):
    app.enemy_attack_x1 = app.player_pos_x - 24
    app.enemy_attack_y1 = app.enemy_pos_y + 20
    app.enemy_attack_x2 = app.player_pos_hix + 24
    app.enemy_attack_y2 = app.enemy_pos_y +40  

    app.show_b3_a3 = True
    app.b3_a3_f = 0
    app.stop_showing_b3_a3 = 20

def boss_three_attack_three(app):
    app.b3_a3_f = 1
    enemy_attack_hitbox = app.enemy_attack_x1, app.enemy_attack_y1, app.enemy_attack_x2, app.enemy_attack_y2
    if collision_detection_enemy_attack(app, enemy_attack_hitbox) == True and app.i_frames == 0:
        app.player_health -= 12
        app.i_frames += 4

    app.boss_stagger = 0

##############################################
#################final boss###################
##############################################
def boss_final_attack_one_phase_one(app):
    #attack en, fase en av angrepet
    if app.enemy_direction == 1:

        app.enemy_attack_x1 = app.enemy_pos_x 
        app.enemy_attack_y1 = app.enemy_pos_y + 70
        app.enemy_attack_x2 = app.enemy_pos_x - 40 
        app.enemy_attack_y2 = app.enemy_pos_y + 10
    elif app.enemy_direction == -1:
        app.enemy_attack_x1 = app.enemy_pos_hix 
        app.enemy_attack_y1 = app.enemy_pos_y + 70
        app.enemy_attack_x2 = app.enemy_pos_hix + 40
        app.enemy_attack_y2 = app.enemy_pos_y + 10   

def boss_final_attack_one_phase_two(app):
    #attack en, fase to av angrepet
    if app.enemy_direction == 1:

        app.enemy_attack_x1 = app.enemy_pos_x
        app.enemy_attack_y1 = app.enemy_pos_y + 70
        app.enemy_attack_x2 = app.enemy_pos_x - 50 
        app.enemy_attack_y2 = app.enemy_pos_y + 10
    elif app.enemy_direction == -1:
        app.enemy_attack_x1 = app.enemy_pos_hix 
        app.enemy_attack_y1 = app.enemy_pos_y + 70
        app.enemy_attack_x2 = app.enemy_pos_hix + 50 
        app.enemy_attack_y2 = app.enemy_pos_y + 10
    enemy_attack_hitbox = app.enemy_attack_x1, app.enemy_attack_y1, app.enemy_attack_x2, app.enemy_attack_y2
    if collision_detection_enemy_attack(app, enemy_attack_hitbox) == True and app.i_frames == 0:
        app.player_health -= 5
        app.i_frames += 4
    app.show_boss_attack += 10
    app.boss_stagger = 0    

def boss_final_attack_two(app):
    #angrep nr 2 av final boss
    if app.enemy_direction == 1:

        app.enemy_attack_x1 = app.enemy_pos_x  
        app.enemy_attack_y1 = app.enemy_pos_y + 70
        app.enemy_attack_x2 = app.enemy_pos_x - 50 
        app.enemy_attack_y2 = app.enemy_pos_y + 10
    elif app.enemy_direction == -1:
        app.enemy_attack_x1 = app.enemy_pos_hix
        app.enemy_attack_y1 = app.enemy_pos_y + 70
        app.enemy_attack_x2 = app.enemy_pos_hix + 50 
        app.enemy_attack_y2 = app.enemy_pos_y + 10   
    enemy_attack_hitbox = app.enemy_attack_x1, app.enemy_attack_y1, app.enemy_attack_x2, app.enemy_attack_y2
    if collision_detection_enemy_attack(app, enemy_attack_hitbox) == True and app.i_frames == 0:
        app.player_health -= 10
        app.i_frames += 6

    app.show_boss_attack += 10
    app.boss_stagger = 0  

def boss_final_show_attack_three(app):
    #viser lyn angrepene til attack tre
    random1 = (random.randrange(10, 80) * 10)
    random2 = (random.randrange(10, 80) * 10)
    random3 = (random.randrange(10, 80) * 10)
    app.show_zone_attack = True
    app.zone_attack_one = [[random1, app.enemy_pos_y, random1 + 48, app.enemy_pos_hiy],
                           [random2, app.enemy_pos_y, random2 + 48, app.enemy_pos_hiy],
                           [random3, app.enemy_pos_y, random3 + 48, app.enemy_pos_hiy],
                           ]
    
def boss_final_attack_three(app):
    #triggere angrepet til attack tre
    enemy_attack_hitbox = app.zone_attack_one[0]
    if collision_detection_enemy_attack(app, enemy_attack_hitbox) == True and app.i_frames == 0:
        app.player_health -= 5
        app.i_frames += 6
    enemy_attack_hitbox = app.zone_attack_one[1]
    if collision_detection_enemy_attack(app, enemy_attack_hitbox) == True and app.i_frames == 0:
        app.player_health -= 5
        app.i_frames += 6
    enemy_attack_hitbox = app.zone_attack_one[2]
    if collision_detection_enemy_attack(app, enemy_attack_hitbox) == True and app.i_frames == 0:
        app.player_health -= 5
        app.i_frames += 6


def collision_detection_enemy_attack(app, attack_hitbox):
    ### collision detection på enemy attacks
    hitbox_lo_x = attack_hitbox[0] 
    hitbox_lo_y = attack_hitbox[1]
    hitbox_hi_x = attack_hitbox[2] 
    hitbox_hi_y = attack_hitbox[3] 
    if hitbox_lo_x >= app.player_pos_x and hitbox_hi_x <= app.player_pos_x:
        enemy_hit = True
    elif hitbox_lo_x >= app.player_pos_hix and hitbox_hi_x <= app.player_pos_hix:
        enemy_hit = True
    elif (hitbox_lo_x + hitbox_hi_x) / 2 >= app.player_pos_x and (hitbox_lo_x + hitbox_hi_x) / 2 <= app.player_pos_hix:
        enemy_hit = True
    elif app.player_pos_x >= hitbox_lo_x and app.player_pos_x <= hitbox_hi_x:
        enemy_hit = True
    elif app.player_pos_hix >= hitbox_lo_x and app.player_pos_hix <= hitbox_hi_x:
        enemy_hit = True
    else:
        enemy_hit = False

    if enemy_hit == True and app.i_frames == 0:
        app.player_took_damage = 6
    return enemy_hit


def create_projectile_one(app, area):
    #lager projectile for boss to
    #altså flammeballene som faller
    x1 = area[0]
    x2 = area[1]
    y1= 100
    y2= 124
    app.projectile_1 = [[x1, y1 , x2 ,y2],
                        [x1 + 60, y1-300, x2+ 60, y2-300]
                ]
    app.show_projectile_1 = True
    app.show_projectile_2 = True

def create_projectile_two(app):
    #lager projectile for boss tre
    #altså soppen som blir skøte ut
    x = app.enemy_pos_x
    y = app.enemy_pos_y + 10
    x2 = x + 20
    y2 = y + 20
    app.projectile_2 = [x, y, x2 , y2]
    app.show_projectile_3 = True

def projectile_manager_one(app):
    #projectile manager for flammeballene til boss to
    if app.projectile_1[0][1] < 700:
        app.projectile_1[0][1] += app.projectile_speed
        app.projectile_1[0][3] += app.projectile_speed
    else:
        app.show_projectile_1 = False
        

    if app.projectile_1[1][1] < 700:
        app.projectile_1[1][1] += app.projectile_speed
        app.projectile_1[1][3] += app.projectile_speed
    else:
        app.show_projectile_2 = False
        app.b2_p_cd = False
    if app.projectile_1[0][1] <= app.player_pos_hiy and app.projectile_1[0][1] >= app.player_pos_y:
        if collision_detection_enemy_attack(app, app.projectile_1[0]) == True and app.i_frames == 0:
            app.player_health -= 5
            app.i_frames += 5


    if app.projectile_1[1][1] <= app.player_pos_hiy and app.projectile_1[1][1] >= app.player_pos_y:
        if collision_detection_enemy_attack(app, app.projectile_1[1]) == True and app.i_frames == 0:
            app.player_health -= 5
            app.i_frames += 5



def projectile_manager_two(app):
    #manager for soppen som boss tre skyter ut
    if app.projectile_2[0] > -100:
        app.projectile_2[0] -= app.projectile_speed
        app.projectile_2[2] -= app.projectile_speed
    else:
        app.show_projectile_3 = False

    if app.projectile_2[0] <= app.player_pos_hix and app.projectile_2[0] >= app.player_pos_x:
        if collision_detection_enemy_attack(app, app.projectile_2) == True and app.i_frames == 0:
            app.player_invert_controll = 10
            #invert_controll(app)
            app.player_health -= 5
            app.i_frames += 5

