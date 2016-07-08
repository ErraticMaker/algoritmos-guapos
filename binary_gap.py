def solution(N):
    
    max_gap = 0
    curr_gap = 0
    while N > 0:
        b = N % 2
        N = N/2
        if ( b == 1 ):
            if curr_gap > max_gap :
                max_gap = curr_gap
            curr_gap = 0
        else:
            curr_gap = curr_gap + 1

    return max_gap
