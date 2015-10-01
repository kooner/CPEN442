
CIPHER_TEXT = "GTOKKPKKYXXKSVHWCYSSYAPISKDIEODHUKISKMIQQYISKDIEOPHWGLIMIQQYISKDIEOKHNTGGLIYSVSIGKYGKSVIDYXXKSVHWMVIGHGLYPHSIOHNHSCHACIPXOHUYGKVHYOJMIQQYLTHMTTKGIIFLHGTTHQGIOHUKSVKAAVIGDOIVICOIENTGHGCYMFGIGTKPTHOKMIQQYGINKGTKOLHGTQYSJAIIPKAKYUKPIDSIGKPMIQQYYSVVEOHSNPVIGOVIGISKDIEOGLIRKOIISKTKSKYOAJDHAAKVHGPXYNKPLHGTTHPYMMIESGIDGTKLYOVIGCEGYSSKWKVGIHGYSVXOKPKOUKVLHGTHGMIQQYXOICYCAJHSYPHSNAKOKVMYPKMIQQYLKOKGTKGTOKKAYONKUIAEQKPMIQQYCIESVHSOKVAKYGTKOMIQQYGTYGCHACINYUKGITHQYPYXYOGHSNNHDGVIGGIGTKPKDIEOUIAEQKPGTKOKLYPYVVKVHSLKPGQYOMTYDHDGTMISGYHSHSNMIQQKSGYOHKPMIQQYNKSKYAINHKPMIQQYYSVUYOHIEPIGTKOQYGGKOMISMKOSHSNGTKTICCHGQKQCKOPIDGTKDKAAILPTHX"

def p(t):
    n = ""
    for c in t:
        if ord(c) >= ord("A") and ord(c) <= ord("Z"):
            n += c
        elif ord(c) >= ord("a") and ord(c) <= ord("z"):
            n += "\033[0;31m" + c + "\033[0m"
        else:
            assert False
    print n

def printMostFrequentNChars(t, n):
    histogram = {}
    i = 0
    while i <= len(t) - n:
        key = t[i:i+n]
        histogram.setdefault(key, 0)
        histogram[key] += 1
        i += 1
    for i in sorted(histogram.items(), key=lambda h: h[1], reverse=True):
        print i
    exit()

def bruteForceCaesar(t):
    for i in xrange(26):
        new = ""
        for c in t:
            newchar = ord(c) + i
            if newchar > 90:
                newchar -= 26
            new += chr(newchar)
        print new
        print "-------------------"
    exit()

#bruteForceCaesar(CIPHER_TEXT)
#printMostFrequentNChars(CIPHER_TEXT, 3)
substitutions = [
    ("A", "l"),
#   ("B", "B"),
    ("C", "b"),
    ("D", "f"),
    ("E", "u"),
    ("F", "k"),
    ("G", "t"),
    ("H", "i"),
    ("I", "o"),
    ("J", "y"),
    ("K", "e"),
    ("L", "w"),
    ("M", "c"),
    ("N", "g"),
    ("O", "r"),
    ("P", "s"),
    ("Q", "m"),
    ("R", "z"),
    ("S", "n"),
    ("T", "h"),
    ("U", "v"),
    ("V", "d"),
    ("W", "x"),
    ("X", "p"),
    ("Y", "a"),
#   ("Z", "Z"),
]
for s in substitutions:
    CIPHER_TEXT = CIPHER_TEXT.replace(s[0], s[1])
p(CIPHER_TEXT)

