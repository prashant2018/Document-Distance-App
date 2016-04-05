import time
import math
class DocDist(object):

    def __init__(self,doc):
        self.doc = doc

    def readDoc(self):
        self.d = {}
       
        ch = self.doc.split()
        for i in ch:
            self.d.setdefault(i,0)
            self.d[i]+=1
        return self.d


def findingDistance(d1,d2):

    l1=0
    l2=0

    for i in d1:
        if i not in d2:
            d2[i] = 0
        l1 = l1 + pow(d1[i],2)

    for i in d2:
        if i not in d1:
            d1[i] = 0
        l2 = l2 + pow(d2[i],2)

    l1 = math.sqrt(l1)
    l2 = math.sqrt(l2)
    product = l1*l2
    s=0

    if len(d1) > len(d2):
        d = d1
    else:
        d = d2

    for i in d:
        try:
            s = s + (d1[i]*d2[i])/product
        except:
            pass
    print(d1)
    print(d2)
    return s*100

def main_prog(f1,f2):
	obj1 = DocDist(f1)
	obj2 = DocDist(f2)
	x1 = obj1.readDoc()
	x2 = obj2.readDoc()
	result = findingDistance(x1,x2)
	#print(result)
	return round(result,2)

