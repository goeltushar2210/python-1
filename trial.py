def box(a):
  print(a[1]+'|'+a[2],)
d=["z","b","c"]
box(d)
def player():
    marker="  "
    while marker!='x' and marker!= 'o':
        marker=input("player1 : choose x or o")
    if marker== 'x':
            return ('x','o')
    else :
                return ('o','x')
    player1_marker,player2_marker=player_input()
    








F