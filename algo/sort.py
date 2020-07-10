# 选择排序：每次轮询找出最小值放到新的列表，然后第二小。。。
def SelectSort(arr):
    
    for beg in range(len(arr) - 1):
        for i in range(beg, len(arr)): 
            if arr[beg] > arr[i]:
                arr[beg], arr[i] = arr[i], arr[beg]

if __name__ == '__main__':
    arr = [ 3, 2, 1, 19, 12, 7 ]
    SelectSort(arr)
    print(arr)