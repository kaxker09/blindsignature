from crypto import genkeys, signature, blindsignature, removeblind, blindvar

#generowanie klucza dla A
na,ea,da = genkeys()

#generowanie klucza dla B
nb,eb,db = genkeys()

sig = signature(da,na)

r = blindvar(na)

blind = blindsignature(ea,na,da,r)

rems = removeblind(r,na,bs=blind)

print(sig)
print(rems)