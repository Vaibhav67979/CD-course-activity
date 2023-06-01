def isterminal(char):
    if (char.isupper() or char == "`"):
        return False
    else:
        return True


def insert(grammar, lhs, rhs):
    if (lhs in grammar and rhs not in grammar[lhs] and grammar[lhs] != "null"):
        grammar[lhs].append(rhs)
    elif (lhs not in grammar or grammar[lhs] == "null"):
        grammar[lhs] = [rhs]
    return grammar


def first(lhs, grammar, grammar_first):
    rhs = grammar[lhs]
    for i in rhs:
        k = 0
        flag = 0
        current = []
        confirm = 0
        flog = 0
        if (lhs in grammar and "`" in grammar_first[lhs]):
            flog = 1
        while (1):
            check = []
            if (k >= len(i)):
                if (len(current) == 0 or flag == 1 or confirm == k or flog == 1):
                    grammar_first = insert(grammar_first, lhs, "`")
                break
            if (i[k].isupper()):
                if (grammar_first[i[k]] == "null"):
                    grammar_first = first(i[k], grammar, grammar_first)
                # print("state ", lhs, "i ", i, "k, ", k, grammar_first[i[k]])
                for j in grammar_first[i[k]]:
                    grammar_first = insert(grammar_first, lhs, j)
                    check.append(j)
            else:
                grammar_first = insert(grammar_first, lhs, i[k])
                check.append(i[k])
            if (i[k] == "`"):
                flag = 1
            current.extend(check)
            if ("`" not in check):
                if (flog == 1):
                    grammar_first = insert(grammar_first, lhs, "`")
                break
            else:
                confirm += 1
                k += 1
                grammar_first[lhs].remove("`")
    return (grammar_first)
