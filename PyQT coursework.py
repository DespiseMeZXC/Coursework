import sys
import webbrowser

from PyQt5 import uic
from PyQt5.QtWidgets import QApplication, QWidget, QMainWindow


class InfoAboutMe(QWidget):
    def __init__(self):
        super().__init__()
        self.setting_about()

    def setting_about(self):
        uic.loadUi("info_about_me.ui", self)
        self.setWindowTitle('Данные о разработчике')
        self.vk.clicked.connect(lambda: webbrowser.open('https://vk.com/taske69'))
        self.github.clicked.connect(lambda: webbrowser.open('https://github.com/DespiseMeZXC/coursework'))


class Calc(QWidget):
    def __init__(self):
        super().__init__()
        self.setting_calc()

    def setting_calc(self):
        uic.loadUi("Calculating.ui", self)
        self.setWindowTitle('Результат вычисления')

    def returnres(self, result):
        self.textedit.setText(result)
        text = open('zxc.txt')
        history = text.read()
        text.close()
        with open('zxc.txt', 'w'):pass

        text = open('zxc.txt', 'a+')
        text.write(result)
        text.write(history)
        text.close()


class Help(QWidget):
    def __init__(self):
        super().__init__()
        self.setting_help()

    def setting_help(self):
        uic.loadUi("help.ui", self)
        self.setWindowTitle('Help')
        self.textEdit.setText("После открытия программы:\n"
                              "1) Ознакомьтесь с допустимыми значениями,"
                              " нажав на кнопку 'Допустимые значения некоторых переменных'.\n"
                              "2) Начинайте вводить переменные."
                              "Также выберите класс бетона и арматуры. "
                              "Перед вводом А_s посмотрите таблицу значений A_s. "
                              "Для этого нажмите на кнопку "
                              "'Таблица значений A_s'. После выбора значения,"
                              " введите его в соответствующее поле.\n"
                              "3) Смело жмите на кнопку 'Вычислить'.\n"
                              "4) Для просмотра истории ваших "
                              "вычислений нажмите на кнопку 'История вычислений'.\n"

                              "5) Для очистки истории и текстового "
                              "файла используйте кнопку 'Очистить текстовый файл'.\n"
                              "6) Для того, чтобы очистить введённые вами данные, "
                              "достаточно нажать на кнопку 'Очистить данные'.")
        self.info.clicked.connect(self.info_about)
        self.instuction.clicked.connect(self.instraction_use)
        self.limit.clicked.connect(self.limit_mean)

    def info_about(self):
        strin = "b, h, a - Размеры колонны среднего" \
                " этажа рамного каркаса с сечением.\n" \
                "Продольная сила и изгибающие моменты в опорном сечении " \
                "от вертикальных нагрузок: полная N_v, M_v," \
                " постоянных и длительных: N_l, M_l.\n" \
                "От ветровых нагрузок: N_h, M_h.\n" \
                "Высота этажа: l\n" \
                "Тяжёлый бетон: от B15 до B60 включительно.\n" \
                "Арматура: от A240 до A500 включительно.\n" \
                "Площадь сечения арматуры: A_s(значения из таблицы)."

        self.textEdit.setText(strin)

    def limit_mean(self):
        strin = 'Размеры колонны среднего этажа рамного каркаса с сечением:' \
                '\n1) b от 1/5*h до h\n' \
                '2) h от 100 до 8000\n' \
                '3) а от 10 до 1/2*h'
        self.textEdit.setText(strin)

    def instraction_use(self):
        self.textEdit.setText("После открытия программы:\n"
                              "1) Ознакомьтесь с допустимыми значениями,"
                              " нажав на кнопку 'Допустимые значения некоторых переменных'.\n"
                              "2) Начинайте вводить переменные."
                              "Также выберите класс бетона и арматуры. "
                              "Перед вводом А_s посмотрите таблицу значений A_s. "
                              "Для этого нажмите на кнопку "
                              "'Таблица значений A_s'. После выбора значения,"
                              " введите его в соответствующее поле.\n"
                              "3) Смело жмите на кнопку 'Вычислить'.\n"
                              "4) Для просмотра истории ваших "
                              "вычислений нажмите на кнопку 'История вычислений'.\n"

                              "5) Для очистки истории и текстового "
                              "файла используйте кнопку 'Очистить текстовый файл'.\n"
                              "6) Для того, чтобы очистить введённые вами данные, "
                              "достаточно нажать на кнопку 'Очистить данные'.")


class Asform(QWidget):
    def __init__(self):
        super().__init__()
        self.setting_asform()

    def setting_asform(self):
        uic.loadUi("A_sForm.ui", self)
        self.setWindowTitle('Таблица значений A_s')


class HistoryCalc(QWidget):
    def __init__(self):
        super().__init__()
        self.settingHistoryCalc()

    def settingHistoryCalc(self):
        uic.loadUi("histirycalc.ui", self)
        self.setWindowTitle('История вычислений')

    def concatStr(self):
        text = open('zxc.txt')
        a = text.read()
        text.close()
        result = a
        self.textedit1.setText(self.textedit1.toPlainText() + result + '\n')


class BuildingCalc(QMainWindow):
    def __init__(self):
        super().__init__()
        self.string_result = ''
        self.settingBuildCalc()
        self.res = ''
        self.R_s = 350
        self.R_sc = 350
        self.R_b = 14.5
        self.E_b = 30000

    def settingBuildCalc(self):
        uic.loadUi("Mainwindow.ui", self)
        self.setWindowTitle("Прямоугольные сечения с симметричной арматурой")

        self.calculating.clicked.connect(self.print_result)
        self.history_calc.clicked.connect(self.show_history)
        self.clear.clicked.connect(self.clear_data)
        self.btn_clear_file.clicked.connect(self.clear_file)
        self.help.clicked.connect(self.help_form)
        self.A_sForm.clicked.connect(self.input_A_s)
        self.infoabout.clicked.connect(self.infoaboutme)
        self.comboBox.addItem("B15")
        self.comboBox.addItem("B20")
        self.comboBox.addItem("B25")
        self.comboBox.addItem("B30")
        self.comboBox.addItem("B35")
        self.comboBox.addItem("B40")
        self.comboBox.addItem("B45")
        self.comboBox.addItem("B50")
        self.comboBox.addItem("B55")
        self.comboBox.addItem("B60")
        self.comboBox.activated[str].connect(self.selectcombobeton)

        self.comboBox_2.addItem("A240")
        self.comboBox_2.addItem("A400")
        self.comboBox_2.addItem("A500")
        self.comboBox_2.activated[str].connect(self.selectcomboarmatura)

    def selectcombobeton(self):
        self.meanbox = str(self.comboBox.currentText())
        if self.meanbox == "B15":
            self.E_b = 24000
            self.R_b = 8.5
        elif self.meanbox == "B20":
            self.E_b = 27500
            self.R_b = 11.5
        elif self.meanbox == "B25":
            self.E_b = 30000
            self.R_b = 14.5
        elif self.meanbox == "B30":
            self.E_b = 32500
            self.R_b = 17
        elif self.meanbox == "B35":
            self.E_b = 34500
            self.R_b = 19.5
        elif self.meanbox == "B40":
            self.E_b = 36000
            self.R_b = 22
        elif self.meanbox == "B45":
            self.E_b = 37000
            self.R_b = 25
        elif self.meanbox == "B50":
            self.E_b = 38000
            self.R_b = 27.5
        elif self.meanbox == "B55":
            self.E_b = 39000
            self.R_b = 30
        elif self.meanbox == "B60":
            self.E_b = 39500
            self.R_b = 33

    def selectcomboarmatura(self):
        self.meanbox = str(self.comboBox_2.currentText())
        if self.meanbox == "A240":
            self.R_s = 210
            self.R_sc = 210
        elif self.meanbox == "A400":
            self.R_s = 340
            self.R_sc = 340
        elif self.meanbox == "A500":
            self.R_s = 435
            self.R_sc = 435

    def take(self, result):
        self.res1 = result

    def help_form(self):
        self.help = Help()
        self.help.show()

    def infoaboutme(self):
        self.aboutme = InfoAboutMe()
        self.aboutme.show()

    def input_A_s(self):
        self.take_A_s = Asform()
        self.take_A_s.show()

    def show_history(self):
        self.history_result = HistoryCalc()
        self.history_result.concatStr()
        self.history_result.show()

    def clear_data(self):
        self.seven.clear()
        self.eight.clear()
        self.first.clear()
        self.ten.clear()
        self.second.clear()
        self.nine.clear()
        self.third.clear()
        self.eleven.clear()
        self.five.clear()
        self.six.clear()
        self.lineEdit.clear()

    def clear_file(self):
        with open('zxc.txt', 'w'): pass

    def print_result(self):
        self.calc = Calc()
        self.A_s1 = self.lineEdit.text()
        if self.A_s1 == '':
            self.A_s1 = 1232
        self.h = self.second.text()
        self.b = self.first.text()
        self.a = self.third.text()
        self.N_v = self.five.text()
        self.M_v = self.six.text()
        self.N_l = self.seven.text()
        self.M_l = self.eight.text()
        self.A_s2 = self.A_s1
        self.N_h = self.nine.text()
        self.M_h = self.ten.text()
        self.l = self.eleven.text()

        self.E_s = 200000

        if not self.b.strip() or not self.h.strip() or not self.a.strip() \
                or not self.N_v.strip() \
                or not self.M_v.strip() or not self.N_l.strip() \
                or not self.M_l.strip() or not self.N_h.strip() \
                or not self.M_h.strip() or not self.l.strip():
            self.string_result += ("Некорректный ввод переменных!\n"
                                   "Проверьте все ли поля заполнены!!!\n\n")
            self.take(self.string_result)


        elif self.b.isdigit() == False or self.h.isdigit() == False or self.a.isdigit() == False or self.N_v.isdigit() == False \
                or self.M_v.isdigit() == False or self.N_l.isdigit() == False \
                or self.M_l.isdigit() == False or self.N_h.isdigit() == False \
                or self.M_h.isdigit() == False or self.l.isdigit() == False:
            self.string_result = ("Не все переменные, введённые\n"
                                  "вами, являются числами!\n"
                                  "Проверьте корректность ввода!!!\n\n")
            self.take(self.string_result)
        elif (float(self.b) < 1 / 5 * float(self.h) or float(self.b) > float(self.h)) or \
                (float(self.h) < 10 or float(self.h) > 8000) or (
                float(self.a) < 10 or float(self.a) > float(self.h) / 2):
            self.string_result = "Вы вышли за диапазон допустимых значений ознакомьтесь с 'HELP'"
            self.take(self.string_result)
        else:
            self.string_result += f"Исходные переменные: b = {self.b} мм, h = {self.h} мм," \
                                  f" a = {self.a} мм, E_b = {self.E_b} МПа, R_b = {self.R_b} МПа, " \
                                  f"R_s = R_sc = {self.R_s} МПа, A_s = {self.A_s1} мм*2, " \
                                  f"N_v = {self.N_v} кH, M_v = {self.M_v} кH*м, " \
                                  f"N_l = {self.N_l} кH, M_l = {self.M_l} кH*м, " \
                                  f"N_h = {self.N_h} кH, M_h = {self.M_h} кH*м, l = {self.l} м.\n"
            self.h_0 = int(self.h) - int(self.a)
            self.string_result += f"Расчет. h_0 = h - a = {self.h} - {self.a} = {self.h_0}\n"
            n_v = 1
            self.string_result += ("Так как рассматриваемое сечение опорное \n"
                                   "и колонна у этой опоры имеет податливую заделку,"
                                   "принимаем n_v = 1,0,\n")
            l_O = 1.2 * int(self.l)
            l_O = round(l_O, 1)
            self.string_result += (f"Для вычислаения коэффициента n_h\nпринимаем согласно 3.2.42,\n"
                                   f"б) расчётную длинну колонны равной\nl_0 = 1,2 * {self.l} = {l_O} м.\n")

            self.string_result += f"При этом l_O/h = {l_O}/ {self.h} > 4,\n" \
                                  "т.е учет прогиба обязателен.\n"
            M = int(self.M_v) + int(self.M_h)
            self.string_result += "Усилия от всех нагрузок равны\n" \
                                  f" M = M_v + M_h = {self.M_v} + {self.M_h} = {M}кH*м,\n"
            N = int(self.N_v) + int(self.N_h)
            self.string_result += f"N = N_v + N_h = {self.N_v} + {self.N_h} = {M} кH.\n"
            e_0 = M / N
            e_0 = round(e_0, 3)
            self.string_result += f"При этом e_0 = M/N = {M} / {N} = {e_0} м\n{e_0} м > e_a = h/30, " \
                                  "т.е. согласно 3.2.36 значение момента M не корректируем.\n"
            self.string_result += "Определяем моменты M_1 и M_1l относительно растянутой арматуры " \
                                  "соответственно от полной нагрузки и от постоянных и длительных нагрузок\n"
            self.h_0 = int(self.h_0) / 1000
            self.a = int(self.a) / 1000
            self.h = int(self.h) / 1000
            M_1 = M + N * (self.h_0 - self.a) / 2
            M_1 = int(M_1)
            self.string_result += "M_1 = M + N * (h_0 - a) / 2 =\n" \
                                  f"{M} + {N} * ({self.h_0} - {self.a}) / 2 = {M_1} кH*м;\n"
            M_1l = int(self.M_l) + int(self.N_l) * (self.h_0 - self.a) / 2
            M_1l = round(M_1l, 1)
            self.string_result += "M_1l = M_l + N_l * (h_0 - a) / 2 =\n" \
                                  f"{self.M_l} + {self.N_l} * ({self.h_0} - {self.a}) / 2 = {M_1l} кH*м.\n"
            F_l = 1 + M_1l / M_1
            F_l = round(F_l, 2)
            self.string_result += f"Тогда F_l = 1 + M_1l/M_1 =\n 1 + {M_1l} / {M_1} = {F_l}.\n"
            delta_e = e_0 / self.h

            self.string_result += f"Так как e_0/h = {e_0} / {self.h} = {delta_e}\n" \
                                  f"{delta_e} > 0,15, принимаем delta_e = {delta_e}."
            self.h = self.h * 1000
            self.h = int(self.h)
            ua = (float(self.A_s1) + float(self.A_s2)) * float(self.E_s) / (
                    float(self.b) * float(self.h) * float(self.E_b))
            ua = round(ua, 4)
            self.string_result += "ua =(A_s1 + A_s2) / (b * h) * E_s / E_b =\n" \
                                  f"({self.A_s1} + {self.A_s2}) " \
                                  f"/ ({self.b} * {self.h}) * {self.E_s}/{self.E_b} = {ua}."
            self.h_0 = self.h_0 * 1000
            self.a = self.a * 1000
            self.a = int(self.a)
            self.h_0 = int(self.h_0)

            D = float(self.E_b) * float(self.b) * \
                (float(self.h) ** 3) * ((0.0125 / (float(F_l) * (0.3
                                                                 + float(delta_e)))) + (0.175 *
                                                                                        float(ua) * ((float(
                        self.h_0) - float(self.a)) / float(self.h)) ** 2))
            D = round(D, 0)
            D = int(D)
            D = '%.3e' % D
            self.string_result += "\nПо формуле (3.89) определим жёсткость D\n" \
                                  "D = E_b*b*h^3[0,0125/F_l(0,3 + delta) " \
                                  "+ 0,175ua(h_0 - a / h)^2] =\n" \
                                  f"{self.E_b} * {self.b} * {self.h}^3*[0,0125 /" \
                                  f" {F_l}*(0,3 + {delta_e}) + 0,175 * {ua} * ({self.h_0}" \
                                  f" - {self.a}/ {self.h})^2] = {D} мм^2.\n"
            N_cr = eval(f"3.14**2 * {D} / {l_O}**2")

            N_cr_buf = str(N_cr)
            N_cr = ''
            for i in range(7):
                N_cr += str(N_cr_buf[i])
            N_crH = int(N_cr)
            N_crkH = N_crH / 1000
            N_crkH = round(N_crkH, 0)
            N_crkH = int(N_crkH)
            self.string_result += "Отсюда N_cr = pi**2*D/l_0**2 = " \
                                  f" 3.14**2*{D}/{l_O}**2 = {N_crH} H ={N_crkH} кH\n"
            n_h = 1 / (1 - N / N_crkH)
            n_h = round(n_h, 3)
            self.string_result += f"n_h = 1/ 1-N/N_cr = 1 / 1- {N} / {N_crkH} = {n_h}\n"
            self.string_result += "Расчетный момент с учетом прогиба определяем\n" \
                                  "по формуле (3.81), принимая M_t = 0,0 кH*м."
            M_t = 0.0
            M = float(self.M_v) * float(n_v) + float(self.M_h) * float(n_h)
            M = round(M, 1)
            self.string_result += f"M = M_v * n_v + M_h * n_h = " \
                                  f"{self.M_v} * {n_v} + {self.M_h} * {n_h} = {M}кh*м. "
            self.string_result += "Проверяем прочность сечения согласно 3.2.43.\n"
            N = N * 1000
            a_n = N / (float(self.R_b) * float(self.b) * float(self.h_0))
            a_n = round(a_n, 3)
            self.string_result += "a_n = N/ R_b*b*h_0 = " \
                                  f"{N} / {self.R_b} * {self.b} *" \
                                  f" {self.h_0} = {a_n} < E_r = 0,533(таблица 3.3)."
            x = a_n * self.h_0
            x = round(x, 1)
            self.string_result += f"Следовательно, x = a_n*h_0 =" \
                                  f" {a_n} * {self.h_0} = {x} мм."
            end_res = float(self.R_b) * float(self.b) * float(x) * (float(self.h_0) - float(x) / 2) \
                      + (float(self.R_sc) * float(self.A_s2) - float(N) / 2) * (float(self.h_0) - float(self.a))

            end_res_buf = str(end_res)
            end_res_buf = end_res_buf[0] + end_res_buf[1] + end_res_buf[2] + ',' + end_res_buf[3] + end_res_buf[
                4] + "*10^6"
            end_res = end_res / 1000000
            end_res = round(end_res, 1)
            self.string_result += "R_b * b * x(h_0 - x/2) + (R_sc*A_s - N/2)(h_0-a) =\n" \
                                  f"{self.R_b} * {self.b} * {x} * ({self.h_0} - {x}/2) +" \
                                  f" ({self.R_sc} * {self.A_s2} " \
                                  f"- {N}/2)({self.h_0} - {self.a}) =" \
                                  f" {end_res_buf} H*мм = {end_res} кH*м > M = 224,4 кH*м,\n "
            if end_res > 224.4:
                self.string_result += "т.е. прочность сечения обеспечена!\n\n"
            else:
                self.string_result += "т.е. прочность сечения не обеспечена!\n\n"


            self.take(self.string_result)
        self.calc.returnres(self.res1)
        self.calc.show()
        self.string_result = ''


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = BuildingCalc()
    ex.show()
    sys.exit(app.exec())
