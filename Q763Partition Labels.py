class Solution:
    def partitionLabels(self, S):
        """
        :type S: str
        :rtype: List[int]
        """
        result = []
        while(S):
            value = S[0]
            lastoccur = S.rfind(S[0])
            flag = 0
            while(flag == 0):
                sub = S[:lastoccur+1]
                print(sub)
                for i in sub:
                    #print(i)
                    #print(lastoccur)
                    if(lastoccur < S.rfind(i)):
                        print(sub.rfind(i))
                        lastoccur = S.rfind(i)
                        tempV = i

                if(lastoccur == S.rfind(value)):
                    flag = 1
                    result.append(lastoccur+1)
                    S = S[lastoccur+1:]
                    #print(S)
                    if(S):
                        lastoccur = S.rfind(S[0])
                else:
                    value = tempV
        
        return result
            