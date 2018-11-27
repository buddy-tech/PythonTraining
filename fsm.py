#!/usr/bin/env python3

"""
有限状态机的简单实现
"""

import random
from time import sleep

class Car:
    def stop(self):
        print("Stop!!!")

    def go(self):
        print("Goooo!!!")

    def attach_fsm(self, state, fsm):
        """获得一个fsm"""

        self.fsm = fsm
        self.curr_state = state

    def change_state(self, new_state, new_fsm):
        """转换状态"""

        self.curr_state = new_state
        self.fsm.exit_state(self)  # 退出当前状态
        self.fsm = new_fsm  # 使用新状态的管理类
        self.fsm.enter_state(self)
        self.fsm.exec_state(self)

    def keep_state(self):
        """保持当前状态"""

        self.fsm.exec_state(self)

class base_fsm:
    """状态管理接口"""

    def enter_state(self, obj):
        raise NotImplementedError()  # 抛出异常

    def exec_state(self, obj):
        raise NotImplementedError()

    def exit_state(self, obj):
        raise NotImplementedError()

class stop_fsm(base_fsm):
    """停止状态管理类"""

    def enter_state(self, obj):
        print(f"Car{id(obj)} enter stop state!")

    def exec_state(self, obj):
        print(f"Car{id(obj)} in stop state!")
        obj.stop()

    def exit_state(self, obj):
        print(f"Car{id(obj)} exit stop state!")

class run_fsm(base_fsm):
    """运行状态管理类"""

    def enter_state(self, obj):
        print(f"Car{id(obj)} enter run state!")

    def exec_state(self, obj):
        print(f"Car{id(obj)} in run state!")
        obj.go()

    def exit_state(self, obj):
        print(f"Car{id(obj)} exit run state!")

class fsm_mgr:
    """状态管理器

    管理已有的状态类，并控制车子的状态转换
    """

    def __init__(self):
        self._fsm = {}
        self._fsm[0] = stop_fsm()
        self._fsm[1] = run_fsm()

    def get_fsm(self, state):
        return self._fsm[state]

    def frame(self, objs, state):
        """持续判断并控制对象（车子）的状态"""

        for obj in objs:
            if obj.curr_state == state:
                obj.keep_state()
            else:
                obj.change_state(state, self._fsm[state])

class World:
    def init(self):
        self._cars = []
        self._fsm_mgr = fsm_mgr()
        self.__init_car()

    def __init_car(self):
        """汽车工厂"""

        for i in range(1):
            car = Car()
            car.attach_fsm(0, self._fsm_mgr.get_fsm(0))  # 初始状态为0（停止）
            self._cars.append(car)

    def __frame(self):
        self._fsm_mgr.frame(self._cars, state_factory())  # 检测并控制车子状态

    def run(self):
        while True:
            self.__frame()
            sleep(0.5)

def state_factory():
    """随机生成状态"""
    
    return random.randint(0, 1)

if __name__ == "__main__":
    world = World()
    world.init()
    world.run()
