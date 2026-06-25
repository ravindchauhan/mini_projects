paragraph=str(input("Enter the paragraph : "))
# count word
cleanpara=paragraph.replace("?","").replace(".","").replace(",","").replace("(","").replace(")","").replace("'","").replace("'","")
newpara=cleanpara.split()
length=len(newpara)
print("Total words: ",length)
word=list(newpara)
# longest word
wordlength=""
for word in newpara:
  if len(wordlength)<len(word):
    wordlength=word
    longest=word
print("Longest word is: ",longest)
# vowels
vowels="aeiou"
vow=str(newpara).lower().replace(" ","")
vowelcounter=0
for char in vow:
  if char in char in vowels:
    vowelcounter+=1
print("Total vowels: ",vowelcounter)
characters=len(cleanpara.replace(" ",""))
print("Total characters: ",characters)
