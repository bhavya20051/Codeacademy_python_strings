def letter_check(word,letter):
  counter=0
  for i in word:
    if i==letter:
      counter=counter+1
  if counter==0:
    return False
  else:
    return True