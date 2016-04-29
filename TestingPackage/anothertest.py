#from TestingPackage.MyString import MyString


from mystring import MyString
s=MyString("Hi how are you today?")
print(s.getVowels())
print(s.getSubstring(2,4))
print(s.getSubstring("start", "end"))
print(s.getCharlist("self"))
print(s.indexOf("self", 'c'))
print(s.removeChar("self",'c'))
print(s.Invert("self"))





