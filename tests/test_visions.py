import jojen
import unittest
import os

class VisionTest(unittest.TestCase):
  def test_see(self):
    os.environ["FOO"] = "bar"
    self.assertEquals(jojen.see("FOO"), "bar")
    self.assertRaises(Exception, jojen.see, ("BAZ",))

  def test_see_number(self):
    os.environ["FOO"] = "3"
    os.environ["BAR"] = "bar"
    self.assertEquals(jojen.see_number("FOO"), 3)
    self.assertRaises(Exception, jojen.see_number, ("BAR",))


  def test_see_boolean(self):
    os.environ["FOO"] = "False"
    os.environ["BAR"] = "bar"
    self.assertEquals(jojen.see_boolean("FOO"), False)
    self.assertRaises(Exception, jojen.see_boolean, ("BAR",))

  def test_see_sequence(self):
    os.environ["FOO"] = "a,b,c"
    self.assertEquals(jojen.see_sequence("FOO"), ("a", "b", "c"))

  def test_see_interpretation(self):
    os.environ["FOO"] = "1.1"
    os.environ["BAR"] = "bar"
    self.assertEquals(jojen.see_interpretation("FOO", float), 1.1)
    self.assertRaises(Exception, jojen.see_interpretation, ("BAR", float))

  def test_tell(self):
    os.environ["FOO"] = "bar"
    foo = jojen.tell("FOO")
    self.assertEquals(foo(), "bar")
