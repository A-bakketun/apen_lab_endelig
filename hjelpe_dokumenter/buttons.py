
def button_creator(app):
    #lager buttons for tegning egentlig
    main_menu_buttons(app)
    map_buttons(app)
    settings_buttons(app)
    rebind_buttons(app)

def main_menu_buttons(app):
    #lager main menu buttonsene
    app.main_menu_buttons =[[100 , 100, 300 , 300 , "Start"],
                            [100 , 320 , 300 , 520 , "Settings"],
                            [100 , 540, 300 , 740, "Exit\nwithout save"]
                        ]   
def map_buttons(app):
    #lager map buttonsene
    app.map_buttons = [[100, 100, 400 , 400, "Boss 1"],
                       [100 , 450, 400 , 750, "Boss 2"],
                       [450, 100, 750, 400, "Boss 3"],
                       [450, 450, 750, 750, "Final Boss"]
                    ]
def settings_buttons(app):
    #lager settings buttonsene
    app.settings_buttons = [[100, 100, 400 , 400, "Rebinds"],
                            [100, 450, 400, 750, "Practise"],
                            [500, 100, 800, 400, "Credits"],
                            [500, 450, 800, 750, "Back"]
                            ]

    app.difficulty_buttons= [[100, 300, 300, 500, "Baby"],
                             [350, 300, 550, 500, "Easy"],
                             [600, 300, 800, 500, "Hard"]
                             ]
def rebind_buttons(app):
    app.rebind_buttons = [[100, 70, 300, 260, f"Up \n[{app.bind_up}]"],
                          [100, 270, 300, 460, f"Down\n  [{app.bind_down}]"],
                          [100, 470, 300, 660, f"Left\n [{app.bind_left}]"],
                          [100, 670, 300, 860, f"Right\n  [{app.bind_right}]"],
                          [350, 70, 550, 260, f"Dodge\n [{app.bind_dodge}]"],
                          [350, 270, 550, 460, f"Dash\n[{app.bind_dash}]"],
                          [350, 470, 550, 660, f"Attack\n[{app.bind_attack}]"],
                          [350, 670, 550, 860, "Back"]
                          ]