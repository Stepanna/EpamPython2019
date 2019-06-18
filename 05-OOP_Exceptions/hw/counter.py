"""
Написать декоратор instances_counter, который применяется к любому классу
и добавляет ему 2 метода:
get_created_instances - возвращает количество созданых экземпляров класса
reset_instances_counter - сбросить счетчик экземпляров,
возвращает значение до сброса
Имя декоратора и методов не менять

Ниже пример использования
"""


def instances_counter(cls):
    class NewUser(object):
        num_created_instances = 0

        def __init__(self):
            NewUser.num_created_instances += 1
            super().__init__()

        @classmethod
        def get_created_instances(cls):
            return cls.num_created_instances

        def reset_instances_counter(self):
            result = self.num_created_instances
            NewUser.num_created_instances = 0
            return result

    return NewUser


@instances_counter
class User:
    pass


if __name__ == '__main__':

    User.get_created_instances()  # 0
    user, _, _ = User(), User(), User()
    user.get_created_instances()  # 3
    user.reset_instances_counter()  # 3
