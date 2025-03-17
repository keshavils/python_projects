def calculate_love_score(name1, name2):
    letters = ["t", "r", "u", "l", "o", "v", "e"]
    t = r = u = l = o = v = e = 0
    love_birds = (name1 + name2).lower().replace(" ", "")
    for ltr in letters:
        if ltr in love_birds:
            if ltr == "t":
                for char in love_birds:
                    if char == ltr:
                        t += 1  
            elif ltr == "r":
                for char in love_birds:
                    if char == ltr:
                        r += 1
            elif ltr == "u":
                for char in love_birds:
                    if char == ltr:
                        u += 1
            elif ltr == "l":
                for char in love_birds:
                    if char == ltr:
                        l += 1
            elif ltr == "o":
                for char in love_birds:
                    if char == ltr:
                        o += 1
            elif ltr == "v":
                for char in love_birds:
                    if char == ltr:
                        v += 1
            elif ltr == "e":
                for char in love_birds:
                    if char == ltr:
                        e += 1

    print(f"T occurs {t} times")
    print(f"R occurs {r} times")
    print(f"U occurs {u} times")
    print(f"E occurs {e} times")
    print(f"L occurs {l} times")
    print(f"O occurs {o} times")
    print(f"V occurs {v} times")
    print(f"E occurs {e} times")
    
    print("Love Score = ", str(t+r+u+e) + str(l+o+v+e))


calculate_love_score("Kanye West", "Kim Kardashian")