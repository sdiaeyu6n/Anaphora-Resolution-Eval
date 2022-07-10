answer=['철수','시은','진원','유리','불필요','불필요','불필요','불필요']
output=['철수','불필요','유리','불필요','불필요','불필요','훈이','불필요']

'''
categorization 함수: TP, FP, TN, FN 개수 계산

True Positive = 복원이 필요하고 output이 맞음
False Positive = 복원이 불필요하고 output이 틀림 (output이 불필요가 아님)
True Negative = 복원이 불필요하고 output이 맞음 (=output이 불필요)
False Negative = 복원이 필요하고 output이 틀림
'''
def categorization(answer,output): 
    true_positive=0
    for i in range(0,len(answer)):
        if answer[i]!='불필요' and answer[i] == output[i]:
            true_positive=true_positive+1
    
    false_positive=0
    for i in range(0,len(answer)):
        if answer[i] == '불필요' and output[i] != '불필요':
            false_positive=false_positive+1
    
    true_negative=0
    for i in range(0,len(answer)):
        if answer[i] == '불필요' and output[i] == '불필요':
            true_negative=true_negative+1    

    false_negative=0
    for i in range(0,len(answer)):
        if answer[i]!='불필요' and answer[i] != output[i]:
            false_negative=false_negative+1

    return true_positive, false_positive, true_negative, false_negative

'''
Accuracy = 
(복원이 필요하고 output이 맞는 경우)+(복원이 불필요하고 output이 맞음)
/ (복원이 필요하고 output이 맞는 경우) + (복원이 필요하고 output이 틀림) + (복원이 불필요하고 output이 틀림) + (복원이 불필요하고 output이 맞음)
'''
def accuracy(tp, fp, tn, fn):
    result=(tp+tn)/(tp+fn+fp+tn)
    
    return result

'''
Precision = 
(복원이 필요하고 output이 맞는 경우)
/ (복원이 필요하고 output이 맞는 경우) + (복원이 불필요하고 output이 틀림)
'''
def precision(tp,fp):
    result=(tp)/(tp+fp)
 
    return result

'''
Recall = 
(복원이 필요하고 output이 맞는 경우)
/ (복원이 필요하고 output이 맞는 경우) + (복원이 필요하고 output이 틀림)
'''
def recall(tp,fn):
    result=(tp)/(tp+fn)
  
    return result

def f1(tp, fp, fn):
    pre=precision(tp,fp)
    rec=recall(tp,fn)

    result=(2*pre*rec)/(pre+rec)
    return result

result = categorization(answer,output)
true_positive, false_positive, true_negative, false_negative = result

print('Accuracy = ', accuracy(true_positive, false_positive, true_negative, false_negative))
print('Precision = ', precision(true_positive, false_positive))
print('Recall = ', recall(true_positive, false_negative))
print('F1 = ', f1(true_positive, false_positive, false_negative))
