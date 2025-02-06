def k_most_frequent(lst, k):
    occurences, highest, kth = {}, 0, []
    for i in range(len(lst)):
        if hasher(lst[i]) not in occurences.keys():
            occurences.update({hasher(lst[i]):[lst[i]]})
            if  highest == 0:
                highest = 1
        else:
            occurences[hasher(lst[i])].append(lst[i])
            if len(occurences[hasher(lst[i])]) >= k and lst[i] not in kth:
                kth.append(lst[i])
                highest += 1
    if highest <= k:
        for key in occurences.keys():
            kth.append(occurences[key][0])
    if len(lst) == 0:
        kth = []
    return kth
def hasher(word):
    return(hash(word))
def main():
    k_most_frequent([], 1)
if __name__ == "__main__":
    main()
