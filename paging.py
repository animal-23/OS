memo=int(input("Enter the memory size: "))
page=int(input("Enter the page size: "))
countp=memo//page
print("No of pages available : ",countp)
countf=int(input("enter the number of frames: "))
print("total size of memory: ",page*countf)
page_table=[]
for i in range(countp):
    fnum=int(input("Enter frame numbers:"))
    page_table.append([i,fnum])
print("Page table: ")
print(page_table)
pno,off=map(int,input("Enter the logical address:  ").split())
frame=None
for i in page_table:
    if (i[0]==pno):
        frame=i[1]
if (frame==None):
    print("Page not found")
else:
    base=int(input("Enter the base register: "))
    mac=base+frame*page+off
    print("Physical address is : ",mac)
