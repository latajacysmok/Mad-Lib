from tkinter import *

class Application(Frame):
    def __init__(self, master):
        super(Application, self).__init__(master)
        self.grid()
        self.create_widgets()

    def create_widgets(self):
        Label(self,
              text = "Wprowadź informację do nowego opowiadania: "
              ).grid(row=0, column=0, columnspan=2, sticky=W)

        Label(self,
              text = "Podaj proszę imię bohatera: "
              ).grid(row=1, column=0, sticky=W)
        self.person_ent = Entry(self)
        self.person_ent.grid(row=1, column=1, sticky=W)

        Label(self,
              text="Podaj proszę rzeczownik w liczbie mnogiej: "
              ).grid(row=2, column=0, sticky=W)
        self.noun_ent = Entry(self)
        self.noun_ent.grid(row=2, column=1, sticky=W)

        Label(self,
              text="Podaj proszę czasownik: "
              ).grid(row=3, column=0, sticky=W)
        self.verb_ent = Entry(self)
        self.verb_ent.grid(row=3, column=1, sticky=W)

        Label(self,
              text="Wybierz proszę przymiotnik(i): "
              ).grid(row=4, column=0, sticky=W)

        self.is_itchy = BooleanVar()
        Checkbutton(self,
                    text = "naglące",
                    variable = self.is_itchy
                    ).grid(row=4, column=1, sticky=W)

        self.is_joyous = BooleanVar()
        Checkbutton(self,
                    text="radosne",
                    variable=self.is_joyous
                    ).grid(row=4, column=2, sticky=W)

        self.is_electric = BooleanVar()
        Checkbutton(self,
                    text="elektryzujące",
                    variable=self.is_electric
                    ).grid(row=4, column=3, sticky=W)

        self.body_part = StringVar()
        self.body_part.set(None)

        Label(self,
              text="Wybierz proszę jedną część ciała: "
              ).grid(row=5, column=0, sticky=W)

        body_parts = ["pępek", "duży palec u nogi", "rdzeń przedłużony"]
        column = 1
        for part in body_parts:
            Radiobutton(self,
                        text = part,
                        variable = self.body_part,
                        value = part
                        ).grid(row=5, column=column, sticky=W)
            column += 1

        Button(self,
               text = "Kliknij aby wyświetlić opowiadanie",
               command = self.tell_story
               ).grid(row=6, column=0, sticky=W)

        self.story_txt = Text(self,
                              width = 75,
                              height = 10,
                              wrap = WORD)

        self.story_txt.grid(row = 7,
                            column = 0,
                            columnspan =4)

    def tell_story(self):
        person = self.person_ent.get()
        noun   = self.noun_ent.get()
        verb   = self.verb_ent.get()
        adjectives = ""
        if self.is_itchy.get():
            adjectives += "naglące, "
        if self.is_joyous.get():
            adjectives += "radosne, "
        if self.is_electric.get():
            adjectives += "elektryzujące, "
        body_part = self.body_part.get()

        story = "Sławny badacz i odkrywca "
        story += person
        story += " o mało co nie zrezygnował z życiowej misji poszukiwania "
        story += "zaginionego miasta, które zamieszkiwały "
        story += noun
        story += ", gdy pewnego dnia "
        story += noun
        story += " znalazły "
        story += person + "a. "
        story += "Silne, "
        story += adjectives
        story += "osobliwe uczucie owładnęło badaczem."
        story += "Po tak długim czasie poszukiwanie wreszcie się zakończyło. W oku "
        story += person + "a pojawiłą się łza, która spadła na jego "
        story += body_part + "."
        story += "Jaki morał płynie z tego opowiadania? Pomyśl, zanim zaczniesz "
        story += verb
        story += "."

        self.story_txt.delete(0.0, END)
        self.story_txt.insert(0.0, story)


root = Tk()
root.title("Mad Lib")
root.geometry("600x300")


app = Application(root)

root.mainloop()