# 题目描述，给定 4 个小于 10 的正整数，可以使用加减乘除四种运算以及括号将这 4 个数连接起来得到一个表达式。
# 现在的问题是，是否存在一种方式使得得到的表达式的结果等于 24。
# 加减乘除及括号的运算结果与运算优先度与平时的定义一致（除法为实数除法）
#
# 样例输入：
# [5, 5, 5, 1]
# 样例输出：
# False


# 代码
def get_24(nums):
    """
    用于求 nums 中的数字能否通过加减乘除与括号得到 24

    思路：
        有 4 个数进行运算，我们假设第一个数进行了乘法运算，那么就相当于用剩下的两个数与第一个数乘法的结果凑出 24。
        由此可见，我们可以将问题拆分为多个子问题求解。因此，自然而然地想到递归。

        递归状态：
            1. 初始状态：4个数、结果数24
            2. 递归过程：
                a. 从 nums 中随机抽取两个数，分别进行四则运算（注意：减法与除法不可逆，除法的分母不能为 0）
                b. 从 nums 移除选取的两个数（在进行递归后复原），并将运算结果添加到 nums 中
            3. 边界条件：若数组中只剩一个数，则判断该数是否等于 24 并返回结果

    :param nums: type:list 存放数的数组
    :return: type:bool 返回是否能凑出 24
    """
    if len(nums) == 1:
        if nums[0] == 24:
            return True
        return False
    else:
        for i in range(len(nums) - 1):
            for j in range(i + 1, len(nums)):
                # 存取运算后剩下的数
                temp = []
                for x in nums:
                    if x != nums[i] and x != nums[j]:
                        temp.append(x)
                # 加法
                temp.append(nums[i] + nums[j])
                if get_24(temp): return True
                temp.pop()
                # 减法
                temp.append(nums[i] - nums[j])
                if get_24(temp): return True
                temp.pop()
                temp.append(nums[j] - nums[i])
                if get_24(temp): return True
                temp.pop()
                # 乘法
                temp.append(nums[i] * nums[j])
                if get_24(temp): return True
                temp.pop()
                # 除法
                if nums[i]:
                    temp.append(nums[j] / nums[i])
                    if get_24(temp): return True
                    temp.pop()
                if nums[j]:
                    temp.append(nums[i] / nums[j])
                    if get_24(temp): return True
                    temp.pop()
        return False


if __name__ == "__main__":
    print(get_24([1, 2, 4, 1]))
    print(get_24([5, 5, 5, 1]))
    print(get_24([7, 5, 9, 8]))
    print(get_24([1, 5, 9, 8]))
    print(get_24([8, 3, 2, 5]))
