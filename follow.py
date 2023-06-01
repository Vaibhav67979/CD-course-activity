from first import insert, first
from main import grammar_first

def rec_follow(k, next_i, grammar_follow, i, grammar, start, grammar_first, lhs):
    if len(k) == next_i:
        if grammar_follow[i] == "null":
            grammar_follow = follow(i, grammar, grammar_follow, start)
        for q in grammar_follow[i]:
            grammar_follow = insert(grammar_follow, lhs, q)
    else:
        if k[next_i].isupper():
            for q in grammar_first[k[next_i]]:
                if (q == "`"):
                    grammar_follow = rec_follow(k, next_i + 1, grammar_follow, i, grammar, start, grammar_first, lhs)
                else:
                    grammar_follow = insert(grammar_follow, lhs, q)
        else:
            grammar_follow = insert(grammar_follow, lhs, k[next_i])

    return (grammar_follow)


def follow(lhs, grammar, grammar_follow, start):
    for i in grammar:
        j = grammar[i]
        for k in j:
            if (lhs in k):
                next_i = k.index(lhs) + 1
                grammar_follow = rec_follow(k, next_i, grammar_follow, i, grammar, start, grammar_first, lhs)
    if (lhs == start):
        grammar_follow = insert(grammar_follow, lhs, "$")
    return (grammar_follow)