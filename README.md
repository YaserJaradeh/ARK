# ARK
Text-based game that uses NLP models

## Components
ARK relies on a python backend and a Vue frontend. The frontend intercepts users input and funnels it to the backend for processing using the business logic.

### Python code
The python code is responsible for parsing the story from YAML format into in-memory decision tree structure.

Tha backend makes use of [Huggingface zero-shot classifier](https://huggingface.co/facebook/bart-large-mnli) to deal with natural language text input of the user.  

### Vue.js code
The code for the frontend is mostly based on the [Vue-shell](https://github.com/HalasProject/vue-shell) project.

## Deployment
Online demo available [here]().

deployment infrastructure through [Streamlit.io](https://streamlit.io/)

## Credits
Thanks to ...
