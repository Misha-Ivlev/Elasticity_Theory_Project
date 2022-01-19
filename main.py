from managers.managers import create_material_body
from managers.managers import move_material_body
from managers.managers import plot_body_trajectory
from managers.managers import move_through_space
from managers.managers import create_space_points


material_body = create_material_body(1, 1, 10)
plot_body_trajectory(move_material_body(1, 0.01, material_body))

n = 10
space_grid = create_space_points(1, 1, n)
move_through_space(1, 0.1, n, space_grid)