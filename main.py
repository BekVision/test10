# # nested if 
# age = int(input("yoshingizi kiriting: "))
# fom = input("Ota onasi bilanmi? (Ha/Yo'q): ")

# if age > 18:
#     print('Xush kelibsiz')
# elif age < 18:
#     if fom.lower() == "ha":
#         print("Ruxsat berildi")
#     elif fom.lower() == "yo'q":
#         print("Kechirasiz, yoshingiz yetmaydi")
#     else:
#         print("Faqat ha yoki Yo'q yozish mumkun")
# else:
#     have_passport = input("Passportingiz bormi? (ha/yo'q): ")
#     if have_passport.lower() == "ha":
#         print("Ruxsat bor")
#     else:
#         print("Sizda passport yo'q, ruxsat ham yo'q.")




son = int(input("son kiriting: "))
if son > 0:
    if son % 2 == 0:
        print("Son juft")
    else:
        print("Son toq")
elif son < 0:
    if son < -100:
        print("-100 dan kichik son")
    else:
        print("-100 dan kichik emas")
else:
    print("Bu son 0ga teng")