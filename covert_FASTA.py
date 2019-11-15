import os
def read(name):
    file=open(name)
    seq=file.read()
    seq=seq.split('\n')
    title=seq[0]
    del seq[0]
    for i in range(len(seq)):
        seq[i]=list(seq[i])
    return title,seq
def main(seq):
    for i in range(len(seq)):
        j=0
        while j < len(seq[i]):
                if seq[i][j] not in ['a','t','g','c','A','T','G','C','u','U','n','N']:
                    del seq[i][j]
                else:
                    j=j+1
    k=0
    while k < len(seq):
            if len(seq[k])==0:
                del seq[k]
            else:
                k=k+1
    return seq
def write(title,seq):
    os.system("touch result.FASTA")
    file=open("result.FASTA",'w')
    state=file.write(">covert Sequence")
    state=file.write(title)
    state=file.write("\n")
    for i in range(len(seq)):
        for j in range(len(seq[i])):
            state=file.write(seq[i][j])
        state=file.write("\n")
    file.close()
name=input("please input your file path:")
title,seq=read(name)
seq_result=main(seq)
write(title,seq_result)
