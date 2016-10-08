#!/usr/bin/env python3
# -*- coding: utf-8 -*-
#
#  OpenST.py
#  
#  Copyright 2016 Dmitriy <dmitriy@dmitriy-Lenovo-B590>
#  
#  This program is free software; you can redistribute it and/or modify
#  it under the terms of the GNU General Public License as published by
#  the Free Software Foundation; either version 2 of the License, or
#  (at your option) any later version.
#  
#  This program is distributed in the hope that it will be useful,
#  but WITHOUT ANY WARRANTY; without even the implied warranty of
#  MERCHANTABILITY or FITNESS FOR A PARTICULAR PURPOSE.  See the
#  GNU General Public License for more details.
#  
#  You should have received a copy of the GNU General Public License
#  along with this program; if not, write to the Free Software
#  Foundation, Inc., 51 Franklin Street, Fifth Floor, Boston,
#  MA 02110-1301, USA.
# 
#  
import gtts
import speech_recognition as sr
import vlc
import slowclap as sc
#synth

def say(_phrase : str, _lang : str = 'en', mp3buf : str = 'openst.buf.mp3') :
        tts = gtts.gTTS(text=_phrase, lang=_lang)
        tts.save(mp3buf)
        vlco = vlc.MediaPlayer(mp3buf)
        vlco.play()

#end synth

#recognition

r = sr.Recognizer()
feed = sc.MicrophoneFeed()
detector = sc.AmplitudeDetector(feed, threshold=6500000)

def calibrate(debug_mode : bool = False, clap_tresh : int = 6500000) :
    with sr.Microphone() as source :
        print("A moment of silence, please...")
        r.adjust_for_ambient_noise(source)
        if(debug_mode) :
            print("Set minimum energy threshold to {}".format(r.energy_threshold))
        detector = sc.AmplitudeDetector(feed, threshold=clap_tresh)

def listen(lang : str = "en-US", clap_detection : bool = False, debug_mode : bool = False) :
    # Record Audio
    if(clap_detection) :
        for clap in detector :
            with sr.Microphone() as source:
                print("Say something!")
                vlco = vlc.MediaPlayer("Start.wav")
                vlco.play();
                audio = r.listen(source)
                vlco = vlc.MediaPlayer("End.wav")
                vlco.play()
        
                # Speech recognition using Google Speech Recognition
                try:
                    # for testing purposes, we're just using the default API key
                    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                    # instead of `r.recognize_google(audio)`
                    rec = ""
                    rec = r.recognize_google(audio, language=lang)
                    print("You said: " + rec)
                    vlco = vlc.MediaPlayer("Success.wav")
                    vlco.play()
                except sr.UnknownValueError:
                    vlco = vlc.MediaPlayer("Fail.wav")
                    vlco.play()
                    if(debug_mode) :
                        print("Google Speech Recognition could not understand audio")
                except sr.RequestError as e:
                    vlco = vlc.MediaPlayer("Fail.wav")
                    vlco.play()
                    if(debug_mode) :
                        print("Could not request results from Google Speech Recognition service; {0}".format(e))
                except TimeoutError as e:
                    vlco = vlc.MediaPlayer("Fail.wav")
                    vlco.play()
                    if(debug_mode) :
                        print("Timed out; {0}".format(e))
            break
    else :
        with sr.Microphone() as source:
                print("Say something!")
                vlco = vlc.MediaPlayer("Start.wav")
                vlco.play();
                audio = r.listen(source)
        
                # Speech recognition using Google Speech Recognition
                try:
                    # for testing purposes, we're just using the default API key
                    # to use another API key, use `r.recognize_google(audio, key="GOOGLE_SPEECH_RECOGNITION_API_KEY")`
                    # instead of `r.recognize_google(audio)`
                    rec = ""
                    rec = r.recognize_google(audio, language=lang)
                    print("You said: " + rec)
                    vlco = vlc.MediaPlayer("Success.wav")
                    vlco.play()
                except sr.UnknownValueError:
                    vlco = vlc.MediaPlayer("Fail.wav")
                    vlco.play()
                    if(debug_mode) :
                        print("Google Speech Recognition could not understand audio")
                except sr.RequestError as e:
                    vlco = vlc.MediaPlayer("Fail.wav")
                    vlco.play()
                    if(debug_mode) :
                        print("Could not request results from Google Speech Recognition service; {0}".format(e))
                except TimeoutError as e:
                    vlco = vlc.MediaPlayer("Fail.wav")
                    vlco.play()
                if(debug_mode) :
                    print("Timed out; {0}".format(e))
    return rec

#end recognition
