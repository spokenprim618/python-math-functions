from pyscript import document


def percentError(event):
    input1 = document.querySelector("#percent1")
    input2 = document.querySelector("#percent2")

    experimental = input1.value
    actual = input2.value
    experimental = float(experimental)
    actual = float(actual)
    output_div = document.querySelector("#output-percent")
    answer = round(((abs(experimental - actual))/actual)*100, 1)
    output_div.innerText = "The difference is {} percent".format(answer)
