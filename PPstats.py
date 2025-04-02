import pandas as pd
import matplotlib.pyplot as plt

class PSStatistics:
    def init(self, filename):
        self.filename = filename
        self.df = None
    
    def load_data(self):
        
        self.df = pd.read_csv(self.filename)
    
    def plot_pie_chart(self):
       
        if self.df is None:
            raise ValueError("Данные не загружены.")
        
        # Группировка данных по 'Account Name' и суммирование расходов
        expense_data = self.df.groupby('country')['Amount'].sum()
        
        plt.figure(figsize=(7, 7))
        expense_data.plot(kind='pie', autopct='%1.1f%%', startangle=140)
        plt.title("Распределение игроков PlayStation по странам")
        plt.ylabel("")
        plt.show()