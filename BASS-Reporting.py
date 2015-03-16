def reporting():
    """Begins the script and presents the user with report selections.
       This script is designed to produce templates for Github issues.
    """"
    print("Select the type of reporting:")
    print("1. Bug report")
    print("2. Enhancement report")
    type = input("Report type: ")
    if type == "1":
        return bug_report()
    elif type == "2":
        return enhancement_template()
    else:
        print("Not a valid selection")
        reporting()

def bug_report():
    """Bug report template generator"""
    print("\nSelect type of bug: \n")
    print("1. Graphical bug")
    print("2. Security bug")
    print("3. Other bug")
    type = input("Bug type is: ")
    if type == "1":
        bug_type = "Graphical"
    elif type == "2":
        bug_type = "Security"
    else:
        bug_type = "Other"
    screenshot_present
    print("\n \n<h5>Type: " + bug_type + " bug" + "</h5> \n")
    print("<h4>Machine Info:</h4> \nOS: Ubuntu 14.04.2 LTS \nBrowser: Google Chrome (64-bit)")
    print("<h5>Expected output:</h5> \n ... \n<h5>Actual output:</h5> \n ...")
    print("Steps to recreate:\n1. \n2. \n3.")
    print("<h4>Additional information:</h4> \n ....")
    print("<h4>Screenshots:</h4> \n ...")

def enhancement_template():
    """Enhancement report template generator"""
    print("\nSelect the type of enhancement:")
    print("1. User Flow")
    print("2. Graphical")
    print("3. Security")
    type = input("Enhancement type is: ")
    if type == "1":
        enhancement_type = "User Flow"
    elif type == "2":
        enhancement_type = "Graphical"
    elif type == "3":
        enhancement_type = "Security"
    else:
        enhancement_type = "Other"
    print("\n \n<b>Type: " + enhancement_type + " Enhancement</b>\n")
    print("<h4>Description</h4> \n ...")
    print("<h4>Screenshot</h4> \n ...")

reporting()
