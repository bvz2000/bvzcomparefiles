#! /usr/bin/env python3


def get_user_input():
    """
    This function is used to get some data from the user. It is included in this sample just so that it is a fully
    functioning tool. It is not a necessary part of using this library.

    :return:
        A tuple containing the two paths to the files to be compared, and a boolean whether to run in parallel or not.
    """

    from argparse import ArgumentParser

    # Read in an arbitrary list of query directories or files from the command line
    help_msg = "Compares two files to see if they are identical."

    parser = ArgumentParser(description=help_msg)

    help_str = "The first file to be compared."
    parser.add_argument('File_A',
                        metavar='file_a_p',
                        type=str,
                        help=help_str)

    help_str = "The second file to be compared."
    parser.add_argument('File_B',
                        metavar='file_b_p',
                        type=str,
                        help=help_str)

    args = parser.parse_args()

    return args.File_A, args.File_B


# The following is the actual minimum example of the code needed to use this library
# ======================================================================================================================
def do_compare(file_a_p: str, file_b_p: str):
    """
    The code in this function is the minimum code required to compare two files. Simply prints True or False depending
    on whether the files are identical or not.

    :param file_a_p:
        The full path to the first file to be compared.
    :param file_b_p:
        The full path to the second file to be compared.

    :return:
        Nothing
    """

    from bvzcomparefiles import comparefiles_new

    result = comparefiles_new.compare(file_a_p=file_a_p,
                                      file_b_p=file_b_p,
                                      file_a_checksum=None,
                                      file_b_checksum=None)

    return result

# ======================================================================================================================
# The previous is the actual minimum example of the code needed to use this library


def main():

    import datetime

    file_a_p, file_b_p = get_user_input()
    start = datetime.datetime.now()

    try:
        result = do_compare(file_a_p=file_a_p,
                            file_b_p=file_b_p)
        if result:
            print(f"The files are identical, and their shared checksum is: {result}")
        else:
            print("The files are not the same.")
    except AssertionError:
        print("One or more of the files provided either do not exist or are links or are directories")

    diff = datetime.datetime.now() - start
    delta = str(datetime.timedelta(seconds=diff.seconds))
    hours = f"{delta.split(':')[0]} hours"
    minutes = f"{delta.split(':')[1]} minutes"
    seconds = f"{delta.split(':')[2]} seconds"
    print(f"\nTotal compare time: {hours}, {minutes}, {seconds}")


main()
