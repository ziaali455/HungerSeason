import openai
import streamlit as st
st.markdown("# The Hunger Season")
st.markdown("_Created by Ali Zia (az2741@columbia.edu) for NewsGamer")
st.markdown('Years of poor farming practices and drought have cast European Country X into a devastating hunger season. \nTwo years ago, in an attempt to protect Country Xs nuclear weapons program amid tensions with Ghana, President Felix terminated the Open Dialogue Agreement (ODA)between Country X, the US, and major European/African powers to maintain open economic and military discourse and motivate world peace. Now, in an attempt to pull Country X out of disaster, \
    you have been appointed as the new president, and must resume talks with world leaders for aid.\nCan you right the wrongs of Silvas diplomatic strategy, or will the people of Country X stay hungry?')
st.markdown('Looking for words similar to one you already know? **Type the word in English and press Enter below.**')
openai.api_key = "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"
model_engine = "gpt-3.5-turbo" 
choice = input("--------\nYears of poor farming practices and drought have cast European Country X into a devastating hunger season. \nTwo years ago, in an attempt to protect Country X's nuclear weapons program amid tensions with Ghana, \
President Felix terminated the Open Dialogue Agreement (ODA)\nbetween Country X, the US, and major European/African powers to maintain open economic and military discourse and motivate world peace.\nNow, in an attempt to pull Country X out of disaster, \
    you have been appointed as the new president, and must resume talks with world leaders for aid.\nCan you right the wrongs of Silva's diplomatic strategy, or will the people of Country X stay hungry? Let's go! \n-------\n Step 1: You're at a UN banquet dinner and have the choice to sit next to one of the two leaders: \
          \n 1: Pedro do Santos (Brazilian head of foreign affairs) \n 2: Elizabeth Kjellburg (Swedish PM and current member of the ODA)\n Choice: ")
contextString = " "
person = " "
if(choice == "1"):
    contextString = "You're the President of Brazil in a game. The user is the president of Country X which is undergoing heavy famine. The last president of Country X terminated the ODA. You're at a UN banquet. You are not in the ODA, but Brazil has lots of agriculture, so Country X wants to talk. Don't be too enthusiastic, but talk to Country X about their famine and help Brazil expand into Europe without deals with the US. 100 words max "
    person = "Pedro"
if(choice == "2"):
    contextString = "You are a character in a game called The Hunger Season. The user is the president of Country X which is undergoing heavy famine. You will act as PM Elizabeth Kjellburg at a UN banquet. You \
        are a current member of the ODA, which includes the US, all Eastern European countries, Ghana, and Kenya. Negotiate with Country X without risking your allies and losing GDP. 100 words max"
    person = "Elizabeth"

while True:
    userDialogue = input("What would you like to ask " + person + "?\n")
    if (userDialogue=="-1"):
        break
    response = openai.ChatCompletion.create(
        model='gpt-3.5-turbo',
        temperature = 0.5,
        messages=[
            #first line gives GPT a context of its role, second line feeds quesitons it's asked
            {"role": "system", "content": contextString},
            {"role": "user", "content": userDialogue},
        ])
    message = response.choices[0]['message']
    print("{}: {}".format(message['role'], message['content']))


