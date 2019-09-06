﻿This is sample code for Text Analytics sentiment v3 - Japanese
 
 ## Sentiment Analysis v3 public preview

The [next version of Sentiment Analysis](https://westcentralus.dev.cognitive.microsoft.com/docs/services/TextAnalytics-v3-0-preview/operations/56f30ceeeda5650db055a3c9) is now available for public preview. It provides significant improvements in the accuracy and detail of the API's text categorization and scoring.


### Sentiment Analysis v3 example request

The following JSON is an example of a request made to the new version of Sentiment Analysis. The request formatting is the same as the previous version:

```json
    {
        "documents": [
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
        ],
    }
```

### Sentiment Analysis v3 example response

A score closer to 0 indicates a negative sentiment, while a score closer to 1 indicates a positive sentiment:

```console
Document Id:  1 , Sentiment Score:  0.56
Document Id:  2 , Sentiment Score:  0.68
```
