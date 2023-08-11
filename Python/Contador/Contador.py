import datetime, time
import customtkinter as ctk
from tkcalendar import Calendar, DateEntry
import threading

ctk.set_appearance_mode("Dark") # Modes: "System" (standard), "Dark", "Light"
ctk.set_default_color_theme("blue")  # Themes: "blue" (standard), "green", "dark-blue"

#self.protocol("WM_DELETE_WINDOW", callback) # Altera a funcionalidade do botão fechar

class App(ctk.CTk):
    def __init__(self):
        super().__init__()
        
        largura = 260
        altura = 280
        #geom = str(largura) + " x " + str(altura)

        
        self.title("Contador")
                        
        largura_tela = self.winfo_screenwidth()
        altura_tela =  self.winfo_screenmmheight()
        
        # posicao da tela
        posix = self.winfo_screenwidth() - (self.winfo_screenwidth() * 0.20)
        posiy =  self.winfo_screenmmheight() - (self.winfo_screenmmheight() * 0.15 )
        self.geometry("%dx%d+%d+%d" % (largura,altura,posix,posiy))
        self.resizable(width=False, height=False)
        self.protocol("WM_DELETE_WINDOW", self.stop_countdown) # Altera a funcionalidade do botão fechar
        self.wm_attributes('-toolwindow', 'False') #Remover icone padrão
        self.overrideredirect(False) #Remover janela
        
        
        self.tela_inicial = ctk.CTkFrame(self,
                                        fg_color='transparent',
                                        border_color='gray',
                                        border_width=1
                                        )
        self.tela_inicial.grid(row=0, column=0, padx=10, pady=10,  sticky="nsew")                
                       
        self.data_label =ctk.CTkLabel(self.tela_inicial, fg_color='transparent', text='Selecione a DATA FIM' )
        self.data_label.grid(row=0, column=0, sticky="wne", padx=10, pady=10 )
        
        mindate = datetime.datetime(datetime.date.today().year, datetime.date.today().month, (datetime.date.today().day +1)) 
        
        self.data_to = Calendar(self.tela_inicial, 
                                firstweekday='sunday', 
                                #selectmode='day', 
                                mindate=mindate, 
                                showweeknumbers = False,  
                                disabledforeground='red', 
                                disableddayforeground = 'black', 
                                year=2023, month=9, day=19)
        self.data_to.grid(row=1, column=0, sticky="wne", padx=10, pady=10 )
        
        self.btn = ctk.CTkButton(self.tela_inicial,
                                 command=self.start_countdown,
                                 text="Start"
                                 )
        self.btn.grid(row=2, column=0, sticky='esw')
      
        
        self.loop_time = ctk.CTkFrame(self, 
                                        fg_color="transparent",                                                         
                                        border_color='gray',
                                        border_width=1                                                                                        )
        self.loop_time.grid(row=0, column=0, padx=10, pady=10,  sticky="nsew")                
        self.texto = ctk.CTkLabel(self.loop_time, text='00', fg_color='transparent' , font=("sans-serif", 180))
        self.texto.grid(row=0, column=0, sticky='nsew', padx=2, pady=10)                
        self.tempodias = ctk.CTkLabel(self.loop_time, text='DIAS', fg_color='transparent')
        self.tempodias.grid(row=1, column=0, sticky='nsew', padx=2, pady=2)        
        
        self.date_end = datetime.datetime.strptime(self.data_to.get_date(), '%d/%m/%Y')
        self.thr = threading.Thread()
        self.stop_thread = False
        
        
        # select default frame
        self.select_frame_by_name("tela_inicial")
        
    def start_countdown(self):
      self.date_end = datetime.datetime.strptime(self.data_to.get_date(), '%d/%m/%Y')
      self.select_frame_by_name("loop_time")
      self.stop_thread = False
      self.thr = threading.Thread(target=self.loop_countdown)
      if not self.thr.is_alive():
        self.thr.start()
    
    def stop_countdown(self):
      self.stop_thread = True       
      if self.thr.is_alive():                
        self.thr.join()      
      quit()
            
    def loop_countdown(self):              
      data_TO =  self.date_end 
      resultado = 1
      
      while resultado > 0 and self.stop_thread == False :
        result = data_TO - datetime.datetime.now()  
        self.texto.configure(text=str(result.days))        
        self.tempodias.configure(text=str(result))            
        resultado = result.days
        if self.stop_thread: # Aqui paramos a thread
          self.tempodias.configure(text='Encerrando ...') 
          quit()                   
        time.sleep(0.01)                    
        
    def select_frame_by_name(self, name):
      #self.loop_time.grid_forget()
      #self.tela_inicial.grid_forget()      
      if name == "tela_inicial":
            self.tela_inicial.grid(row=0, column=0, sticky="nsew")
      else:
            self.tela_inicial.grid_forget()
      if name == "loop_time":
            self.loop_time.grid(row=0, column=0, sticky="nsew")
            
            posix = self.winfo_screenwidth() - (self.winfo_screenwidth() * 0.20)
            posiy =  self.winfo_screenmmheight() - (self.winfo_screenmmheight() * 0.15 )
            self.geometry("%dx%d+%d+%d" % (210,260,posix,posiy))
            
      else:
            self.loop_time.grid_forget()

if __name__ == "__main__":
    app = App()
    app.mainloop()