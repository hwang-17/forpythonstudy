def fab(n):
    tu1=1
    tu2=1
    tu3=1
    if n<1:
        print("wrong inputs")
        return -1

    while (n-2)>0:
        tu3=tu2+tu1
        tu1=tu2
        tu2=tu3
        n=n-1

    return tu3

result = fab(20)

if result!=-1:
    print("there are %d Tuzi: " %(result))
