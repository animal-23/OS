class File:
    def __init__(self, fname="", start=0, size=0):
        self.fname = fname
        self.start = start
        self.size = size
        self.block = [start+i for i in range(size)]
n = int(input("Enter the number of files: "))
files = [File() for _ in range(n)]
for file in files:
    file.fname = input("Enter file name: ")
    file.start = int(input("Enter starting block: "))
    file.size = int(input("Enter number of blocks: "))
    file.block = [file.start + int(input("Enter block number: ")) for _ in range(file.size)]
print("\nFile\tstart\tsize\tblock")
for file in files:
    print(f"{file.fname}\t{file.start}\t{file.size}\t", end="")
    print("-->".join(map(str, file.block)))
