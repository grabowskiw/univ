def space():
    print("\n"*3)

nickname = "Hello Wojtek"
age = 20
print(nickname)
print(age)

space()
print(nickname, end="")
print(age)

space()
print(type(nickname), type(age))

space()
# pkt 2
name = "Dua\nLipa\nFuture\nNostalgia"
print(name.splitlines(False))

space()
name = "Wojtek"
print("Witajcie, mam na imię "+name+" i mam "+str(age)+" lat")

space()
print(f"No i yahoo, ja też jestem {name}, \nmam {age} lat")
print(R"a ja jestem raw {name}, \nmam {age} lat")

space()
hi = ("Hey, I'm {imie}, mam wlasnie {wiek} lat".format(imie=name, wiek=age))
print(hi)

space()
# pkt 3
status = ''' HOME OFFICE '''

_profile_img = ""

me_about_hobby = 'Jag studerar svenska på Duolingo och jag tycker om programmering. Det är min Hobby. Vad tycker du om det?'


me_about_job = 'this is me talking about my job'

me_about_motivation = """Now I'm talkin' about Motivation by Normani"""

me_about_motivation_r = r"""Give me 6 hrs to chop down a tree\nand I'll spend the first 4 sharpening the axe."""

space()
print(status.lower().strip(" "))
print(me_about_hobby.upper())
print(me_about_job.capitalize())
print(hi.replace("Wojtek", "Wojciech"))
print(me_about_motivation_r[4:-4])
print(name.endswith("k"))
print(len(name)) # 6
print(me_about_job.count("i")) # 3
print(me_about_hobby.split("."))
print(name.find('e'))
print(name.isalnum())
print(str(age).isalpha())
print(str(age).isnumeric())
