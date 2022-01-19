from managers.managers import create_material_body
from managers.managers import move_material_body
from managers.managers import plot_body_trajectory


material_body = create_material_body(1, 1, 10)
plot_body_trajectory(move_material_body(1, 0.01, material_body))