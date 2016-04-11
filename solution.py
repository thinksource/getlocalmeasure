def make_delta1(p):
    p=p.lower()
    ALPHABET_LEN = 256
    i = 0
    patternlen = len(p)
    delta1 = [0] * ALPHABET_LEN

    while i < ALPHABET_LEN:
        delta1[i] = patternlen
        i += 1

    i = 0
    while i < patternlen-1:
        delta1[ord(p[i])] = patternlen-1 - i
        i += 1
    return delta1

def find(s, p):
    # find first occurrence of p in s
    n = len(s)
    m = len(p)
    skip = make_delta1(p)[ord(p[m-1])]
    i = 0
    re=[]
    while i <= n-m:
        if s[i+m-1].lower() == p[m-1].lower(): # (boyer-moore)
            # potential match
            if s[i:i+m-1].lower() == p[:m-1].lower():
                re.append(i)
            if i+m<n and s[i+m].lower() not in p.lower():
                i = i + m + 1 # (sunday)
            else:
                i = i + skip # (horspool)
        else:
            # skip
            if i+m<n and s[i+m].lower() not in p.lower():
                i = i + m + 1 # (sunday)
            else:
                i = i + 1
    return re
