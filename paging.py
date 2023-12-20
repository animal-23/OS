<<<<<<< HEAD
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
=======
no_of_pages = int(input('Enter the number of pages: '))
page_size = int(input('Enter the page size: '))

mem_size = no_of_pages*page_size
print('Total size of memory: ', mem_size)
no_of_frames = int(input('Enter the number of frames: '))

page_table = []

for i in range(no_of_pages):
    fno = int(input(f'Enter frame number for page {i+1}: '))
    page_table.append([i, fno])
    
inp_pno, inp_off = map(int, input('Enter page number and offset: ').split())
inp_fra = None

for i in page_table:
    if i[0] == inp_pno:
        inp_fra = i[1]

if inp_fra is None:
    print('Page not found')
else:
    base_reg = int(input('Enter the base register: '))
    phy_add = base_reg + inp_fra * page_size + inp_off
    print('Physical address is: ', phy_add)
>>>>>>> 0bce224 (Eigth commit)
