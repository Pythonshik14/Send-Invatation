import smtplib                                      
import login

# Добавляем необходимые подклассы - MIME-типы
from email.mime.multipart import MIMEMultipart           
from email.mime.text import MIMEText                
from email.mime.image import MIMEImage            

def send_mail(mans, time, place, you):
    addr_from = login.addr_from                         
    addr_to   = login.addr_to                           
    password  = login.password                          
                        
    msg = MIMEMultipart()                               
    msg['From']    = addr_from                          
    msg['To']      = addr_to                            
    msg['Subject'] = 'Приглашение на свадьбу!'   

    msg_text = f"""Дорогие {mans}!
    Приглашаем Вас на торжество,
    посвященное нашему бракосочетанию,
    которое состоится {time}
    в банкетном зале,
    по адресу: {place}
    Будем счастливы видеть Вас на нашем празднике!
    {you}
    """

    with open(r"C:\Users\user\Desktop\congrat\ring.jpg", 'br') as f: body = f.read()
    msg.attach(MIMEText(msg_text, 'plain'))                 
    msg.attach(MIMEImage(body))                 

    server = smtplib.SMTP('smtp.gmail.com', 587)                        
    server.starttls()                                   
    server.login(addr_from, password)                   
    server.send_message(msg)                            
    server.quit()


who = input("Кого приглашаете(имя) - ")
time = input("Время свадьбы - ")      
place = input("Адрес где будет проходить мероприятие - ")
you = input("Представтесь кто вы - ")                                 
send_mail(who, time, place, you)