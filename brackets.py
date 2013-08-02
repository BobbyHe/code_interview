import sys

def main(n):
    ret = set()
    if n == 0 :
        return ''
    elif n == 1 :
        return set(['()'])
    else :
        for item in main(n-1):
            for i in range(len(item)+1) :
                ret.add(item[0:i]+'()'+item[i:])
        print n , len(ret), ret
        return ret

if __name__ == '__main__':
    main(9)        