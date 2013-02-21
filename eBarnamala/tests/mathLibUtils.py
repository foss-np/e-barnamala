def mreplace(s, englishChr, nepaliChr):
    for a, b in zip(englishChr, nepaliChr):
        s = s.replace(a, b)
    return s

numberAboveNineStr = []
nepaliStr = loadData.numberStr
englishStr = ['1','2','3','4','5','6','7','8','9','0']
numberAboveNineNames = ['b;','P3f/','afx|','t]x|','rf}w','k+b|',';f]x|',';q','c7f/','pG8fO;\\','aL;']
tempRange = range(10,21)
for i in range(len(tempRange)):
    tempRange[i] = str(tempRange[i])
for i in tempRange:
    numberAboveNineStr.append(mreplace(i, englishStr, nepaliStr))
