import unittest
import deviation_db

class deviation_DeviationComment(unittest.TestCase):
    def test_comment(self):
        test_comment = "		/* DR#MISRA C:2012#Rule 10.6#A1#필요한 내용을 적습니다. */   "

        c = deviation_db.DeviationComment(test_comment)

        self.assertEqual("MISRA C:2012", c.getStandard())
        self.assertEqual("Rule 10.6", c.getRuleID())
        self.assertEqual("A1", c.getDeviationID())

if __name__ == "__main__":
    unittest.main()