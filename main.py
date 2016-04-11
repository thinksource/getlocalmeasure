import solution as sl

def array2StringOutput(a):
    re=""
    if len(a)==0:
        return "<No Output>"
    else:
        for i in a:
            re+=str(i+1)+','
        return re[:-1]


if __name__ =="__main__":
    textToSearch = "Peter told me that peter the pickle piper piped a pitted pickle before he petered out. Phew!"
    subtext="Peter"
    r=sl.find(textToSearch,subtext)
    print subtext, array2StringOutput(r)
    subtext="peter"
    print subtext, "'%s'" % array2StringOutput(sl.find(textToSearch,subtext))
    subtext="pick"
    print subtext, "'%s'" % array2StringOutput(sl.find(textToSearch,subtext))
    subtext="pi"
    print subtext, "'%s'" % array2StringOutput(sl.find(textToSearch,subtext))
    subtext="Z"
    print subtext, "'%s'" % array2StringOutput(sl.find(textToSearch,subtext))
    subtext="Peterz"
    print subtext, "'%s'" % array2StringOutput(sl.find(textToSearch,subtext))
