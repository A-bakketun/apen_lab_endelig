#denne heter character one fordi jeg var ambisiøs og vil ikke fjerne det om jeg skulle legge til flere senere
def init_playable_character_one(app):
    # initer playable_character fra en clean save
    app.player_direction = "East"
    app.player_state = "Idle"
    app.player_moving = False
    app.player_health = 100
    app.player_pos_x = 300 -48
    app.player_pos_y = 380
    app.player_pos_hix = 300
    app.player_pos_hiy = 424 
    app.player_took_damage = 0
    app.dash_timer = 0
    app.dodge_timer = 0
    app.player_facing = 1
    app.show_basic_attack = 0
    app.basic_attack_cooldown = 0
    app.animation_counter = 0
    app.do_animation = 0
    app.attack_hitbox = []
    app.idle_counter = 0
    app.i_frames = 0
    app.attack_stops_movement = 0
    app.input_delay = 0
    app.player_speed = 10
    app.player_damage = 50
    app.dodge_cd = 24
    app.attack_cd = 10
    app.attack_stop_movement_duration = 12
    app.input_delay = 0
    #debug verdi
    app.player_color = "red"
    app.player_dash_distance = 40

def soft_init_player(app):
    # initer playable character fra forrige boss (for å ikke heale den)
    app.player_direction = "East"
    app.player_state = "Idle"
    app.player_pos_x = 300 -48
    app.player_pos_y = 380
    app.player_pos_hix = 300
    app.player_pos_hiy = 424 
    app.player_took_damage = 0
    app.player_facing = 1
    app.show_basic_attack = 0
    app.basic_attack_cooldown = 0
    app.animation_counter = 0
    app.do_animation = 0
    app.idle_counter = 0
    app.input_delay = 0
    app.player_moving = False

def init_boss_1(app):
    #initer boss 1
    import hjelpe_dokumenter.uib_inf100_music as music
    music.stop_all_sounds()
    app.boss_fight = "One"
    app.boss_stage = ""
    app.enemy_action = "Idle"
    app.game_state = "Running"
    app.enemy_direction = 1
    app.enemy_health = 700
    app.enemy_pos_x = 700
    app.enemy_pos_hix = 740
    app.enemy_pos_y = 380
    app.enemy_pos_hiy = 440
    app.music_boss_one.play()
    app.animate_boss_one_attack_one = False
    app.boss_one_attack_one_frame = 0
    app.animation_tick = 0
    app.stagger = False
    app.enemy_i_frames = 0
    app.player_facing = 1
    app.boss_stagger = 0
    app.enemy_cd = 10
    app.enemy_hit = 0
    app.enemy_attack_x = 0
    app.enemy_attack_y = 0
    app.show_boss_attack = 0
    app.enemy_speed = 20

def init_boss_2(app):
    #initer boss 2
    import hjelpe_dokumenter.uib_inf100_music as music
    music.stop_all_sounds()
    app.enemy_direction = 1
    app.boss_two_show_attack_one = False
    app.boss_two_show_attack_three = False
    app.boss_fight = "Two"
    app.boss_stage = "One"
    app.enemy_action = "Attack_2"
    app.enemy_health = 600
    app.enemy_pos_x = 720
    app.enemy_pos_hix = 736
    app.enemy_pos_y = 380
    app.enemy_pos_hiy = 440
    app.enemy_cd = 70
    app.game_state = "Running"
    app.stop_show_boss_two_attack_one = 0
    app.stop_showing_b2_a3 = 0
    app.enemy_tp_cd = 0
    app.boss_two_teleport = False
    app.boss_two_projectile_cd = False
    app.b2_animation_f = 0
    app.animation_tick = 0
    app.b2_animation = 0
    app.enemy_i_frames = 0
    app.projectile_speed = 10
    app.boss_stagger = 0
    app.enemy_cd = 0
    app.enemy_hit = 0
    app.enemy_attack_x = 0
    app.enemy_attack_y = 0
    app.show_boss_attack = 10
    app.enemy_projectile_cd = 20
    app.enemy_attack_x1 = 0
    app.enemy_attack_y1 = 0
    app.enemy_attack_x2 = 0
    app.enemy_attack_y2 = 0
    app.music_boss_two.play()
    app.projectile_1 = [[0 , 0 , 0 ,0],
                        [0 , 0 , 0 , 0]
    ]
    app.show_projectile_1 = False
    app.show_projectile_2 = False

def init_boss_3(app):
    #initer boss 3
    import hjelpe_dokumenter.uib_inf100_music as music
    music.stop_all_sounds()
    app.game_state = "Running"
    app.enemy_action = "Idle"
    app.boss_fight = "Three"
    app.boss_stage = ""
    app.projectile_2 = [0 , 0 , 0 , 0]
    app.enemy_health = 700
    app.enemy_pos_x = 700
    app.enemy_pos_hix = 718
    app.enemy_pos_y = 380
    app.enemy_pos_hiy = 440
    app.enemy_i_frames = 0
    app.show_projectile_3 = False
    app.player_invert_controll = 0
    app.show_b3_a2 = False
    app.show_b3_a3 = False
    app.stop_showing_b3_a3 = 0
    app.b3_a2_f = 0 
    app.enemy_direction = 1
    app.music_boss_three.play()
    app.projectile_speed = 20
    app.boss_stagger = 0
    app.enemy_cd = 0
    app.enemy_hit = 0
    app.enemy_attack_x = 0
    app.enemy_attack_y = 0
    app.show_boss_attack = 0
    app.enemy_projectile_cd = 20
    app.boss_three_spam_protection = 0

def init_final_boss(app):
    #initer final boss
    import hjelpe_dokumenter.uib_inf100_music as music
    music.stop_all_sounds()
    app.boss_fight = "Final"
    app.boss_stage = "One"
    app.enemy_health = 1000
    app.enemy_pos_x = 700
    app.enemy_pos_hix = 740
    app.enemy_pos_y = 380
    app.enemy_pos_hiy = 440
    app.game_state = "Running"
    app.enemy_i_frames = 0
    app.enemy_action = "Idle"
    app.enemy_speed = 10
    app.enemy_direction = 1
    app.b4_animation_f = 0
    app.animation_tick = 0
    app.b4_a1_frame = 0
    app.boss_final_attack_two_frame = 0
    app.final_boss_song.play()
    app.b4_a3_done = False
    app.boss_stagger = 0
    app.enemy_cd = 0
    app.enemy_hit = 0
    app.enemy_attack_x = 0
    app.enemy_attack_y = 0
    app.show_boss_attack = 0
    app.show_zone_attack = False
    app.zone_attack_one = [[0 , 0 , 0 , 0],
                           [0 , 0 , 0 , 0],
                           [0 , 0 , 0 , 0],
                           ]
    app.final_attack_aframe = 0
    app.final_attack_timer = 0