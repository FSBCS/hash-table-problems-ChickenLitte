def k_most_frequent(lst, k):
    if k <= 0:
        return []

    counts = {}
    for e in lst:
        counts[e] = counts.get(e, 0) + 1

    leaderboard = sorted(counts, key=lambda x: counts[x], reverse=True)
    
    if k > len(leaderboard):
        return leaderboard

    i = min(len(leaderboard)-1, k)

    while i < len(leaderboard) and counts[leaderboard[i]] == counts[leaderboard[k-1]]:
        i += 1

    return leaderboard[:i]

def main():
    print(k_most_frequent([1, 1, 1, 2, 2, 3], 2))  # Example usage
    print(k_most_frequent([], 1))  # Test with empty list

if __name__ == "__main__":
    main()