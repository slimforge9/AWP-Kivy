from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen


class Menu(Screen):
    pass

class Person(GridLayout, Screen):
    pass

class Creator(GridLayout, Screen):
    list_of_documents = []

    # detain
    def checkbox_detain(self, instance, value):
        if value:
            self.list_of_documents.append("1_detain")
        else:
            self.list_of_documents.remove("1_detain")

        print(self.list_of_documents)

    # rights
    def checkbox_rights(self, instance, value):
        if value:
            self.list_of_documents.append("2_rights")
        else:
            self.list_of_documents.remove("2_rights")

        print(self.list_of_documents)

    #sober
    def checkbox_sober(self, instance, value):
        if value:
            self.list_of_documents.append("3_sober")
        else:
            self.list_of_documents.remove("3_sober")

    # doprowadzenie 79
    def checkbox_79(self, instance, value):
        if value:
            self.list_of_documents.append("4_79")
        else:
            self.list_of_documents.remove("4_79")

    # Nakaz przyjęcia
    def checkbox_przyjecie(self, instance, value):
        if value:
            self.list_of_documents.append("5_NPrzyjecia")
        else:
            self.list_of_documents.remove("5_NPrzyjecia")

    # Notatka z ujawnienia wykroczenia
    def checkbox_notka_wykroczenie(self, instance, value):
        if value:
            self.list_of_documents.append("6_NWykr")
        else:
            self.list_of_documents.remove("6_Nwykr")

    # Rozliczenie IW
    def checkbox_iw(self, instance, value):
        if value:
            self.list_of_documents.append("7_iw")
        else:
            self.list_of_documents.remove("7_iw")

    # Przerwa w konwoju
    def checkbox_przerwa_konwoj(self, instance, value):
        if value:
            self.list_of_documents.append("8_przerwa")
        else:
            self.list_of_documents.remove("8_przerwa")

    # Poswiadczenie pod opiekę nielata
    def checkbox_posw_nielat(self, instance, value):
        if value:
            self.list_of_documents.append("9_poswNielat")
        else:
            self.list_of_documents.remove("9_poswNielat")

    # Zlecenie na badania
    def checkbox_zlec_badanie(self, instance, value):
        if value:
            self.list_of_documents.append("10_zlecBadanie")
        else:
            self.list_of_documents.remove("10_zlecBadanie")

    # Kradzież rejestracja
    def checkbox_kradziez_rej(self, instance, value):
        if value:
            self.list_of_documents.append("11_kradziezRej")
        else:
            self.list_of_documents.remove("11_kradziezRej")


    # Pouczenia Wykroczenia
    def checkbox_wykr_pouczenia(self, instance, value):
        if value:
            self.list_of_documents.append("12_wykrPouczenia")
        else:
            self.list_of_documents.remove("12_wykrPouczenia")


    # Notatka UMP
    def checkbox_ump(self, instance, value):
        if value:
            self.list_of_documents.append("13_ump")
        else:
            self.list_of_documents.remove("13_ump")




# Load GUI with screen change
GUI = Builder.load_file("AWP.kv")


class AWPApp(App):

    def build(self):
        return GUI  # Menu()

    def change_screen(self, screen_name):
        # Get the screen manager from kv file
        screen_manager = self.root.ids['screen_manager']
        screen_manager.current = screen_name


AWPApp().run()
