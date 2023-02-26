# Import required libraries
import pyodbc
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.button import Button
from kivy.uix.label import Label
from kivy.uix.textinput import TextInput
from kivy.metrics import dp
from kivy.uix.floatlayout import FloatLayout

# Connect to MSSQL Server database
conn = pyodbc.connect('DRIVER={ODBC Driver 17 for SQL Server};'
                          'SERVER=ITLNB619;'
                          'DATABASE=SSIS_Practice;'
                          'UID=sa;'
                          'PWD=admin@123')

# Define main app class
class DataEntryFormApp(App):
    def build(self):
        # Create layout for the form
        #layout = BoxLayout(orientation='vertical', padding=10, spacing=10, size_hint=(1,0.5), pos_hint={'top': 1})
        layout       =BoxLayout(orientation='vertical', padding=5, spacing=10, size=(200, 500), size_hint=(1,0.4), pos_hint={'top': 1})
        # Add labels and text inputs for each field
        layout.add_widget(Label(text='Name', size_hint=(0.2, None), height=dp(10), size=(dp(100), dp(10))))
        self.name_input = TextInput(multiline=False, height=dp(10), width=dp(200))
        layout.add_widget(self.name_input)

        layout.add_widget(Label(text='Age', size_hint=(0.2, None), height=dp(10), size=(dp(100), dp(30))))
        self.age_input = TextInput(multiline=False, height=dp(10), width=dp(200))
        layout.add_widget(self.age_input)

        layout.add_widget(Label(text='Email', size_hint=(0.2, None), height=dp(10), size=(dp(100), dp(30))))
        self.email_input = TextInput(multiline=False, height=dp(10), width=dp(200))
        layout.add_widget(self.email_input)

        # Add submit button
        submit_button = Button(text='Submit', size_hint=(0.3, None), height=dp(8), width=dp(100))
        submit_button.bind(on_press=self.submit_data)
        layout.add_widget(submit_button)

        # Create FloatLayout and add BoxLayout to it
        float_layout = FloatLayout()
        float_layout.add_widget(layout)

        return float_layout

    def submit_data(self, instance):
        # Get values from text inputs
        name = self.name_input.text
        age = self.age_input.text
        email = self.email_input.text

        # Insert data into MSSQL Server database
        cursor = conn.cursor()
        cursor.execute("INSERT INTO Tbl_1 (Name, Age, Email) VALUES (?, ?, ?)", name, age, email)
        conn.commit()
        cursor.close()

        # Clear text inputs
        self.name_input.text = ''
        self.age_input.text = ''
        self.email_input.text = ''


# Run the app
if __name__ == '__main__':
    DataEntryFormApp().run()
