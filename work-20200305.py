import numpy as np
import pandas as pd
import matplotlib
matplotlib.use('Agg')
import matplotlib.pyplot as plt
from sklearn.svm import OneClassSVM
import warnings


clf = OneClassSVM(kernel="rbf", gamma='auto')


## データの読み込み ##
filename = 'left_hip.csv'
left_hip_df = pd.read_csv(filename, usecols=['recipe', 'label', 'mean_X', 'mean_Y', 'mean_Z', 'var_X', 'var_Y', 'var_Z'], encoding='Shift-JIS').dropna()
left_hip_df = left_hip_df[left_hip_df['label'] == 'Take']
left_hip = left_hip_df.values[:, 2:8]
left_hip_label = left_hip_df.values[:, 1:2]


filename = 'right_arm.csv'
right_arm_df = pd.read_csv(filename, usecols=['recipe', 'label', 'mean_X', 'mean_Y', 'mean_Z', 'var_X', 'var_Y', 'var_Z'], encoding='Shift-JIS').dropna()
right_arm_df = right_arm_df[right_arm_df['label'] == 'Take']
right_arm = right_arm_df.values[:, 2:8]
right_arm_label = right_arm_df.values[:, 1:2]

filename = 'left_wrist.csv'
left_wrist_df = pd.read_csv(filename, usecols=['recipe', 'label', 'mean_X', 'mean_Y', 'mean_Z', 'var_X', 'var_Y', 'var_Z'], encoding='Shift-JIS').dropna()
left_wrist_df = left_wrist_df[left_wrist_df['label'] == 'Take']
left_wrist = left_wrist_df.values[:, 2:8]
left_wrist_label = left_wrist_df.values[:, 1:2]

filename = 'right_wrist.csv'
right_wrist_df = pd.read_csv(filename, usecols=['recipe', 'label', 'mean_X', 'mean_Y', 'mean_Z', 'var_X', 'var_Y', 'var_Z'], encoding='Shift-JIS').dropna()
right_wrist_df = right_wrist_df[right_wrist_df['label'] == 'Take']
right_wrist = right_wrist_df.values[:, 2:8]
right_wrist_label = right_wrist_df.values[:, 1:2]



left_hip_train = left_hip
right_arm_train = right_arm
left_wrist_train = left_wrist
right_wrist_train = right_wrist



wash_take = ['subject2_file_679', 'subject2_file_52', 'subject2_file_485', 'subject2_file_263', 'subject2_file_792', 'subject2_file_635', 'subject3_file_537', 'subject3_file_901', 'subject3_file_389', 'subject3_file_829', 'subject1_file_780', 'subject1_file_319']

with warnings.catch_warnings():
    warnings.filterwarnings("error")
    
    print('\n---left_hip---\n')
    for file in wash_take:
        try:
            data = np.loadtxt('./train/left_hip/'+file+'.csv', delimiter=',', skiprows=1)
            temp = []
            left_hip_test = []
            start = data[0][3]
            for row in data:
                if row[3]-start > 5000:
                    #書き込み
                    left_hip_test.append(list(np.concatenate([np.mean(np.array(temp)[:, :3], axis=0), np.var(np.array(temp)[:, :3], axis=0)])))
                    
                    # スライドするので先頭を削除
                    del temp[0]
                    start = temp[0][3]
                temp.append(row[0:4])
        except IOError:
            continue
        except UserWarning: 
            continue
      
        # OneClassSVM
        clf.fit(left_hip_train)
        pred = clf.predict(left_hip_test)
        plt.figure()
        plt.plot(range(len(pred)), list(pred))
        plt.savefig('./figures/left_hip/'+file+'.png', bbox_inches='tight', pad_inches=0)
        plt.close()
    print('OK\n------------')
    
    print('\n---right_arm---\n')
    for file in wash_take:
        try:
            data = np.loadtxt('./train/right_arm/'+file+'.csv', delimiter=',', skiprows=1)
            temp = []
            right_arm_test = []
            start = data[0][3]
            for row in data:
                if row[3]-start > 5000:
                    #書き込み
                    right_arm_test.append(list(np.concatenate([np.mean(np.array(temp)[:, :3], axis=0), np.var(np.array(temp)[:, :3], axis=0)])))
                    
                    # スライドするので先頭を削除
                    del temp[0]
                    start = temp[0][3]
                temp.append(row[0:4])
        except IOError:
            continue
        except UserWarning: 
            continue
      
        # OneClassSVM
        clf.fit(right_arm_train)
        pred = clf.predict(right_arm_test)
        plt.figure()
        plt.plot(range(len(pred)), list(pred))
        plt.savefig('./figures/right_arm/'+file+'.png', bbox_inches='tight', pad_inches=0)
        plt.close()
    print('OK\n------------')
    
    print('\n---left_wrist---\n')
    for file in wash_take:
        try:
            data = np.loadtxt('./train/left_wrist/'+file+'.csv', delimiter=',', skiprows=1)
            temp = []
            left_wrist_test = []
            start = data[0][3]
            for row in data:
                if row[3]-start > 5000:
                    #書き込み
                    left_wrist_test.append(list(np.concatenate([np.mean(np.array(temp)[:, :3], axis=0), np.var(np.array(temp)[:, :3], axis=0)])))
                    
                    # スライドするので先頭を削除
                    del temp[0]
                    start = temp[0][3]
                temp.append(row[0:4])
        except IOError:
            continue
        except UserWarning: 
            continue
      
        # OneClassSVM
        clf.fit(left_wrist_train)
        pred = clf.predict(left_wrist_test)
        plt.figure()
        plt.plot(range(len(pred)), list(pred))
        plt.savefig('./figures/left_wrist/'+file+'.png', bbox_inches='tight', pad_inches=0)
        plt.close()
    print('OK\n------------')
    
    print('\n---right_wrist---\n')
    for file in wash_take:
        try:
            data = np.loadtxt('./train/right_wrist/'+file+'.csv', delimiter=',', skiprows=1)
            temp = []
            right_wrist_test = []
            start = data[0][3]
            for row in data:
                if row[3]-start > 5000:
                    #書き込み
                    right_wrist_test.append(list(np.concatenate([np.mean(np.array(temp)[:, :3], axis=0), np.var(np.array(temp)[:, :3], axis=0)])))
                    
                    # スライドするので先頭を削除
                    del temp[0]
                    start = temp[0][3]
                temp.append(row[0:4])
        except IOError:
            continue
        except UserWarning: 
            continue
      
        # OneClassSVM
        clf.fit(right_wrist_train)
        pred = clf.predict(right_wrist_test)
        plt.figure()
        plt.plot(range(len(pred)), list(pred))
        plt.savefig('./figures/right_wrist/'+file+'.png', bbox_inches='tight', pad_inches=0)
        plt.close()
    print('OK\n------------')
