
# pip install --upgrade imvickykumar999
# C:\Users\Vicky\anaconda3\Lib\site-packages\vicksbase
# https://stackoverflow.com/questions/1802971/childerror-child-self-is-not-defined

import json
txt = open('hideme.txt', "r")
txtread = txt.read().strip()
print(txtread, type(txtread))

class vicks:
    def __init__(self,
                password,
                child = None,
                link = 'https://new-project-ab9c7-default-rtdb.firebaseio.com/',
                ):

        try:
            self.link = link
            self.child = f"auth/{child}"
            self.password = password

            from vicksbase import firebase as f
            self.firebase_obj = f.FirebaseApplication(self.link, None)
            # print(self.pull(child = '/'))

        except Exception as e:
            print(e)
            print('try: pip install imvickykumar999')

    def show(self):
        return self.link, self.child

    def pull(self):

        if self.password == txtread:
            result = self.firebase_obj.get('/', None)
            return result

        else:
            error = '\n...Wrong Credentials !!!\n'
            print(error)
            return error

    def push(self, data = None):

        if self.password == txtread:
            if data == None:
                data = f"...hi, I am {self.child}"

            self.firebase_obj.put('/', self.child, data)
            # self.firebase_obj.post(child, data)
            # return self.pull(child = '/')

        else:
            error = '\n...Wrong Credentials !!!\n'
            print(error)
            return error

    def add(self, data = None,
                   child = None):

        if self.password == txtread:
            self.firebase_obj.post(self.child, data)

        else:
            error = '\n...Wrong Credentials !!!\n'
            print(error)
            return error

    def remove(self, child): # danger to run... loss of data.

        if self.password == txtread:
            data = self.firebase_obj.delete('/', self.child)
            # return self.pull(child = '/')

        else:
            error = '\n...Wrong Credentials !!!\n'
            print(error)
            return error

    def save(self):

        if self.password == txtread:
            with open('data.json', 'w', encoding ='utf8') as json_file:
                json.dump(self.pull(self.child), json_file, ensure_ascii = False)

        else:
            error = '\n...Wrong Credentials !!!\n'
            print(error)
            return error

# link = 'https://chatting-c937e-default-rtdb.firebaseio.com/'
obj = vicks(txtread)

# f = obj.show()
# f = obj.pull()
# f = obj.push(1)
# f = obj.remove()

# print(f)
