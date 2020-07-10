import sys, os

def IsExist(fileName):
    return os.path.exists(fileName)

def GetTrunkSize(fileName, cnt):
    size = os.path.getsize(fileName) / int(cnt) + 1
    return int(size)

def SpliteFile(fileName, cnt):
    if not IsExist(fileName):
        return False

    file = open(fileName, 'rb')
    trunkSize = GetTrunkSize(fileName, cnt)
    index = 0
    while True and index < int(cnt):
        name = '{}{}'.format(fileName, index)
        buf = file.read(trunkSize)
        if not buf:
            break

        newFile = open(name, 'wb')
        newFile.write(buf)
        newFile.close()
        index += 1
    
    file.close()
    return True

if __name__ == '__main__':
    while True:      
        fileName = input('File to be Split?')
        if not fileName:
            break

        if not IsExist(fileName):
            print('{} not exist'.format(fileName))
            continue

        cnt = input('Split count?')
        if int(cnt) <= 1:
            print('{} is not valid count'.format(cnt))
            continue

        if SpliteFile(fileName, cnt):
            print('spliter ok')
        else:
            print('failed to split file {}'.format(fileName))

        break