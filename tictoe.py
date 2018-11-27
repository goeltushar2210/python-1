def board(box):
    
    print (box[1]+'|'+box[2]+'|'+box[3])
test_board=['#','x','0','u']
board(test_board)



def name(a,b):
    
    return a+b,b

e,d=name(5,6)
print(e)
print(d)