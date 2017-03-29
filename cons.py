class token:
  sttable={"x":"5"}
  
  def __init__(self,typ,value):
    self.type=typ
    self.value=value
  
  def __str__(self):
    
    return '{typ},{value}'.format(typ=self.type,value=self.value)
    
  
class consexp:
  def eval(self,st):
    if(st.isalnum()):
      return int(st)
    else:
      return float(st)

class varexp(token):
  
  def eval(self,st):
    return self.sttable[st] 
    

cons=consexp()
var=varexp('INT','556.5')
st=var.value

print(cons.eval(st)+1)

print(var.eval("x"))


