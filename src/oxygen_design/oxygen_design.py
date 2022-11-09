import glob
import os.path


class OxygenDesign:
    def __init__(self):
        ...

    @property
    def styles_path(self):
        return os.path.abspath(os.path.join(os.path.dirname(__file__), 'styles'))

    def read_style_from_name(self, style_name):
        style_path = '{base}/{style_name}.qss'.format(base=self.styles_path, style_name=style_name)
        if not os.path.exists(style_path):
            raise FileNotFoundError('{style_name} style not found'.format(style_name=style_name))

        return self.read_style_from_path(style_path)

    def load_style(self, item, style_name):
        style = self.read_style_from_name(style_name)

        if not hasattr(item, 'setStyleSheet'):
            raise AttributeError('{obj} can not set style'.format(obj=type(item)))

        item.setStyleSheet(style)

    @staticmethod
    def __connect_styles(styles):
        return '\n'.join(styles)

    @staticmethod
    def read_style_from_path(style_path):
        with open(style_path, 'r') as file:
            style = file.read()
            return style

    def get_all_styles(self):
        styles = []
        for style_path in glob.glob(self.styles_path + '/*.qss'):
            styles.append(self.read_style_from_path(style_path))

        return self.__connect_styles(styles)

    def get_basic_styles(self):
        styles = []
        basic_styles = [
            'global',
            'button-primary'
        ]

        for style_name in basic_styles:
            styles.append(self.read_style_from_name(style_name))

        return self.__connect_styles(styles)
