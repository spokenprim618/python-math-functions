from pyscript import document

def arit(event):
  input1 = document.querySelector("#arithmetic1")
  input2 = document.querySelector("#arithmetic2")
  input3 = document.querySelector("#arithmetic3")

  n1 = input1.value
  n2 = input2.value
  nthTerm = input3.value

  n1 = float(n1)
  n2 = float(n2)
  nthTerm = float(nthTerm)

  output_div = document.querySelector("#output-arit")
  d=n2-n1
  ans=n1+(nthTerm-1)*d
  output_div.innerText = "The difference is {}".format(ans)
  
