from controllers.base import Controller
from views.base import View


def main():
    view = View()
    players = Controller(view)
    players.run()


if __name__ == '__main__':
    main()
