from unittest import TestCase
from MyString import MyString
class TestMyString(TestCase):
    #this will test if init is working correctly
    def test_getString(self):
        s = MyString("trEeIiOoUuttAa")

        self.assertEquals("trEeIiOoUuttAa",s.getString())

     #using a combination of upper and lowercase to check for vowels
    def test_getVowels(self):
        s=MyString("AaYoueiP")
        self.assertEquals("Aaouei",s.getVowels())

     # Using a number in the string
    def test_getVowels2(self):
        s = MyString("AaYouei5P")
        self.assertEquals("Aaouei", s.getVowels())
     # testing the substring function
    def test_getSubstring(self):
        s = MyString("Apple")
        self.assertEquals("ple",s.getSubstring(3,5))

     # we will raise an exception of the index is out of bounds
    def test_getSubstring2(self):
            s = MyString("Apple")
            self.assertEquals("Index out of bounds", s.getSubstring(11,25))