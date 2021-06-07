from controllers.base_controller import BaseController
from views.base_view import BaseView


def main():
    view = BaseView()
    programm = BaseController(view)
    programm.run()


if __name__ == '__main__':
    main()
