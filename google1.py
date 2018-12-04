def solve(S,K):
    s = S.replace("-","").upper()[::-1]
    sol = ""
    aux = 1
    while aux <= len(s):
        sol = sol + s[aux-1]
            if aux%K == 0 and aux != len(s):
                sol = sol + "-"
        aux += 1
    return sol[::-1]
print(solve("2-4A0r7-4k", 3)) #24-A0r-74k
