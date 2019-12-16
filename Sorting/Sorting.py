def sort(array,noOfElements):
    for startIndex in range(noOfElements):
        for currentIndex in range(startIndex,noOfElements):
            if array[currentIndex] < array[startIndex]:
                array[currentIndex],array[startIndex] = array[startIndex],array[currentIndex]
            
def main():
    noOfElements = int(input('Enter the numbers of elements:'))
    array =[]
    for x in range(noOfElements):
        print('Enter element number ',x)
        array.append(int(input()))
    sort(array,noOfElements)
    print('The array before sorting:',array)
    print('The array after sorting:',array)
    input()
main()
