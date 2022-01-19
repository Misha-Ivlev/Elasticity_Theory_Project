from models.models import MaterialPoint
from models.models import MaterialBody
from models.models import BodyTrajectory
from models.models import PointTrajectory
from math import ceil
from math import exp
import matplotlib.pyplot as plt


def create_material_body(x0, y0, n):
    material_points = []
    id_number = 0
    for i in range(n + 1):
        id_number -= 1
        material_points.append(MaterialPoint(id_number, x0 + i * 2 / n, y0,
                                             0, y0, x0 + i * 2 / n, y0, 0))

    for j in range(n + 1):
        id_number -= 1
        material_points.append(MaterialPoint(id_number, x0 + 2, y0 + j * 2 / n,
                                             0, y0, x0 + 2, y0 + j * 2 / n, 0))

    for i in range(n + 1):
        id_number -= 1
        material_points.append(MaterialPoint(id_number, x0 + 2 - i * 2 / n, y0 + 2,
                                             0, y0, x0 + 2 - i * 2 / n, y0 + 2, 0))

    for j in range(n + 1):
        id_number -= 1
        material_points.append(MaterialPoint(id_number, x0, y0 + 2 - j * 2 / n,
                                             0, y0, x0, y0 + 2 - j * 2 / n, 0))

    id_number = 0
    for i in range(n + 1):
        for j in range(n + 1):
            material_points.append(MaterialPoint(id_number, x0 + i*2/n, y0 + j*2/n, 0, y0,
                                                 x0 + i*2/n, y0 + j*2/n, 0))
            id_number += 1
    return MaterialBody(material_points)


def move_material_body(time, h, material_body: MaterialBody):
    body_trajectory = BodyTrajectory(material_body, [])
    points_trajectory = []

    def function_x(var, t):
        return - t * t * var

    def function_y(var, t):
        return exp(t) * var

    for material_point in material_body.material_points:
        x = [material_point.x_0]
        y = [material_point.y_0]
        for i in range(1, ceil(time/h) + 1):
            x.append(x[-1] + h/2 * function_x(x[-1], h*(i-1)) + h/2*function_x(h*function_x(x[-1], h*(i-1)), h*i))
            y.append(y[-1] + h/2 * function_y(y[-1], h*(i-1)) + h/2*function_y(h*function_y(y[-1], h*(i-1)), h*i))
        points_trajectory.append(PointTrajectory(material_point, x, y))
    body_trajectory.points_trajectory = points_trajectory
    return body_trajectory


def plot_body_trajectory(body_trajectory: BodyTrajectory):
    initial_position = [[], []]
    final_position = [[], []]
    for i in range(body_trajectory.points_trajectory.__len__()):
        if body_trajectory.points_trajectory[i].material_point.id < 0:
            initial_position[0].append(body_trajectory.points_trajectory[i].material_point.x_0)
            initial_position[1].append(body_trajectory.points_trajectory[i].material_point.y_0)
            final_position[0].append(body_trajectory.points_trajectory[i].x[-1])
            final_position[1].append(body_trajectory.points_trajectory[i].y[-1])
    plt.plot(initial_position[0], initial_position[1])
    for i in range(body_trajectory.points_trajectory.__len__()):
        plt.plot(body_trajectory.points_trajectory[i].x, body_trajectory.points_trajectory[i].y)

    plt.plot(final_position[0], final_position[1])
    plt.show()
