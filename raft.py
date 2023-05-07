from One_D_Problem_file import *


FUN1 = lambda t: 1  # ...заптсываем в начале файла функции ограничений для каждого из этапов (на каждый этап по две-три?)


def phi1_stage_1(w, h, a, q, t):
    return w + h + t


class raft:
    def __init__(self, param_dict):
        self.params_is_fixed = param_dict
        self.params_values = {k: w or 0 for(k, w) in self.params_is_fixed.items}

    def square(self):
        return self.params_values['w'] * self.params_values['h'] +\
               self.params_values['a'] * self.params_values['q']

    def gradient_evaluate(self):
        return {'w': 0 if self.params_is_fixed['w'] is not None else self.params_values['h'],
                'h': 0 if self.params_is_fixed['h'] is not None else self.params_values['w'],
                'a': 0 if self.params_is_fixed['a'] is not None else self.params_values['q'],
                'q': 0 if self.params_is_fixed['q'] is not None else self.params_values['a']}


class river_turn:
    def __init__(self, z1, z2):
        self.corner_coords = [z1, z2]


class raft_makes_right_turn:  # или лучше отнаследоваться?
    def __init__(self, z1, z2, param_dict):
        self.accuracy = 0.001  # точность, с которой мы будем решать задачу. Согласовать её с этапами
        self.my_river = river_turn(z1, z2)
        self.my_raft = raft(param_dict)  # допустимая точка
        #  меняем параметры плота - ставим допустмую точку

        self.distance = lambda t: phi1_stage_1(self.my_raft.params_values['w'],
                                               self.my_raft.params_values['h'],
                                               self.my_raft.params_values['a'],
                                               self.my_raft.params_values['q'],
                                               t)
        # потом настоящее представление этой фцнкции написать - брать данные из my_raft and my_river

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


    def phi_gradient_evaluate(self):
        eps = 0.01
        return {'w': 0 if self.my_raft.params_is_fixed['w'] is not None else 1 / (2*eps) * (self.distance_min(self.my_raft.params_values['w'] + eps) - self.distance_min(self.my_raft.params_values['w'] - eps)),
                'h': 0 if self.params_is_fixed['h'] is not None else self.params_values['w'],
                'a': 0 if self.params_is_fixed['a'] is not None else self.params_values['q'],
                'q': 0 if self.params_is_fixed['q'] is not None else self.params_values['a']}

def stages_execute():
    stage_1 = raft_makes_right_turn(10, 10, {'w': None, 'h': 2, 'a': None, 'q': None})  # передать координаты угла и параметры (словариком None / not None)
    #  определяю плот и реку
    #  определяю функции ограничения
    #  вычисляю решение. Если True, то

    stage_2 = stage_1
    #  изменяем функции ограничения
    #  вычисляю решение. Если True, то...



# Test area

raft1 = raft({'w': None, 'h': None, 'a': None, 'q': 34})
raft1.params_values['w'] = 99
print(raft1.gradient_evaluate())

pr1 = One_D_Problem()
pr1.target_function = lambda t: t**2

print(pr1.target_function(5))
print(pr1.golden_search(0.001))








