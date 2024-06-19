import sys
from PyQt6.QtWidgets import (QApplication, QWidget, QVBoxLayout, QLabel, QLineEdit, QPushButton, QSpacerItem,
                             QSizePolicy, QStackedWidget, QHBoxLayout)
from PyQt6.QtCore import Qt, pyqtSignal

DARK_THEME_STYLE = """
QWidget {
    background-color: #333333;
    color: white;
    font-family: 'Helvetica', 'Arial', sans-serif;
}

QPushButton {
    background-color: #555555;
    color: white;
    border: none;
    padding: 10px;
    border-radius: 5px;
    width: 200px;
    height: 40px;
}

QLineEdit {
    background-color: #555555;
    color: white;
    border-radius: 5px;
    padding: 5px;
    height: 40px;
    width: 200px;
    font-size: 14pt;
}

QLabel {
    font-size: 14pt;
}

QTextEdit {
    background-color: #555555;
    color: white;
    border-radius: 5px;
    padding: 10px;
    font-size: 14pt;
}
"""


# Tela 1
class Screen1(QWidget):
    nextSignal = pyqtSignal()

    def __init__(self):
        super().__init__()
        self.initUI()

    def initUI(self):
        self.setStyleSheet(DARK_THEME_STYLE)
        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)

        self.setWindowTitle('Doctors Without Weekends')
        self.setGeometry(350, 100, 1280, 720)

        # Título
        title = QLabel('Doctors Without Weekends')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet('font-size: 24pt; font-weight: bold;')
        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addSpacerItem(QSpacerItem(5, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Instruções e entradas
        instruction_label = QLabel('Por favor, insira os valores de K, N e C:')
        instruction_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(instruction_label)
        layout.addSpacerItem(QSpacerItem(5, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        k_label = QLabel('K: Número de Períodos de Férias')
        k_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(k_label)

        input_layout = QHBoxLayout()
        input_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        self.k_input = QLineEdit(self)
        self.k_input.setPlaceholderText("Número de períodos")
        input_layout.addWidget(self.k_input)
        input_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        layout.addLayout(input_layout)

        n_label = QLabel('N: Número de Médicos')
        n_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(n_label)

        input_layout = QHBoxLayout()
        input_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        self.n_input = QLineEdit(self)
        self.n_input.setPlaceholderText("Número de médicos")
        input_layout.addWidget(self.n_input)
        input_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        layout.addLayout(input_layout)

        c_label = QLabel('C: Máximo de dias que um médico pode trabalhar em feriados')
        c_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(c_label)

        input_layout = QHBoxLayout()
        input_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        self.c_input = QLineEdit(self)
        self.c_input.setPlaceholderText("Máximo de dias")
        input_layout.addWidget(self.c_input)
        input_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
        layout.addLayout(input_layout)

        # Botão Próximo
        self.next_button = QPushButton('Próximo')
        self.next_button.clicked.connect(self.validate_and_next)
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        layout.addWidget(self.next_button, alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

    def validate_and_next(self):
        if hasattr(self, 'error_label'):
            self.layout().removeWidget(self.error_label)
            self.error_label.deleteLater()
            del self.error_label
        try:
            k = int(self.k_input.text())
            n = int(self.n_input.text())
            c = int(self.c_input.text())
            if k > 0 and n > 0 and c > 0:
                self.nextSignal.emit()
            else:
                self.show_error("Todos os valores devem ser maiores que zero.")
        except ValueError:
            self.show_error("Por favor, insira apenas números inteiros positivos.")

    def show_error(self, message):
        self.error_label = QLabel(message)
        self.error_label.setStyleSheet("color: red;")
        self.error_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout().addWidget(self.error_label, alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter)


# Tela 2
class Screen2(QWidget):
    nextSignal = pyqtSignal()

    def __init__(self, k):
        super().__init__()
        self.k = k
        self.initUI()

    def initUI(self):
        self.setStyleSheet(DARK_THEME_STYLE)
        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)

        self.setWindowTitle('Período de Férias')
        self.setGeometry(350, 100, 1280, 720)

        # Título
        title = QLabel('Período de Férias')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet('font-size: 24pt; font-weight: bold;')
        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addSpacerItem(QSpacerItem(5, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Instruções
        instructions = QLabel('Por favor, insira os dias de férias para cada período.\n'
                              'Exemplo: 1,2,3,4')
        instructions.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(instructions)
        layout.addSpacerItem(QSpacerItem(5, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Entradas
        self.dj_inputs = []
        for i in range(self.k):
            label = QLabel(f'Férias {i + 1}:')
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(label)

            input_layout = QHBoxLayout()
            input_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
            input_field = QLineEdit(self)
            input_field.setPlaceholderText("Dias de férias")
            self.dj_inputs.append(input_field)
            input_layout.addWidget(input_field)
            input_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
            layout.addLayout(input_layout)

        # Botão Próximo
        self.next_button = QPushButton('Próximo')
        self.next_button.clicked.connect(self.validate_and_next)
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        layout.addWidget(self.next_button, alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

    def validate_and_next(self):
        if hasattr(self, 'error_label'):
            self.layout().removeWidget(self.error_label)
            self.error_label.deleteLater()
            del self.error_label
        try:
            self.dj = []
            for input_field in self.dj_inputs:
                days = list(map(int, input_field.text().split(',')))
                self.dj.append(days)
            self.nextSignal.emit()
        except ValueError:
            self.show_error("Por favor, insira os dias no formato correto, separados por vírgulas.")

    def show_error(self, message):
        self.error_label = QLabel(message)
        self.error_label.setStyleSheet("color: red;")
        self.error_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout().addWidget(self.error_label, alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter)


# Tela 3
class Screen3(QWidget):
    nextSignal = pyqtSignal()

    def __init__(self, n, dj_str):
        super().__init__()
        self.n = n
        self.dj_str = dj_str
        self.initUI()

    def initUI(self):
        self.setStyleSheet(DARK_THEME_STYLE)
        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)

        self.setWindowTitle('Disponibilidade Médica')
        self.setGeometry(350, 100, 1280, 720)

        # Título
        title = QLabel('Disponibilidade Médica')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet('font-size: 24pt; font-weight: bold;')
        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addSpacerItem(QSpacerItem(5, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Instruções
        dj_label = QLabel(f'Dias de Férias: {self.dj_str}')
        dj_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(dj_label)

        instructions = QLabel('Por favor, insira os dias disponíveis para cada médico.\n'
                              'Exemplo: 1,2,3,4')
        instructions.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(instructions)
        layout.addSpacerItem(QSpacerItem(5, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))

        # Entradas
        self.si_inputs = []
        for i in range(self.n):
            label = QLabel(f'Médico {i + 1}:')
            label.setAlignment(Qt.AlignmentFlag.AlignCenter)
            layout.addWidget(label)

            input_layout = QHBoxLayout()
            input_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
            input_field = QLineEdit(self)
            input_field.setPlaceholderText("Dias disponíveis")
            self.si_inputs.append(input_field)
            input_layout.addWidget(input_field)
            input_layout.addSpacerItem(QSpacerItem(40, 20, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum))
            layout.addLayout(input_layout)

        # Botão Próximo
        self.next_button = QPushButton('Próximo')
        self.next_button.clicked.connect(self.validate_and_next)
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        layout.addWidget(self.next_button, alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

    def validate_and_next(self):
        if hasattr(self, 'error_label'):
            self.layout().removeWidget(self.error_label)
            self.error_label.deleteLater()
            del self.error_label
        try:
            self.si = []
            for input_field in self.si_inputs:
                days = list(map(int, input_field.text().split(',')))
                self.si.append(days)
            self.nextSignal.emit()
        except ValueError:
            self.show_error("Por favor, insira os dias no formato correto, separados por vírgulas.")

    def show_error(self, message):
        self.error_label = QLabel(message)
        self.error_label.setStyleSheet("color: red;")
        self.error_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.layout().addWidget(self.error_label, alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter)


# Tela 4
class Screen4(QWidget):
    restartSignal = pyqtSignal()

    def __init__(self, result):
        super().__init__()
        self.result = result
        self.initUI()

    def initUI(self):
        self.setStyleSheet(DARK_THEME_STYLE)
        layout = QVBoxLayout()
        layout.setSpacing(10)
        layout.setContentsMargins(20, 20, 20, 20)

        self.setWindowTitle('Resultado')
        self.setGeometry(350, 100, 1280, 720)

        # Título
        title = QLabel('Resultado')
        title.setAlignment(Qt.AlignmentFlag.AlignCenter)
        title.setStyleSheet('font-size: 24pt; font-weight: bold;')
        layout.addWidget(title, alignment=Qt.AlignmentFlag.AlignTop)
        layout.addSpacerItem(QSpacerItem(5, 5, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        # Resultado
        result_label = QLabel(self.result)
        result_label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        layout.addWidget(result_label, alignment=Qt.AlignmentFlag.AlignCenter)

        # Botão Recomeçar
        self.restart_button = QPushButton('Recomeçar')
        self.restart_button.clicked.connect(self.restart)
        layout.addSpacerItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Expanding))
        layout.addWidget(self.restart_button, alignment=Qt.AlignmentFlag.AlignBottom | Qt.AlignmentFlag.AlignCenter)

        self.setLayout(layout)

    def restart(self):
        self.restartSignal.emit()


# MainApp
class MainApp(QWidget):
    def __init__(self):
        super().__init__()
        self.initUI()

    # <editor-fold desc="Prepara inicialização de cada tela a medida em que elas são chamadas">

    def initUI(self):
        self.setStyleSheet(DARK_THEME_STYLE)
        self.setWindowTitle('Doctors Without Weekends')
        self.setGeometry(350, 100, 1280, 720)

        self.stackedWidget = QStackedWidget()
        layout = QVBoxLayout()
        layout.addWidget(self.stackedWidget)
        self.setLayout(layout)

        self.prepare_screen1()

    def prepare_screen1(self):
        self.screen1 = Screen1()
        self.screen1.nextSignal.connect(self.prepare_screen2)
        self.stackedWidget.addWidget(self.screen1)
        self.stackedWidget.setCurrentWidget(self.screen1)

    def prepare_screen2(self):
        k = int(self.screen1.k_input.text())
        self.screen2 = Screen2(k)
        self.screen2.nextSignal.connect(self.prepare_screen3)
        self.stackedWidget.addWidget(self.screen2)
        self.stackedWidget.setCurrentWidget(self.screen2)

    def prepare_screen3(self):
        dj_str = ", ".join([",".join(map(str, days)) for days in self.screen2.dj])
        n = int(self.screen1.n_input.text())
        self.screen3 = Screen3(n, dj_str)
        self.screen3.nextSignal.connect(self.prepare_screen4)
        self.stackedWidget.addWidget(self.screen3)
        self.stackedWidget.setCurrentWidget(self.screen3)

    def prepare_screen4(self):
        dj = self.screen2.dj
        si = self.screen3.si
        k = int(self.screen1.k_input.text())
        n = int(self.screen1.n_input.text())
        c = int(self.screen1.c_input.text())

        result = self.doctors_schedule_algorithm(k, n, c, dj, si)
        self.screen4 = Screen4(result)
        self.screen4.restartSignal.connect(self.restart)
        self.stackedWidget.addWidget(self.screen4)
        self.stackedWidget.setCurrentWidget(self.screen4)

    def restart(self):
        self.stackedWidget.setCurrentIndex(0)

    # </editor-fold>

    #Busca em Largura
    def bfs(self, C, F, source, sink):
        P = [-1] * len(C)  # parent in search tree
        P[source] = source
        queue = [source]
        while queue:
            u = queue.pop(0)
            for v in range(len(C)):
                if C[u][v] - F[u][v] > 0 and P[v] == -1:
                    P[v] = u
                    queue.append(v)
                    if v == sink:
                        path = []
                        while True:
                            path.insert(0, v)
                            if v == source:
                                break
                            v = P[v]
                        return path
        return None

    #Algoritmo de Edmonds Karp
    def edmonds_karp(self, C, source, sink):
        n = len(C)  # C is the capacity matrix
        F = [[0] * n for _ in range(n)]
        # residual capacity from u to v is C[u][v] - F[u][v]

        while True:
            path = self.bfs(C, F, source, sink)
            if not path:
                break
            # traverse path to find the smallest capacity
            flow = min(C[u][v] - F[u][v] for u, v in zip(path, path[1:]))
            # traverse path to update flow
            for u, v in zip(path, path[1:]):
                F[u][v] += flow
                F[v][u] -= flow
        return sum(F[source][i] for i in range(n))

    def doctors_schedule_algorithm(self, k, n, c, dj, si):
        # Convert the input data into a graph representation
        all_days = sorted(set(day for period in dj for day in period))
        day_index = {day: i for i, day in enumerate(all_days)}

        source = 0
        sink = len(all_days) + len(si) + 1
        C = [[0] * (sink + 1) for _ in range(sink + 1)]

        # Connect source to each doctor with capacity c
        for i in range(1, len(si) + 1):
            C[source][i] = c

        # Connect each doctor to available days with capacity 1
        for i, days in enumerate(si, start=1):
            for day in days:
                if day in day_index:
                    C[i][len(si) + 1 + day_index[day]] = 1

        # Connect each day to the sink with capacity 1
        for i in range(len(all_days)):
            C[len(si) + 1 + i][sink] = 1

        max_flow = self.edmonds_karp(C, source, sink)
        if max_flow == len(all_days):
            return "Atribuição de médicos possível."
        else:
            return "Atribuição de médicos não é possível."


if __name__ == '__main__':
    app = QApplication(sys.argv)
    ex = MainApp()
    ex.show()
    sys.exit(app.exec())
