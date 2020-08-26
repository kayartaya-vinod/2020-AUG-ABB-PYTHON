class Camera(object):

    def __init__(self):
        print('Camera constructor called')

    def take_photo(self):
        print('taking picture')


class Radio(object):

    def __init__(self):
        print('Radio constructor called')

    def play_music(self):
        print('playing music')


class Phone(object):

    def __init__(self):
        print('Phone constructor called')

    def make_call(self):
        print('making a phone call')


class SmartPhone(Camera, Phone, Radio):

    def __init__(self):
        # super().__init__()
        Phone.__init__(self)
        Camera.__init__(self)
        Radio.__init__(self)

        print('SmartPhone constructor called')


def main():
    sm1 = SmartPhone()
    sm1.take_photo()
    sm1.make_call()
    sm1.play_music()


if __name__ == '__main__':
    main()
