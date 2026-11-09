
#######################################
####     action calc        #############
#########################################

def boss_one_action_calc(app):
    import random
    #hvis han er langt unna beveger han seg nærmere
    if app.enemy_pos_x >= app.player_pos_x + 80:
            app.enemy_action = "Walk_West"
    elif app.enemy_pos_x <= app.player_pos_x - 80:
            app.enemy_action = "Walk_East"
            
    #velger angrep om han er nærme
    elif random.randrange(5) == 3:
        app.enemy_action = "Attack_3"
    else:
        app.enemy_action = "Attack_1"

def boss_two_action_calc(app):
    import random
    #velger angrep 
    attack_prompt = random.randrange(2)
    #utfører angrep 
    if attack_prompt == 0 and app.enemy_action == "Idle":
            app.enemy_action = "Attack_1"
            
    elif attack_prompt == 1 and app.enemy_projectile_cd == 0 and app.enemy_action == "Idle" and app.boss_two_projectile_cd == False:
            app.enemy_action = "Attack_2"

    if attack_prompt == 1 and app.enemy_action == "Idle":
            app.enemy_action = "Attack_3"

def boss_three_action_calc(app):
    #hvis player er nærme nok, utfører knockback angrep
    if app.player_pos_hix > app.enemy_pos_x - 150 and app.player_pos_x < app.enemy_pos_hix + 120 and app.boss_three_spam_protection < 2:
        app.enemy_action = "Attack_2"
        app.boss_three_spam_protection += 1

    elif app.show_projectile_3 == False and app.player_pos_x < app.enemy_pos_hix:
        app.enemy_action = "Attack_1"
    else:
        app.enemy_action = "Attack_3"
        app.boss_three_spam_protection = 0

def boss_final_action_calc(app):
    import random
    #velger angrep
    r = random.randrange(11)
    #beveger seg om han er langt vekke
    if app.enemy_pos_x >= app.player_pos_x + 60:
            app.enemy_action = "Walk_West"
    elif app.enemy_pos_x <= app.player_pos_x - 60:
            app.enemy_action = "Walk_East" 
    #hvis han er nærme nok, angriper han med valgt angrep
    elif r % 2== 0:
        app.enemy_action = "Attack_1"
    else:
        app.enemy_action = "Attack_2"




