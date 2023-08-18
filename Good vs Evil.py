def good_vs_evil(good, evil):
    good = good.split(" ")
    good = [eval(i) for i in good]
    evil = evil.split(" ")
    evil = [eval(i) for i in evil]
    good[1] = good[1] * 2
    good[2] = good[2] * 3
    good[3] = good[3] * 3
    good[4] = good[4] * 4
    good[5] = good[5] * 10
    evil[1] = evil[1] * 2
    evil[2] = evil[2] * 2
    evil[3] = evil[3] * 2
    evil[4] = evil[4] * 3
    evil[5] = evil[5] * 5
    evil[6] = evil[6] * 10
    good = sum(good)
    evil = sum(evil)
    if evil > good:
        return 'Battle Result: Evil eradicates all trace of Good'
    if good > evil:
        return 'Battle Result: Good triumphs over Evil'
    if good == evil:
        return 'Battle Result: No victor on this battle field'
        
