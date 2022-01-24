# Nie dzieli się liter oznaczających jedną głoskę,
# np. cie-szyć, a nie cies-zyć,
# ani wyrazów jednosylabowych, gdyż ośrodkiem sylaby powinna być zawsze samogłoska
# np. krzak, a nie krz-ak.
# Zawsze rozdziela się dwie jednakowe spółgłoski,
# np. wan-na, Jo-an-na.
# Grupę kilku spółgłosek można dzielić w dowolnym miejscu,
# np. mat-ka, ma-tka.
# Zawsze należy oddzielić pojedynczą spółgłoskę, która stoi między samogłoskami,
# np. ra-tu-nek.
# Trzeba brać pod uwagę granicę pomiędzy przedrostkiem (przed-, nie-, roz-, …) i rdzeniem wyrazu,
# np. roz‑mowa, przed-kła-dać.


def replace_in_str(string, i, char):
    string = [char for char in string]
    string[i] = char

    return "".join(string)


def get_sylaby(word):
    word = word.lower()
    vowels = ["a", "e", "i", "o", "u", "y", "ą", "ę", "ó"]
    digraphs = ["ch", "rz", "sz", "dz"]

    syllable = ""
    syllables = []

    word = [char for char in word]
    i = 0

    while i < len(word):
        s = word[i]

        # digraphs
        if i < len(word) - 1 and s in ["c", "r", "s", "d"] and word[i+1] in ["h", "z"]:
            word[i] += word[i+1]
            word.pop(i + 1)

            s = word[i]

        if s in vowels:
            # spół + i + samo -> usuń i
            if s == "i" and 0 < i < len(word) - 1 and word[i-1] not in vowels and word[i+1] in vowels:
                syllable += s
            # eu, au
            elif s == "u" and 0 < i and word[i-1] in ["a", "e"]:
                syllables[-1] += s

            # end syllable
            else:
                syllable += s
                syllables.append(syllable)
                syllable = ""
        else:
            # two same consonants side by side
            if i < len(word) - 1 and word[i+1] == s:
                if syllable != "" or len(syllables) == 0:
                    syllable += s
                    syllables.append(syllable)
                    syllable = ""
                else:
                    syllables[-1] += s

            else:
                syllable += s

        i += 1

    if syllable != "":
        if syllable[-1] not in vowels:
            syllables[-1] += syllable
        else:
            syllables.append(syllable)

    return syllables, len(syllables)


def test_for(t_list):
    for tw in t_list:
        print(get_sylaby(tw))


if __name__ == '__main__':
    print("---test---")
    test_for(["twoja", "samochód", "chodzić", "matka"])

    print("---dwuznak---")
    test_for(["cieszyć", "ucieszony"])

    print("---jednosylabowe---")
    test_for(["drzwi", "znak"])

    print("---spółgłoski obok---")
    test_for(["wanna", "Joanna"])

    print("---zmiękczenia---")
    test_for(["wiedza", "pociecha"])

    print("---au eu---")
    test_for(["europa", "auto"])

    print("---inne---")
    test_for(["kakao", "ratunek", "dalekowzroczność", "ponapisywaliby"])

    print("---dziwne---")
    test_for(["wwlec", "odessie", "podróżować"])

