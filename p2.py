def k_most_frequent(lst, k):
    occurences = {}#Should I even be using a hashing FN?\
    highest = 0
    kth = []
    for i in range(len(lst)):
        print(lst[i],hasher(lst[i]))
        if hasher(lst[i]) not in occurences.keys():
            occurences.update({hasher(lst[i]):[lst[i]]})
            print("new")
            if  highest == 0:
                highest = 1
                #kth.append(lst[i])
                print('hi')
        else:
            occurences[hasher(lst[i])].append(lst[i])
            print(hasher(lst[i]),"old")
            if len(occurences[hasher(lst[i])]) >= k and lst[i] not in kth:
                kth.append(lst[i])
                highest += 1
                print('sup')
        print("highest=",highest,kth)
    if highest <= k:
        for key in occurences.keys():
            kth.append(occurences[key][0])
        print("yikes")
    if len(lst) == 0:
        kth = []
    print(occurences)
    print(kth)
    return kth
def hasher(word):
    return(hash(word))

def main():
    k_most_frequent([], 1)
if __name__ == "__main__":
    main()
#Given a list and a value k, return the k most frequently occurring elements. 
# If there is a tie for kth-most frequent, return all the tied elements. 
# If k is greater than the number of unique elements, return a list of all the unique elements.