import unittest
from EmotionDetection import emotion_detector

class TestEmotionDetection(unittest.TestCase):
    def test_joy(self):
        output = emotion_detector("I am glad this happened")
        self.assertEqual(output['dominant_emotion'], 'joy')

    def test_anger(self):
        output = emotion_detector("I am really mad about this")
        self.assertEqual(output['dominant_emotion'], 'anger')

    def test_disgust(self):
        output = emotion_detector("I feel disgusted just hearing about this")
        self.assertEqual(output['dominant_emotion'], 'disgust')

    def test_sadness(self):
        output = emotion_detector("I am so sad about this")
        self.assertEqual(output['dominant_emotion'], 'sadness')

    def test_fear(self):
        output = emotion_detector("I am really afraid that this will happen")
        self.assertEqual(output['dominant_emotion'], 'fear')

if __name__ == '__main__':
    unittest.main()
