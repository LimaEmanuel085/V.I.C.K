import speech_recognition as sr
import pyttsx3
import datetime
from datetime import date
import pyautogui as pg
import time
import wikipedia

pg.PAUSE = 1

#transformar texto em fala:
bot = pyttsx3.init()
def executa_comando():
 #Habilita o microfone para ouvir o usuario
 microfone = sr.Recognizer()
 with sr.Microphone() as source:
    microfone.adjust_for_ambient_noise(source)
    print("Diga alguma coisa: ")
  #Armazena a informacao de audio na variavel
    audio = microfone.listen(source)
    try:
        #transforma áudio em texto

        comand = microfone.recognize_google(audio,language='pt-BR')
        comand = str(comand)
        comand = comand.lower()
      #retorno do comando
        if 'vick' in comand:
            comand = comand.replace('vick' , '')
            print(comand)
            if 'horas' in comand:
                hora = datetime.datetime.now().strftime('%H:%M')
                bot.say('Agora são exatamente' + hora)
                bot.runAndWait()
            elif 'data' in comand:
                data = date.today().strftime('%d/%m/%Y')
                bot.say('Hoje é' + data)
                bot.runAndWait()


            elif 'emily' in comand:
                bot.say('A dona Emilly é a namorada de meu criador, uma perfeita e linda moça que esbanja perfeição. Estou a sua dispozição, Emilly')
                bot.runAndWait()

            elif 'hoje é aula da priscila' in comand:
                bot.say('Vixe, melhor o senhor ir buscando logo a chave e o projetor, se não, com certeza ela quebra o senhor na porrada.')
                bot.runAndWait()

            elif 'quem sou eu' in comand:
                bot.say('Você é meu criador, Emanuel Lima, atualmente, estudante da EEEP Marwin.')
                bot.runAndWait()

            elif 'bom dia' in comand:
                bot.say('Bom dia, como o senhor está ?')
                bot.runAndWait()

            elif 'o que é' in comand:
                comand = comand.replace('o que é', '')
                wikipedia.set_lang('pt')
                result = wikipedia.summary(comand, sentences = 3)
                bot.say('De acordo com wikipedia' + result)
                bot.runAndWait()

            elif 'pesquise por' in comand:
                comand = comand.replace('pesquisar por', '')
                wikipedia.set_lang('pt')
                result = wikipedia.summary(comand, sentences = 3)
                bot.say('De acordo com wikipedia' + result)
                bot.runAndWait()

            elif 'quem é' in comand:
                comand = comand.replace('quem é', '')
                wikipedia.set_lang('pt')
                result = wikipedia.summary(comand, sentences = 3)
                bot.say('De acordo com wikipedia' + result)
                bot.runAndWait()

            elif 'quem foi' in comand:
                comand = comand.replace('quem foi', '')
                wikipedia.set_lang('pt')
                result = wikipedia.summary(comand, sentences = 3)
                bot.say('De acordo com wikipedia' + result)
                bot.runAndWait()

            elif 'tocar' in comand:
                comand = comand.replace('tocar', '')
                bot.say('Reproduzindo sua playlist principal no spotify.')
                bot.runAndWait()
                pg.press('win')
                pg.write('spotify')
                pg.press('enter')

                time.sleep(15)

                pg.click(x=40, y=247)
                time.sleep(0.5)
                pg.moveTo(x=141, y=397)
                pg.click(x=141, y=397)

    except sr.UnkownValueError:
        print("Não entendi")
 return comand
executa_comando()