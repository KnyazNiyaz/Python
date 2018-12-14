import random
import time

player = random.randint(1,6)
print('You rolled ' + str(player))

time.sleep(2)

ai = random.randint(1,6)
print('AI rolled ' + str(ai))

if player > ai:
    print('You win')
elif player == ai:
    print('Tie game')
else:
    print('You lose')
