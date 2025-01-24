# Chatbot for FAQs

The FAQ Chatbot is a simple automated responder that answers frequently asked questions (FAQs) about a specific product or service. It utilizes Natural Language Processing (NLP) techniques using Python and libraries such as NLTK and SpaCy to understand user queries and provide appropriate responses.


## Features

- Handles common FAQs about a product.
- Responds to greetings.
- Provides fallback responses for unrecognized queries.

## Requirements

- Python 3.x
- NLTK library

## Installation

```bash
git clone https://github.com/yourusername/codealpha_tasks.git
cd codealpha_tasks/chatbot_faq
pip install -r requirements.txt

## Set Up a Virtual Environment (optional but recommended)

```bash
   python -m venv venv
   source venv/bin/activate  # On Windows use venv\Scripts\activate
   
## Install Required Libraries

```bash
   pip install nltk
   pip install spacy  # Only if you plan to use SpaCy
   python -m spacy download en_core_web_sm  # Necessary for SpaCy
   

## Interacting with the Chatbot
   Type your questions as prompted.
   To exit the chat, type quit.

## Adding More Questions

To enhance the chatbot's knowledge base, you can simply modify the faq_pairs list within the script. Each FAQ entry is defined as a regular expression pattern and its corresponding responses in a list.

## Contributing

If you would like to contribute to the project, please fork the repository and create a new branch for your feature or bug fix. Then, submit a pull request detailing your changes.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgments
https://www.nltk.org/
https://spacy.io/

Author
Zunaid Hasan
hasan15-6033@diu.edu.bd

