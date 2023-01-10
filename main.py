# Election eligibility Test
#Created by : Matrika Regmi (Mrt009)

print("Checking your eligibility in upcoming election of Mangsir 4")

print("Select your country of Origin ")
print("1 for Nepal \n2 for other Asian Country  \n3 for South American Country \n4 for North American Country")
print("5 for European Country\n6 for African Country ")
z = int(input())
if 1<= z <=6:
 print()

 Country2 = input("Country Citizenship you have (write the first letter in block to avoid error) : ")
 if Country2 == "Nepal":
  print("wow")
  n1 = input("Please enter your first name :  ")
  n2 = input("Please enter your last name :   ")
  n3 = (n2 + ',')

  gender = input("Choose your gender: \n For female select F \n For male select M \n For custom select T : ")
  DOB = int(input(" When you were born? [in BS] (yyyy) :  "))
  if 140 >= 2079-DOB >= 18:


    c = input(" Enter your citizenship number : ")
    if c == "1111111111":
                 print("Dear", n1, n3, "you are capable to cast the vote in upcoming election. \n Use your rights wisely")
                 print ("and your voter id number : 9387hvgv38")
    elif c == "2222222222":
                 print("Dear", n1, n3, "you are capable to cast the vote in upcoming election. \n Use your rights wisely")
                 print("and your voter id number : 93809hb38")
    elif c == "4444444444":
                 print("Dear",n1,n3, "you are capable to cast the vote in upcoming election. \n Use your rights wisely")
                 print("and your voter id number : 938908768")
    elif c == '5555555555':
                print("Dear",n1,n3,"you are capable to cast the vote in upcoming election. \n Use your rights wisely")
                print("and your voter id number : 93876577838")
    elif c == '6666666666':

                print("Dear",n1,n3,"you are capable to cast the vote in upcoming election. \n Use your rights wisely")
                print("and your voter id number : 9387647838")
    else:
                print("Dear", n1, n3, "you may have filled any information incorrect please try again.")
  elif 2079-DOB >= 140:
        print("error")
  elif 2079-DOB <= 0:
        print("error")
  else:
      print("You are underage to cast vote")
 else:
    print("Sorry you are uneligible to  cast vote")


else:
 print("error")



