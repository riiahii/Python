"""
COMP.CS.100 Programming 1
Riia Hiironniemi
Tourist dictionary.
"""


def main():
    english_spanish = {"hey": "hola", "thanks": "gracias", "home": "casa"}
    english_words = ", ".join(sorted(english_spanish))
    print("Dictionary contents:")
    print(english_words)
    while True:
        command = input("[W]ord/[A]dd/[R]emove/[P]rint/[T]ranslate/[Q]uit: ")

        if command == "W":

            word = input("Enter the word to be translated: ")
            if word in english_spanish:
                print(f"{word} in Spanish is {english_spanish[word]}")
            else:
                print("The word", word, "could not be found from "
                                        "the dictionary.")

        elif command == "A":
            word = input("Give the word to be added in English: ")
            translation = input("Give the word to be added in Spanish: ")
            english_spanish[word] = translation
            english_words = ", ".join(sorted(english_spanish))
            print("Dictionary contents:")
            print(english_words)

        elif command == "R":
            word = input("Give the word to be removed: ")
            if word in english_spanish:
                del english_spanish[word]
            else:
                print("The word", word, "could not be found from "
                                        "the dictionary.")

        elif command == "P":
            spanish_english = {}
            for word in english_spanish:
                new_word = english_spanish[word]
                new_translation = word
                spanish_english[new_word] = new_translation
            print()
            print("English-Spanish")
            for word in sorted(english_spanish):
                print(word, english_spanish[word])
            print()
            print("Spanish-English")
            for word in sorted(spanish_english):
                print(word, spanish_english[word])
            print()

        elif command == "T":
            text = input("Enter the text to be translated into Spanish: ")
            print("The text, translated by the dictionary:")
            words = text.split()
            translation = ""
            for index in range(0, len(words) - 1):
                if words[index] in english_spanish:
                    words[index] = english_spanish[words[index]]
                    translation += words[index] + " "
                else:
                    translation += words[index] + " "
            if words[-1] in english_spanish:
                words[-1] = english_spanish[words[-1]]
                translation += words[-1]
            else:
                translation += words[-1]
            print(translation)

        elif command == "Q":
            print("Adios!")
            return

        else:
            print("Unknown command, enter W, A, R, P, T or Q!")


if __name__ == "__main__":
    main()
