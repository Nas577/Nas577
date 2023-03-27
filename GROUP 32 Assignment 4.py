# -*- coding: utf-8 -*-
"""
Created on Thu Mar 23 11:41:41 2023

@author: Abubakar Anas
"""

'''// Problem Statement
// -------------------------------------------------------
// Program to compute and display the number of trails and passes as well as the minimum, maximum and average marks/scores of the trail/pass list of a class in a course(say MATH 279)
//
// **********Test Data***********
// Number of Students: 10
// Examination Scores: 67,34,58,77,82,30,46,61,29,70 '''

print("Enter the number of students")
nStds = int(input())
passMark = 40
nPass = 0
nTrail = 0
sumTrail = 0
sumPass = 0
initTrail = False
initPass = False
for k in range(1, nStds + 1, 1):
    print("Enter your Score")
    stdMark = float(input())
    if stdMark >= passMark:
        nPass = nPass + 1
        sumPass = sumPass + stdMark
        if initPass == False:
            minPass = stdMark
            maxPass = stdMark
            initPass = True
        else:
            if stdMark >= maxPass:
                maxPass = stdMark
            if stdMark <= minPass:
                minPass = stdMark
    else:
        nTrail = nTrail + 1
        sumTrail = sumTrail + stdMark
        if initTrail == True:
            if stdMark >= maxTrail:
                maxTrail = stdMark
            if stdMark <= minTrail:
                minTrail = stdMark
        else:
            minTrail = stdMark
            maxTrail = stdMark
            initTrail = True
if nPass != 0 and nTrail != 0:
    meanPass = sumPass / nPass
    meanTrail = sumTrail / nTrail
    print("\nClass Size: " + str(nStds) + chr(13) + \
          "\nNumber of Passes: " + str(nPass) + chr(13) + \
          "\nNumber of Trails: " + str(nTrail) + chr(13) + \
          "\nMin/Max Trails: " + str(minTrail) + "/" + str(maxTrail) + chr(13) + \
          "\nMin/Max Pass: " + str(minPass) + "/" + str(maxPass) + chr(13) + \
          "\nMean Pass Mark: " + str(meanPass) + chr(13) + \
          "\nMean Trail Mark: " + str(meanTrail))
else:
    if nPass != 0:
        meanPass = sumPass / nPass
        print("\nClass Size: " + str(nStds) + chr(13) + \
              "\nNumber of Passes: " + str(nPass) + chr(13) + \
              "\nNumber of Trails: " + str(nTrail) + chr(13) + \
              "\nMin/Max Trails: " + "Not Applicable." + chr(13) + \
              "\nMin/Max Pass: " + str(minPass) + "/" + str(maxPass) + chr(13) + \
              "\nMean Pass Mark: " + str(meanPass) + chr(13) + \
              "\nMean Trail Mark: " + "Not Applicable")
    else:
        meanTrail = sumTrail / nTrail
        print("\nClass Size: " + str(nStds) + chr(13) + \
              "\nNumber of Passes: " + str(nPass) + chr(13) + \
              "\nNumber of Trails: " + str(nTrail) + chr(13) + \
              "\nMIn/Max Trails: " + str(minTrail) + "/" + str(maxTrail) + chr(13) + \
              "\nMIn/Max Pass: " + "Not Applicable" + chr(13) + \
              "\nMean Pass Mark: " + "Not Applicable" + chr(13) + \
              "\nMean Trail Mark: " + str(meanTrail))




'''

GROUP 32 MEMBERS
1. ANOKYE ERNEST - 8598821
2. DOWOUNA NII NOI BENJAMIN - 8602721
3. OFOSU YEBOAH PRINCE - 8607321
4. ABUBAKAR ANAS - 8596221
'''
