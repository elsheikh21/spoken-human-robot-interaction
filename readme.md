# Spoken Human Robot Interaction

**Goal**: Simply to make a simple dialogue between a human being and an agent

1. We need to install the required dependencies `pip install requirements.txt`

2. (Speech-To-Text) `STT`

   - Use google speech recognition api
   - calibrates the microphone to the ambient noise for 2 seconds
   - plays a beep sound after calibration, so the user can say his/her words
   - audio file is sent to google speech recognition api to be analyzed and return the text

3. (Text-To-Speech) `TTS`

   - two approaches (one is by using google text to speech, and the other by using python native library pyttsx3)
   - both of them takes a text as input, and say it using PC speakers, however, using google we can specify the language
   - we can save the dialog as well

4. (Understanding Natural Language) `NLP`

   - Named Entity Recognition `NER`
     - extracting information from unstructured text to classify named entities into a set of predefined categories, for example person names, organizations, locations, medical codes, time expressions, quantities, monetary values, percentages, etc.
   - Part-of-speech Tagging `POS`
     - to get better understanding of the text, we need to understand what are the properties -or predicates- of the nouns in a given text

5. Putting it all together, this mini project was built using few strings for the bot to speak out `TTS`, and afterwards, waiting for the user input -after mic calibration- `STT`, these words from the user were analyzed using `spa

Read more about [SHRI](docs/report.md) 
