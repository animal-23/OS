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
