import random
marks=list(range(0,4)) #マーク 0から c,h,d,s
nums=list(range(1,14))
RSF=10
SF=9
FC=8
FH=7
FL=6
ST=5
TC=4
TP=3
OP=2
HC=1

def getCards():
    temp_cards=random.sample(list(range(52)), 10)
    temp_cards.sort()
    cards=[]
    print(temp_cards)
    for temp_card in temp_cards:
        mark=marks[temp_card%4]
        num=nums[temp_card%13]
        cards.append((mark,num))

    return cards
def convertTupleToCards(tus):
    mongon="あなたのカードは"
    for tu in tus:
        if tu[0]==0:
            mongon+="♣"
        elif tu[0]==1:
            mongon+="♥"
        elif tu[0]==2:
            mongon+="◆"
        elif tu[0]==3:
            mongon+="♠"
        mongon+=str(tu[1])
        mongon+=" "
    mongon+="\nです!"
    return mongon


def prizeJudge(cards): #役を決める
    marks=[]
    nums=[]
    mark_same=False

    #print("cards:"+str(cards))

    for card in cards:
        marks.append(card[0])
        nums.append(card[1])
    nums.sort()
    marks.sort()

    mark=flushJudge(marks) #フラッシュ判定
    pair=pairJudge(nums) #ペア系判定
    straight=straightJudge(nums) #ストレート判定

    if straight==2 and mark==1: #rsf
        return RSF
    elif straight==1 and mark==1:
        return SF
    elif pair==5:
        return FC
    elif pair==4:
        return FH

    elif mark==1:
        return FL

    elif straight>0:
        return ST
    elif pair==3:
        return TC
    elif pair==2:
        return TP
    elif pair==1:
        return OP

    #print("marks after :"+str(marks))
    return HC

def pairJudge(nums): #1,2,3,4,5 → or,tp,tc,fh,fc ソート済みの数列がくる
    pairs=0
    three=0
    four=0
    for num in nums:
        temp=nums.count(num)

        if temp==4:
            four=1
            return 5 #フォーカードが確定するため
        if temp==3:
            three=1
            for i in range(3):
                nums.remove(num)
        if temp==2:
            pairs+=1
            for i in range(2):
                nums.remove(num)
    if pairs==1:
        if three==1:
            return 4
        else:
            return 1

    if three==1:
        return 3

    if pairs==2:
        return 2

    return 0 #ペア系の役はない

def straightJudge(nums): #普通のストレート  1  10~13,1のストレート  2 なし  0 の三種
    i=0
    hs=[1,10,11,12,13]
    s=[0,1,2,3,4]
    temp=nums[0]
    s=list(map(lambda x:x+temp,s))
    if s==nums:
        return 1
    if nums==hs:
        return 2
    return 0
def flushJudge(marks): #マークが同じかを確認
    if marks[0]==marks[-1]:
        return 1
    else:
        return 0
