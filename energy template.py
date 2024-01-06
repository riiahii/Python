"""
COMP.CS.100 Ohjelmointi 1 / Programming 1
Name:       Riia Hiironniemi
Name:       Roope Hiironniemi
Energiankulutushistogrammi
"""


def input_values():
    """
    Kerää ohjelmaan syötettyjä energian arvoja niin kauan, kunnes syötetään
    tyhjä rivi.
    :return: str, listan energian arvoista
    """
    # tyhjä lista, johon lisätään kysytyt arvot
    consumptions = []
    consumption = True
    # kysyy arvoja niin kauan, kunnes syötetään tyhjä. Jos syötetty luku on
    # negatiivinen, tulostetaan virheilmoitus ja kysytään arvoa uudestaan.
    # Lisätään arvot listaan
    while consumption != "":
        consumption = input("Enter energy consumption (kWh): ")
        if consumption:
            value = int(consumption)
            if value < 0:
                print(f"You entered: {value}. Enter non-negative numbers "
                      f"only!")
            elif value >= 0:
                consumptions.append(value)
    return consumptions


def which_classes(list_of_values):
    """
    Laskee kuinka monta energian arvoa on kussasin energialuokassa
    :param list_of_values: str, lista, jossa energian arvot
    :return: str, listan, jossa luokittain arvojen lukumäärät
    """
    # suurimman luokan arvo (aluksi 0)
    max_class = 0
    # käy jokaisen listan indeksin arvon läpi ja katsoo mihin kulutusluokkaan
    # arvo kuuluu. Kun tarkasteltava arvo on luokan minimin ja maksimin
    # välissä vaihtaa alkuperäisen listan arvon kulutusluokaksi. Tarkastaa
    # myös aina että onko saatu luokka suurempi kuin aiempi maksimiluokka ja
    # jos on niin muuttaa maksimiluokan kyseiseksi luokaksi.
    for index in range(0, len(list_of_values)):
        class_num = 1
        while True:
            class_min = 10 ** class_num // 100 * 10
            class_max = 10 ** class_num - 1
            if class_min <= list_of_values[index] <= class_max:
                list_of_values[index] = class_num
                if max_class < class_num:
                    max_class = class_num
                break
            class_num += 1
    # luo listan kulutusluokille, jossa jokaisen kulutusluokan arvo on nolla
    # maksimiluokkaan asti
    classes = [0] * max_class
    # laskee kuinka monta arvoa on kussakin luokassa ja korvaa listaan arvojen
    # lukumäärän nollan tilalle
    for class_number in range(0, len(classes)+1):
        count = list_of_values.count(class_number)
        classes[class_number - 1] = count
    return classes


def print_histogram(classes, consumptions):
    """
    Tulostaa arvojen mukaisen histogrammin
    :param classes: str, lista kulutusluokista ja niiden arvojen määrästä
    :param consumptions: str, lista alkuperäisistä energian arvoista
    """
    # etsii suurimman syötetyn energian arvon
    largest_class_number = max(consumptions)
    # tulostaa koko histogrammin rivi kerrallaan
    for index in range(1, len(classes) + 1):
        print_single_histogram_line(index, classes[index - 1],
                                    largest_class_number)


def class_minimum_value(class_number):
    """
    Laskee kulutusluokan minimiarvon
    :param class_number: kulutusluokka
    :return: luokan minimiarvo
    """
    return 10 ** class_number // 100 * 10


def class_maximum_value(class_number):
    """
    Laskee kulutusluokan maksimiarvon
    :param class_number: kulutusluokka
    :return: luokan maksimiarvo
    """
    return 10 ** class_number - 1


def print_single_histogram_line(class_number, count, largest_class_number):
    """
    Tämä on luultavasti projektin haastavin funktio, joten tässä se on
    valmiina.  Funktio tulostaa oikean muotoisen histogrammin rivin,
    kuhan kutsut sitä oikeilla parametrien arvoilla.

    :param class_number: int,
        Mitä kulutuskatergoriaa tulostettava rivi kuvaa (1, 2, 3, ...)
        Parametria <class_number> käytetään päättämään, mikä arvoväli
        (0-9, 10-99, 100-999, ...) riville tulostuu ennen diagrammin
        "*"-merkkejä.

    :param count: int,
        Kuinka monta "*"-merkkiä riville on tarpeen tulostaa, eli
        kuinka monta käyttäjän syöttämää arvoa kuuluu <class_number>-
        parametrin kuvaamalle välillä.

    :param largest_class_number: int,
        Mikä on kaikkein suurin kategorian numero.  Riippuu
        suurimmasta käyttäjän syöttämästä kulutusarvosta.
        Esimerkiksi jos suurin käyttäjän syöttämä luku
        oli 91827364 (8 numeromerkkiä) <largest_class_number>-parametrin
        arvon tulisi myös olla 8.  Parametrin arvoa käytetään
        määriteltäessä, kuinka monta välilyöntiä muiden kuin viimeisen
        histogrammin rivin eteen pitäisi tulostaa.
    """

    # <range_string>-muuttujaan talletetaan merkijonona rivin
    # histogrammissa kuvaama arvoväli. Esimerkiksi "1000-9999".
    # Apufunktiot class_minimum_value ja class_maximum_value
    # sinun on määriteltävä itse.

    min_value = class_minimum_value(class_number)
    max_value = class_maximum_value(class_number)
    range_string = f"{min_value}-{max_value}"

    # Kun histogrammin viimeinen rivi tulostetaa, kuinka monta
    # merkkiä leveä tulee <range_string> silloin olemaan.
    # Jos esimerkiksi <largest_class_number> on 7, tarkoittaisi
    # se, että arvoväliksi tulostetaan "1000000-9999999" eli
    # muuttujaan <largest_width> pitää tallentaa arvo 15.
    # Kaikkien arvovälien <range_string> tulostetaan tämän
    # levyisen kentän oikeaan laitaan.

    largest_width = 2 * largest_class_number + 1

    # Kaikki valmistelun on tehty, voidaan tulostaa rivi,
    # jonka alussa on oikea määrä välilyöntejä, niiden perässä
    # arvoväli ja lopulta oikea määrä "*"-merkkejä.
    # Merkki ">" seuraavassa f""-merkkijonossa tulostaa
    # <range_string>:in arvon tulostuskentän oikeaan laitaan
    # (täytevälilyönnit tulostetaan alkuun).

    print(f"{range_string:>{largest_width}}: {'*' * count}")


def main():
    print("Enter energy consumption data.")
    print("End by entering an empty line.")
    print()
    # tekee listan energian arvoista funktiolla input_values
    consumptions = input_values()
    # jos ei syötetä yhtään energian arvoja, ohjelma tulostaa vain tekstin.
    if not consumptions:
        print("Nothing to print. Done.")
    # jos syötetään energian arvoja tuodaan kulutusluokkalista ja tulostetaan
    # histogrammi
    else:
        classes = which_classes(consumptions)
        print_histogram(classes, consumptions)


if __name__ == "__main__":
    main()
