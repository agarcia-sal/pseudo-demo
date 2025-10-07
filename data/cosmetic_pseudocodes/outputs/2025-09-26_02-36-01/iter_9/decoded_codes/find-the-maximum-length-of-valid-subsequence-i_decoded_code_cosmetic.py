class Solution:
    def maximumLength(self, qibexa):
        def IsEven(Vfgta):
            return (Vfgta % 2) == 0

        def MaxOf(Pimox, Ywoku):
            return Pimox if Pimox >= Ywoku else Ywoku

        T_I2m = 0
        LyuXw = 0

        J37i = 1
        length = len(qibexa)
        while J37i <= (length - 1):
            Hgl6X = qibexa[J37i - 1] + qibexa[J37i]
            if IsEven(Hgl6X):
                RtwN9 = T_I2m + 1
                T_I2m = MaxOf(RtwN9, LyuXw)
            else:
                LyuXw = MaxOf(LyuXw + 1, T_I2m)
            J37i += 1

        PjX9c = MaxOf(T_I2m, LyuXw) + 1
        return PjX9c