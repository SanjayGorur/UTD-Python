# {"first":{"f1":1, "f2":2}, "second":{"s2":2, "s3":3 , "second1":{"ss1":1,"ss2":2}},"third":3}

# "first"
#   "f1":1
#   "f2":2
# "second"
#   "s2":2
#   "s3":3
#   "second1"
#     "ss1":1
#     "ss2":2
# "third": 3

d = {"first":{"f1":1, "f2":2}, "second":{"s2":2, "s3":3 , "second1":{"ss1":1,"ss2":2}},"third":3}

check = "   "
count = 0

def go(d):
  count = 0
  for key in d:
    if(type(d.get(key)) == dict):
      print(key)
      for k in d.get(key):
        print(check * count, repeat(d.get(key), k))
    else:
      print(str(key) + ":" + str(d.get(key)))

def repeat(di, ke):
    subs = count
    if(type(di.get(ke)) == dict):
      subs += 1
      print(check * count, ke)
      return(loop(di.get(ke)))
    coord = str(ke) + ":" + str(di.get(ke))
    return coord

def loop(dicti):
    for k in dicti:
      print((check) + str(k) + ":" + str(dicti[k]))
    return ""


go(d)

    

