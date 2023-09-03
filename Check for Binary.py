# Return true if str is binary, else false
def isBinary(str):
    #code here
    x=int(str)
    c=0
    d=0
    while x!=0:
        r=x%10
        x=x//10
        if r==1 or r==0:
            c=c+1
        d=d+1
    if c==d:
        return True
    else:
        return False
