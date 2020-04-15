# [ ] print long_word from the location of the first and second "t"
long_word = "juxtaposition"
location = long_word.find("t")
second_location = long_word.find("t",location + 1)
print(long_word[location:second_location+1])
print(type(location))
