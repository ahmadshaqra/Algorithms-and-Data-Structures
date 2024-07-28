"""
    Edit Distance

    Function: Finds the minimum number of edits required to transform word n to word m
    Time Complexity (Worst): O(n*m)
    Space Complexity (Auxiliary): O(n*m)

"""

def edit_distance(word_n: str, word_m: str) -> int:
        
    # initialises memo array
    distance = [[] for _ in range(len(word_n)+1)]
    for n in range(len(distance)):
        distance[n] = [0 for _ in range(len(word_m)+1)]
    
    # initialises base cases
    for n in range(len(word_n)+1):
        distance[n][0] = n
    for m in range(len(word_m)+1):
        distance[0][m] = m
    
    # finds distance[n][m] which contains min edit distance for word_n[0...n] and word_m[0...m], for each n and m
    for n in range(1, len(word_n)+1):
        for m in range(1, len(word_m)+1):
            if word_n[n-1] == word_m[m-1]:
                distance[n][m] = distance[n-1][m-1]
            else:
                distance[n][m] = min(distance[n-1][m-1], distance[n-1][m], distance[n][m-1]) + 1

    # returns min edit distance from word n to m
    return distance[len(word_n)][len(word_m)]

if __name__ == '__main__':
    word_n = "two"
    word_m = "four"
    print(f"Edit Distance from '{word_n}' to '{word_m}' = {edit_distance(word_n, word_m)}")
    