import random;
import time;

key = "0x";

bitNum = input("Enter size of key in bites : ");
keys=2**int(bitNum);
print(keys);
for j in range (int(bitNum)):
    i = random.randint(0, 15);
    if(i == 0):
        key+="0"
    else:
       if i == 1:
           key+="1";
       else:
        if i == 2:
         key+="2"
        else:
            if i == 3:
                key+="3"
            else:
                if i == 4:
                 key+="4"
                else:
                    if i == 5:
                     key+="5"
                    else:
                       if i == 6:
                           key+="6"
                       else:
                           if i == 7:
                               key+="7"
                           else:
                               if i == 8:
                                   key+="8"
                               else:
                                   if i == 9:
                                       key+="9"
                                   else:
                                       if i == 10:
                                           key+="A"
                                       else:
                                           if i == 11:
                                               key+="B"
                                           else:
                                               if i == 12:
                                                   key+="C"
                                               else:
                                                   if i == 13:
                                                       key+="D"
                                                   else:
                                                       if i == 14:
                                                           key+="E"
                                                       else:
                                                           if i == 15:
                                                               key+="F"

print ("Your key: ",key);
print ("Haking proces strated");
start_time = time.time()
tempKey = "0x";
isCracked=False;
wrongKey=[];
while isCracked == False:
            for j in range (int(bitNum)):
                i = random.randint(0, 15);
                if(i == 0):
                   tempKey+="0"
                else:
                   if i == 1:
                       tempKey+="1";
                   else:
                    if i == 2:
                     tempKey+="2"
                    else:
                        if i == 3:
                            tempKey+="3"
                        else:
                            if i == 4:
                             tempKey+="4"
                            else:
                                if i == 5:
                                 tempKey+="5"
                                else:
                                   if i == 6:
                                       tempKey+="6"
                                   else:
                                       if i == 7:
                                           tempKey+="7"
                                       else:
                                           if i == 8:
                                              tempKey+="8"
                                           else:
                                               if i == 9:
                                                   tempKey+="9"
                                               else:
                                                   if i == 10:
                                                       tempKey+="A"
                                                   else:
                                                       if i == 11:
                                                           tempKey+="B"
                                                       else:
                                                           if i == 12:
                                                               tempKey+="C"
                                                           else:
                                                               if i == 13:
                                                                   tempKey+="D"
                                                               else:
                                                                   if i == 14:
                                                                       tempKey+="E"
                                                                   else:
                                                                       if i == 15:
                                                                           tempKey+="F"
            if tempKey not in wrongKey:
               if tempKey!=key:
                    wrongKey.append(tempKey);
                    tempKey="0x";
               else : 
                   isCracked=True;
           
print("done")
print("--- %s seconds ---" % (time.time() - start_time))
