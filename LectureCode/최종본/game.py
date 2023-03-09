import sys
from PyQt5 import QtWidgets
import onepage, twopage, threepage, fourpage


class ShowPages:

    def __init__(self):
        pass

    def show_onepage(self):
        self.onepage = onepage.Layout()
        self.onepage.switch_window.connect(self.show_twopage)
        try:
            self.fourpage.close()
        except AttributeError:
            pass
        self.onepage.show()

    def show_twopage(self):
        self.twopage = twopage.Layout()
        self.twopage.switch_window.connect(self.show_three_to_twopage)
        self.onepage.close()
        self.twopage.show()

    def show_two_to_threepage(self):
        self.twopage = twopage.Layout()
        self.twopage.switch_window.connect(self.show_three_to_twopage)
        self.threepage.close()
        self.twopage.show()

    def show_three_to_twopage(self):
        question_number_txt = open('textFile/question_number.txt', 'r', encoding='utf8')
        self.question_number_list = []
        for line in question_number_txt:
            word = line.rstrip('\n')
            self.question_number_list.append(word)
        question_number_txt.close()

        self.threepage = threepage.Layout()
        checkpage = self.threepage.switch_window.connect
        if int(self.question_number_list[1]) < 10:
            self.question_number_list[1] = int(self.question_number_list[1])
            self.question_number_list[1] += 1
            self.question_number_list[1] = str(self.question_number_list[1])
            a = open('textFile/question_number.txt', 'w', encoding='utf8')
            for p in self.question_number_list:
                a.write(p + '\n')
            a.close()
            checkpage(self.show_two_to_threepage)
        else:
            checkpage(self.show_fourpage)
        self.twopage.close()
        self.threepage.show()

    def show_fourpage(self):
        self.fourpage = fourpage.Layout()
        self.fourpage.switch_window.connect(self.show_onepage)
        self.threepage.close()
        self.fourpage.show()


def main():
    app = QtWidgets.QApplication(sys.argv)
    controller = ShowPages()
    controller.show_onepage()
    sys.exit(app.exec_())


if __name__ == '__main__':
    main()
