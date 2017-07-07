start = input("what is your the start number?")
end = input("what is your end number?")

def generatenumbers(start,end):
    while start < end:
        print (start)
        start = start + 1


generatenumbers(int(start),int(end))
