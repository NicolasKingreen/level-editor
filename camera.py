from pygame.math import Vector2


class Camera:

    def __init__(self):
        self.position = Vector2()
        self.move_direction = Vector2()
        self.speed = 100

        self.width = 640
        self.height = 480
        self.zoom = 1.0

    def update(self, frame_time_s):
        self.position += self.move_direction * self.speed * frame_time_s
