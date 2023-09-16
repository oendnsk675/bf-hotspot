from itertools import combinations

def reset():
    f = open("wordlist.txt", "w")
    f.write("")
    f.close()

    
reset()

f = open("wordlist.txt", "a")
username = list("abcdefghijklmnopqrstuvwxyz")
password = list("0123456789")
username_comb = list(combinations(username, 4))
password_comb = list(combinations(password, 4))
comb = username_comb + password_comb
final_comb = list(combinations(comb, 2))
# print(final_comb[0])
xx = [[ "".join(x) for x in a] for a in final_comb]

for data in xx:
    for ds in data:
        f.write(ds)
        f.write(":")
    f.write("\n")

f.close()