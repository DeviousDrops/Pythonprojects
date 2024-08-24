from data import question_data
from question_model import Question
from quiz_brain import Qbrain
p=[]
for i in question_data:
    p.append(Question(i['text'],i['answer']))
c=0
qq=Qbrain(p)
while qq.stillhasqns():
    qq.check(qq.nextqn())