#!/usr/bin/python3
# cognition: 인지/지각/사고

# python module
from text_to_speech import TextToSpeech
from src.data import behavior_list
from src.NLP import NLP, Dictionary
import os
import sys
import time
import re

# openpibo module
import openpibo

# my module
sys.path.append(os.path.dirname(os.path.abspath(os.path.dirname(
    os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))))
# print(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(os.path.abspath(os.path.dirname(__file__))))))))
# from speech_to_text import speech_to_text

NLP = NLP()
Dic = Dictionary()
tts = TextToSpeech()


def text_to_speech(text):
    filename = "tts.wav"
    print("\n" + text + "\n")
    tts.tts_connection(text, filename)
    tts.play(filename, 'local', '-1500', False)


def wait_for(item):
    while True:
        print(f"{item} 기다리는 중")
        break


def ends_with_jong(kstr):
    m = re.search("[가-힣]+", kstr)
    if m:
        k = m.group()[-1]
        return (ord(k) - ord("가")) % 28 > 0
    else:
        return


def lee(kstr):
    josa = "이" if ends_with_jong(kstr) else ""
    print(f"{kstr}{josa} ", end='')
    return josa


def aa(kstr):
    josa = "아" if ends_with_jong(kstr) else "야"
    print(f"{kstr}{josa} ", end='')
    return josa


def Project_A(user_name):
    print(f"user name: {user_name} \n")

    while True:
        time.sleep(1)
        text_to_speech(
            f"미안해 {user_name}{aa(user_name)}. 다음에는 꼭 이름을 기억할게. 오늘은 너의 이야기를 들어주는 서비스를 보여줄거야. 자, 최근에 있었던 일 중에서 기억에 남는 일이 있으면 나에게 이야기해 주겠니?")
        text_to_speech(
            "앞에 있는 그림 일기에 다가 오늘 너의 하루는 어땠는지 그림으로 표현해줘. 그리고 그림을 다 그린 후에 다 했다고 말해줘.")
        break

    while True:
        user_said = input("답변: ")
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'DONE':
            while True:
                time.sleep(1)
                text_to_speech("우와! 혹시 그림 일기에 대해서 설명해 줄 수 있어?")
                break
        else:
            wait_for('DONE')
            continue
        break

    while True:
        user_said = input("답변: ")
        answer = NLP.nlp_answer(user_said=user_said, dic=Dic)

        if answer == 'DONE':
            while True:
                time.sleep(1)
                text_to_speech("아, 그런 일이 있었구나, 너에 대해서 조금 더 알게 된 것 같아.")
                break
        else:
            wait_for('DONE')    # DONE 답변 들어올 때까지 stt open 반복
        break

    while True:
        behavior_list.do_question_S()
        text_to_speech(
            f"너의 일상에 대해서 알려줘서 고마워. 이번에도 너를 위해서 선물을 하나 준비했는데, 두 가지 종류의 스티커를 준비했어. 저번에 네가 어떤 종류의 스티커를 가져갔는지 기억이 잘 나지않아. {user_name}{lee(user_name)}는 무엇을 가져갈래?")
        user_said = input("답변: ")
        if user_said == '귀여운':
            while True:
                time.sleep(1)
                text_to_speech("귀여운 스티커는 좋은 선택이야!")
                break
        else:
            while True:
                time.sleep(1)
                text_to_speech("멋있는 스티커는 좋은 선택이야!")
                break
        break

    while True:
        text_to_speech("오늘 만나서 반가웠어. 잘가!")
        break


def Play_Project():
    behavior_list.do_question_S()
    text_to_speech(
        "안녕. 우리 지난번에 만났던 것 같은데, 너의 이름이 잘 기억나지 않아. 혹시 다시 한번 알려줄 수 있어?")
    user_said = input("답변: ")
    Project_A(user_said)


Play_Project()
