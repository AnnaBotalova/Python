class Books:

    def __init__(self,n,a,p,s):
    	self.Name=n
    	self.Author=a
    	self.Pages=p
    	self.PublishingHouse=s
    def Inf(self):
        return f'"{self.Name}" {self.Author} contains {self.Pages} pages'



def GetName(self):
	 return {self.Name}



def GetPage(self):
	 return self.Pages



h1=Books("Fox Hole","Nora Sakavich",336,"Popcorn Books")
h2=Books('Harry Potter',"Joanne Rowling",399,"Rosmen")
h3=Books('Orleans',"Lia Steffi",544,"AST")
h4=Books('Muddy',"Lia Steffi",416,"AST")
h5=Books('Call me by your name',"Andre Asiman",362,"Popcorn Books")


print('map')
a=[h1,h2,h3,h4,h5]
b = []
for i in range(5):
	b.append((GetName(a[i])))
print(b)


s1=GetPage(a[0])
s2=GetPage(a[1])
s3=GetPage(a[2])
s4=GetPage(a[3])
s5=GetPage(a[4])

print('reduce')
s=s1+s2+s3+s4+s5
print(s)
