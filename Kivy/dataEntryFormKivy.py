import kivy
from kivy.app import App
from kivy.uix.gridlayout import GridLayout
from kivy.uix.scrollview import ScrollView
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button
import pyodbc

class MyGridLayout(GridLayout):
    def __init__(self, **kwargs):
        super(MyGridLayout, self).__init__(**kwargs)
        self.cols = 2
        self.add_widget(Label(text='Name'))
        self.name = TextInput(multiline=False)
        self.add_widget(self.name)
        self.add_widget(Label(text='Age'))
        self.age = TextInput(multiline=False)
        self.add_widget(self.age)

        self.save_button = Button(text="Save")
        self.save_button.bind(on_press=self.save_data)
        self.add_widget(self.save_button)

        self.grid = GridLayout(cols=3)
        self.scrollview = ScrollView(size_hint=(1, None), size=(800, 500))
        self.scrollview.add_widget(self.grid)
        self.add_widget(self.scrollview)

        self.load_data()

    def save_data(self, instance):
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                              'SERVER=192.168.0.109,1433;'
                              'DATABASE=SSIS_Practice;'
                              'UID=sa;'
                              'PWD=admin@123')
        cursor = conn.cursor()
        cursor.execute("INSERT INTO pyDE_Students (Name, Age) VALUES (?, ?)",
                       (self.name.text, self.age.text))
        conn.commit()
        conn.close()
        self.load_data()

    def edit_data(self, row):
        print(row)

    def load_data(self):
        conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                              'SERVER=192.168.0.109,1433;'
                              'DATABASE=SSIS_Practice;'
                              'UID=sa;'
                              'PWD=admin@123')
        cursor = conn.cursor()
        cursor.execute("SELECT ID, Name, Age FROM pyDE_Students order by Id")
        rows = cursor.fetchall()

        self.grid.clear_widgets()
        for i, row in enumerate(rows):
            for j, value in enumerate(row):
                label = Label(text=str(value))
                self.grid.add_widget(label)
            # add an "Edit" button at the end of the row
            edit_button = Button(text="Edit")
            #edit_button.bind(on_press=self.edit_data(row))
            self.grid.add_widget(edit_button)
        conn.close()


class MyApp(App):
    def build(self):
        return MyGridLayout()


if __name__ == '__main__':
    MyApp().run()
