import pandas as pd

print("Welcome to student Data Portal")
ans='y'
data={"Name":[],"sid":[],"address":[],"m1":[],"m2":[],"m3":[],"total":[],"avg":[],"grade":[]}
while ans=='y':
    class Student:
                def __init__(self):
                   self. name=input("name:")
                   self.sid=int(input("sid:"))
                   self.ads=input("address:")

    class Marks():
                def __init__(self):
                    self.m1=int(input("m1:"))
                    self.m2=int(input("m2:"))
                    self.m3=int(input("m3:"))
                    self.t=self.m1+self.m2+self.m3
                    self.a=self.t/3
    class dis1(Student):
                
                def details(self):
                
                    data["Name"].append(self.name)
                    data["sid"].append(self.sid)
                    data["address"].append(self.ads)
                    
    class dis2(Marks):
                def marks(self):
                    data["m1"].append(self.m1)
                    data["m2"].append(self.m2)
                    data["m3"].append(self.m3)
                    data["total"].append(self.t)
                    data["avg"].append(self.a)
                    if (self.m1>=40 and self.m2>=40 and self.m3>=40):
                      if(self.a>=60):
                        data["grade"].append("firstclass")
                      elif(self.a>=50):
                        data["grade"].append("Second Class")
                      else:
                        data["grade"].append("third class")
                    else:
                      data["grade"].append("Failed")
    

              
    d=dis1()
    d2=dis2()
    d.details()
    d2.marks()
    
    
    col=["name","sid","address","m1","m2","m3","tot","avg","grade"]
    df=pd.DataFrame(data)    
    df.to_csv("st.csv",index=False)
    print("Do you like to insert student")
    ans=input()  

        



  
