"""
Projekti graafinen käyttöliittymä: Mene kalaan! -peli
Tekijät: Anna Koskinen ja Riia Hiironniemi

Saimme insipiraation projektiin lempipelistämme Littlest PetShop Go Fish!
korttipelistä. Pelissä kerätään neljän kortin muodostamia "perheitä" kysymällä
vuorotellen vastustajalta tietyn numeroista korttia. Jos vastapelaajalla ei ole
korttia, nostaa vuorossa oleva yhden kortin "kalalammesta" eli ylijääneistä
korteista. Pelin alussa pelaajille jaetaan 5 korttia ja voittaja on se, jolla
on pelin lopuksi enemmän "perheitä". Tarkemmat peliohjeet löytyvät koodin
menusta tekstin "Help" alla kohdassa "instructions".
Kommentointi on tehty suomeksi selkeyden vuoksi.
Tavoittelemme projektin käyttöliittymällä kehittynyttä versiota.
"""

#   Tuodaan käyttöliittymää varten "tkinter" ja "random" jotta saadaan arvottua
#   kortteja.
from tkinter import *
import random


class UserInterface:
    def __init__(self):
        """
        Rakentaja sisältää kaikki kolme korttipakkaa (pelaaja, PC ja lammikko),
        perhelaskurit, ikkunan otsikon, menun, jossa ohjeet pelin pelaamiseen,
        aloitus- ja lopetusnapit, kuvan kalasta, tekstikentät, syötelaatikon,
        kysymysnapin ja kaikkien komponenttien sijoitukset ikkunassa.
        """
        # Game window on ohjelman pääikkuna.
        self.__game_window = Tk()
        # Muodostetaan tyhjät listat, joista player_cards sisältää ohjelmaa
        # käyttävän henkilön pelikortit, PC_cards tietokoneen kortit ja cards
        # kaikki loput kortit.
        self.__cards = []
        self.__player_cards = []
        self.__PC_cards = []

        # Muodostetaan laskurit pelaajan ja koneen saamille "perheille".
        self.__player_family_counter = 0
        self.__PC_family_counter = 0

        # Pääikkunan otsikko
        self.__game_window.title("Go fish!")

        #   Luodaan pääikkunalle (self.__game_window) valikkopalkki sivun
        #   yläreunaan ja lisätään valintoihin "Help". Pudotusvalikosta
        #   voi valita "Instructions", josta aukeaa uuteen ikkunaan pelin
        #   ohjeet.
        self.__menubar = Menu(self.__game_window)
        self.__helpmenu = Menu(self.__menubar, tearoff=0)
        self.__helpmenu.add_command(label="Instructions",
                                    command=self.new_window)
        self.__menubar.add_cascade(label="Help", menu=self.__helpmenu)
        self.__game_window.config(menu=self.__menubar)

        # Aloitus- ja lopetusnapit. Aloitusnapin komentona toimii metodi
        # deal_cards ja lopetusnapin komentona metodi quit.
        self.__start = Button(self.__game_window, text="Start game",
                              command=self.deal_cards, background="pink")
        self.__quit = Button(self.__game_window, text="Quit",
                             command=self.quit, background="red")

        #   Avaa kuvatiedoston ja sijoittaa sen Label-kenttään kuvana.
        self.__picture = PhotoImage(file="kalakuva.gif", )
        self.__picture_label = Label(image=self.__picture)

        # Pelaajan korttitilanteen kertovat Labelit. Self_cards_in_hand kertoo
        # kaikki pelaajan kortit.
        self.__text = Label(self.__game_window, text="You have these cards:")
        self.__cards_in_hand = Label(self.__game_window, text="")

        # Korttien pyytämistä varten ask label, ask_entry syöttölaatikko ja
        # ask_button kysymisnappi. Ask_button napin komentona toimii ask_card
        # metodi.
        self.__ask = Label(self.__game_window, text="Ask for a card:")
        self.__ask_entry = Entry(self.__game_window)
        self.__ask_button = Button(self.__game_window, text="Ask",
                                   command=self.ask_card, background="orange")

        # Pelaajien perhetietoja kertovat labelit. Family_message on teksti
        # pelaajan perheistä ja family_message_PC tietokoneen perheistä.
        # Family_counter_label kertoo pelaajan perheiden lukumäärään ja
        # Family_counter_label_PC kertoo tietokoneen perheiden lukumäärän.
        # Näissä tekstinä on aikasemmin muodostetut perhelaskurit.
        self.__family_message = Label(self.__game_window,
                                      text="You have this many families:")
        self.__family_message_PC = Label(self.__game_window,
                                         text="PC has this many families:")
        self.__family_counter_label = Label(self.__game_window,
                                            text=self.__player_family_counter)
        self.__family_counter_label_PC = Label(self.__game_window,
                                               text=self.__PC_family_counter)

        # Pelin aikana muodostuvien viestien labelit. Message labelin kohdalle
        # tulee tietoa pelaajan pelikuvioista, virheellisistä syätteistä ja
        # pelin voittajasta. Go_fish_card kohdalle tulee tietoa pelaajan
        # nostamista korteista ja PC_message kohdalle tulee tietoa tietokoneen
        # pelistä.
        self.__message = Label(self.__game_window, text="")
        self.__go_fish_card = Label(self.__game_window, text="")
        self.__PC_message = Label(self.__game_window, text="")

        # Edellä mainitut komponentit on aseteltu grid:in avulla haluttuun
        # järjestykseen. Komponentit ovat järjestyksessä riveittäin ylhäältä
        # alas ja vasemmalta oikealle.
        self.__game_window.grid()
        self.__start.grid(row=0, columnspan=6)
        self.__picture_label.grid(row=1, columnspan=6)
        self.__text.grid(row=2, sticky=W)
        self.__cards_in_hand.grid(row=3, sticky=W)
        self.__family_message.grid(row=4, sticky=W)
        self.__family_counter_label.grid(row=4, column=1, sticky=W)
        self.__family_message_PC.grid(row=5, sticky=W)
        self.__family_counter_label_PC.grid(row=5, column=1, sticky=W)
        self.__ask.grid(row=6, column=0, sticky=W)
        self.__ask_entry.grid(row=6, column=1, sticky=E)
        self.__ask_button.grid(row=6, column=2, sticky=W)
        self.__message.grid(row=7, columnspan=3, sticky=W)
        self.__go_fish_card.grid(row=7, column=1, sticky=E)
        self.__PC_message.grid(row=8, columnspan=10, sticky=W)
        self.__quit.grid(row=9, column=5, sticky=E)

        self.__game_window.mainloop()

    def deal_cards(self):
        """
        Jakaa kortit pelin alussa pelaajalle ja PC:lle sekä loput kortit
        "lampeen".
        :return: None
        """

        #   Jos pelin osapuolilla on vielä kortteja, eli uusi peli aloitetaan
        #   kesken peliä, tyhjennetään osapuolien kortit, perhelaskurit ja
        #   "lammikon" kortit. Tiedot päivitetään myös peli-ikkunan
        #   tekstikenttiin.
        if len(self.__player_cards) != 0 and len(self.__PC_cards) != 0:
            self.__player_cards.clear()
            self.__PC_cards.clear()
            self.__cards.clear()

        # Täytetään cards lista numeroista 1-13 niin, että jokaista numeroa
        # on neljä kappaletta.
        for number in range(1, 14):
            for card in range(1, 5):
                self.__cards.append(number)

        self.__player_family_counter = 0
        self.__family_counter_label.configure(text="0")
        self.__PC_family_counter = 0
        self.__family_counter_label_PC.configure(text="0")


        # Jaetaan 5 korttia sattumanvaraisesti kaikista korteista pelaajalle
        # sekä tietokoneelle. Jaetut kortit myös poistetaan cards listasta.
        for card in range(1, 6):
            # Tietokoneelle jaettavat kortit import random:in avulla. Kortit
            # lisätään listaan PC_cards.
            card = random.choice(self.__cards)
            self.__PC_cards.append(card)
            self.__cards.remove(card)
        for card in range(1, 6):
            # Pelaajalle jaettavat kortit samalla tavalla kuin edellä, mutta
            # kortit lisätään listaan player_cards.
            card = random.choice(self.__cards)
            self.__player_cards.append(card)
            self.__cards.remove(card)
        self.cards_in_hand()
        self.__start.configure(text="Start again")
        self.empty_text()

    def cards_in_hand(self):
        """
        Jotta peli-ikkunassa saadaan näytettyä pelaajalle hänen korttinsa,
        tehdään listasta str-muotoinen teksti, jota päivitetään kierrosten
        mukaan tekstikenttään.
        :return: None
        """
        cards = ""
        for card in sorted(self.__player_cards):
            card = str(card)
            cards += card + " "
        self.__cards_in_hand.configure(text=cards)

    def ask_card(self):
        """
        Tarkastaa, ettäpelaaja syöttää oikeanlaisen kortin ja jos ei, antaa
        virheilmoituksen. Jos kysytty kortti on sääntöjen mukainen, kutsuu
        tarvittavia metodeja.
        :return:
        """
        try:

            #   Syötetty kortti.
            card = int(self.__ask_entry.get())

            #   Kortin on oltava väliltä 1-13.
            if card < 1 or card > 13:
                raise ValueError

            #   Kortin on oltava jokin niistä, mitä pelaajalla jo on.
            elif card not in self.__player_cards:
                self.empty_text()
                self.__message.configure(text="You must choose a card "
                                              "from your deck.")
                self.__ask_entry.delete(0, END)
            else:

                #   Jos kortti hyväksytää, pelataan pelaajan vuoro loppuun
                #   tyhjennetään syöttö-ikkuna, pelataan PC:n vuoro,
                #   päivitetään pelaajan pakka peli-ikkunaan ja tarkastellaan
                #   voittiko jompi kumpi osapuolista.
                self.player_turn()
                self.__ask_entry.delete(0, END)
                self.PC_turn()
                self.cards_in_hand()
                self.has_won()
        except ValueError:
            self.empty_text()
            self.__message.configure(text="You must enter a number between "
                                          "1-13.")
            self.__ask_entry.delete(0, END)

    def player_turn(self):
        if len(self.__player_cards) == 0 and len(self.__cards) != 0:
            card = random.choice(self.__cards)
            self.__player_cards.append(card)
            self.__cards.remove(card)
            self.family()
        elif len(self.__player_cards) != 0:
            card = int(self.__ask_entry.get())
            if card not in self.__PC_cards:
                self.__message.configure(text="Go fish!")
                go_fish = random.choice(self.__cards)
                self.__player_cards.append(go_fish)
                self.__cards.remove(go_fish)
                self.__go_fish_card.configure(
                    text=f"You fished number {go_fish}.")
            else:
                amount = self.__PC_cards.count(card)
                while card in self.__PC_cards:
                    self.__player_cards.append(card)
                    self.__PC_cards.remove(card)
                    self.__message.configure(
                        text=f"You got {amount}x number {card}"
                             f" card(s) from PC.")
                    self.__go_fish_card.configure(text="")
            self.family()

    def PC_turn(self):
        if len(self.__PC_cards) == 0 and len(self.__cards) != 0:
            card = random.choice(self.__cards)
            self.__PC_cards.append(card)
            self.__cards.remove(card)
            self.family()
        elif len(self.__player_cards) == 0 and len(self.__PC_cards) != 0:
            card = random.choice(self.__cards)
            self.__PC_cards.append(card)
            self.__cards.remove(card)
            self.family()

        elif len(self.__PC_cards) != 0:
            ask = random.choice(self.__PC_cards)
            if ask not in self.__player_cards:
                go_fish = random.choice(self.__cards)
                self.__PC_cards.append(go_fish)
                self.__cards.remove(go_fish)
                self.__PC_message.configure(
                    text=f"PC asked for number {ask} and "
                         f"went to fish.")
            else:
                amount = self.__player_cards.count(ask)
                while ask in self.__player_cards:
                    self.__PC_cards.append(ask)
                    self.__player_cards.remove(ask)
                    self.__PC_message.configure(
                        text=f"PC asked for number {ask} and "
                             f"stole {amount}x number {ask} "
                             f"card(s) from you.")
            self.family()
        print(f"Player cards:{sorted(self.__player_cards)}")
        print(f"PC cards: {sorted(self.__PC_cards)}")
        print(f"Lampi {self.__cards}")

    def family(self):
        """
        Trakastelee, onko pelaajalla tai PC:llä "perheitä" eli neljää samaa
        korttia. Jos on, lisätään perhe perhelaskuriin ja poistetaan kortit
        pois pelistä.
        :return: None
        """

        #   Pelaajan kortit käydään läpi numeroittain (1-13).
        for card in range(1, 14):
            number = self.__player_cards.count(card)

            #   Jos samaa korttia on 4 kpl tehdään peliin kuuluvat
            #   toimenpiteet.
            if number == 4:
                self.__player_family_counter += 1

                #   Päivitetään peli-ikkunan tekstikenttään oikea numero.
                self.__family_counter_label.configure(
                    text=self.__player_family_counter)

                #   Poistetaan kortit yksitellen.
                for remove in range(1, 5):
                    self.__player_cards.remove(card)
                self.__go_fish_card.configure(text="")

                self.__message.configure(text=f"You got a family of {card}'s!")

        #   Samat toimenpiteet tehdään PC:n korteille.
        for card in range(1, 14):
            number = self.__PC_cards.count(card)
            if number == 4:
                self.__PC_family_counter += 1
                self.__family_counter_label_PC.configure(
                    text=self.__PC_family_counter)
                for remove in range(1, 5):
                    self.__PC_cards.remove(card)
                self.__PC_message.configure(text=f"PC got a family of "
                                                 f"{card}'s.")

    def empty_text(self):
        """
        Tyhjentää kriittiset tekstikentät.
        :return: None
        """
        self.__message.configure(text="")
        self.__go_fish_card.configure(text="")
        self.__PC_message.configure(text="")

    def has_won(self):
        """
        Tarkastelee voittiko pelaaja vai PC ja ilmoittaa tuloksen
        "self.__game_window":n Labelissa "self.__message".
        :return:
        """
        if (len(self.__player_cards) == 0 and len(self.__cards) == 0) or (
                len(self.__PC_cards) == 0 and len(self.__cards) == 0):

            #   Tyhjentää kaikki mahdolliset tekstikentät, jotta tilalle
            #   ilmestyy vain tarvittavat tekstit.
            self.empty_text()

            #   Kehotetaan aloittamaan peli vielä uudestaan.
            self.__PC_message.configure(
                text="You can start a new game by pressing"
                     " the 'Start again' button.")

            #   Näytölle tulostuu oikea teksti "countereiden" mukaan.
            if self.__player_family_counter > self.__PC_family_counter:
                self.__message.configure(text="You have won!")
            else:
                self.__message.configure(text="PC has won!")

    def new_window(self):
        """
        Avaa ohjeet uuteen ikkunaan otsikolla "Instructions" ja koossa 400x300
        :return: None
        """
        new_window = Toplevel(self.__game_window)
        new_window.title("Instructions")
        new_window.geometry("400x300")

        #   Ohjeet on riveittäin Label-komponentteina.
        Label(new_window,
              text='During a turn the player asks PC if it has ').pack()
        Label(new_window,
              text='a particular rank of card. For example, the player may '
                   'ask ').pack()
        Label(new_window,
              text='PC if it has any nines. If PC has any nines, then ').pack()
        Label(new_window,
              text='it must give all of its nines to the player. If PC').pack()
        Label(new_window,
              text='does not have any nines, then it says "go fish".').pack()
        Label(new_window,
              text='When you "go fish" you get any card from the pool.').pack()
        Label(new_window,
              text='If the player gets all four suits of the same rank, '
                   'then ').pack()
        Label(new_window,
              text='they get "a family". For example, if you already '
                   'had').pack()
        Label(new_window,
              text='three nines and then you picked up another nine from '
                   'the').pack()
        Label(new_window,
              text='pool, you then get a family. The turn changes '
                   'after.').pack()
        Label(new_window,
              text='Go Fish is over when  there are no more cards in the '
                   'pool.').pack()
        Label(new_window,
              text='The winner is then determined by who has the most '
                   'families.').pack()

    def quit(self):
        """
        Lopettaa ohjelman suorituksen ja sulkee peli-ikkunan.
        :return: None
        """
        self.__game_window.destroy()


def main():
    UserInterface()


if __name__ == '__main__':
    main()
