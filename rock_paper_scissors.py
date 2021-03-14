import random
def play():
    user =input("'r'for rock, 'p' for paper, 's' for scissors \n")
    computer = random.choice(['r','s','p'])

    if user == computer:
        return 'It\'s a tie'

    if is_win(user, computer):
        return 'You Won!'
    return 'You Lost!'

def is_win(player,opponent):
    #return player wins
    #r>s,s>p,p>r
    if(player =='r' and oppenent =='s') or (player =='s' and opponent =='p')  or (player =='p' and opponent =='r'):
        return True
print(play())