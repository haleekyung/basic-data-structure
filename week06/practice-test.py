import practiceCheckBrackets as cb

str = ('[0]', 'if( (i==0)', 'A[ (i+1] ) =0;')
for s in str:
    m = cb.Stack.checkBrackets(s)
    print(s, '-->', m)


