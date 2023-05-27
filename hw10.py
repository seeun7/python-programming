import pickle
import os
filename='score.bin'
scores=[]
def input_scores():
    print('[점수 입력]')
    score=0
    i=1
    total=0
    while score>=0:
        score=int(input(f'#{i}? '))
        if score<0:
            break
        scores.append(score)
        total+=scores[i-1]
        i+=1
    return total
def get_average(t): #평균
    average=t/len(scores)
    return average
def save_data(scores,avr): #저장
    with open(filename,'wb') as file:
        sc=pickle.dump(scores,file)
        av=pickle.dump(avr,file)
    return sc,av
#주 프로그램부
if not os.path.exists(filename):
    avr=get_average(input_scores())
    print('[점수 출력]')
    print(f'개인점수:{scores}')
    print(f'평균:{avr}')
    save_data(scores,avr)
else:
    print('[파일 읽기]')
    with open(filename,'rb') as file:
        s=pickle.load(file)
        a=pickle.load(file)
    print('[점수 출력]')
    print(f'개인 점수:{s}')
    print(f'평균:{a}')