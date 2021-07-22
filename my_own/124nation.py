#124나라의 숫자
'''


'''
from itertools import product

def sum_of_product(n):
    return (3 ** (n + 1) - 3) / 2
    


def solution(n):
    
    num = [1,2,4]
    s = []
    i = 0
    cnt = 1

    while n > i:
      i += 3 ** cnt
      cnt += 1

    i -= 3 ** (cnt - 1)
    for x in range(cnt - 1):
      s.append('num')
                
    c = ','.join(s) #문자열로 만들고
    c = 'list(product(' + c + '))' #해당 자릿수만큼의 경우의 수를 생성
            
    #해당 자릿수에서, 나올 수 있는 num
    print('n:{}, i:{}, cnt:{}, i - n:{}'.format(n,i,cnt, n-i))
    sequence = n - i
    result = eval(c)
    result = result[sequence - 1]

    print(c)
    c = ''.join(map(str, result))

    return int(c)


print(solution(20))
