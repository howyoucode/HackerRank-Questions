import os



#
# Complete the 'stringAnagram' function below.
#
# The function is expected to return an INTEGER_ARRAY.
# The function accepts following parameters:
#  1. STRING_ARRAY dictionary
#  2. STRING_ARRAY query
#

def stringAnagram(dictionary, query):
    freq_map = {}
    
    for word in dictionary:
        sorted_word = ''.join(sorted(word))
        if sorted_word in freq_map:
            freq_map[sorted_word] += 1
        else:
            freq_map[sorted_word] = 1
    
    result = []
    for q in query:
        sorted_q = ''.join(sorted(q))
        result.append(freq_map.get(sorted_q, 0))
    
    return result

if __name__ == '__main__':
    fptr = open(os.environ['OUTPUT_PATH'], 'w')

    dictionary_count = int(input().strip())

    dictionary = []

    for _ in range(dictionary_count):
        dictionary_item = input()
        dictionary.append(dictionary_item)

    query_count = int(input().strip())

    query = []

    for _ in range(query_count):
        query_item = input()
        query.append(query_item)

    result = stringAnagram(dictionary, query)

    fptr.write('\n'.join(map(str, result)))
    fptr.write('\n')

    fptr.close()
