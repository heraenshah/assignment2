def verbing(s):
    if s[-3:]!='ing' and len(s)>3:
        x=s+'ing'
        return x
    elif s[-3:]=='ing'and len(s)>3:
        x=s+'ly'
        return x
    else:
        return s
def not_bad(s):
    l=s.strip().split()
    if 'not' and 'bad' in l:
        if l.index("not")<l.index("bad"):
            d=''
            for i in range(0,len(l)):
                if l[i]=='not':
                    break
            for j in range(i,len(l)):
                l.pop()
            l.append('good')
            for i in range(0,len(l)):
                if(i==0 or i==len(l)):
                    d=d+l[i]
                else:
                    d=d+' '+l[i]
            return d
        elif l.index("not")>l.index("bad"):
            return s
    elif "not" and "bad!" in l:
        if l.index("not")<l.index("bad!"):
            d=''
            for i in range(0,len(l)):
                if l[i]=='not':
                    break
            for j in range(i,len(l)):
                l.pop()
            l.append('good!')
            for i in range(0,len(l)):
                if(i==0 or i==len(l)):
                    d=d+l[i]
                else:
                    d=d+' '+l[i]
            return d
        elif l.index("not")>l.index("bad!"):
            return s
    else:
        return s
def front_back(a,b):
    x=int(len(a)/2)
    y=int(len(b)/2)
    if len(a)%2==0:
        a_front=a[0:x]
        a_back=a[x:]
    else:
        a_front=a[0:x+1]
        a_back=a[x+1:]
    if len(b)%2==0:
        b_front=b[0:y]
        b_back=b[y:]
    else:
        b_front=b[0:y+1]
        b_back=b[y+1:]
    result=a_front+b_front+a_back+b_back
    return result
def test(got, expected):
  if got == expected:
    prefix = ' OK '
  else:
    prefix = '  X '
  print('%s got: %s expected: %s' % (prefix, repr(got), repr(expected)))


# main() calls the above functions with interesting inputs,
# using the above test() to check if the result is correct or not.
def main():
  print('verbing')
  test(verbing('hail'), 'hailing')
  test(verbing('swiming'), 'swimingly')
  test(verbing('do'), 'do')

  print()
  print('not_bad')
  test(not_bad('This movie is not so bad'), 'This movie is good')
  test(not_bad('This dinner is not that bad!'), 'This dinner is good!')
  test(not_bad('This tea is not hot'), 'This tea is not hot')
  test(not_bad("It's bad yet not"), "It's bad yet not")

  print()
  print('front_back')
  test(front_back('abcd', 'xy'), 'abxcdy')
  test(front_back('abcde', 'xyz'), 'abcxydez')
  test(front_back('Kitten', 'Donut'), 'KitDontenut')

if __name__ == '__main__':
  main()
