# Вычисление остальных значений матрицы сравнений по формуле
def fillTheMatrix(matrix, num):
    for i in range(matrix.__len__()):
        for j in range(matrix.__len__()):
            if i == j or j == num:
                continue
            else:
                matrix[i][j] = matrix[i][num] / matrix[j][num]


class Solution:
    def __init__(self):
        # Множество возможных альтернатив
        self.X = 6
        # Множество возможных критериев
        self.P = 5
        # Массив для названий фильмов
        self.filmArr = []
        # Зададим матрицу парных сравнений в общем виде
        self.matrix = [[1, 0, 0, 0, 0, 0], [0, 1, 0, 0, 0, 0], [0, 0, 1, 0, 0, 0], [0, 0, 0, 1, 0, 0],
                       [0, 0, 0, 0, 1, 0], [0, 0, 0, 0, 0, 1]]
        # Матрица парных сравнений для критериев
        self.criteriaMatrix = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]
        # Массив для хранения всех матриц
        self.array = []
        self.critArray = []
        # Массив, где мы суммируем элементы i-ого столбца
        self.newArr = []

    # Функция для ввода названий фильмов
    def films(self):
        for i in range(self.X):
            print("Введите название фильма " + str(i) + ":")
            self.filmArr.append(input())

    # Заполнение критериев
    def criteria(self):
        print("Введите номер фильма от 0 до 5, относительно которого будет проводиться сравнение(те фильм n "
              "лучше по критерию, чем остальные фильмы, на значение): ")
        num = input()
        for j in range(self.X):
            if j == int(num):
                continue
            else:
                print("Фильм " + str(num) + " лучше, чем фильм " + str(j) + "\nВведите значение для критерия: ")
                self.matrix[j][int(num)] = int(input())
        fillTheMatrix(self.matrix, int(num))
        self.array.append(self.matrix)
        print(self.matrix)
        self.criteriaMatrix = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]

    # Добавление весов для критериев
    def addNodes(self):
        print("Введите номер критерия от 0 до 4, относительно которого будет проводиться сравнение(те критерий n "
              "более важен, чем остальные критерии, на значение): ")
        numm = input()
        for j in range(self.P):
            if j == int(numm):
                continue
            else:
                print("Критерий " + str(numm) + " более важен, чем критерий " + str(j) + "\nВведите значение: ")
                self.criteriaMatrix[j][int(numm)] = int(input())
        fillTheMatrix(self.criteriaMatrix, int(numm))
        self.critArray.append(self.criteriaMatrix)
        print(self.criteriaMatrix)
        self.criteriaMatrix = [[1, 0, 0, 0, 0], [0, 1, 0, 0, 0], [0, 0, 1, 0, 0], [0, 0, 0, 1, 0], [0, 0, 0, 0, 1]]

    # Подсчет при равновесных критериях
    def equal(self, array, films):
        for i in range(self.P - 1):
            matrix = array[i]
            self.newArr.append([sum(x) for x in zip(*matrix)])
        self.count(films, )

    # Подсчет при неравновесных критериях
    def unequal(self, critArray, films):
        newArray = []
        for i in range(critArray.__len__()):
            matrixCrit = critArray[i]
            newArray.append([sum(x) for x in zip(*matrixCrit)])
        for h in range(critArray.__len__()):
            self.newArr[h] = self.newArr[h]**newArray[h]
        self.count(films)

    # Подсчет
    def count(self, films):
        l = 10000000
        res = 0
        for k in range(self.newArr.__len__()):
            for j in range(self.X):
                if l > self.newArr[k][j]:
                    l = self.newArr[k][j]
                    res = j
        return films[res]

    # Решение поставленной задачи
    def solve(self):
        self.films()
        print("По условию задачи существует 5 критериев оценки")
        for i in range(self.P):
            print("По критерию " + str(i + 1))
            self.criteria()
        print("Теперь введем весы для критериев")
        self.addNodes()
        print("При равновесных критериях: " + str(self.equal(self.array, self.filmArr)))
        print("При неравновесных критериях: " + str(self.unequal(self.critArray, self.filmArr)))


solve = Solution()
solve.solve()
