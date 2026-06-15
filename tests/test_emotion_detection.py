import unittest
from unittest.mock import patch, Mock
from EmotionDetection.emotion_detection import emotion_detector


class TestEmotionDetector(unittest.TestCase):

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_emotion_detector_joy(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'emotionPredictions': [{
                'emotion': {
                    'anger': 0.003,
                    'disgust': 0.002,
                    'fear': 0.001,
                    'joy': 0.987,
                    'sadness': 0.001
                }
            }]
        }
        mock_post.return_value = mock_response

        result = emotion_detector("I am so happy today!")

        self.assertEqual(result['anger'], 0.003)
        self.assertEqual(result['disgust'], 0.002)
        self.assertEqual(result['fear'], 0.001)
        self.assertEqual(result['joy'], 0.987)
        self.assertEqual(result['sadness'], 0.001)
        self.assertEqual(result['dominant_emotion'], 'joy')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_emotion_detector_anger(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'emotionPredictions': [{
                'emotion': {
                    'anger': 0.876,
                    'disgust': 0.045,
                    'fear': 0.032,
                    'joy': 0.001,
                    'sadness': 0.012
                }
            }]
        }
        mock_post.return_value = mock_response

        result = emotion_detector("I am really angry right now!")

        self.assertEqual(result['dominant_emotion'], 'anger')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_emotion_detector_disgust(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'emotionPredictions': [{
                'emotion': {
                    'anger': 0.012,
                    'disgust': 0.912,
                    'fear': 0.023,
                    'joy': 0.001,
                    'sadness': 0.034
                }
            }]
        }
        mock_post.return_value = mock_response

        result = emotion_detector("This is utterly disgusting!")

        self.assertEqual(result['dominant_emotion'], 'disgust')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_emotion_detector_sadness(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'emotionPredictions': [{
                'emotion': {
                    'anger': 0.012,
                    'disgust': 0.002,
                    'fear': 0.045,
                    'joy': 0.001,
                    'sadness': 0.923
                }
            }]
        }
        mock_post.return_value = mock_response

        result = emotion_detector("I am so sad about this.")

        self.assertEqual(result['dominant_emotion'], 'sadness')

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_emotion_detector_fear(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 200
        mock_response.json.return_value = {
            'emotionPredictions': [{
                'emotion': {
                    'anger': 0.012,
                    'disgust': 0.002,
                    'fear': 0.945,
                    'joy': 0.001,
                    'sadness': 0.034
                }
            }]
        }
        mock_post.return_value = mock_response

        result = emotion_detector("I am really scared!")

        self.assertEqual(result['dominant_emotion'], 'fear')

    def test_emotion_detector_blank_input(self):
        result = emotion_detector("")
        self.assertIsNone(result)

        result = emotion_detector("   ")
        self.assertIsNone(result)

        result = emotion_detector(None)
        self.assertIsNone(result)

    @patch('EmotionDetection.emotion_detection.requests.post')
    def test_emotion_detector_error_400(self, mock_post):
        mock_response = Mock()
        mock_response.status_code = 400
        mock_post.return_value = mock_response

        result = emotion_detector("Some text")

        self.assertIsNotNone(result)
        self.assertIsNone(result['anger'])
        self.assertIsNone(result['disgust'])
        self.assertIsNone(result['fear'])
        self.assertIsNone(result['joy'])
        self.assertIsNone(result['sadness'])
        self.assertIsNone(result['dominant_emotion'])


if __name__ == '__main__':
    unittest.main()
