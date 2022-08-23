from loguru import logger


class TwoSum:
    def __init__(self, num, target):
        self.num = num
        self.target = target

    # def __call__():

    def twosum(self):  # bayad baghei self haram beidm?
        for index, value in enumerate(self.num):
        # for i in range(len(self.num)):  # other methods for this like enumerate
            # https://www.techiedelight.com/loop-through-list-with-index-python/
            # for methods of class, self. is needed?
            # loop over indexing?
            if abs(self.num[index]-self.target) in self.num:
                # print(self.num[index])
                print(f' [{index}, {self.num.index(abs(self.num[index]-self.target))}]')
                # the print line is not beautiful
                # also uses logger instead of prints
                break
            # else:
            #     logger.info(f'not founded!')
            # else is not completed

if __name__ == '__main__':
    tmp = TwoSum(num = [2,3,4,5], target = 6)
    tmp.twosum()
    # there is a bug, try target 1 :D

# what other oprions?
