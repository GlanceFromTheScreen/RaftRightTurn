from One_D_Problem_file import *

FUN1 = lambda t: 1  # ...заптсываем в начале файла функции ограничений для каждого из этапов (на каждый этап по две-три?)


class raft:
    def __init__(self):
        self.params_is_fixed = {'w': None, 'h': None, 'a': None, 'q': 34}  # None => unfixed param
        self.params_values = {'w': 0, 'h': 0, 'a': 0, 'q': 34}  #  потом сделать repalce None на 0 (без хардкода)

    def square(self):
        return self.params_values['w'] * self.params_values['h'] +\
               self.params_values['a'] * self.params_values['q']

    def gradient_evaluate(self):
        return {'w': 0 if self.params_is_fixed['w'] is not None else self.params_values['h'],
                'h': 0 if self.params_is_fixed['h'] is not None else self.params_values['w'],
                'a': 0 if self.params_is_fixed['a'] is not None else self.params_values['q'],
                'q': 0 if self.params_is_fixed['q'] is not None else self.params_values['a']}


class river_turn:
    def __init__(self):
        self.corner_coords = [1, 1]  # z1, z2


class raft_makes_right_turn:  # или лучше отнаследоваться?
    def __init__(self):
        self.accuracy = 0.001  # точность, с которой мы будем решать задачу. Согласовать её с этапами
        self.my_raft = raft()  # здесь содержится максимизируемая функция
        self.my_river = river_turn()
        self.distance = lambda t: t**2  # потом настоящее представление этой фцнкции написать - брать данные из my_raft and my_river

        pr = One_D_Problem()
        pr.target_function = self.distance
        self.distance_min = pr.golden_search(self.accuracy)
        #  добавить ограничения на сами переменные (x,y) и на stages

        # предлагаю вывести здесь значения x, y, а потом отнаследоваться и сделать stages.
        # нет, так не получится, потому что t будет определяться разными точками
        # тогда наверное этот класс - это общий интерфейс, а конкретные реализации функций - канкретные объекты
        # то есть в объектах надо будет менять функции ограничений

        # в таком случае должен быть здесь метод решения задачи. По сути получается, что этот класс - это stage

        # та точка, которая скользит по верхнему берегу определяет каждое из ограничений. Поэтому просто меняя
        # функции ограничений, мы таким образом переходим от stage к stage


def stages_execute():
    stage_1 = raft_makes_right_turn()
    #  определяю плот и реку
    #  определяю функции ограничения
    #  вычисляю решение. Если True, то

    stage_2 = stage_1
    #  изменяем функции ограничения
    #  вычисляю решение. Если True, то...



# Test area

raft1 = raft()
raft1.params_values['w'] = 99
print(raft1.gradient_evaluate())

pr1 = One_D_Problem()
pr1.target_function = lambda t: t**2

print(pr1.target_function(5))
print(pr1.golden_search(0.001))








