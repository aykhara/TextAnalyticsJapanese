from azure.cognitiveservices.language.textanalytics import TextAnalyticsClient
from msrest.authentication import CognitiveServicesCredentials
import os

# TODO: Configure an environment variable for authentication (e.g.Windows  $setx COGNITIVE_SERVICE_KEY "your-key")
# replace this endpoint with the correct one for your Azure resource. 
text_analytics_url = "TEXT_ANALYTICS_ENDPOIN"
# This sample assumes you have created an environment variable for your key
key = os.environ["TEXT_ANALYTICS_SUBSCRIPTION_KEY"]
credentials = CognitiveServicesCredentials(key)

# Authenticate the client
text_analytics = TextAnalyticsClient(endpoint=text_analytics_url, credentials=credentials)

# Sentiment analysis
documents = [
    {
        "id": "1",
        "language": "ja",
        "text": "今日は祝日だ"
    },
        {
        "id": "2",
        "language": "ja",
        "text": "美味しいごはんを食べて幸せ"
    }
]
response = text_analytics.sentiment(documents=documents)
for document in response.documents:
    print("Document Id: ", document.id, ", Sentiment Score: ",
          "{:.2f}".format(document.score))


# Language detection
documents = [
    {
        'id': '1',
        'text': 'このドキュメントは日本語で書かれています'
    }
]
response = text_analytics.detect_language(documents=documents)
for document in response.documents:
    print("Document Id: ", document.id, ", Language: ",
          document.detected_languages[0].name)


# Entity recognition
documents = [
    {
        "id": "1",
        "language": "ja",
        "text": "マイクロソフトは1975年4月4日にビルゲイツとポールアレンによって創設された"
    }
]
response = text_analytics.entities(documents=documents)

for document in response.documents:
    print("Document Id: ", document.id)
    print("\tKey Entities:")
    for entity in document.entities:
        print("\t\t", "NAME: ", entity.name, "\tType: ",
              entity.type, "\tSub-type: ", entity.sub_type)
        for match in entity.matches:
            print("\t\t\tOffset: ", match.offset, "\tLength: ", match.length, "\tScore: ",
                  "{:.2f}".format(match.entity_type_score))


# Key phrase extraction
documents = [
    {
        "id": "1",
        "language": "ja",
        "text": "私の犬は獣医に見てもらう必要がある"
    }
]
response = text_analytics.key_phrases(documents=documents)

for document in response.documents:
    print("Document Id: ", document.id)
    print("\tKey Phrases:")
    for phrase in document.key_phrases:
        print("\t\t", phrase)