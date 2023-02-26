"""
150271556 Riia Hiironniemi
COMP.CS.100
Murtolukulista
"""

class Fraction:
    """
    This class represents one single fraction that consists of
    numerator (osoittaja) and denominator (nimittäjä).
    """

    def __init__(self, numerator, denominator):
        """
        Constructor. Checks that the numerator and denominator are of
        correct type and initializes them.

        :param numerator: int, fraction's numerator
        :param denominator: int, fraction's denominator
        """

        # isinstance is a standard function which can be used to check if
        # a value is an object of a certain class.  Remember, in Python
        # all the data types are implemented as classes.
        # ``isinstance(a, b´´) means more or less the same as ``type(a) is b´´
        # So, the following test checks that both parameters are ints as
        # they should be in a valid fraction.
        if not isinstance(numerator, int) or not isinstance(denominator, int):
            raise TypeError

        # Denominator can't be zero, not in mathematics, and not here either.
        elif denominator == 0:
            raise ValueError

        self.__numerator = numerator
        self.__denominator = denominator

    def return_string(self):
        """
        :returns: str, a string-presentation of the fraction in the format
                       numerator/denominator.
        """

        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"

    def simplify(self):
        """
        simplifyes the fraction
        :return: none
        """
        divisor = greatest_common_divisor(self.__numerator, self.__denominator)
        self.__numerator = int(self.__numerator / divisor)
        self.__denominator = int(self.__denominator / divisor)

    def complement(self):
        """
        Makes the fraction a new fraction of complement
        :return: the complement olio
        """
        numerator = 0 - self.__numerator
        comp = Fraction(numerator, self.__denominator)
        return comp

    def reciprocal(self):
        """
        Makes a new fraction of the original fraction and changes it to
         reciprocal
        :return:  reciprocal
        """
        numerator = self.__denominator
        denominator = self.__numerator
        reci = Fraction(numerator, denominator)
        return reci

    def multiply(self, fraction_2):
        """
        multiplies two fractions
        :param fraction_2: second fraction
        :return: the answer
        """
        new_numerator = self.__numerator * fraction_2.__numerator
        new_denominator = self.__denominator * fraction_2.__denominator
        multi = Fraction(new_numerator, new_denominator)
        return multi

    def divide(self, fraction_2):
        """
        Divides two fractions
        :param fraction_2: second fraction
        :return: the answer
        """
        new_2 = fraction_2.reciprocal()
        new_numerator = self.__numerator * new_2.__numerator
        new_denominator = self.__denominator * new_2.__denominator
        divi = Fraction(new_numerator, new_denominator)
        return divi

    def add(self, fraction_2):
        """
        Sums two fractions
        :param fraction_2: second fraction
        :return: sum
        """
        nu_1 = self.__numerator * fraction_2.__denominator
        de_1 = self.__denominator * fraction_2.__denominator
        nu_2 = fraction_2.__numerator * self.__denominator
        new_nu = nu_1 + nu_2
        add = Fraction(new_nu, de_1)
        return add

    def deduct(self, fraction_2):
        """
        Deducts two fractions
        :param fraction_2: second fraction
        :return: deduct
        """
        nu_1 = self.__numerator * fraction_2.__denominator
        de_1 = self.__denominator * fraction_2.__denominator
        nu_2 = fraction_2.__numerator * self.__denominator
        new_nu = nu_1 - nu_2
        dedu = Fraction(new_nu, de_1)
        return dedu

    def __lt__(self, other):
        """
        Compares two fraction
        :param other: other fraction
        :return: bool
        """
        return self.__numerator / self.__denominator < \
               other.__numerator / other.__denominator

    def __le__(self, other):
        """
        Compares two fractions
        :param other: other fraction
        :return: bool
        """
        return self.__numerator / self.__denominator == \
               other.__numerator / other.__denominator

    def __str__(self):
        """
        Now you can print right away the fraction
        :return: str
        """
        if self.__numerator * self.__denominator < 0:
            sign = "-"

        else:
            sign = ""

        return f"{sign}{abs(self.__numerator)}/{abs(self.__denominator)}"


def greatest_common_divisor(a, b):
    """
    Euclidean algorithm. Returns the greatest common
    divisor (suurin yhteinen tekijä).  When both the numerator
    and the denominator is divided by their greatest common divisor,
    the result will be the most reduced version of the fraction in question.
    """

    while b != 0:
        a, b = b, a % b

    return a


def main():
    print("Enter fractions in the format integer/integer.")
    print("One fraction per line. Stop by entering an empty line.")
    fractions = []
    while True:
        frac = input()
        if frac != "":
            number = frac.split("/")
            og = Fraction(int(number[0]), int(number[1]))
            fractions.append(og)
        else:
            break

    print("The given fractions in their simplified form:")
    for index in fractions:
        print(index, end="")
        index.simplify()
        print(f" = {index}")

if __name__ == '__main__':
    main()