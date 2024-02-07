import time
import RPi.GPIO as GPIO

GPIO.setmode(GPIO.BCM)

heure_date = [10, 34, 18, 18, 10, 2022]  # seconde minute heure jour mois année
mod = [60, 60, 24, 31, 12, 3000]  # limite d'incrementation
GPIO.setup(12, GPIO.OUT)
GPIO.setup(11, GPIO.OUT)
GPIO.setup(5, GPIO.OUT)
GPIO.setup(4, GPIO.OUT)
GPIO.setup(3, GPIO.OUT)
GPIO.setup(2, GPIO.OUT)
lcd = [12, 11, 5, 4, 3, 2]  # Pins pour l'écran LCD

def setup():
    for pin in lcd:
        GPIO.output(pin, GPIO.OUT)

def clear_lcd():
    for pin in lcd:
        GPIO.output(pin, GPIO.LOW)

def print_lcd(message, line, delay_time=0):
    clear_lcd()
    GPIO.output(lcd[0], GPIO.HIGH)  # BlueConnect!
    time.sleep(delay_time)
    clear_lcd()

def loop():
    seconds = 0
    while True:
        time.sleep(1)
        if seconds <= 2:
            print_lcd("BlueConnect!", 0, 3)
            seconds = 3

        heure_date[0] += 1  # incrementation du temps
        for i in range(6):
            if heure_date[i] == mod[i]:  # verification du dépassement de limite
                if i < 5:
                    heure_date[i + 1] += 1
                heure_date[i] = 0

        print_lcd_date_time()
        time.sleep(0.25)

def print_lcd_date_time():
    for j in range(3, 5):  # affichage de la date
        lcd_print_number(heure_date[j])

    lcd_print_number(heure_date[5])
    GPIO.output(lcd[1], GPIO.HIGH)  # Nouvelle ligne pour l'heure

    for j in range(2, -1, -1):  # affichage de l'heure
        lcd_print_number(heure_date[j])
        if j != 0:
            GPIO.output(lcd[3], GPIO.HIGH)  # Deux-points

def lcd_print_number(number):
    if number < 10:
        GPIO.output(lcd[4], GPIO.HIGH)  # Zéro initial
    for i in range(2):
        GPIO.output(lcd[i], GPIO.HIGH)  # Affichage du chiffre
        time.sleep(0.1)
        GPIO.output(lcd[i], GPIO.LOW)  # Éteindre le chiffre
        time.sleep(0.1)

if __name__ == "__main__":
    try:
        setup()
        loop()
    except KeyboardInterrupt:
        GPIO.cleanup()
"""#Include libraries
import RPi.GPIO as GPIO 
import time
from RPLCD.gpio import CharLCD

# Configure the LCD
lcd = (pin_rs = 19, pin_rw = None, pin_e = 16, pins_data = [21,18,23,24], 
numbering_mode = GPIO.BOARD)

# Create a variable ‘number’ 
number = 0

# Main loop
while(True):
# Increment the number and then print it to the LCD number = number + 1
lcd.clear()
lcd.write_string(“Count: “+ str(number))
time.sleep(1) 

lcd.close() 
GPIO.cleanup()"""
