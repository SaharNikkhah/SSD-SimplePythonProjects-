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
            if (self.target-self.num[index]) in self.num:
                logger.info(f' [{index}, {self.num.index(abs(self.num[index]-self.target))}]')
                break
            else:
                logger.info(f'not founded!')
                break

if __name__ == '__main__':
    tmp = TwoSum(num = [2,3,4,5], target = 6)
    tmp.twosum()
    logger.info(f'Done!')

# what other options?
# the code is not as beautiful as I like to be
# not neat very much, where i used indexing
# and where i used long lines
