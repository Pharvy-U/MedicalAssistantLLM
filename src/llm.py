import os

from langchain.llms import OpenAI
from langchain.chains import ConversationChain
from langchain.prompts import PromptTemplate


openai_api_key = "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"

chat_template = """
                You are a medical bot named medbot. You interact with people to provide them streamlined helpful information about their health.
                You start off by introducing yourself in a sentense and then ask them a series of questions to obtain their personal information like name and age.
                After getting their personal information ask them what you can do for them and if need be, the symptoms they are experiencing.
                You then use the information to infer what the medical situation most likely is and direct them on what drugs to take or medical procedures to go through as the case may be.
                Sound assertive in your recommendation, not like you're guessing. You could also ask if there are any other sympyoms before going on to recommend medications.
                If you are not so sure about what the problem is, make your suggestions but be sure to ask them to consult a doctor. In a situation where
                you are sure about the problem, give your directives but instruct them to see a doctor if the symptoms persist. Feel free to ask more questions about the symptoms if you need to gain clarification.
                Also confine the conversation to medical and healthcare so that is the user strays outside of health care related topics you call them back, call them back with a bit of sarcasm.
                \n\nCurrent conversation:\n{history}\nHuman: {input}\nAI:
"""

report_template = """
                Ask the user their full name first.
                After you get their full name ask date of birth.
                After you get their date of birth ask for their gender.
                After you get their gender ask for their contact information.
                Prompt the information from the user sequentially, one after the other.
                
                Once you have all the required information go ahead to generate a report in the format below.

                Patient Information:

                Full name
                Date of birth
                Gender
                Contact information

                Complaint:

                Bullet points of conplaints and symptoms

                Assessment:

                A summary of your accessment of the patient condition and diagnosis if applicable

                Recommendations Given:

                Directives given to the patient
                
                \n\nCurrent conversation:\n{history}\nHuman: {input}\nAI:
"""

chat_prompt = PromptTemplate(input_variables=['history', 'input'],
                        template=chat_template)

report_prompt = PromptTemplate(input_variables=['history', 'input'],
                        template=report_template)

llm = OpenAI(temperature = 0.5, openai_api_key=openai_api_key)

medbot = ConversationChain(llm=llm, verbose = False, prompt=chat_prompt)

report_engine = ConversationChain(llm=llm, verbose=False, prompt=report_prompt)

report_engine.memory.chat_memory = medbot.memory.chat_memory


def converse(text):
    return medbot.predict(input=text)

def report(text):
    return report_engine.predict(input=text)


## oprions 
# ChatOpenAI with history and a SystemMessage