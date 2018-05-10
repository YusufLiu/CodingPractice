class Solution:
    def countBattleships(self, board):
        """
        :type board: List[List[str]]
        :rtype: int
        """
        count = 0
        value = 0
        for i in range(len(board)):
            for j in range(len(board[0])):
                if(board[i][j]=='X'):
                    value = 1
                    if(i>0 and board[i-1][j]=='X'): 
                        value = 0
                    if(j>0 and board[i][j-1] =='X'): 
                        value = 0
                count += value
                value =0
        return count