def binary_search(item_list,item):
    first=0
    last=len(item_list)-1
    found=False
    while(first<=last and not found):
        mid=(first+last)//2
        if item_list[mid]==item:
            found=True
            print("element found in the position:",mid)
        else:
                if item<item_list[mid]:
                    last=mid-1
                else:
                    first+mid+1
                if(found==false):
                            print("element not found")
                            a=[]
                            n=int(input("enter the number of elements:"))
                            for i in range(0,n):
                                b=int(input("enter the number to be searched:"))
                                a.append(b)
                                x=int(input("enter the number to be searched:"))
                                binary_search(a,x)
