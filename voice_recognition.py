def pilih_menu():
    print("Halo Selamat Datang!!")
    print("""Pilih Menu:
          1. Speech To Text
          2. Text To Speech
          3. Speech To Translate""")
    opsi = int(input("Masukkan pilihan anda: "))
    if opsi == 1:
        ubah_suara_teks()
    elif opsi == 2:
        ubah_teks_suara()
    elif opsi == 3:
        ubah_suara_translate()


def ubah_suara_teks():
    import speech_recognition as sr
    recognizer = sr.Recognizer()
    def capture_voice_input(): 
        with sr.Microphone() as source: 
            print("Listening...") 
            audio = recognizer.listen(source) 
        return audio

    def convert_voice_to_text(audio): 
        try: 
            text = recognizer.recognize_google(audio) 
            print("You said: " + text) 
        except sr.UnknownValueError: 
            text = "" 
            print("Sorry, I didn't understand that.") 
        except sr.RequestError as e: 
            text = "" 
            print("Error; {0}".format(e)) 
        return text 

    def process_voice_command(text): 
        if "hello" in text.lower(): 
            print("Hello! How can I help you?") 
        elif "goodbye" in text.lower(): 
            print("Goodbye! Have a great day!") 
            return True 
        else: 
            print("I didn't understand that command. Please try again.") 
            return False
    
    def main(): 
        end_program = False 
        while not end_program: 
            audio = capture_voice_input() 
            text = convert_voice_to_text(audio) 
            end_program = process_voice_command(text)
          
    if __name__ == "__main__": 
        main()


def ubah_teks_suara():
    # jika ingin mengonversi teks menjadi suara dan menyimpannya ke dalam file audio menggunakan kode di bawah ini
    # from gtts import gTTS
    # kalimat=input("Masukan Text=") 
    # bahasa="id" 
    # filesaya=gTTS(text=kalimat,lang=bahasa) 
    # filesaya.save("apaitu.mp3") 
    # print("File tersimpan")

    import pyttsx3 

    # Teks yang ingin Anda konversi menjadi suara 
    text = input("Masukkan teks: ") 
 
    # Inisialisasi engine TTS 
    engine = pyttsx3.init() 
  
    # Set properti suara (opsional) 
    engine.setProperty('rate', 100)  # Ubah kecepatan bicara 
    engine.setProperty('volume', 0.9)  # Ubah volume suara 
  
    # Konversi teks menjadi suara dan putar 
    engine.say(text) 
    engine.runAndWait()


def ubah_suara_translate():
    import speech_recognition as sr 
    from googletrans import Translator 
    
    # Fungsi untuk melakukan speech-to-text menggunakan library speech_recognition 
    def speech_to_text(): 
        recognizer = sr.Recognizer() 
        with sr.Microphone() as source: 
            print("Silahkan mulai berbicara...") 
            audio_data = recognizer.listen(source) 
            try: 
                text = recognizer.recognize_google(audio_data, language='id-ID')  # Menentukan bahasa input sebagai Bahasa Indonesia
                print("Text:", text) 
                return text 
            except sr.UnknownValueError: 
                print("Maaf, Speech Recognition tidak bisa memahami audio.") 
            except sr.RequestError as e: 
                print("Maaf, tidak ada respon dari Google Speech Recognition service; {0}".format(e)) 
        return None 
    
    # Fungsi untuk menerjemahkan teks menggunakan Google Translate 
    def translate_text(text, target_language='en'): 
        translator = Translator() 
        translated_text = translator.translate(text, src='id', dest=target_language)  # Mengatur bahasa sumber sebagai Bahasa Indonesia
        print("Translated Text:", translated_text.text) 
        return translated_text.text
    
    # Merekam suara dari mikrofon, mentranskripsi teks, dan kemudian menerjemahkan ke bahasa lain 
    input_text = speech_to_text() 
    if input_text: 
        translated_text = translate_text(input_text, target_language='en')  # Mengatur bahasa tujuan sebagai Bahasa Inggris

pilih_menu()