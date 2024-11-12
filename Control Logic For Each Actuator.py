#mv101
def Final_classifier_MV101 (row):
    if row['FIT101'] <= 0.9834096: 
        return 1
    if row['FIT101'] >= 2.334869 and row['LIT101'] <= 800.0301 : 
        return 2
    else:
        return 99

#P101
def Final_classifier_P101 (row):
    if row['LIT301'] >= 999.7637: 
        return 1 
    elif row['FIT201'] <= 2.4174545 and row['LIT301'] >= 796.6106500000001 : 
        return 1
    if row['FIT201'] >= 2.4174545 and row['LIT301'] <= 982.9811500000001 : 
        return 2
    else:
        return 99


#MV201
def Final_classifier_MV201 (row):
    if row['FIT201'] <= 2.3990644999999997 and row['LIT301'] >= 796.2301500000001 : 
        return 1
    if row['FIT201'] >= 2.3990644999999997 and row['FIT301'] >= 0.0003202767 : 
        return 2
    
    else:
        return 99


#P203
def Final_classifier_P203 (row):
    
    if row['FIT201'] <= 2.369269: 
        return 1 
    if row['FIT201'] >= 2.452376: 
        return 2 
    elif row['FIT201'] >= 2.4015630000000003 and row['LIT301'] <= 999.74365 : 
        return 2
    else:
        return 99



#P205
def Final_classifier_P205 (row):
    
    if row['FIT201'] <= 2.0299875: 
        return 1 
    elif row['AIT203'] >= 436.0036 and row['AIT202'] <= 8.426718000000001 and row['LIT301'] <= 977.8942999999999 : 
        return 1
    if row['FIT201'] >= 2.3683725000000004 and row['AIT203'] <= 436.0036 and row['LIT301'] <= 977.8942999999999 : 
        return 2
    
    else:
        return 99



#MV301
def Final_classifier_MV301 (row):
    if row['FIT601'] <= 0.0013135555499999999 and row['FIT301'] >= 0.19978859999999998 : 
        return 1
    elif row['FIT601'] <= 0.0013135555499999999 and row['LIT301'] >= 875.85715 and row['FIT201'] <= 2.4489795 : 
        return 1 
    if row['FIT601'] >= 0.0013135555499999999 and row['FIT301'] <= 0.19978859999999998 and row['LIT301'] <= 875.85715 : 
        return 2
    elif row['FIT601'] >= 0.0013135555499999999 and row['FIT301'] <= 0.19978859999999998 and row['AIT501'] >= 7.859555 : 
        return 2
    else:
        return 99

#MV302
def Final_classifier_MV302 (row):
    
    if row['DPIT301'] <= 12.57283 and row['FIT301'] <= 2.114595 : 
        return 1 
    if row['DPIT301'] <= 12.57283:
        return 1
    if row['DPIT301'] >= 19.281: 
        return 2
    
    else:
        return 99

#MV303
def Final_classifier_MV303 (row):
    
    if row['DPIT301'] >= 3.2172355: 
        return 1
    if row['LIT301'] >= 910.4036 and row['FIT301'] <= 0.00044838734999999997 and row['FIT601'] <= 0.00028834140000000004 : 
        return 1
     
    if row['FIT301'] <= 0.00044838734999999997 and row['FIT601'] >= 0.00028834140000000004 : 
        return 2
    if row['FIT601'] >= 0.00028834140000000004 and row['DPIT301'] <= 2.599398 : 
        return 2 
    if row['DPIT301'] <= 3.2172355 and row['LIT301'] <= 910.4036 : 
        return 2
    else:
        return 99

#MV304
def Final_classifier_MV304 (row):
    if row['DPIT301'] >= 12.948975 and row['LIT401'] >= 909.5360499999999 : 
        return 1
    if row['DPIT301'] >= 12.948975 and row['LIT401'] >= 798.0453500000001 : 
        return 1
    if row['DPIT301'] <= 2.591395 and row['LIT401'] >= 909.5360499999999 : 
        return 1
    if row['LIT401'] >= 798.0453500000001 and row['FIT301'] <= 0.01748711 : 
        return 1
    if row['DPIT301'] <= 12.948975 and row['DPIT301'] >= 2.591395 and row['LIT101'] >= 810.92275 : 
        return 2
    if row['DPIT301'] <= 12.948975 and row['LIT401'] <= 798.0453500000001 and row['FIT301'] >= 0.36389839999999996 : 
        return 2
    if row['DPIT301'] <= 12.948975 and row['FIT301'] >= 0.36389839999999996 and row['FIT502'] <= 1.26124 : 
        return 2
    if row['DPIT301'] >= 2.591395 and row['FIT301'] >= 0.36389839999999996 and row['DPIT301'] <= 3.0555735 : 
        return 2 
    if row['DPIT301'] <= 12.948975 and row['DPIT301'] >= 2.591395 : 
        return 2
    else:
        return 99

#P301
def Final_classifier_P301 (row):
    
    if row['LIT101'] >= 495.91935: 
        return 1
     
    if row['LIT101'] <= 282.36474999999996 and row['FIT301'] >= 2.211511 : 
        return 2
    else:
        return 99

#P302
def Final_classifier_P302 (row):
    
    if row['FIT301'] <= 1.924543 and row['LIT401'] >= 898.5965 : 
        return 1
    if row['AIT201'] <= 264.19505000000004 and row['DPIT301'] <= 3.0219605 : 
        return 1
    if row['FIT101'] >= 2.525382 and row['DPIT301'] <= 3.0219605 : 
        return 1
     
    if row['FIT301'] >= 1.924543 and row['LIT101'] >= 508.97090000000003 and row['LIT401'] <= 863.3362999999999 : 
        return 2
    if row['FIT301'] >= 1.924543 and row['LIT401'] >= 863.3362999999999 and row['LIT401'] <= 898.5965 : 
        return 2
    if row['DPIT301'] >= 19.57392 and row['AIT503'] >= 269.00154999999995 and row['LIT401'] <= 999.2629999999999 : 
        return 2
    if row['FIT301'] >= 1.924543 and row['LIT101'] >= 508.97090000000003 : 
        return 2
    else:
        return 99

#P402 

def Final_classifier_P402 (row):
    
    if row['LIT301'] <= 285.2634: 
        return 1 
    if row['LIT301'] >= 285.2634: 
        return 2 
    else:
        return 99



#UV401 
def Final_classifier_UV401 (row):
    
    if row['AIT201'] <= 252.89995: 
        return 1  
    if row['FIT502'] <= 1.1711925 and row['PIT502'] <= 0.91308105 : 
        return 1
    if row['FIT502'] >= 1.1711925 and row['PIT502'] >= 0.91308105 : 
        return 2
    else:
        return 99
# P501 
def Final_classifier_P501 (row):
    
    if row['AIT201'] <= 252.86790000000002: 
        return 1
    if row['FIT502'] <= 1.185987 and row['PIT502'] <= 0.91308105 : 
        return 1
    if row['FIT502'] >= 1.185987 and row['PIT502'] >= 0.91308105 : 
        return 2
    else:
        return 99



#P602
def Final_classifier_P602 (row):
    
    if row['FIT601'] <= 0.00246692075: 
        return 1
     
    if row['FIT601'] >= 0.00246692075 and row['LIT301'] >= 871.31105 and row['LIT401'] >= 914.47705 : 
        return 2
    if row['FIT601'] >= 0.00246692075 and row['LIT301'] <= 871.31105 and row['FIT301'] <= 0.0039714315 : 
        return 2
    if row['FIT601'] >= 0.00246692075 and row['LIT401'] >= 914.47705 and row['DPIT301'] <= 2.1944425 : 
        return 2
    else:
        return 99


