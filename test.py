
import schedule
import time
from plyer import notification

def alert(title, message):
    notification.notlify(
        title=title,
        message=message,
        app_name='Alerta do Windows',
        timeout=1
    )

    def msg():
        alert('Alerta do windows', 'hora de caralhar!!')

    if __name__=="__main__":
        schedule.every().day.at("19:36").do(msg)

        while True:
            schedule.run_pending()
            time.sleep(1)    
