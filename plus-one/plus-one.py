class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        # convert to number
        num = ''
        for item in digits:
            num += str(item)
        num = int(num) + 1

        output = []
        for item in str(num):
            output.append(item)
        return output
