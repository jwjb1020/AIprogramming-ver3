from setup import Setup


class HillClimbing:
    def __init__(self):
        Setup.__init__(self)
        self._pType = 0
        self._limitStock = 100

    def run(self):
        pass

    def displaySetting(self):
        if self._pType == 1:  # Numeric일떄
            print()
            print("Mutation step size : ", self._delta)
            print()

    def setVariables(self, pType):
        self._pType = pType


class SteepedAscent(HillClimbing):
    def run(self, p):
        current = p.randomInit()  # 'current' is a list of values
        valueC = p.evaluate(current)
        while True:
            neighbors = p.mutants(current)
            successor, valueS = self.bestOf(neighbors)
            if valueS >= valueC:
                break
            else:
                current = successor
                valueC = valueS
        p.storeResult(current, valueC)

    def bestOf(self, neighbors, p):
        best = neighbors[0]  # 'best' is a value list
        bestValue = p.evaluate(best)
        for i in range(1, len(neighbors)):
            newValue = p.evaluate(neighbors[i])
            if newValue < bestValue:
                best = neighbors[i]
                bestValue = newValue
        return best, bestValue

    def displaySetting(self):
        print()
        print("Search algorithm: Steepest-Ascent Hill Climbing")
        HillClimbing.displaySetting(self)


class FirstChoice(HillClimbing):
    def run(self, p):
        current = p.randomInit()  # 'current' is a list of values
        valueC = p.evaluate(current)
        i = 0
        while i < self._LIMIT_STUCK:
            successor = p.randomMutant(current)
            valueS = p.evaluate(successor)
            if valueS < valueC:
                current = successor
                valueC = valueS
                i = 0  # Reset stuck counter
            else:
                i += 1
        p.storeResult(current, valueC)

    def displaySetting(self):
        print()
        print("Search algorithm: First-Choice Hill Climbing")
        print()
        print("Mutation step size:", self._delta())
        print("Max evaluations with no improvement: {0:,} iterations".format(self._LIMIT_STUCK))


class GradientDescent(HillClimbing):
    def run(self, p):
        current = (
            p.randomInit()
        )  # 'current' is a list of values, 계속 업데이트 되는 파트/ randomInit()-> 시작점을 모르기 떄매 random하게 넣어쥼
        valueC = p.evaluate(current)  # valueC 시작점에 해당하는 함수값
        while True:
            successor = p.takeStep(current, valueC)  # 한번더 값을 계산하는것을 방지하기 위해 valueC추가
            valueS = p.evaluate(successor)  # successor(제일 좋은 변수), valueS(제일 좋은 함수값)
            if valueS >= valueC:  # 현재보다 좋은지 비교(후보값: valueS)
                break  # 후보값이 더 크면 나빠진 것임으로 탈출
            else:
                current = successor
                valueC = valueS
        p.storeResult(current, valueC)

    def displaySetting(self):
        print()
        print("Search algorithm : Gradient Descent")
        print()
        print("Mutation step size:", self._alpha())
