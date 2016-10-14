from Scene import *
from Object_Player import *
from Stage import *


class PlayScene(Scene):
    def __init__(self, scene_name='Play'):
        Scene.__init__(self, scene_name)
        # Set Stage
        self._m_Stage = None

        # Set Player
        self._m_Player = None
        self._m_SHAKE_TIME = 0.2
        self._m_pulse_power = 5
        self._m_earth_shake_power = 0
        self._m_Shack_pulse = 0.0
        self._m_ShackTimer = 0.0
        self._m_bShake = False

    def build_object(self, framework, sound_manager, BKImagePath=None):
        Scene.build_object(self, framework, sound_manager)
        self._m_Stage = Stage(self._m_framework.WINDOW_WIDTH, self._m_framework.WINDOW_HEIGHT)
        self._m_BKImage = load_image('Resource\Graphics\Background\Play.png')
        self._m_Player = Player(self._m_SoundManager, self._m_framework.WINDOW_WIDTH / 2, self._m_framework.WINDOW_HEIGHT / 2)
        self._m_Player.targeting(self._m_Stage.MeteorList, self._m_Stage.ItemList)
        self._m_Stage.Player = self._m_Player

    def release(self):
        del self._m_BKImage

    def update(self, TimeElapsed):
        if self._m_Player.crash_check() or self._m_Player.check_hit_earth():
            self._m_bShake = True
            self._m_Shack_pulse = 0.0
            self._m_ShackTimer = 0.0
        self._m_earth_shake_power = self._m_Player.Shake_Earth

        if self._m_bShake:
            self._m_ShackTimer += TimeElapsed
            self._m_Shack_pulse = \
                self._m_Player.ATK * self._m_earth_shake_power * self._m_pulse_power * \
                math.sin(self._m_ShackTimer * 100) * math.pow(0.5, self._m_ShackTimer)
            if self._m_ShackTimer > self._m_SHAKE_TIME:
                self._m_Shack_pulse = 0.0
                self._m_ShackTimer = 0.0
                self._m_bShake = False

        self._m_Player.update(TimeElapsed)
        self._m_Stage.update(TimeElapsed)
        if self._m_Player.isGameover():
            self._m_framework.change_scene('Gameover')
        if self._m_Player.isQuit():
            self._m_framework.quit()

    def draw(self):
        self._m_BKImage.draw(self._m_framework.WINDOW_WIDTH / 2, self._m_framework.WINDOW_HEIGHT / 2 + self._m_Shack_pulse)
        self._m_Stage.draw(self._m_Shack_pulse)
        self._m_Player.draw(self._m_Shack_pulse)

    def reset(self):
        pass

    def handle_events(self):
        self._m_Player.handle_events()
