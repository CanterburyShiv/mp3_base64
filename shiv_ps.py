

def convert_two_mp3_file_to_one_base64(src_mp3_filename_a, src_mp3_filename_b, output_b64_text_file):
    """
    Takes the contents of the two mp3 files and then APPENDS the bytes
    from the 2nd one to the end of the first one so that you will have
    a single array of bytes.

    converts it to base64 text

    then save that text to a file
    """
    print('starting convert two mp3 files to one base64')
    pass


def convert_base64_to_mp3_file(base64_text, target_mp3_filename):
    """
    Takes a base64_text as string adn a target mp3filename
    Then decodes the base64 text and then writes it out
    to the target mp3 filename
    """
    print('convert base64 to mp3 file')
    pass

def which_mp3_file_is_larger(src_mp3_filename_a, src_mp3_filename_b):
    """
    this takes in two source filenames which are mp3 files
    and then compares them.
    IF the the first file is longer (larger, ie., has more bytes) than the second file, then print out "A".  If second is larger then print out
    "B".  If they are the same size then print out "="
    """
    print('which mp3 file is larger')
    pass
