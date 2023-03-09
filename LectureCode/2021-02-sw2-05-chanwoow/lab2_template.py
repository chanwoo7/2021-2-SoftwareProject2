def solution(lst):
    freq_dict = {k: lst.count(k) for k in set(lst)}

    if len(freq_dict) == 1 or len(freq_dict) == len(lst):
        return []
    else:
        val_max = max(freq_dict.values())
        return [x for x in freq_dict.keys() if freq_dict[x] == val_max]

print(solution([1, 2, 3, 4, 5, 5]))     #[5]
print(solution([12, 17, 19, 17, 23]))   #[17]
print(solution([26, 37, 26, 37, 91]))   #[26, 37]
print(solution([28, 30, 32, 34, 144]))  #[]