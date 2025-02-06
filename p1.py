def group_anagrams(words):
    result = {}
    for i in range(len(words)):
        if hasher(words[i]) not in result.keys():
            result.update({hasher(words[i]):[words[i]]})
        else:
            result[hasher(words[i])].append(words[i])
    final = []
    for val in result.keys():
        final.append(result[val]) 
    print(final)
    return final
def hasher(word,mod = 13):
    word = sort(word)
    return hash(word)

def sort(word):
        word = list(word)
        word.sort()
        return ''.join(word)

def main():
    words = ["bat", "tab", "eat", "tea", "tan", "nat"]
    group_anagrams(words)
if __name__ == "__main__":
    main()
# Given a list of strings, group the strings into lists of anagrams. Return the groups as a list of lists. For example, if the input is: ["bat", "meta", "tab", "tea", "ate", "tame", "jazz" "eat"], the output would be: [["bat", "tab"], ["meta", "tame"], ["tea", "ate", "eat"],["jazz"]]
# If three words are anagrams, what common key could we store to represent them in a hash table?
# To convert a list to a string, we can use `''.join(someList)` to concatenate the elements of the list to the empty string.