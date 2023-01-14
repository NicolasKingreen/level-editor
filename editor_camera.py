import pygame.mouse
from pygame.math import Vector2


class EditorCamera:

    def __init__(self, camera):
        self.drag_debounce = 0.032  # ~2 frames (at 60fps)

        self.camera = camera
        self.click_origin = Vector2()
        self.drag_sensitivity = 30.0

    def update(self, frame_time_s):
        mouse_pos = Vector2(pygame.mouse.get_pos())
        if pygame.mouse.get_pressed()[0]:
            if self.drag_debounce > 0:
                self.click_origin = mouse_pos
                self.drag_debounce -= frame_time_s
            else:
                delta = mouse_pos - self.click_origin
                self.camera.position -= delta * frame_time_s * self.drag_sensitivity
                self.click_origin = self.click_origin.lerp(mouse_pos, frame_time_s * 12)

        if self.drag_debounce <= 0 and not pygame.mouse.get_pressed()[0]:
            self.drag_debounce = 0.032

        # print(mouse_pos, self.click_origin, self.camera.position, self.drag_debounce)
