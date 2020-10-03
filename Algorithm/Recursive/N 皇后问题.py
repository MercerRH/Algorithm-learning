# 题目描述：
#    输入一个正整数 n，要求 n 个国际象棋的皇后在 n*n 的棋盘上不能相互攻击。输出全部摆放方案。
#    皇后能攻击到相同行、相同列及对角线上的所有棋子

# 样例输入：
#     4
#
# 样例输出：
#     2 4 1 3
#     3 1 4 2
#
# 解释：
#     输出结果中的每一行都代表一种摆法，行里的第 i 个数字如果是 n，就代表第 i 行的皇后应该放在第 n 列
#     皇后的行、列编号都是从 1 开始算。

# 代码：
def NQueen(n):
    """
    用于输出N皇后问题的各种解法。

    思路：
        使用递归进行穷举，判断每一行放置皇后的位置是否会与先前的皇后产生冲突

    :param n: 正整数，表示皇后的个数
    :return: None
    """
    queen = []  # 棋子列表，用于储存皇后的位置，第 i 个数表示第 i 行皇后的位置

    def set_position(k):
        """用于在第 k 行放置可行的皇后位置"""
        if k < n:
            for i in range(n):  # 对第 k 行的所有位置进行遍历
                for x,y in enumerate(queen):  # 判断所放的位置是否会与先前的皇后位置产生冲突，x/y 分别为行与列
                    if (k==x) or (i==y) or (abs(k-x)==abs(i-y)):
                        break
                else:  # 若未产生冲突则将位置添加到 queen 中
                    queen.append(i)
                    set_position(k+1)  # 递归放置下一行的皇后
                    queen.pop()  # 在递归结束时将刚刚插入栈的值弹出以避免影响后序递归
        else:
            print([i+1 for i in queen])  # 当 k==n 即单次遍历完成时，queen 中储存的即为结果，将其值加一后打印（因为实际的行数是从1开始的）

    set_position(0)


if __name__ == "__main__":
    NQueen(5)