import math

import pygame

from vizualization_lib.raft_visualisation.Colors import *
from vizualization_lib.raft_visualisation.Window import *
from vizualization_lib.raft_visualisation.River import *
from vizualization_lib.raft_visualisation.Params import *
from vizualization_lib.raft_visualisation.Window import *


class Raft():
    river = River()
    raft_width = 40
    raft_height = 81.375
    triangle_width = 20
    triangle_height = 30
    # x_s = [20.000000000000025, 21.062725706207296, 22.11658408034231, 23.16141844090993, 24.197047781381094, 25.2232645614457, 26.239832059334397, 27.246481199681998, 28.242906747999488, 29.22876273216201, 30.20365691066588, 31.167144052822653, 32.118717721798276, 33.057800148952325, 33.98372964443217, 34.89574478465068, 35.79296432105058, 36.674361316461514, 37.53872935293218, 38.384637628136595, 39.210370120670895, 39.21037012067088, 40.190629373687656, 41.170888626704425, 42.1511478797212, 43.131407132737976, 44.111666385754745, 45.09192563877152, 46.0721848917883, 47.052444144805065, 48.03270339782184, 49.01296265083862, 49.993221903855385, 50.97348115687216, 51.95374040988894, 52.933999662905705, 53.91425891592248, 54.89451816893926, 55.874777421956026, 56.8550366749728, 57.83529592798958, 58.815555181006346, 58.81555518100632, 59.472022594522166, 60.1231124606571, 60.768510500203384, 61.40786482641933, 62.04077933710849, 62.666805523706685, 63.28543220654868, 63.89607251452753, 64.49804714509261, 65.09056251404677, 65.67268174417174, 66.24328539020485, 66.80101706974331, 67.34420622493407, 67.8707550046495, 68.37796647367622, 68.86227194650789, 69.31877381360057, 69.74042326994832, 70.11639653232515]
    # y_s = [70.6875, 70.66306910501775, 70.58925825455816, 70.46519492854512, 70.28987114686993, 70.0621311694307, 69.78065675187443, 69.44394948076112, 69.05030958153017, 68.59781042191128, 68.0842677070307, 67.50720205849225, 66.86379325617625, 66.15082385096639, 65.36460905749578, 64.50090869816364, 63.55481532006661, 62.5206101668373, 61.39157499850932, 60.15974203462992, 58.815555181006346, 58.815555181006324, 58.15011579349498, 57.460252226539176, 56.745073695184104, 56.00361037468923, 55.234803746567934, 54.43749533582069, 53.610413499122295, 52.75215783501183, 51.86118067058322, 50.935764924436924, 49.97399743788638, 48.97373658400999, 47.93257257514845, 46.84777834580311, 45.71624811592562, 44.53441962403909, 43.298174376027376, 42.0027077810169, 40.642357229519455, 39.21037012067085, 39.210370120670895, 38.818769755678275, 38.40841094469603, 37.978197390634435, 37.52690161041039, 37.05314188460203, 36.55535368516682, 36.03175386907285, 35.48029525957163, 34.898608252212604, 34.283924594994254, 33.63297618826954, 32.94185808206577, 32.205838820899274, 31.419091014132867, 30.574296748174184, 29.662048330267908, 28.669897149628586, 27.580758922734436, 26.37004537195075, 24.99999999999997]
    # angle_s = [0.0, 1.5064284764424478, 3.0210969716061515, 4.545219776865109, 6.080076675581018, 7.6270244262153115, 9.187509908424518, 10.763085322425246, 12.355425931153778, 13.966350966172335, 15.59784849392494, 17.252105276161174, 18.93154298249816, 20.638862561888782, 22.377099210212396, 24.149691271161764, 25.960567715321645, 27.814260780485824, 29.71605329281452, 31.67217474923203, 33.6900675259798, 33.690067525979785, 34.65040747306981, 35.62200497061353, 36.605555227261036, 37.60181169637998, 38.61159351868443, 39.63579421324216, 40.67539188334486, 41.7314612735829, 42.805188106338996, 43.897886248014, 45.01101841940879, 46.14622138797797, 47.30533688755614, 48.490449941892265, 49.70393688059153, 50.948526221748324, 52.227376901832194, 53.54418030200865, 54.90329555942068, 56.30993247402024, 56.30993247402021, 57.28159408523905, 58.271324088157684, 59.28048266355463, 60.31059398238252, 61.363375503224574, 62.4407743417211, 63.545012916205266, 64.67864693448323, 65.84464006004428, 67.0464615216224, 68.28821591459172, 69.57481919875272, 70.91224271970717, 72.30786042406456, 73.77095818149955, 75.31350853606743, 76.95140239398194, 78.70651756571648, 80.61044543164365, 82.71186262150215]

    # start_x = river.river_corner_x + river.river_width/2 - raft_width/2
    # start_y = raft_height/2

    def up_ledge_center_coord(self,x, y):
        l_x = x - params["raft width"] / 2 + params["dist from left"] + params["triangle width"]/2
        l_y = y - params["raft height"]/2 - params["triangle height"]
        return l_x, l_y

    def down_ledge_center_coord(self, x, y):
        l_x = x - params["raft width"] / 2 + params["dist from left"] + params["triangle width"]/2
        l_y = y + params["raft height"]/2
        return l_x, l_y

    def count_coord_y(self, cur_x, cur_y):
        cur_y -= 5
        if cur_y == 0:
            cur_y = HEIGHT
        return cur_y

    # def count_coordinates(self, x, y, angle):
    #     if y > constant_params["river width"] - 3:
    #         angle = 0
    #         y -= 5
    #     elif y > constant_params["river width"]/2:
    #         angle += 5
    #         x += 5
    #         y -=5
    #     else:
    #         x += 5
    #     if x > Window.WIDTH:
    #        x, y = River.river_corner_x + constant_params["river width"]/2, HEIGHT
    #        angle = 0
    #     return x, y, angle
    #
    def rotate(self, surface, angle, pivot, offset):
        rotated_image = pygame.transform.rotozoom(surface, -angle, 1)  # Rotate the image.
        rotated_offset = offset.rotate(angle)  # Rotate the offset vector.
        # Add the offset vector to the center/pivot point to shift the rect.
        rect = rotated_image.get_rect(center=pivot + rotated_offset)
        return rotated_image, rect  # Return the rotated image and shifted rect.

    def draw_raft(self, sc, x, y,  params, angle=0,):
        # x, y, angle = self.count_coordinates(x, y, angle)
        rect_surf = pygame.Surface((params["raft width"], params["raft height"]), pygame.SRCALPHA)
        rect_surf.fill(Colors.BROWN)
        # rect_surf.set_colorkey(Colors.BLACK)
        pivot = [x, y]
        offset = pygame.math.Vector2(0, 0)
        rotated_image, rect = self.rotate(rect_surf, angle, pivot, offset)
        sc.blit(rotated_image, rect)
        rotated_triangle_points = []
        triangle_points = [
            (x - params["triangle width"] / 2, y - params["raft height"] / 2),
            (x, y - params["raft height"] / 2 - params["triangle height"]),
            (x + params["triangle width"] / 2, y - params["raft height"] / 2)
        ]
        for point in triangle_points:
            rotated_point = self.rotate_point(point, angle, pivot)
            rotated_triangle_points.append(rotated_point)
        pygame.draw.polygon(sc, Colors.BROWN, rotated_triangle_points)

        triangle_points = [
            (x - params["triangle width"] / 2, y + params["raft height"] / 2),
            (x, y + params["raft height"] / 2 + params["triangle height"]),
            (x + params["triangle width"] / 2, y + params["raft height"] / 2)
        ]
        for point in triangle_points:
            rotated_point = self.rotate_point(point, angle, pivot)
            rotated_triangle_points.append(rotated_point)
        pygame.draw.polygon(sc, Colors.BROWN, rotated_triangle_points)

        # return x, y, angle

    def rotate_point(self, point, angle, pivot):
        x, y = point
        px, py = pivot
        nx = px + (x - px) * math.cos(math.radians(angle)) - (y - py) * math.sin(math.radians(angle))
        ny = py + (x - px) * math.sin(math.radians(angle)) + (y - py) * math.cos(math.radians(angle))
        return int(nx), int(ny)
