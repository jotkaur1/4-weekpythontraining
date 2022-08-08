strg="computerscience"
print("the length of a string is:", len(strg))


######################################################################
print()
print("enter a string:")
s=input()
all_freq={}
for i in s:
    if i in all_freq:
        all_freq[i]+=1
    else:
        all_freq[i]=1
print("count of all characters in " ,s, ":",str(all_freq))
print()


#######################################################################
print("enter a string:")
s1=input()
length=len(s1)
if (length >2):
   print((s1[0:2])+s1[-2:])
else:
    print("empty string")
print()

##########################################################################
def remove_char(str, n):
      first_part = str[:n] 
      last_part = str[n+1:]
      return first_part + last_part
print(remove_char('Python', 0))
print(remove_char('Python', 3))
print(remove_char('Python', 5))

########################################################################

def find_longest_word(words_list):
    word_len = []
    for n in words_list:
        word_len.append((len(n), n))
    word_len.sort()
    return word_len[-1][0], word_len[-1][1]
result = find_longest_word(["PHP", "Exercises", "Backend"])
print("\nLongest word: ",result[1])
print("Length of the longest word: ",result[0])
#######################################################################
def not_poor(str1):
  snot = str1.find('not')
  spoor = str1.find('poor')
  

  if spoor > snot and snot>0 and spoor>0:
    str1 = str1.replace(str1[snot:(spoor+4)], 'good')
    return str1
  else:
    return str1
print(not_poor('The lyrics is not that poor!'))
print(not_poor('The lyrics is poor!'))


##############################################################################

def chars_mix_up(a, b):
  new_a = b[:2] + a[2:]
  new_b = a[:2] + b[2:]

  return new_a + ' ' + new_b
print(chars_mix_up('abc', 'xyz'))

