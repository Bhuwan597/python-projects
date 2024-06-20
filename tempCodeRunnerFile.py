def take_command():
    r = sr.Recognizer()
    with sr.Microphone() as source:
        with yaspin(text="Listening to your voice . . . . . .", color="green") as spinner:
            # playsound.playsound('mic.wav',False)
            winsound.Beep(700,500)
            r.pause_threshold=1
            audio = r.listen(source,timeout=2,phrase_time_limit=5)
            spinner.ok('✅')

    try:
        with yaspin(text="Recognizing your voice . . . . . .", color="green") as spinner:
            winsound.Beep(700,500)
            query = r.recognize_google(audio,language='en-in')
            print(f'\nYou said: {query}')
            spinner.ok("✅ ")

    except:
        speak("Sorry sir, I didn't hear you properly")
        print('😢😌😢🙉')
        spinner.fail("❌ ")
        return ''
    return query