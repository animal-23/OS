n=int(input("Enter the number of files: "))
filelength=[]
startingblock=[]
allocationblock=[]
for i in range(n):
    filelength.append(int(input(f"Enter the length of the file {i+1}:")))
    startingblock.append(int(input(f"Enter the starting block of the file {i+1}:")))
    allocationblock.append(list(range(startingblock[i],filelength[i]+startingblock[i])))
print("Filename\tStartingBlock\tLength")
for i in range(n):
    print(f"{i+1}\t\t{startingblock[i]}\t\t{filelength[i]}")
x=int(input("Enter the file name to retrieve the information:"))
if 1<=x<=n:
    print("File name:",x)
    print("Starting Block:",startingblock[x-1])
    print("File length:",filelength[x-1])
    print("Blocks Occupied are:")
    for block in allocationblock[x - 1]:
        print(block,end=" ")
else:
    print("Invalid file name.")
