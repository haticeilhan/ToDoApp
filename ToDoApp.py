import sys
from PyQt5.QtWidgets import (
    QApplication, QMainWindow, QVBoxLayout, QWidget,
    QLineEdit, QPushButton, QListWidget, QListWidgetItem, QHBoxLayout, QCheckBox
)
from PyQt5.QtGui import QFont, QColor
from PyQt5.QtCore import Qt

class ToDoListApp(QMainWindow):
    def __init__(self):
        super().__init__()
        
        self.setWindowTitle("To-Do List")
        self.setGeometry(300, 200, 400, 500)

        self.central_widget = QWidget()
        self.setCentralWidget(self.central_widget)

        self.layout = QVBoxLayout()
        self.central_widget.setLayout(self.layout)

        self.input_field = QLineEdit()
        self.input_field.setPlaceholderText("Enter a new task")
        self.input_field.setFont(QFont("Arial", 12))
        self.input_field.setStyleSheet("padding: 5px; border: 2px solid #5B9BD5; border-radius: 5px;")

        self.add_button = QPushButton("Add Task")
        self.add_button.setFont(QFont("Arial", 12))
        self.add_button.setStyleSheet("background-color: #5B9BD5; color: white; padding: 5px; border-radius: 5px;")
        self.add_button.clicked.connect(self.add_task)

        self.layout.addWidget(self.input_field)
        self.layout.addWidget(self.add_button)

        self.task_list = QListWidget()
        self.task_list.setStyleSheet("border: 2px solid #D9D9D9; border-radius: 5px; padding: 5px;")
        self.layout.addWidget(self.task_list)

    def add_task(self):
        task_text = self.input_field.text().strip()
        if task_text:
            task_item = QListWidgetItem()
            
            task_widget = QWidget()
            task_layout = QHBoxLayout()
            task_layout.setContentsMargins(0, 0, 0, 0)

            task_checkbox = QCheckBox(task_text)
            task_checkbox.setFont(QFont("Arial", 11))
            task_checkbox.stateChanged.connect(self.update_task_order)
            
            delete_button = QPushButton("Delete")
            delete_button.setFont(QFont("Arial", 11))
            delete_button.setStyleSheet("background-color: #E74C3C; color: white; padding: 3px; border-radius: 3px;")
            delete_button.clicked.connect(lambda: self.delete_task(task_item))

            task_layout.addWidget(task_checkbox)
            task_layout.addWidget(delete_button)
            task_widget.setLayout(task_layout)

            task_item.setSizeHint(task_widget.sizeHint())
            self.task_list.addItem(task_item)
            self.task_list.setItemWidget(task_item, task_widget)

            self.input_field.clear()

    def delete_task(self, task_item):
        row = self.task_list.row(task_item)
        self.task_list.takeItem(row)

    def update_task_order(self):
        completed_tasks = []
        uncompleted_tasks = []

        for i in range(self.task_list.count()):
            item = self.task_list.item(i)
            widget = self.task_list.itemWidget(item)
            checkbox = widget.layout().itemAt(0).widget()

            if checkbox.isChecked():
                completed_tasks.append(item)
            else:
                uncompleted_tasks.append(item)

        self.task_list.clear()
        for task in uncompleted_tasks + completed_tasks:
            self.task_list.addItem(task)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = ToDoListApp()
    window.show()
    sys.exit(app.exec_())

