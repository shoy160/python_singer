# coding=utf-8
from singer import Singer
# from config import SingerConfig
logger = Singer.logger('z_test')


def task(index):
    logger.info('running task01 %s', index)
    return index + index


def task_02(index, name):
    logger.info('running task02 %s %s', index, name)
    return index * index


def task_completed(task):
    logger.info('completed %s', task.result())


if __name__ == "__main__":
    s = Singer()
    cache = s.cache()
    cache.set_cache('shay', 12345)
    value = cache.get_cache('shay')
    print(s.guid, value)
    config = s.config(mode='prod')
    print(config.get_items('dev'))
    name = config.get_config('name')
    print(s.guid, name)

    with Singer.executor() as executor:
        for i in range(5):
            executor.start(task, i)
        for i in range(5):
            executor.start(task_02, i, i+2)
        executor.completed(task_completed)
