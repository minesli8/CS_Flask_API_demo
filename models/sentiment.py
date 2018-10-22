from flask_restful import reqparse, Resource
import requests
import numpy


class sentiment_analyzer(Resource):

    def get(self):
        # argument parsing
        parser = reqparse.RequestParser()
        # parser.add_argument('query')
        parser.add_argument('query')

        args = parser.parse_args()
        user_input = args['query']

        article_url = user_input.strip()

        temp = numpy.random.uniform(0, 1, 1)
        if temp<0.5:
            sentiment = 'negative'
        else:
            sentiment = 'positive'

        # response = requests.get(article_url)
        #
        # content = response.text
        #
        # start = content.find('content=')
        #
        # partial_content = content[start: start+100]

        output = {'sentiment': sentiment}

        return output
