import wx
from time import sleep
from direction import Direction
from algrithm.dqn import DQN

EPISODE = 100000     # Episode limitation
MAX_STEP = 300          # Step limitation in an episode
INIT_POSITION = [1, 1]
INIT_DIRECTION = Direction.EAST


class Game(object):
    def __init__(self, house_frame, env):
        self._house_frame = house_frame
        self._env = env

    def play(self):
        dqn = DQN()

        for episode in xrange(EPISODE):
            print 'start episode:', episode
            sleep(1)
            self.train_episode(dqn)
            dqn.save_train_params()

            sleep(1)
            if episode % 5 == 0:
                self.test_dqn(dqn)

    def train_episode(self, dqn):
        total_reward = 0
        state = self._env.reset()

        for step in xrange(MAX_STEP):
            action_type = dqn.get_egreedy_action(state)
            next_state, reward, done = self._env.accept(action_type)
            dqn.perceive(state, action_type, reward, next_state, done)

            wx.CallAfter(self._house_frame.refresh, 'training...')
            sleep(0.01)
            state = next_state
            total_reward += reward

            if done:
                break

        print 'this episode total reward is %d' % total_reward

    def test_dqn(self, dqn):
        total_reward = 0
        state = self._env.reset()

        for step in xrange(MAX_STEP):
            action_type = dqn.get_action(state)
            next_state, reward, done = self._env.accept(action_type)
            dqn.perceive(state, action_type, reward, next_state, done)

            wx.CallAfter(self._house_frame.refresh, 'testing...')
            sleep(0.01)
            state = next_state
            total_reward += reward

            if done:
                break

        print 'TEST!!! total reward is %d' % total_reward