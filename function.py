def function(parameter):
    print("Hello, " + parameter + ". Good morning!")

function('Tanu')
########
def traingle_area(base,hight):
    area=base*hight

    print("The area of triangle is:"+str(area))

traingle_area(5,7)

##############
def traingle_area(base, hight):
    return base * hight

area_a=traingle_area(5,7)
area_b=traingle_area(7,9)
sum=area_a + area_b
print("Sum of the area of triangle is:" + str(sum))
print("Te area of triangle area_a is:" + str(area_a))
print("Te area of triangle area_b is:" + str(area_b))

#######

def convert_secand(sec):
    hour= sec // 3600
    min= (sec - hour * 3600) //60
    sec= sec - hour * 3600 - min * 60

    return hour,min,sec
hour,min,sec=convert_secand(5000)
print(hour,min,sec)



def convert_distance(miles):
    return miles * 1.6

my_trip_miles = 55

# 2) Convert my_trip_miles to kilometers by calling the function above

my_trip_km = convert_distance(my_trip_miles)

# 3) Fill in the blank to print the result of the conversion

print("The distance in kilometers is " + str(my_trip_km))


# 4) Calculate the round-trip in kilometers by doubling the result, and fill in the blank to print the result

print("The round-trip in kilometers is " + str(my_trip_km * 2))

#########
def lucky_num(name):
    number= len(name)*10

    print("Hi "+name+" your lucky number is "+str(number))

lucky_num("Tanu")
lucky_num("test")



# REPLACE THIS STARTER CODE WITH YOUR FUNCTION
# REPLACE THIS STARTER CODE WITH YOUR FUNCTION
def month_days(month,days):
  june_days = 30
  july_days = 31

  print("June has " + str(june_days) + " days.")
  print("July has " + str(july_days) + " days.")
month_days(30,31)




print(1> int("2"))

# def lucky_num(name):
#     number= len(name)*9
#
#     result  = "Hi "+name+" your lucky number is "+str(number)
#     result
#
# lucky_num("Kay")
# lucky_num("Cameron")

def hint_username(username):
    if len(username) < 3:
        print("Invalid Username. Must be at 3 character long")
    elif len(username)  >15:
        print("Invalid Username. Must be at15 character long")

    else:
        print("valid user name")

##########

def is_positive(number):
  if number > 0:
    return True
  else:
    return False
##########
  def is_even(number):
      if number %2==0:
          return True
      return False
#########
def number_group(number):
  if number > 0:
    return "Positive"
  elif number < 0:
    return "Negative"
  else :
    return  "Zero"

print(number_group(10)) #Should be Positive
print(number_group(0)) #Should be Zero
print(number_group(-5)) #Should be Negative

print(9999+8888 )

print(100*100)

18,887
10,000

def square(n):
    n=sum

    return n*n

def sum_squares(x):

    sum = 0
    for n in range(x):
        print("output"+str(n))
        sum += x
    return sum

print(sum_squares(10)) # Should be 28

def double_word(word):
    result=word*2
    return result + str(len(result))


print(double_word("hello"))  # Should return hellohello10
print(double_word("abc"))  # Should return abcabc6
print(double_word(""))  # Should return