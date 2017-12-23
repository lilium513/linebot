import random
marks=list(range(0,4)) #マーク 0から c,h,d,s
nums=list(range(1,14))


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

def prizeJudge(cards): #役を決める
    marks=[]
    nums=[]
    mark_same=False

    print("marks:"+str(marks))

    for card in cards:
        marks.append(card[0])
        nums.append(card[1])
    nums.sort()
    marks.sort()
    if marks[0]==marks[-1]:
        mark_same=True
        print("marks is same :")
    print("marks after :"+str(marks))
    return cards

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

def straightJudge(nums):
    return
def flushJudge(marks):
    return
