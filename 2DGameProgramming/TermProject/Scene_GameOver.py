from pico2d import *
from Scene import *


class GameoverScene(Scene):
    def __init__(self, scene_name='Gameover'):
        Scene.__init__(self, scene_name)
        self.DRAW_TIME = 5
        self._m_Timer = 0.0

    def build_object(self, framework, image_manager, sound_manager):
        Scene.build_object(self, framework, image_manager, sound_manager)

    def update(self, TimeElapsed):
        self._m_Timer += TimeElapsed
        if self._m_Timer > self.DRAW_TIME:
            self._m_Timer = 0.0
            self._m_framework.change_scene('Title')  # TODO: Ranking 구현 후 변경
            self._m_SoundManager.BGM_Title.play(-1)


