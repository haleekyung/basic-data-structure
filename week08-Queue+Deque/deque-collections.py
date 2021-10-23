import collections


dq = collections.deque( 'data' )
for elem in dq:
    print(elem.upper(), end='')

print()
dq.append('r')
dq.appendleft('k')
print(dq)
dq.pop()
dq.popleft()
print(dq[-1])
print('x' in dq)
dq.extend('structure')
dq.extendleft(reversed('python'))
print()