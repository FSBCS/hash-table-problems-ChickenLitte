def group_anagrams(words):
    result = {}
    for i in range(len(words)):
        print(words[i],hasher(words[i]))
        if hasher(words[i]) not in result.keys():
            result.update({hasher(words[i]):[words[i]]})
            print("new")
        else:
            result[hasher(words[i])].append(words[i])
            print(hasher(words[i]),"old")
    print(result)
    final = []
    for val in result.keys():
        final.append(result[val]) 
    return final
def hasher(word,mod = 13):
    # combinedVal = 0
    # for char in word:
    #     combinedVal += ord(char)
    # return combinedVal % mod
    val = 0 
    word = sort(word)
    for i in range(0,len(word)):
        val += ord(word[i]) * 31^i 
    return val

def sort(word):
        word = list(word)
        for i in range(0,len(word)):
            smallestElement = i
            for j in range(i,len(word)):
                if word[j]<=word[smallestElement]:smallestElement = j#set the new smallest element
            word[i],word[smallestElement] = word[smallestElement],word[i]#swap stuff
        return ''.join(word)

def main():
    words = ["bat", "tab", "eat",  "tea", "tan", "nat"]
    group_anagrams(words)
if __name__ == "__main__":
    main()
# Given a list of strings, group the strings into lists of anagrams. Return the groups as a list of lists. For example, if the input is: ["bat", "meta", "tab", "tea", "ate", "tame", "jazz" "eat"], the output would be: [["bat", "tab"], ["meta", "tame"], ["tea", "ate", "eat"],["jazz"]]
# If three words are anagrams, what common key could we store to represent them in a hash table?
# To convert a list to a string, we can use `''.join(someList)` to concatenate the elements of the list to the empty string.