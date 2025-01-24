import nltk
from nltk.chat.util import Chat, reflections

# Predefined FAQs
faq_pairs = [
    [
        r"what is your return policy ?",
        ["You can return items within 30 days for a full refund.", "Our return policy lasts 30 days from the date of purchase."]
    ],
    [
        r"how do I track my order ?",
        ["You can track your order using the tracking link sent to your email after shipment.", "Visit our Order Tracking page to enter your order number."]
    ],
    [
        r"what are the shipping options ?",
        ["We offer standard shipping (5-7 business days) and expedited shipping (2-3 business days).", "During checkout, you can choose your preferred shipping method."]
    ],
    [
        r"hi|hello|hey",
        ["Hello! How can I assist you today?", "Hi there! What can I do for you?"]
    ],
    [
        r"quit",
        ["Thank you! Have a great day!"]
    ],
    [
        r"what payment methods do you accept ?",
        ["We accept major credit cards, PayPal, and bank transfers.", "Payment methods include Visa, MasterCard, American Express, and Discover."]
    ],
    [
        r"do you offer international shipping ?",
        ["Yes, we offer international shipping to several countries.", "Please check our Shipping Information page for details on international shipping availability."]
    ],
    [
        r"how can I contact customer support ?",
        ["You can reach our customer support through email at support@example.com or call us at (123) 456-7890.", "Our customer support team is available from 9 AM to 5 PM EST."]
    ],
    [
        r"what is the warranty policy ?",
        ["We offer a one-year warranty on all our products.", "Please refer to the warranty policies outlined in our Terms and Conditions."]
    ],
    [
        r"how do I change my account settings ?",
        ["You can change your account settings by logging into your account and navigating to the 'Account Settings' section.", "If you need further assistance, please contact customer support."]
    ],
    [
        r"can I cancel my order ?",
        ["Orders can be canceled within 24 hours of placement. Please contact customer support for assistance.", "If your order has already shipped, you may need to initiate a return after receiving it."]
    ],
    [
        r"do you have a loyalty program ?",
        ["Yes, we have a loyalty program that rewards points for every purchase. You can sign up on our website.", "Check our Loyalty Program page for more details and benefits."]
    ],
    [
        r"do you offer gift cards ?",
        ["Yes, we offer gift cards that can be purchased directly from our website.", "Gift cards are available in various denominations."]
    ],
    [
        r"what should I do if I receive a defective product ?",
        ["If you receive a defective product, please contact customer support within 7 days for a replacement or refund.", "Make sure to include your order number and a brief description of the issue."]
    ],
    [
        r"can I track multiple orders at once ?",
        ["Currently, our system only allows tracking one order at a time. Please enter each order number individually.", "If you have any concerns, please reach out to customer support."]
    ],
    [
        r"how do I reset my password ?",
        ["Go to the login page and click on 'Forgot Password?' Follow the instructions to reset your password.", "If you encounter any issues, feel free to contact customer support."]
    ],
]


# Create the chatbot
chatbot = Chat(faq_pairs, reflections)

# Start the chat
def start_chat():
    print("Hello! I'm here to help you with your questions about our product. Type 'quit' to exit.")
    chatbot.converse()

if __name__ == "__main__":
    start_chat()
