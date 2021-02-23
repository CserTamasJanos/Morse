
class Quote:
    def __init__(self, text):
        self.author = Morse2Text(text[0].split("       "), morseABC)
        self.quote = Morse2Text(text[1].split("       "), morseABC)


def Morse2Text(someText, morze_abc):
    transformed = ""
    for dose in someText:
        dose = dose.split("   ")
        for aLetter in dose:
            if aLetter in morze_abc:
                transformed += (morze_abc[aLetter])
        transformed += " "
    return transformed.strip()


morseABC = {}
leave = True
for line in open("morzeabc.txt"):
    if not leave:
        portion = line.split("\t")
        morseABC[portion[1].strip()] = portion[0].strip()
    leave = False

print(f"Task 3.: Morse abc Contains {len(morseABC)} character codes.")

letter = input(f"Task 4: Give me a character: ").strip().upper()

got = False
for x in morseABC:
    if letter == morseABC[x]:
        print(f"Task 5.: The code of {morseABC[x]} is: {x}")
        got = True
if not got: print("Task 5.: Character not found.")

texts = []
for textLine in open("morze.txt"):
    texts.append(Quote(textLine.split(";")))

print(f"Task 6.: The author of the first quote is: {texts[0].author}")
maxid = 0
for t in range(len(texts)):
    if len(texts[t].quote) > len(texts[maxid].quote):
        maxid = t

print(f"Task 7.: The longest author's name and his or her quotes: \n \t{texts[maxid].author}:")
for ari in texts:
    if ari.author == "ARISZTOTELÉSZ":
        print(f"\t- {ari.quote}")

translated = open("translation.txt", "w")

for save in texts:
    translated.write(f"{save.author}: {save.quote}\n")