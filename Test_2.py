from raft import *

if __name__ == '__main__':
    print('-----------------')

    raft1 = raft({'w': 4, 'h': 8, 'a': 2, 'q': 3})
    river1 = river_turn(8, 5)
    t0, t1 = raft1.find_t0_t1('1')
    t00, t11 = raft1.find_t0_t1('2_b')
    t000, t111 = raft1.find_t0_t1('3_b', river1.corner_coords[1])  # не забывать вписывать!!!
    print(t0, t1)
    print(t00, t11)
    print(t000, t111)

    plot_fun(t0, t1, t00, t11, t000, t111, phi1_stage_2_b, raft1, river1)
    print('U: ', phi1_stage_3(raft1, river1, 10.64))

    print()

    stage_1 = raft_makes_right_turn_stage(raft1, river1, t0, t1, phi1_stage_1)
    t_star = stage_1.constraint(raft1)
    print(t_star)
    print(stage_1.phi_1(raft1, river1, t_star))

    print()

    stage_2_b = raft_makes_right_turn_stage(raft1, river1, t00, t11, phi1_stage_2_b)
    t_star = stage_2_b.constraint(raft1)
    print(t_star)
    print(stage_2_b.phi_1(raft1, river1, t_star))

    print()

    stage_3_b = raft_makes_right_turn_stage(raft1, river1, t000, t111, phi1_stage_3)
    t_star = stage_3_b.constraint(raft1)
    print(t_star)
    print(stage_3_b.phi_1(raft1, river1, t_star))

