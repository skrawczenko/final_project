from EmotionDetection.emotion_detection import emotion_detector
import unittest
class TestEmotionDetectorunittest.TestCase): 
    def test_emotion_detector(self):
      result_1 = emotion_detector('I am glad this happened')
      print(result_1)
      self.assertEqual(result_1['label'], 'SENT_POSITIVE') # 
unittest.main()

