from random import *
import os

chars = ['A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z', 'a', 'b', 'c', 'd', 
'e','f','g','h','i','j','k','l','m','n','o','p','q','r','s','t','u','v','w','x','y','z','1','2','3','4','5','6','7','8','9','0','!','@','#','$','%','_','+','.',',','|','[',']']

users = []
pwlist = []

pwl = 12
i = 0

while 1:
	i+=1
	user = input("Enter one username, hit enter, and repeat. Input 'done' when done.\n")
	f = open('userfile.txt', 'w')
	pw = ''
	if user == 'done':
		print(users)
		print(pwlist)
		for i in range(len(users)):
			f.write('%s: ' % users[i])
			f.write('%s\n\n' % pwlist[i])
			
		f.close()
		
		exit()
	else:
		while len(pw) <= pwl:
			
			pw += pw.join(x for x in chars[randrange(64)])
		
		pwlist.append(pw)
		users.append(user)
		

		




