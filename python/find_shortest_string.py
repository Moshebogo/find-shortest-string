class Solution:
    def find_shortest_string(self, array):
        shortest = array[0]
        for string in array:
            if len(string) < len(shortest):
                shortest = string
        return shortest        



if __name__ == '__main__':
    s = Solution()
    print(s.find_shortest_string(['aaa', 'bb', 'c']))
