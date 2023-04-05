#print("11\t홍길동\n14\t일지매")

#name=str(input("당신의 이름은?"))
#print("----------\n성:\t",name[0],"\n이름:\t",name[1:],"\n----------")

#a=int(input("첫번째 정수는?"))
#b=int(input("두번쨰 정수는?"))
#c=(a+b)/2
#print(f"{a}와 {b}의 평균은 {c}")

#def introduce():
  #name=str(input("이름?"))
  #grade=int(input("학년?"))
  #a=print(f'{name[1:]}은 내년에 {grade+1}학년입니다')
  #return a
#introduce()


#def rep_char(c,n):
  #print(c*n)
#rep_char('-',5)


#def rep_char(c,n):
  #print(c*n*2)
#c=str(input())
#def draw_line_string(c):
  #l=len(c)
  #rep_char('-',l)
  #print(c)
  #rep_char('-',l)
#draw_line_string(c)

name=str(input("Input his/her name:"))
def rep_char(c,n):
  print(c*n)
def draw_line_string():
  msg1=f'Hello {name},'
  msg2=f'Welcome to Seoul'
  nstr = len(msg1) if (len(msg1) > len(msg2)) else len(msg2)
  rep_char('-',nstr)
  print(msg1)
  print(msg2)
  rep_char('-',nstr)
draw_line_string()