answer=['철수','시은','진원','유리','불필요','불필요','불필요','불필요']
output=['철수','불필요','유리','불필요','불필요','불필요','훈이','불필요']

def accuracy(answer,output):

    accnum=0
    for i in range(0,len(answer)):
        if answer[i] == output[i]:
            accnum=accnum+1

    print('Accuracy = ', (accnum/len(answer)))

'''
#Precision
(예측 중 정답 개수) / (전체 예측 개수 불필요 제외)
'''

def precision(answer,output):

    predictnum=0
    for i in range(0,len(answer)):
        if output[i]!='불필요':
            predictnum=predictnum+1

    corrnum=0
    for i in range(0,len(answer)):
        if answer[i] == output[i] and output[i]!='불필요':
            corrnum=corrnum+1

    result=corrnum/predictnum
    print('Precision = ', result)
    return result

'''
#Recall
(예측 중 정답 개수) / (복원이 필요한 sample 개수)
'''

def recall(answer,output):

    corrnum=0
    for i in range(0,len(answer)):
        if answer[i] == output[i] and output[i]!='불필요':
            corrnum=corrnum+1
            i=i+1

    needrest=0 #복원이 필요한 sample 개수
    for i in range(0,len(answer)):
        if answer[i]!='불필요':
            needrest=needrest+1
            i=i+1
    
    result=corrnum/needrest
    print('Recall = ', result)
    return result


accuracy(answer,output)
pre=precision(answer,output)
rec=recall(answer,output)

# def f1(pre=precision, rec=recall):
#     print('F1 = ', (2*pre*rec)/(pre+rec)))

print('F1 = ', (2*pre*rec)/(pre+rec))