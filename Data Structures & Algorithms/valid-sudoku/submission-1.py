class Solution:
    def isValidSudoku(self, board: List[List[str]]) -> bool:
        flag=True
        c1 = set()
        c2 = set()
        c3 = set()
        c4 = set()
        c5 = set()
        c6 = set()
        c7 = set()
        c8 = set()
        c9 = set()
        b1 = set()
        b2 = set()
        b3 = set()
        b4 = set()
        b5 = set()
        b6 = set()
        b7 = set()
        b8 = set()
        b9 = set()
        for i in range(9):
            a = set()
            for j in range(9):
                if (board[i][j]=="."):
                    continue
                if (board[i][j] in a):
                    flag=False
                    return flag
                a.add(board[i][j])
                if (j==0):
                    if (board[i][0] in b1):
                        flag=False
                        return flag
                    b1.add(board[i][0])
                if (j==1):
                    if (board[i][1] in b2):
                        flag=False
                        return flag
                    b2.add(board[i][1])
                if (j==2):
                    if (board[i][2] in b3):
                        flag=False
                        return flag
                    b3.add(board[i][2])
                if (j==3):
                    if (board[i][3] in b4):
                        flag=False
                        return flag
                    b4.add(board[i][3])
                if (j==4):
                    if (board[i][4] in b5):
                        flag=False
                        return flag
                    b5.add(board[i][4])
                if (j==5):
                    if (board[i][5] in b6):
                        flag=False
                        return flag
                    b6.add(board[i][5])
                if (j==6):
                    if (board[i][6] in b7):
                        flag=False
                        return flag
                    b7.add(board[i][6])
                if (j==7):
                    if (board[i][7] in b8):
                        flag=False
                        return flag
                    b8.add(board[i][7])
                if (j==8):
                    if (board[i][8] in b9):
                        flag=False
                        return flag
                    b9.add(board[i][8])
                if (j<3 and i<3):
                    if (board[i][j] in c1):
                        flag=False
                        return flag
                    c1.add(board[i][j])
                if ((j>=3 and j<6) and i<3):
                    if (board[i][j] in c2):
                        flag=False
                        return flag
                    c2.add(board[i][j])
                if (j>=6 and i<3):
                    if (board[i][j] in c3):
                        flag=False
                        return flag
                    c3.add(board[i][j])
                if (j<3 and (i>=3 and i<6)):
                    if (board[i][j] in c4):
                        flag=False
                        return flag
                    c4.add(board[i][j])
                if ((j>=3 and j<6) and (i>=3 and i<6)):
                    if (board[i][j] in c5):
                        flag=False
                        return flag
                    c5.add(board[i][j])
                if (j>6 and (i>=3 and i<6)):
                    if (board[i][j] in c6):
                        flag=False
                        return flag
                    c6.add(board[i][j])
                if (j<3 and i>=6):
                    if (board[i][j] in c7):
                        flag=False
                        return flag
                    c7.add(board[i][j])
                if ((j>=3 and j<6) and i>=6):
                    if (board[i][j] in c8):
                        flag=False
                        return flag
                    c8.add(board[i][j])
                if (j>=6 and i>=6):
                    if (board[i][j] in c9):
                        flag=False
                        return flag
                    c9.add(board[i][j])
        return flag