menu_option = """
ScreenManager:
    MenuScreen:
    CreatorScreen:
    EduDB:

<MenuScreen>:
    name: 'menu'
    MDRoundFlatButton: 
        text: 'Kreator'
        font_size: 34
        pos_hint: {'center_x': 0.5, 'center_y': 0.85}
        on_press: root.manager.current = 'kreator'

    MDRoundFlatButton:
        text: 'Baza wiedzy'
        font_size: 34
        pos_hint: {'center_x': 0.5,'center_y': 0.7}
        on_press: root.manager.current = 'edu_db'

<CreatorScreen>:
    name: 'kreator'
    MDLabel:
        text: 'Welcome'
        halign: 'center'    
    MDRoundFlatButton: 
        text: 'Cofnij'
        font_size: 34
        pos_hint: {'center_x': 0.2, 'center_y': 0.25}
        on_press: root.manager.current = 'menu'
    MDTextField:
        hint_text: "Wpisz nr PESEL"
        mode: "round"
        pos_hint: {"center_y": .5}
        size_hint_x: None
        width: "300dp"
        max_text_length: 11

<EduDB>:
    name: 'edu_db'
    MDLabel:
        text: 'Under Construction'
        halign: 'center'

"""