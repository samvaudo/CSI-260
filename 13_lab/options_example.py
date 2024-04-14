from options import Options
from pprint import pprint

# Modify this to only include the steps you have written so far
# It will include simplified examples that use features of each step
steps_to_run = [1, 2, 3, 4, 5, 6]


if 1 in steps_to_run:
    print('Step 1\n')
    try:
        print("Setting only with argument list")
        options = Options("debug", "verbose")
        pprint(options)

        print("Setting only with keywords")
        options = Options(log_file="logging.txt", port=80)
        pprint(options)

        print("Setting with arguments and keywords")
        options = Options("debug", "verbose", log_file="logging.txt", port=80)
        pprint(options)
    except Exception as e:
        print('Error initializing with valid arguments during Step 1')
        print('Error was:', e)

    try:
        print("This last one should raise an error")
        options = Options(4, "verbose", log_file="logging.txt", port=80)
    except TypeError:
        print('TypeError correctly raised when argument name is an int')

if 2 in steps_to_run:
    print('\nStep 2\n')
    try:
        options = Options("debug", "verbose", log_file="logging.txt", port=80)
        print('Should print: True logging.txt')
        print(options["debug"], options["log_file"])

        print('Should print: False')
        print(options["unspecified"])
    except Exception as e:
        print('Error accessing values using [] during Step 2')
        print('Error was:', e)

if 3 in steps_to_run:
    print('\nStep 3\n')
    try:
        options = Options("debug", "verbose", log_file="logging.txt", port=80)
        print('Should print: True logging.txt False')
        print(options.debug, options.log_file, options.unspecified)
    except Exception as e:
        print('Error accessing values using attribute during Step 3')
        print('Error was:', e)

if 4 in steps_to_run:
    print('\nStep 4\n')
    try:
        options["log_file"] = "new_logging.txt"
        if options["log_file"] == "new_logging.txt":
            print('Can set via square bracket notation')
    except Exception as e:
        print('Error accessing values using attribute during Step 4')
        print('Error was:', e)

    try:
        options[5] = "new_logging.txt"
        print('Did not correctly raise TypeError for step 4')
    except TypeError:
        print('Correct TypeError raise when using a non string for key')

if 5 in steps_to_run:
    print('\nStep 5\n')
    try:
        options.log_file = "step5_logging.txt"
        if options['log_file'] == "step5_logging.txt":
            print('Can correctly set via attribute for Step 5')
    except Exception as e:
        print('Error during Step 5')
        print('Error was:', e)

if 6 in steps_to_run:
    print('\nStep 6\n')
    try:
        options = Options("debug", "verbose", log_file="logging.txt", port=80)
        del options["log_file"]
        del options.debug
        if options == Options("verbose", port=80):
            print('deleted correctly for step 6')
    except Exception as e:
        print('Error during Step 6')
        print('Error was:', e)
