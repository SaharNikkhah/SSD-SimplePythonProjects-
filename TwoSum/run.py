#Third Version by SNI(just because we are both SN =))))))))))))))))
#SNI Thanks for the code I think you did it all, I will change few things
#from loguru import logger#// SNI: I Do not know what this is? And looked it up seems like i need to install a package for it well I wont!


class TwoSum:
    def __init__(self, num, target):
        self.num = num
        self.target = target

    # def __call__():

    def twosum(self):  # bayad baghei self haram beidm?SNI vagheyat fek konam faghat self o bas bedi=)))))))
        for index, value in enumerate(self.num):# SNI this was nice I did not know about enumerate
        # for i in range(len(self.num)):  # other methods for this like enumerate
            # https://www.techiedelight.com/loop-through-list-with-index-python/ //SNI WELL THANK YOU SO MUCH
            # for methods of class, self. is needed? //SNI I feel like yes!
            # loop over indexing?
            sub=self.target-self.num[index]
            if sub in self.num:
                return [index, self.num.index(sub)]

if __name__ == '__main__':
    list=[0,2,4,5]
    number=6
    tmp= TwoSum (list,number)

    print (tmp.twosum())
    #tmp.twosum()
    #logger.info(f'Done!')

# what other options?
# the code is not as beautiful as I like to be
# not neat very much, where i used indexing
# and where i used long lines
