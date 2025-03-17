from pyscript import document

# Create a linked list instance for arithmetic results
arith_history = LinkedList()


def arit(event):
    """Calculates the nth term of an arithmetic sequence and updates the history."""
    input1 = document.querySelector("#arithmetic1")
    input2 = document.querySelector("#arithmetic2")
    input3 = document.querySelector("#arithmetic3")

    n1 = float(input1.value)
    n2 = float(input2.value)
    nthTerm = float(input3.value)

    d = n2 - n1
    ans = n1 + (nthTerm - 1) * d

    # Update output
    output_div = document.querySelector("#output-arit")
    output_div.innerText = f"The difference is {ans}"

    # Store result in linked list
    arith_history.append(ans)

    # Update UI with stored results
    update_result_list()


def update_result_list():
    """Updates the HTML unordered list with stored arithmetic results."""
    result_list = document.querySelector("#result-list-arit")
    result_list.innerHTML = ""  # Clear the list

    # Retrieve all results from the linked list
    results = arith_history.get_all()
    for index, result in enumerate(results, start=1):
        li = document.createElement("li")
        li.innerText = f"{index}. Result: {result} "

        # Create a delete button for each result
        btn = document.createElement("button")
        btn.innerText = "Delete"
        # Store the current position in a data attribute
        btn.setAttribute("data-index", str(index))
        btn.addEventListener("click", delete_result)

        li.appendChild(btn)
        result_list.appendChild(li)


def delete_result(event):
    """Deletes a result from the linked list based on its position."""
    # Retrieve the position from the button's data attribute
    index = int(event.target.getAttribute("data-index"))
    arith_history.delete(index)
    update_result_list()
