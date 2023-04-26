import copy
import math

def solution(N: int, A: list):
    rank = set_rank(A, N)
    return ''.join([get_rank(i, rank) for i in A])


def get_rank(score: int, rank: dict):
    if score in rank['A']:
        return 'A'
    elif score in rank['B']:
        return 'B'
    else:
        return 'C'


def set_rank(score_list: list, N):
    reverse_A = list(score_list)
    reverse_A.sort(reverse=True)

    N = len(reverse_A)
    A_line = round(N * 0.3)
    B_line = round(N * 0.7)

    rank = {
        'A': reverse_A[:A_line],
        'B': reverse_A[A_line:B_line],
        'C': reverse_A[B_line:]
    }

    check_rank = copy.deepcopy(rank)

    for a in set(rank['A']):
        check_rank['A'].remove(a)
    for b in set(rank['B']):
        check_rank['B'].remove(b)
    for c in set(rank['C']):
        check_rank['C'].remove(c)

    if len(check_rank['A']) != 0:
        for i in range(len(check_rank['A'])):

    if len(check_rank['B']) != 0:
        for i in range(len(check_rank['B'])):
            rank['B'].remove(check_rank['B'][i])

    if len(check_rank['C']) != 0:
        for i in range(len(check_rank['C'])):
            rank['C'].remove(check_rank['C'][i])

    return rank
