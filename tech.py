


list=[1,2,3,4,5,6,7,8,9,0,23,34,45,57]

def tail(array, n=10):
    print(len(array))
    for line in array[len(array)-n:]:
        print(line)

#tail(list)

log =['10.1.2.1 - car [01/Mar/2022:13:05:05 +0900] "GET /python HTTP/1.0" 200 222',
      '10.1.1.9 - dog [01/Mar/2022:13:05:15 +0900] "GET /python HTTP/1.0" 200 222']

def parse1():
    for i in log:
        print(i.split("[")[1].split("]")[0])

def parse3():
    for i in log:
        print(" ".join(i.split()[3:5]).strip("[]"))

num =[1,2,3]
def sqnum(nums):
    print(sum(x**2 for x in nums if x>0))


class FunEvent:
    def __init__(self, tags,year):
       self.tags =tags
       self.year =year

    def __str__(self):
        return f"FunEvent(tags ={self.tags}, year = {self.year})"


tags=["google", "ml"]
year =2022
bootcamp = FunEvent(tags,year)
tags.append("ootcamp")
year =2023
print(bootcamp)
