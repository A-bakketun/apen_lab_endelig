from uib_inf100_graphics.event_app import run_app
from uib_inf100_graphics.helpers import load_image, scaled_image
from PIL import Image

def image_handler(app):
    #kjører alle bilde funksjonene
    create_player_animations(app)
    create_backgrounds(app)
    create_boss_one_animations(app)
    create_boss_two_animations(app)
    create_boss_3_animations(app)
    create_final_boss_animations(app)
    create_hud_images(app)

def create_player_animations(app):
    #lager animasjonene
    #### idle animation
    image = load_image("Story_of_Alfred/Sprite_assets/player/idle1.png")
    image1 = scaled_image(image, 2)
    image = load_image("Story_of_Alfred/Sprite_assets/player/idle2.png")
    image2 = scaled_image(image, 2)
    app.player_idle_animation = [image1 , image2, image1, image2]
    rimage1 = image1.transpose(Image.FLIP_LEFT_RIGHT)
    rimage2 = image2.transpose(Image.FLIP_LEFT_RIGHT)
    app.player_idle_animation1 = [rimage1, rimage2 , rimage1, rimage2]
    #attack animation
    image = load_image("Story_of_Alfred/Sprite_assets/player/player_attack1.png")
    image1 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/player/player_attack2.png")
    image2 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/player/player_attack3.png")
    image3 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/player/player_attack4.png")
    image4 = scaled_image(image , 2)
    app.player_attack_animation = [image4 , image3, image2, image1]
    rimage1 = image1.transpose(Image.FLIP_LEFT_RIGHT)
    rimage2 = image2.transpose(Image.FLIP_LEFT_RIGHT)
    rimage3 = image3.transpose(Image.FLIP_LEFT_RIGHT)
    rimage4 = image4.transpose(Image.FLIP_LEFT_RIGHT)
    app.player_attack_animation1 = [rimage4, rimage3, rimage2, rimage1]

    ### walking animation
    image = load_image("Story_of_Alfred/Sprite_assets/player/walking1.png")
    image1 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/player/walking2.png")
    image2 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/player/walking3.png")
    image3 = scaled_image(image , 2)

    rimage1 = image1.transpose(Image.FLIP_LEFT_RIGHT)
    rimage2 = image2.transpose(Image.FLIP_LEFT_RIGHT)
    rimage3 = image3.transpose(Image.FLIP_LEFT_RIGHT)
    
    app.player_walking_animation = [image1 , image2 , image3, image2]
    app.player_walking_animation1 = [rimage1, rimage2, rimage3, rimage2]
    image = load_image("Story_of_Alfred/Sprite_assets/player/iframe.png")
    image1 = scaled_image(image , 2)
    image2 = image1.transpose(Image.FLIP_LEFT_RIGHT)
    app.player_iframes = image1
    app.player_iframesr = image2
    #om tatt damage, viser en rød versjon av player sprite
    image = load_image("Story_of_Alfred/Sprite_assets/player/player_damaged.png")
    image1 = scaled_image(image , 2)
    image2 = image1.transpose(Image.FLIP_LEFT_RIGHT)
    app.player_damaged_image = image1
    app.player_damaged_imager = image2
    image1 = load_image("Story_of_Alfred/Sprite_assets/player/crown.png")
    app.player_crown = image1
def create_boss_one_animations(app):
    #lager animasjoner for boss one
    image = load_image("Story_of_Alfred/Sprite_assets/Boss_1.png")
    image1 = scaled_image(image, 2)
    rimage1 = image1.transpose(Image.FLIP_LEFT_RIGHT)
    app.boss_one_idle = [image1]
    app.boss_one_idle1 = [rimage1]

    image = load_image("Story_of_Alfred/Sprite_assets/Boss_1_charge.png")
    image1 = scaled_image(image , 2)
    rimage1 = image1.transpose(Image.FLIP_LEFT_RIGHT)
    app.boss_one_charge = [image1]
    app.boss_one_charge1 = [rimage1]


    image = load_image("Story_of_Alfred/Sprite_assets/b1_a1/0.png")
    image1 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b1_a1/1.png")
    image2 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b1_a1/2.png")
    image3 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b1_a1/3.png")
    image4 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b1_a1/4.png")
    app.boss1_attack1 = [image1, image2, image3, image4]

    rimage1 = image1.transpose(Image.FLIP_LEFT_RIGHT)
    rimage2 = image2.transpose(Image.FLIP_LEFT_RIGHT)
    rimage3 = image3.transpose(Image.FLIP_LEFT_RIGHT)
    rimage4 = image4.transpose(Image.FLIP_LEFT_RIGHT)
    app.boss1_attack1f = [rimage1, rimage2, rimage3, rimage4]
    image1 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b1_a1/5.png")
    image2 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b1_a1/6.png")
    image3 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b1_a1/7.png")
    image4 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b1_a1/8.png")
    image5 = scaled_image(image , 2)
    app.boss1_attack2 = [image1, image2, image3, image4,image5]
    rimage1 = image1.transpose(Image.FLIP_LEFT_RIGHT)
    rimage2 = image2.transpose(Image.FLIP_LEFT_RIGHT)
    rimage3 = image3.transpose(Image.FLIP_LEFT_RIGHT)
    rimage4 = image4.transpose(Image.FLIP_LEFT_RIGHT)
    rimage5 = image5.transpose(Image.FLIP_LEFT_RIGHT)
    app.boss1_attack2f = [rimage1, rimage2, rimage3, rimage4, rimage5]
    image = load_image("Story_of_Alfred/Sprite_assets/b1_a3/1.png")
    image1 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b1_a3/2.png")
    image2 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b1_a3/3.png")
    image3 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b1_a3/4.png")
    image4 = scaled_image(image , 2)
    app.boss1_attack3 = [image1, image2, image3, image4]
    rimage1 = image1.transpose(Image.FLIP_LEFT_RIGHT)
    rimage2 = image2.transpose(Image.FLIP_LEFT_RIGHT)
    rimage3 = image3.transpose(Image.FLIP_LEFT_RIGHT)
    rimage4 = image4.transpose(Image.FLIP_LEFT_RIGHT)
    app.boss1_attack3f = [rimage1, rimage2, rimage3, rimage4]
    image = load_image("Story_of_Alfred/Sprite_assets/b1_i.png")
    image1 = scaled_image(image , 2)
    app.boss1_hit = image1

def create_boss_two_animations(app): 
    #lager animasjoner for boss to
    image = load_image("Story_of_Alfred/Sprite_assets/b2_i/0.png")
    image1 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b2_i/1.png")
    image2 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b2_i/2.png")
    image3 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b2_i/3.png")
    image4 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b2_i/4.png")
    image5 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b2_i/5.png")
    image6 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b2_i/6.png")
    image7 = scaled_image(image , 2)
    #idle animasjonen til boss two
    app.boss_two_idle = [image1, image2,image3, image4, image5, image6, image7]
    # de følgende har litt fæle navn
    image = load_image("Story_of_Alfred/Sprite_assets/b2_a1_0.png")
    image1 = scaled_image(image, 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b2_a1_1.png")
    image2 = scaled_image(image , 2)
    #angrep en, stage en og to
    app.b2_a1_i = [image1, image2]
    image = load_image("Story_of_Alfred/Sprite_assets/b2_p1.png")
    image1 = scaled_image( image , 2)
    #prosjektil 
    app.b2_p1_i = image1
    image = load_image("Story_of_Alfred/Sprite_assets/b2_a3_0.png")
    image1 = scaled_image(image, 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b2_a3_1.png")
    image2 = scaled_image(image , 2)
    #angrep tre, stage en og to
    app.b2_a3_i = [image1, image2]

def create_boss_3_animations(app):
    #lager animasjon boss 3
    image = load_image("Story_of_Alfred/Sprite_assets/b3.png")
    image1 = scaled_image(image , 2)
    #bossen står bare i ro så er en frame
    app.boss_three_image = image1
    image = load_image("Story_of_Alfred/Sprite_assets/b3_a1.png")
    image1 = scaled_image(image , 2)
    #tegner soppen han skyter ut, eller angrep en da
    app.boss_three_attack_one = image1
    image = load_image("Story_of_Alfred/Sprite_assets/b3_i.png")
    image1 = scaled_image(image , 2.2)
    #lager en annen farge på bossen når han blir hittet
    app.b3_hit = image1
    image = load_image("Story_of_Alfred/Sprite_assets/b3_a2/b3_a2_0.png")
    image1 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b3_a2/b3_a2_1.png")
    image2 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b3_a2/b3_a2_2.png")
    image3 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b3_a2/b3_a2_3.png")
    image4 = scaled_image(image , 2)
    #lager animasjonen til angrep to
    app.b3_a2 = [image1, image2, image3, image4]
    rimage1 = image1.transpose(Image.FLIP_LEFT_RIGHT)
    rimage2 = image2.transpose(Image.FLIP_LEFT_RIGHT)
    rimage3 = image3.transpose(Image.FLIP_LEFT_RIGHT)
    rimage4 = image4.transpose(Image.FLIP_LEFT_RIGHT)
    #lager en flippet versjon av angrep to
    app.b3_a2f = [rimage1, rimage2, rimage3, rimage4]
    image = load_image("Story_of_Alfred/Sprite_assets/b3_a3_0.png")
    image1 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b3_a3_1.png")
    image2 = scaled_image(image , 2)
    #lager angrep tre
    app.b3_a3 = [image1, image2]


def create_final_boss_animations(app):
    #lager animasjoner til final bossen
    image = load_image("Story_of_Alfred/Sprite_assets/b4_i/0.png")
    image1 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b4_i/1.png")
    image2 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b4_i/2.png")
    image3 = scaled_image(image , 2)
    rimage1 = image1.transpose(Image.FLIP_LEFT_RIGHT)
    rimage2 = image2.transpose(Image.FLIP_LEFT_RIGHT)
    rimage3 = image3.transpose(Image.FLIP_LEFT_RIGHT)
    #idel frames, vanlig og flippet
    app.b4_i = [image1, image2, image3]
    app.b4_i_f = [rimage1, rimage2, rimage3]

    image = load_image("Story_of_Alfred/Sprite_assets/b4_w/0.png")
    image1 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b4_w/1.png")
    image2 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b4_w/2.png")
    image3 = scaled_image(image , 2)
    rimage1 = image1.transpose(Image.FLIP_LEFT_RIGHT)
    rimage2 = image2.transpose(Image.FLIP_LEFT_RIGHT)
    rimage3 = image3.transpose(Image.FLIP_LEFT_RIGHT)
    #gå animasjon, vanlig og flippet
    app.b4_w = [image1, image2, image3]
    app.b4_w_f = [rimage1, rimage2, rimage3]

    image = load_image("Story_of_Alfred/Sprite_assets/b4_a1/0.png")
    image1 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b4_a1/1.png")
    image2 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b4_a1/2.png")
    image3 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b4_a1/3.png")
    image4 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b4_a1/4.png")
    image5 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b4_a1/5.png")
    image6 = scaled_image(image , 2)
    rimage1 = image1.transpose(Image.FLIP_LEFT_RIGHT)
    rimage2 = image2.transpose(Image.FLIP_LEFT_RIGHT)
    rimage3 = image3.transpose(Image.FLIP_LEFT_RIGHT)
    rimage4 = image4.transpose(Image.FLIP_LEFT_RIGHT)
    rimage5 = image5.transpose(Image.FLIP_LEFT_RIGHT)
    rimage6 = image6.transpose(Image.FLIP_LEFT_RIGHT)
    #angrep en animasjon, vanlig og flippet
    app.b4_a1 = [image1, image2, image3, image4, image5, image6]
    app.b4_a1_f =[rimage1, rimage2, rimage3, rimage4, rimage5, rimage6]
    image = load_image("Story_of_Alfred/Sprite_assets/b4_a2/0.png")
    image1 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b4_a2/1.png")
    image2 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b4_a2/2.png")
    image3 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b4_a2/3.png")
    image4 = scaled_image(image , 2)
    rimage1 = image1.transpose(Image.FLIP_LEFT_RIGHT)
    rimage2 = image2.transpose(Image.FLIP_LEFT_RIGHT)
    rimage3 = image3.transpose(Image.FLIP_LEFT_RIGHT)
    rimage4 = image4.transpose(Image.FLIP_LEFT_RIGHT)
    #angrep to vanlig og flippet
    app.b4_a2 = [image1, image2, image3, image4]
    app.b4_a2_f = [rimage1, rimage2, rimage3, rimage4]

    image = load_image("Story_of_Alfred/Sprite_assets/b4_a3/0.png")
    image1 = scaled_image(image , 2)
    image = load_image("Story_of_Alfred/Sprite_assets/b4_a3/1.png")
    image2 = scaled_image(image , 2)
    #angrep tre, begge fasene
    app.b4_a3 = [image1, image2]

    image = load_image("Story_of_Alfred/Sprite_assets/final_boss_taken_dmg.png")
    image1 = scaled_image(image, 2)
    rimage1 = image1.transpose(Image.FLIP_LEFT_RIGHT)
    #om boss har tatt damage, vanlig og flippet
    app.b4_taken_dmg = image1
    app.b4_taken_dmgf = rimage1

def create_backgrounds(app):
    #lager bakgrunnene
    image = load_image("Story_of_Alfred/Sprite_assets/backgrounds/bg_main.png")
    image1 = scaled_image(image, 10)
    app.main_menu_bg = image1
    image = load_image("Story_of_Alfred/Sprite_assets/backgrounds/bg_main2.png")
    image1 = scaled_image(image , 10)
    app.main_menu_bg2 = image1
    image = load_image("Story_of_Alfred/Sprite_assets/backgrounds/bg_b1.png")
    image1 = scaled_image(image , 2)
    app.boss_one_bg = image1
    image = load_image("Story_of_Alfred/Sprite_assets/backgrounds/bg_b2.png")
    image1 = scaled_image(image, 2)
    app.boss_two_bg = image1
    image = load_image("Story_of_Alfred/Sprite_assets/backgrounds/bg_b3.png")
    image1 = scaled_image(image , 2)
    app.boss_three_bg = image1
    image = load_image("Story_of_Alfred/Sprite_assets/backgrounds/bg_b4.png")
    image1 = scaled_image(image , 2)
    app.boss_final_bg = image1

    image = load_image("Story_of_Alfred/Sprite_assets/victory_animation/0.png")
    image1 = scaled_image(image, 14)
    image = load_image("Story_of_Alfred/Sprite_assets/victory_animation/1.png")
    image2 = scaled_image(image, 14)
    image = load_image("Story_of_Alfred/Sprite_assets/victory_animation/2.png")
    image3 = scaled_image(image, 14)
    #lager seiers animasjonen
    app.victory_animation = [image1, image2, image3]

def create_hud_images(app):
    #lager hud bilder, og litt andre små ting som rammer og den slags
    image = load_image("Story_of_Alfred/Sprite_assets/HUD/Frame_1.png")
    image1 = scaled_image(image , 2)
    app.healthbar = image1
    image = load_image("Story_of_Alfred/Sprite_assets/HUD/icon.png")
    image1 = scaled_image(image , 4)
    app.player_icon = image1
    image = load_image("Story_of_Alfred/Sprite_assets/HUD/locked_icon.png")
    image1 = scaled_image(image , 8)
    app.locked_icon = image1
    #lager frames
    image = load_image("Story_of_Alfred/Sprite_assets/HUD/continue_frame.png")
    image1 = scaled_image(image , 14)
    app.continue_frame = image1
    image = load_image("Story_of_Alfred/Sprite_assets/HUD/difficulty_frame.png")
    image1 = scaled_image (image , 10)
    app.difficulty_frame = image1
    image = load_image("Story_of_Alfred/Sprite_assets/HUD/map_frame.png")
    image1 = scaled_image (image , 14)
    app.map_frame = image1
    image = load_image("Story_of_Alfred/Sprite_assets/HUD/rebind_frame.png")
    image1 = scaled_image (image , 8)
    app.rebind_frame = image1
