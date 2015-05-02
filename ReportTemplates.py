#!/usr/bin/python3
import sys


def reporting():
    """Begins the script and presents the user with report selections.
       This script is designed to produce templates for Github issues.
    """
    print("Select the type of reporting:")
    print("1. Bug report")
    print("2. Enhancement report")
    try:
        report_type = input("Report type: ")
        assert type(report_type) == str, "You are not using Python 3!"
        if report_type == "1":
            bug_report()
        elif report_type == "2":
            enhancement_template()
        else:
            print("Not a valid selection")
            reporting()
        repeat = input("Would you like to file another report? (Y/n): ")
        if repeat == "Y" or repeat == "y":
            reporting()
        elif repeat == "N" or repeat == "n":
            sys.exit()
    except KeyboardInterrupt:
        print("\nExiting reporting script")
        sys.exit()


def bug_report():
    """Bug report template generator"""
    # Bug typing
    print("\nSelect type of bug: \n")
    print("1) Graphical bug")
    print("2) Security bug")
    print("3) Feature Bug")
    print("4) Server error")
    print("5) Other bug")
    bug_type = input("\nBug type is: ")
    bug_type = bug_type.split(" ")
    bug_is = ""
    for bug in bug_type:
        if bug == "1":
            bug_is += "Graphical bug"
        elif bug == "2":
            bug_is += "Security bug"
        elif bug == "3":
            bug_is += "Feature bug"
        elif bug == "4":
            server_error = input("Server error code is: ")
            bug_is += "Server error " + server_error
        else:
            bug_is += "Other bug"
    expected_output_present = input("Include Expected Output? (Y/n):")
    screenshot_present = input("Include Screenshot? (Y/n):")
    print("=== Template ===\n")
    print("\n \n" + report_typing("Bug", bug_is) + "\n")
    print(description() + "\n")
    print(machine_info())
    print("\n<h4>Steps to recreate:</h4>\n1. \n2. \n3. \n")
    if expected_output_present == "Y" or expected_output_present == "y":
        print("\n<h5>Expected output:</h5> \n ... \n<h5>Actual output:</h5> \n ...")
    print("\n<h4>Additional information:</h4> \n ....\n")
    print(screenshot(screenshot_present))


def enhancement_template():
    """Enhancement report template generator"""
    print("\nSelect the type of enhancement:")
    print("1. User Flow")
    print("2. Graphical")
    print("3. Security")
    print("4. Feature")
    enhancement_type = input("\nEnhancement type is: ")
    if enhancement_type == "1":
        enhancement_is = "User Flow"
    elif enhancement_type == "2":
        enhancement_is = "Graphical"
    elif enhancement_type == "3":
        enhancement_is = "Security"
    elif enhancement_type == "4":
        enhancement_is = "Feature"
    else:
        enhancement_is = "Other"
    screenshot_present = input("Include Screenshot? (Y/n)")
    print("=== Template ===\n")
    print(report_typing("Enhancement", enhancement_is) + "\n\n")
    print(description())
    print(screenshot(screenshot_present))


def description():
    return "<h4>Description</h4> \n ..."


def machine_info():
    device_info = "<h4>Machine Info:</h4>"
    device_info += "\nOS: Ubuntu 14.04.2 LTS"
    device_info += "\nBrowser: Google Chrome (64-bit)"
    return device_info


def screenshot(include):
    if include == "y" or include == "Y":
        return "<h4>Screenshot</h4> \n ..."
    return "\n===End Template==="


def report_typing(bug_or_enhancement, specified_type):
    return "<b>Type: " + specified_type + " " + bug_or_enhancement + "</b>"

reporting()
