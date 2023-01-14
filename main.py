import pygame
from pygame.locals import *

from camera import Camera
from editor_camera import EditorCamera
from grid import Grid


WIN_SIZE = 640, 480
WIN_WIDTH, WIN_HEIGHT = WIN_SIZE
TARGET_FPS = 60


class Application:
    def __init__(self):
        pygame.init()
        pygame.display.set_caption("Level Editor")
        self.screen = pygame.display.set_mode(WIN_SIZE)
        self.clock = pygame.time.Clock()
        self.running = True

        self.camera = Camera()
        self.editor_camera = EditorCamera(self.camera)
        self.grid = Grid()

    def run(self):
        while self.running:
            frame_time_ms = self.clock.tick(TARGET_FPS)
            frame_time_s = frame_time_ms / 1000.0

            self.handle_events()
            self.update(frame_time_s)
            self.draw()

    def handle_events(self):
        for event in pygame.event.get():
            if event.type == QUIT:
                self.running = False
            elif event.type == KEYDOWN:
                if event.key == K_ESCAPE:
                    self.running = False
                elif event.key == K_w:
                    self.camera.move_direction.y = -1
                elif event.key == K_s:
                    self.camera.move_direction.y = 1
                elif event.key == K_a:
                    self.camera.move_direction.x = -1
                elif event.key == K_d:
                    self.camera.move_direction.x = 1
            elif event.type == KEYUP:
                if event.key == K_w or event.key == K_s:
                    self.camera.move_direction.y = 0
                elif event.key == K_a or event.key == K_d:
                    self.camera.move_direction.x = 0
            elif event.type == MOUSEBUTTONDOWN:
                if event.button == 1:
                    self.on_left_mouse_down(event.pos)
                elif event.button == 3:
                    self.on_right_mouse_down(event.pos)

    def on_left_mouse_down(self, pos):
        pass

    def on_right_mouse_down(self, pos):
        pass

    def update(self, frame_time_s):
        self.camera.update(frame_time_s)
        self.editor_camera.update(frame_time_s)
        self.grid.position = -self.camera.position

    def draw(self):
        self.screen.fill((255, 255, 255))
        self.grid.draw(self.screen)
        pygame.display.flip()


if __name__ == '__main__':
    Application().run()
