# 🚨 Don't change the code below 👇
print("Welcome to the Love Calculator!")
name1 = input("What is your name? \n")
name2 = input("What is their name? \n")
# 🚨 Don't change the code above 👆

#Write your code below this line 👇
name = name1 + name2
t = name.lower().count('t')
r = name.lower().count('r')
u = name.lower().count('u')
e = name.lower().count('e')
total_true = t + r + u + e

l = name.lower().count('l')
o = name.lower().count('o')
v = name.lower().count('v')
e = name.lower().count('e')
total_love = l + o + v + e

score_str = total_true.__str__() + total_love.__str__()
score_int = int(score_str)
if 10 < score_int > 90:
    print('Your score is {}, you go toghter like coke and mentos.'.format(score_int))
elif 40 <= score_int <= 50:
    print('Your score is {}, you are alright together'.format(score_int))
else:
    print('Your score is {}'.format(score_int))
