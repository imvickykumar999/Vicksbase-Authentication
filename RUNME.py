
from crud import vicks as vix

obj = vix(password = '***********',
          # name = 'Anonymous',
          # link = 'https://new-project-ab9c7-default-rtdb.firebaseio.com/',
          )

f = obj.pull()

print(f)

# from vicksbase import firebase as f
# firebase_obj = f.FirebaseApplication('https://new-project-ab9c7-default-rtdb.firebaseio.com/')
# print(firebase_obj)
