from controllers.base_controller import Controller
from views.base import View


def main():
    view = View()
    programm = Controller(view)
    programm.run()


if __name__ == '__main__':
    main()
