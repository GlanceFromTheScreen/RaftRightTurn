from main_algorithm import start_raft
from raft import raft, river_turn, nabla_phi
from vizualization_lib.raft_visualisation.main import vizualization
from constraints import *


if __name__ == '__main__':
    raft11 = raft({'w': 20, 'h': 70, 'a': 5, 'q': 5})
    river11 = river_turn(40, 60)
    eps11 = 0.1
    param11 = 'q'

    move_params = start_raft(raft11, river11, eps11, param11)
    vizualization(move_params[0], move_params[1], move_params[2],
                  raft11.params_values, river11.corner_coords)

    print('f: ', raft11.square())