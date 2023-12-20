<<<<<<< HEAD
count_seg=int(input("Enter the number of segments: "))
seg_table=[]
for i in range(count_seg):
    print("enter the base and limit of segment",i)
    base,limit=map(int,input().split())
    seg_table.append([base,limit])
print(seg_table)
print("Enter logical address:")
seg_no,off=map(int,input().split())
if 0<=seg_no<count_seg:
    if 0<=off<seg_table[seg_no][1]:
        mac=seg_table[seg_no][0]+off
        print("physical address: ",mac)
    else:
        print("offset is greater than limit: ")
else:
    print("Invalid segment number")
=======
import traceback

no_of_segments = int(input('Enter the no of segments: '))

seg_table = {}

for i in range(no_of_segments):
    name = input('Enter the name of the segment: ')
    s_base,s_size = map(int, input(f'Enter the base and size of {name} segment: ').split())
    seg_table.update({name:[s_base,s_size]})

seg_name, offset = map(str, input(f'Enter logical address as segment name and offset: ').split())

try:
    seg = seg_table[seg_name]
except Exception:
    traceback.print_exc()

if 0 <= int(offset) < seg[1]:
    phy_add = seg[0] + int(offset)
    print('Physical address of given logical address is: ',phy_add)
else:
    print('Offset is greater than limit')
>>>>>>> 0bce224 (Eigth commit)
