def group_anagrams(words):
    groups = {}
    for item in words:
        key = "".join(sorted(item))
        if key in groups:
            groups[key].append(item)
        else:
            groups[key] = [item]
    return list(groups.values())
def main():
    group_anagrams(["bat"])#[["bat", "tab"], ["eat", "tea"], ["tan", "nat"]]
if __name__ == "__main__":
    main()