def solution(bin1, bin2):
    bin_sum = int(bin1, 2) + int(bin2, 2)
    return bin(bin_sum)[2:]