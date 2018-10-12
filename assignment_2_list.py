def match_ends(words):
    count=0
    for i in range(0,len(words)):
        if words[i]=='':
            pass
        elif words[i][0]==words[i][-1] and len(words[i])>=2:
            count+=1
    return count
def front_x(words):
    x_list=[]
    l=[]
    for i in words:
        if i.startswith('x')==True:
            x_list.append(i)
        else:
            l.append(i)
    x_list.sort()
    l.sort()
    words=x_list+l
    return words
def sort_last(tuples):
    temp=()
    for j in range(0,len(tuples)):
        for i in range(0,len(tuples)-1):
            if tuples[i][-1]>tuples[i+1][-1]:
                temp=tuples[i]
                tuples[i]=tuples[i+1]
                tuples[i+1]=temp
    return tuples
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))
def main():
  print('match_ends')
  test(match_ends(['aba', 'xyz', 'aa', 'x', 'bbb']), 3)
  test(match_ends(['', 'x', 'xy', 'xyx', 'xx']), 2)
  test(match_ends(['aaa', 'be', 'abc', 'hello']), 1)

  print()
  print('front_x')
  test(front_x(['bbb', 'ccc', 'axx', 'xzz', 'xaa']),
       ['xaa', 'xzz', 'axx', 'bbb', 'ccc'])
  test(front_x(['ccc', 'bbb', 'aaa', 'xcc', 'xaa']),
       ['xaa', 'xcc', 'aaa', 'bbb', 'ccc'])
  test(front_x(['mix', 'xyz', 'apple', 'xanadu', 'aardvark']),
       ['xanadu', 'xyz', 'aardvark', 'apple', 'mix'])

       
  print()
  print('sort_last')
  test(sort_last([(1, 3), (3, 2), (2, 1)]),
       [(2, 1), (3, 2), (1, 3)])
  test(sort_last([(2, 3), (1, 2), (3, 1)]),
       [(3, 1), (1, 2), (2, 3)])
  test(sort_last([(1, 7), (1, 3), (3, 4, 5), (2, 2)]),
       [(2, 2), (1, 3), (3, 4, 5), (1, 7)])


if __name__ == '__main__':
  main()
            
        
    
