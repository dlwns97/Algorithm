s=input()
ans=0
if '-' in s:
    s=s.split('-')
    for i in range(len(s)):
        tmp=sum(list(map(int,s[i].split('+'))))
        if i==0:
            ans+=tmp
        else:
            ans-=tmp
else:
    s=list(map(int,s.split('+')))
    for item in s:
        ans+=item
        
print(ans)
