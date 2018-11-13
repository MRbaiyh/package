# -*- coding: utf-8 -*-
"""
Created on Mon Oct 15 20:30:12 2018

@author: zmddzf
"""
import re

def splitArea(code):
    
    codeList = code.split('\n')
    spaceList = []
    
    for i in range(len(codeList)):
        
        countSpace = 0
        if ':' in codeList[i]:
            codeList[i] = codeList[i].replace(':', '{')
        else:
            codeList[i] += ';'
            
        for j in codeList[i]:
            if j == ' ':
                countSpace += 1
            else:
                break
        spaceList.append(countSpace)
        
    
    for i in range(len(spaceList)):
        if '{' in codeList[i]:
            for j in range(i+1, len(spaceList)):
                if spaceList[j] <= spaceList[i]:
                    codeList[j - 1] += '}'
                    break
            if j == len(codeList) - 1:
                codeList[len(codeList) - 1] += '}'    
    
    splitString = '\n'.join(codeList)
    return splitString

def changeKwd(code):
    pattern = ['for (.+?){', ' (.*?) = ', 'if(.*?){']
    code = code.replace('True', 'true')
    code = code.replace('print', 'System.out.print')
    x1 = re.findall(pattern[0], code)
    x2 = re.findall(pattern[1], code)
    x3 = re.findall(pattern[2], code)
    for i in x1:
        s1 = '(int '+i[0] + '=' + re.findall("[(] (.+?) [)]", i)[0].replace(' ', '').split(',')[0] + ';'
        s2 = s1 + i[0] + '<' + re.findall("[(] (.+?) [)]", i)[0].replace(' ', '').split(',')[1] + ';' + i[0] + '++)'
        code = code.replace(i, s2)
    
    s1 = 'boolean' + x2[0]
    code = code.replace(x2[0], s1, 1)
    
    for i in x3:
        s1 = '(' + i + ')'
        code = code.replace(i, s1)
    
    code = code.replace(", end = '' ", '')
    code = code.replace('"%d   "', '"%d   ",')
    code = 'public class Hk2_5 {\n    public static void main(String args[]) {\n    ' + code + '}}'
    
    return code


        
with open('hk2_5.txt') as f:
    s = f.read()

print(changeKwd(splitArea(s)))   




