player_one = [ int(x) for x in input().split()]
player_two=[ int(x) for x in input().split()]
player_three=[ int(x) for x in input().split()]
on_table=[ int(x) for x in input().split()]

player_one_eat=[]
player_two_eat=[]
player_three_eat=[]

def player_1():
    while(len(player_one)>0):
        kev = player_one[0]
        del player_one[0]
        on_table.append(kev)
        print(len(player_one))
        if (len(player_one)>0):
            if(player_one[0] < on_table[0] ):
                player_2()
            else:
                eat = on_table[0]
                del on_table[0]
                player_one_eat.append(eat)
                player_2()
def player_2():
    while(len(player_two)>0):
        kev = player_two[0]
        del player_two[0]
        on_table.append(kev)
        if (len(player_one)>0):
            if player_two[0] < on_table[0]:
                player_3()
            else:
                eat = on_table[0]
                del on_table[0]
                player_two_eat.append(eat)
                player_3()

def player_3():
    while(len(player_three)>0):
        kev = player_three[0]
        del player_three[0]
        on_table.append(kev)
        if (len(player_one)>0):
            if player_three[0] < on_table[0]:
                player_1()
            else:
                eat = on_table[0]
                del on_table[0]
                player_three_eat.append(eat)
                player_1()
               
player_1()
print("player 1 has eaten {} cookies".format(len(player_one_eat)))
print("player 2 has eaten {} cookies".format(len(player_two_eat)))
print("player 3 has eaten {} cookies".format(len(player_three_eat)))


    




