import json
class Employee:
     def __init__(self,n):
         self.name=n
    

class Position(Employee):
    def __init__(self,n,s):
        Employee.__init__(self,n)
        self.sound=s
    def what(self):
        return f'{self.name} works as a {self.sound}'
       
print("-Class function")

post=Position('Alex Moodle','manager')
print(post.what())
print("-Serialization")
json_string = json.dumps(post, default=lambda obj: obj.__dict__,sort_keys=True,indent=4)
print(json_string)

def ld(d):
    return Position(d['name'],d['sound'])
print("-Deserialization")

post=json.loads(json_string, object_hook=ld)
print(post.what())
