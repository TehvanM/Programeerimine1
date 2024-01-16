"""
Tehvan Marjapuu
21.11.23
ÜL 3
"""
"""
#KORRALIK
nimi =input("ütle oma nimi: ")
print(f"Tere, {nimi.strip().capitalize()}!")
"""
"""
#VANDUMINE

text = input("Ütle kurat küll: ")
print(f"{text.replace('kurat','***')}")
"""
#email
"""
email = input("lisa oma email: ")
print(f"on email? {'@' in email}")
"""
"""
#tundide ajad
# aja tükeldamine
algus = input("Sisesta algus aeg: ")
lopp = input("Sisesta lõppu aeg: ")
#teeme minutiteks
h1, m1 = algus.split(":")
h2, m2 = lopp.split(":")

minutid1 = int(h1) * 60 +int(m1)
minutid2 = int(h2) * 60 +int(m2)

ajavahe = minutid2 - minutid1
#minutid kellaajaks
hh1 = ajavahe // 60
mm1 = ajavahe % 60

print(f"päeva pikkus on {hh1}:{mm1}")
"""
#Palindroom
text = input("sisesta palindroom: ")
def isPalindrome(text):
    return text == text[::-1]
 

vastus = isPalindrome(text)
 
if vastus:
    print("Jah")
else:
    print("Ei")

