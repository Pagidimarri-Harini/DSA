class Solution:
    def minimumRecolors(self, blocks: str, k: int) -> int:
        i, j, count = 1, k, 0
        minops = sys.maxsize
        bcount = blocks[:k].count("B")
        print("smth",bcount)
        while j < len(blocks):
            minops = min(minops, k - bcount)
            
            if blocks[j] == "B":
                bcount += 1
            if blocks[i-1] == "B":
                bcount  -= 1
            print(minops, bcount)
            i += 1
            j += 1
        minops = min(minops, k - bcount)
        return minops        


        