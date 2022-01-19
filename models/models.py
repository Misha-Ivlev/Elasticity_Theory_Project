from typing import List


class MaterialPoint:
    def __init__(self, id_number, coord_x, coord_y, vel_x, vel_y, x_0, y_0, time):
        self.id = id_number
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.x_0 = x_0
        self.y_0 = y_0
        self.t = time


class MaterialBody:
    def __init__(self, material_points: List[MaterialPoint]):
        self.material_points = material_points


class PointTrajectory:
    def __init__(self, material_point: MaterialPoint, x=[], y=[]):
        self.material_point = material_point
        self.x = x
        self.y = y


class BodyTrajectory:
    def __init__(self, material_body: MaterialBody, points_trajectory):
        self.points_trajectory = points_trajectory
        self.material_body = material_body


class SpacePoint:
    def __init__(self, id_number, coord_x, coord_y, vel_x, vel_y, time):
        self.id = id_number
        self.coord_x = coord_x
        self.coord_y = coord_y
        self.vel_x = vel_x
        self.vel_y = vel_y
        self.t = time


class SpaceGrid:
    def __init__(self, space_points: List[SpacePoint]):
        self.space_points = space_points
