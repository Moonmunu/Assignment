file_name=""
file_name=input("enter file name")
arr=[]
arr=[]
#open('kkk.tsv', "r+") , Here we can put the full path of a tsv file in place of 'kkk.tsv'
with open(file_name,"r+") as file:
    for i in file.readlines():
        #if header is there and header contains # or any other specific symbol we can mention here
        if '#' not in i:
            #split() will convert the line into a list
            i=i.split('\t')
            #Iterating new list
            for j in i:
                #Identifying the last column
                if "\n" in j or j==str(i[len(i)-1]):
                    j=j.replace('\n', "")
                    arr.append(j)

def SelectionSorting(arr,n):

    # One by one move boundary of unsorted subarray
    for i in range(n):
        min_index = i
        min_str = arr[i]

        # Find the minimum element in unsorted subarray
        for j in range(i+1,n):

            # If min_str is greater than arr[j]
            if min_str>arr[j]:

                # Make arr[j] as min_str and update min_index as j
                min_str = arr[j]
                min_index = j

        # Swap the found minimum element with the first element
        if min_index != i:

            # Store the first element in temp
            temp = arr[i]

            # Place the min element at the first position
            arr[i] = arr[min_index]

            # place the element in temp at min_index
            arr[min_index] = temp

    # Return the sorted array
    return arr

result=""
print("\nSorted last Column are")
for i in range(len(SelectionSorting(arr,len(arr)))):
    result+=SelectionSorting(arr,len(arr))[i]
    print("   ",SelectionSorting(arr,len(arr))[i])