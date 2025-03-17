from pyscript import document
import math
# for some reason b is c and c is b


def sides(event):
    input1 = document.querySelector("#side1")
    input2 = document.querySelector("#side2")
    input3 = document.querySelector("#side3")
    input4 = document.querySelector("#angle1")
    input5 = document.querySelector("#angle2")
    input6 = document.querySelector("#angle3")

    a = float(input1.value)
    b = float(input2.value)
    c = float(input3.value)
    A = float(input4.value)
    B = float(input5.value)
    C = float(input6.value)

    sideB = 0
    sideC = 0
    sideA = 0

    if ((b and c and A) != 0):
        sideA = round(math.sqrt((b**2+c**2)+((-2*b*c) *
                                             (math.cos((A * math.pi)/180)))), 1)

    if ((a and c and B) != 0):
        sideB = round(math.sqrt((a**2+c**2)+((-2*a*c) *
                                             (math.cos((B * math.pi)/180)))), 1)

    if ((b and a and C) != 0):
        sideC = round(math.sqrt((b**2+a**2)+((-2*b*a) *
                                             (math.cos((C * math.pi)/180)))), 1)

    output_div = document.querySelector("#output-sides")
    output_div.innerText = "The side a is {}, side b is {}, and side c is {}".format(
        sideA, sideB, sideC)
    return [sideA, sideB, sideC]


def angle(event):

    input1 = document.querySelector("#a1")
    input2 = document.querySelector("#b1")
    input3 = document.querySelector("#c1")
    input1 = float(input1.value)
    input2 = float(input2.value)
    input3 = float(input3.value)
    a1 = input1
    b1 = input2
    c1 = input3

    part1A = b1**2 + c1**2
    part1B = a1**2 + c1**2
    part1C = b1**2 + a1**2

    part2C = -2*(b1 * a1)
    part2A = -2*(b1 * c1)
    part2B = -2*(c1 * a1)

    part3A = a1**2 - part1A
    part3B = b1**2 - part1B
    part3C = c1**2 - part1C

    part4A = part3A / part2A
    part4B = part3B / part2B
    part4C = part3C / part2C

    angleA = round(math.degrees(math.acos(part4A)), 0)
    angleB = round(math.degrees(math.acos(part4B)), 0)
    angleC = round(math.degrees(math.acos(part4C)), 0)
    output_div = document.querySelector("#output-angle")
    output_div.innerText = "The angle for side a is {}, the angle for side b is {}, and the angle for side c is {}".format(
        angleA, angleB, angleC)
