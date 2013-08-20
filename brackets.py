import sys

def re1(n):
    ret = set()
    if n == 0 :
        return ''
    elif n == 1 :
        return set(['()'])
    else :
        for item in re1(n-1):
            for i in range(len(item)+1) :
                ret.add(item[0:i]+'()'+item[i:])
        print n , len(ret), ret
        return ret

def DFS(num_l, num_r, str):
    if num_l == 0 and num_r == 0 :
        print str
    else :
        if num_l > 0 :
            DFS(num_l-1, num_r, str+"(")
        if num_r > 0 and num_r > num_l:
            DFS(num_l, num_r-1, str+")")
    return
    


if __name__ == '__main__':
    if len(sys.argv) > 1 :
        DFS(int(sys.argv[1]), int(sys.argv[1]), "")
    else:
        DFS(5,5,"")        

