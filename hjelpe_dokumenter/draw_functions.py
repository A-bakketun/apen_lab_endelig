
#vet ikke hvor ellers jeg skal putte denne
def define_colors(app):
    #definerer farger
    app.background_color = "ivory"
    app.button_color = "bisque"
    app.boss_color = "green"


def draw_main_menu_buttons(app, button , canvas):
    #Tegner buttonsene
    x1, y1, x2, y2 , label = button
    mid_x = (x1 + x2)/2
    mid_y = (y1 + y2)/2
    canvas.create_image(mid_x, mid_y, 
                        pil_image=app.rebind_frame)
    canvas.create_text(mid_x , mid_y,
                       text=label,
                       font="times 20",
                       fill="azure")
    
def draw_map_buttons(app, button , canvas):
    #tegner buttonsene til map
    x1, y1, x2, y2 , label = button
    mid_x = (x1 + x2)/2
    mid_y = (y1 + y2)/2
    canvas.create_image(mid_x, mid_y,
                            pil_image=app.map_frame)
    canvas.create_text(mid_x, mid_y,
                       text=label,
                       font="times 20",
                       fill="orange")
def draw_setting_buttons(app, button , canvas):
    #tegner settings buttons
    x1, y1, x2, y2 , label = button
    mid_x = (x1 + x2)/2
    mid_y = (y1 + y2)/2
    canvas.create_image(mid_x, mid_y,
                        pil_image=app.map_frame)
    canvas.create_text(mid_x, mid_y,
                       text=label,
                       font="times 20",
                       fill="orange")
def draw_difficulty_buttons(app, button, canvas):
    #tegner difficulty buttons
    x1, y1, x2, y2 , label = button
    mid_x = (x1 + x2)/2
    mid_y = (y1 + y2)/2
    canvas.create_image(mid_x, mid_y, 
                            pil_image=app.difficulty_frame)
    canvas.create_text(mid_x-1, mid_y-1,
                       text=label,
                       font="times 25",
                       fill="orange")
    canvas.create_text(mid_x, mid_y,
                       text=label,
                       font="times 25",
                       fill="wheat")

def draw_rebind_buttons(app, button, canvas):
    #tegner rebind knappene
    x1, y1, x2, y2 , label = button
    mid_x = (x1 + x2)/2
    mid_y = (y1 + y2)/2
    canvas.create_image(mid_x, mid_y, 
                            pil_image=app.rebind_frame)
    canvas.create_text(mid_x, mid_y,
                       text=label,
                       font="times 25")

#tegner selector for diverse menyer
def draw_main_menu_selector(app, canvas):
    #tegner main menu selectoren
    canvas.create_rectangle(120 , 120 + (app.menu_selector * 220), 
                            280 , 280 + (app.menu_selector * 220),
                            fill="", 
                            outline="white", width=5)
    
def draw_map_selector(app, canvas):
    #tegner velgeren i map
    canvas.create_rectangle(100 +(app.menu_selector_x * 350),100 + (app.menu_selector) * 350, 
                            400 +(app.menu_selector_x * 350), 400 + (app.menu_selector *350),
                            fill="", outline="white",width=5)

def draw_settings_selector(app, canvas):
    #tegner velgeren i settings
    canvas.create_rectangle(100 +(app.menu_selector_x * 400), 100 + (app.menu_selector * 350), 
                            400 +(app.menu_selector_x * 400), 400 + (app.menu_selector *350),
                            fill="", outline="white",width=5)

def draw_difficulty_selector(app, canvas):
    #tegner velgeren i difficulty menyen
    canvas.create_rectangle(100 + (app.menu_selector * 250), 300  , 
                            300 + (app.menu_selector *250) , 500 ,
                            fill="", outline="white",width=5)
    if app.profile["unlocks"]["difficulty_baby"] == False:
        canvas.create_image(450, 400, pil_image=app.locked_icon)
    if app.profile["unlocks"]["difficulty_easy"] == False:
        canvas.create_image(700, 400, pil_image=app.locked_icon)

def draw_rebind_selector(app, canvas):
    canvas.create_rectangle(100 + (app.menu_selector_x * 250), 70 + (app.menu_selector * 200)  , 
                            300 + (app.menu_selector_x *250) , 260 + (app.menu_selector*200) ,
                            fill="", outline="brown",width=5)  

def draw_main_menu(app, canvas):
    #tegner hoved menyen
    if app.profile["unlocks"]["difficulty_hard"] == True:
        canvas.create_image(450, 450 , pil_image=app.main_menu_bg2)
    else:
        canvas.create_image(450, 450 , pil_image=app.main_menu_bg)
    canvas.create_text(652, 400, text="Story\n  of\nAlfred",
                       font="times 40",
                       fill="black")
    canvas.create_text(650, 400, text="Story\n  of\nAlfred",
                       font="times 40",
                       fill="ivory")
    canvas.create_text(820, 840, text="Et spill av\nAndreas Bakketun")

def draw_character_advanced(app, canvas):
    #tegner spilleren
    draw_hud_player(app, canvas)
    if app.player_state == "Idle":
        if app.player_direction == "East":
            canvas.create_image(app.player_pos_x + 48, app.player_pos_y+25, pil_image=app.player_idle_animation[app.animation_counter] )
        elif app.player_direction == "West":
            canvas.create_image(app.player_pos_x, app.player_pos_y+25, pil_image=app.player_idle_animation1[app.animation_counter] )
    if app.player_state == "Walking":
        if app.player_direction == "East":
            canvas.create_image(app.player_pos_x + 48, app.player_pos_y + 25, pil_image=app.player_walking_animation[app.animation_counter])
        elif app.player_direction == "West":
            canvas.create_image(app.player_pos_x, app.player_pos_y + 25, pil_image=app.player_walking_animation1[app.animation_counter])
    if app.player_state == "Attack":
        if app.player_direction == "East":
            canvas.create_image(app.player_pos_x + 48 , app.player_pos_y + 25 , pil_image=app.player_attack_animation[app.animation_counter])
        elif app.player_direction == "West":
            canvas.create_image(app.player_pos_x, app.player_pos_y + 25 , pil_image=app.player_attack_animation1[app.animation_counter])
    if app.i_frames > 0:
        if app.player_direction == "East":
            canvas.create_image(app.player_pos_x + 48, app.player_pos_y+25, pil_image=app.player_iframes)
        elif app.player_direction == "West":
            canvas.create_image(app.player_pos_x , app.player_pos_y+25, pil_image=app.player_iframesr)
    if app.player_took_damage > 0:
        if app.player_direction == "East":
            canvas.create_image(app.player_pos_x +48, app.player_pos_y +25, pil_image=app.player_damaged_image)
        elif app.player_direction == "West":
            canvas.create_image(app.player_pos_x , app.player_pos_y+25, pil_image=app.player_damaged_imager)
    if app.profile["unlocks"]["difficulty_hard"] == True:
        canvas.create_image(app.player_pos_x+24, app.player_pos_y-14, pil_image=app.player_crown)

def draw_boss_one(app , canvas):
    #tegner boss en
    if app.show_boss_attack > 0 and app.debug == True:
        draw_boss_one_attack(app, canvas)
    if  app.animate_boss_one_attack_one == True and app.enemy_action == "Attack_1":
        if app.enemy_direction == 1:
            canvas.create_image(app.enemy_pos_x-36, app.enemy_pos_y + 24, pil_image=app.boss1_attack1[app.boss_one_attack_one_frame])
        elif app.enemy_direction == -1:
            canvas.create_image(app.enemy_pos_x + 77, app.enemy_pos_y + 24, pil_image=app.boss1_attack1f[app.boss_one_attack_one_frame])
    elif  app.animate_boss_one_attack_one == True and app.enemy_action == "Attack_2":
        if app.enemy_direction == 1:
            canvas.create_image(app.enemy_pos_x-36, app.enemy_pos_y + 24, pil_image=app.boss1_attack2[app.boss_one_attack_one_frame])
        elif app.enemy_direction == -1:
            canvas.create_image(app.enemy_pos_x + 77, app.enemy_pos_y + 24, pil_image=app.boss1_attack2f[app.boss_one_attack_one_frame])

    elif app.animate_boss_one_attack_one == True and app.enemy_action == "Attack_3":
        if app.enemy_direction == 1:
            canvas.create_image(app.enemy_pos_x -36, app.enemy_pos_y + 24,pil_image=app.boss1_attack3[app.boss_one_attack_one_frame])
        elif app.enemy_direction == -1:
            canvas.create_image(app.enemy_pos_x + 77, app.enemy_pos_y + 24,pil_image=app.boss1_attack3f[app.boss_one_attack_one_frame])
    else:
        if app.enemy_direction == 1:
            canvas.create_image(app.enemy_pos_x +12, app.enemy_pos_y +24, pil_image=app.boss_one_idle[0])
        elif app.enemy_direction == -1:
            canvas.create_image(app.enemy_pos_x + 30 , app.enemy_pos_y +24, pil_image=app.boss_one_idle1[0])
    if app.enemy_i_frames > 0:
        if app.enemy_direction == 1:
            canvas.create_image(app.enemy_pos_x+ 12, app.enemy_pos_y + 24, pil_image=app.boss1_hit)
        elif app.enemy_direction == -1: 
            canvas.create_image(app.enemy_pos_x +14, app.enemy_pos_y + 24, pil_image=app.boss1_hit)

def draw_boss_two(app, canvas):
    #tegner boss to
    if app.debug == True:
        canvas.create_rectangle(app.enemy_pos_x, app.enemy_pos_y,
                                app.enemy_pos_hix, app.enemy_pos_hiy,
                                fill="green")
    canvas.create_image(app.enemy_pos_x-12, app.enemy_pos_y + 24, pil_image=app.boss_two_idle[app.b2_animation_f])
    if app.debug == True:
        canvas.create_text(app.enemy_pos_x, app.enemy_pos_y - 300,
                       text=app.enemy_health)
    if app.boss_two_show_attack_one == True:
        canvas.create_image(app.enemy_attack_x1 + 44, app.enemy_attack_y1 +1, pil_image=app.b2_a1_i[app.boss_two_attack_one_frame])
    if app.boss_two_show_attack_three == True:
        canvas.create_image(app.enemy_attack_x1 + 44, app.enemy_attack_y1 +1, pil_image=app.b2_a3_i[app.boss_two_attack_three_frame])
         
def draw_boss_three(app, canvas):
    #tegner boss tre
    canvas.create_image(((app.enemy_pos_x + app.enemy_pos_hix)/2)-2, app.enemy_pos_y+12, pil_image=app.boss_three_image)
    if app.debug == True:
        canvas.create_rectangle(app.enemy_pos_x, app.enemy_pos_y,
                                app.enemy_pos_hix, app.enemy_pos_hiy,
                                fill="black")
    if app.show_b3_a2 == True:
        if app.enemy_direction == 1:
            canvas.create_image(app.enemy_pos_x - 48, app.enemy_pos_y +30, pil_image=app.b3_a2[app.b3_a2_f])
        elif app.enemy_direction == -1:
            canvas.create_image(app.enemy_pos_x + 48, app.enemy_pos_y +30, pil_image=app.b3_a2f[app.b3_a2_f])
    if app.show_b3_a3 == True:
        canvas.create_image(app.enemy_attack_x1 + 48, app.enemy_attack_y1+20, pil_image=app.b3_a3[app.b3_a3_f])
    if app.enemy_i_frames > 0:
        canvas.create_image(((app.enemy_pos_x + app.enemy_pos_hix)/2)-2, app.enemy_pos_y + 15, pil_image=app.b3_hit)

def draw_boss_three_projectiles(app, canvas):
    #tegner prosjektil til boss tre
    canvas.create_image(app.projectile_2[0] +12, app.projectile_2[1], pil_image=app.boss_three_attack_one)

def draw_boss_final(app, canvas):
    #tegner siste boss
    if app.enemy_action == "Idle":    
        if app.enemy_direction == 1:
            canvas.create_image(app.enemy_pos_x+ 10, app.enemy_pos_y + 24, pil_image=app.b4_i[app.b4_animation_f])
        elif app.enemy_direction == -1:
            canvas.create_image(app.enemy_pos_x+ 30, app.enemy_pos_y + 24, pil_image=app.b4_i_f[app.b4_animation_f])
    elif app.enemy_action == "Walk_West":
        if app.enemy_direction == 1:
            canvas.create_image(app.enemy_pos_x+10, app.enemy_pos_y + 24, pil_image=app.b4_w[app.b4_animation_f])
        elif app.enemy_direction == -1:
            canvas.create_image(app.enemy_pos_x+30, app.enemy_pos_y + 24, pil_image=app.b4_w_f[app.b4_animation_f])
    elif app.enemy_action == "Walk_East":
        if app.enemy_direction == 1:
            canvas.create_image(app.enemy_pos_x+10, app.enemy_pos_y + 24, pil_image=app.b4_w_f[app.b4_animation_f])
        elif app.enemy_direction == -1:
            canvas.create_image(app.enemy_pos_x+30, app.enemy_pos_y + 24, pil_image=app.b4_w[app.b4_animation_f])
    elif app.enemy_action == "Attack_1":
        if app.enemy_direction == 1:
            canvas.create_image(app.enemy_pos_x+10, app.enemy_pos_y + 24, pil_image=app.b4_a1[app.b4_a1_frame])
        elif app.enemy_direction == -1:
            canvas.create_image(app.enemy_pos_x+30, app.enemy_pos_y + 24, pil_image=app.b4_a1_f[app.b4_a1_frame])
    elif app.enemy_action == "Attack_2":
        if app.enemy_direction == 1:
            canvas.create_image(app.enemy_pos_x+10, app.enemy_pos_y + 24, pil_image=app.b4_a2[app.boss_final_attack_two_frame])
        elif app.enemy_direction == -1:
            canvas.create_image(app.enemy_pos_x+30, app.enemy_pos_y + 24, pil_image=app.b4_a2_f[app.boss_final_attack_two_frame])

    if app.show_zone_attack == True:
        canvas.create_image(app.zone_attack_one[0][0]+ 24,app.zone_attack_one[0][1]+30,pil_image=app.b4_a3[app.final_attack_aframe])
        canvas.create_image(app.zone_attack_one[1][0]+ 24,app.zone_attack_one[1][1]+30,pil_image=app.b4_a3[app.final_attack_aframe])
        canvas.create_image(app.zone_attack_one[2][0]+ 24,app.zone_attack_one[2][1]+30,pil_image=app.b4_a3[app.final_attack_aframe])

    if app.enemy_i_frames > 0:
        if app.enemy_direction == 1:
            canvas.create_image(app.enemy_pos_x +10, app.enemy_pos_y + 24, pil_image=app.b4_taken_dmg)
        elif app.enemy_direction == -1:
            canvas.create_image(app.enemy_pos_x +30, app.enemy_pos_y + 24, pil_image=app.b4_taken_dmgf)
###hjelper tegninger for debug
def draw_basic_attack(app, canvas):
    canvas.create_rectangle(app.attack_hitbox[0], app.attack_hitbox[1],
                            app.attack_hitbox[2], app.attack_hitbox[3],
                            fill="blue")

def draw_boss_one_hitbox(app, canvas):
    canvas.create_rectangle(app.enemy_pos_x, app.enemy_pos_y,
                          app.enemy_pos_hix, app.enemy_pos_hiy,
                          fill=app.boss_color) 

def draw_boss_one_healthbar(app, canvas):
    canvas.create_text(app.enemy_pos_x, app.enemy_pos_y -300,
                       text=app.enemy_health)
    
def draw_boss_one_attack(app, canvas):
    canvas.create_rectangle(app.enemy_attack_x1, app.enemy_attack_y1,
                            app.enemy_attack_x2, app.enemy_attack_y2,
                            fill="blue")
def draw_boss_two_attack(app, canvas):
    canvas.create_rectangle(app.enemy_attack_x1, app.enemy_attack_y1,
                            app.enemy_attack_x2, app.enemy_attack_y2,
                            fill="blue")
    
def draw_death_screen(app, canvas):
    #tegner death screen
    draw_backgrounds(app, canvas)
    canvas.create_image(450, 450, pil_image=app.map_frame)
    if app.player_lives > 0:
        canvas.create_text(450 , 450 , 
                       text="You died\r press r to restart",
                       font="times, 28",
                       fill="orange")
    elif app.player_lives == 0:
        canvas.create_text(450 , 450 ,
                        text="You lost\r press r for menu",
                        font="times, 28",
                        fill="orange")
def draw_hud_player(app, canvas):
    canvas.create_image(200, 750, pil_image=app.healthbar)
    canvas.create_text(200, 750,
                       text=app.player_health,
                       font="times 20",
                       fill="white")
    for i in range(app.player_lives):
        canvas.create_image(160 + (i * 36), 800, pil_image=app.player_icon)

def draw_character_hitbox(app, canvas):
    canvas.create_rectangle(app.player_pos_x, app.player_pos_y ,
                       app.player_pos_hix, app.player_pos_hiy,
                       fill=app.player_color)
    
#tegner bakgrunner
def draw_backgrounds(app, canvas):
    if app.boss_fight == "One":
        canvas.create_rectangle(0 , 700 , 900 , 900,
                            fill="lightgreen")
        canvas.create_image(450 , 250, pil_image=app.boss_one_bg)
    elif app.boss_fight == "Two":
        canvas.create_rectangle(0 , 700 , 900 , 900,
                            fill="pale violet red")
        canvas.create_image(450 , 250, pil_image=app.boss_two_bg)
    elif app.boss_fight == "Three":
        canvas.create_rectangle(0 , 700 , 900 , 900,
                                fill="lightgreen")
        canvas.create_image(450, 250, pil_image=app.boss_three_bg)
    elif app.boss_fight == "Final":
        canvas.create_image(450, 250, pil_image=app.boss_final_bg)
        canvas.create_rectangle(0, 700, 900 , 900,
                                fill="black")


def draw_binding_key_pop_up(app, canvas):
    canvas.create_rectangle(300 , 300, 600 , 600,
                            fill=app.button_color)
    canvas.create_text(450, 450, 
                       text=f"You are binding{app.action_to_bind}\n press new key\n time left: {round(app.bind_timer / 10)}")

def draw_continue_boss_one(app, canvas):
    canvas.create_image(450, 250, pil_image=app.boss_one_bg)
    canvas.create_image(450, 450, pil_image=app.continue_frame)
    canvas.create_text(450, 450, text=f"Borg is dead\rpress {app.enter_bind} to continue",
                       font="times 20")
def draw_continue_boss_two(app, canvas):
    canvas.create_image(450 , 250, pil_image=app.boss_two_bg)
    canvas.create_image(450, 450, pil_image=app.continue_frame)
    canvas.create_text(450, 450, text=f"Berg is dead\rpress {app.enter_bind} to continue",
                       font="times 20")
def draw_continue_boss_three(app, canvas):
    canvas.create_image(450, 250, pil_image=app.boss_three_bg)
    canvas.create_image(450, 450, pil_image=app.continue_frame)
    canvas.create_text(450, 450, text=f"Bjorn is dead\rpress {app.enter_bind} to continue",
                       font="times 20")
def draw_victory_screen(app, canvas):
    canvas.create_image(450 , 450 , pil_image=app.victory_animation[app.victory_animation_frames])
    canvas.create_text( 450, 750,
                       text=f"You won on {app.diff}.\n{app.victory_text}\nPress esc to return",
                       font= "times 20")

def draw_map(app, canvas):
    for button in app.map_buttons:
        draw_map_buttons(app, button , canvas)
    if app.profile["unlocks"]["defeated_boss_one"] == False:
        canvas.create_image(250, 250, pil_image = app.locked_icon)
    if app.profile["unlocks"]["defeated_boss_two"] == False:
        canvas.create_image(250, 600, pil_image = app.locked_icon)
    if app.profile["unlocks"]["defeated_boss_three"] == False:
        canvas.create_image(600, 250, pil_image = app.locked_icon)
    if app.profile["unlocks"]["defeated_boss_final"] == False:
        canvas.create_image(600, 600, pil_image = app.locked_icon)



def draw_credits(app, canvas):
    canvas.create_text(app.credits_cords_x, app.credits_cords_y,
                       text=app.credits,
                       font="times 20")