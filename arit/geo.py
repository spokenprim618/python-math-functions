from pyscript import document
def geo(event):
  input1 = document.querySelector("#geo1")
  input2 = document.querySelector("#geo2")
  input3 = document.querySelector("#geo3")

  n1 = input1.value
  n2 = input2.value
  nthTerm = input3.value

  n1 = float(n1)
  n2 = float(n2)
  nthTerm = float(nthTerm)

  output_div = document.querySelector("#output-geo")
  d=n2/n1
  first=n1*(d)**(nthTerm-1)
  ans=round(first,3)
  output_div.innerText = "The difference is {}".format(ans)