import base64
import os

def convert_two_mp3_file_to_one_base64(src_mp3_filename_a, src_mp3_filename_b, output_b64_text_file):
    with open(src_mp3_filename_a, 'rb') as srca, open(src_mp3_filename_b, 'rb') as srcb:
        with open(output_b64_text_file, 'w') as targetfile:
            mp3 = srca.read()
            mp32 = srcb.read()
            encoded_mp3 = base64.b64encode(mp3)
            encoded_mp32 = base64.b64encode(mp32)
            targetfile.write(encoded_mp3.decode('utf-8'))
            targetfile.write('\n')
            targetfile.write(encoded_mp32.decode('utf-8'))



#    """
#    Takes the contents of the two mp3 files and then APPENDS the bytes
#    from the 2nd one to the end of the first one so that you will have
#    a single array of bytes.
#
#    converts it to base64 text

#    then save that text to a file
#    """
#    print('starting convert two mp3 files to one base64')
#    pass


def convert_base64_to_mp3_file(base64_text, target_mp3_filename):
    #base64_text = 'sv_intro_b64.txt'
    with open(base64_text, 'rb') as base64_text_encoded:
        with open(target_mp3_filename, 'wb') as targetfile_2:
            decoded_b64 = base64_text_encoded.read()
            decoded_base64_file = base64.b64decode(decoded_b64)
            targetfile_2.write(decoded_base64_file)






#    """
#    Takes a base64_text as string adn a target mp3filename
#    Then decodes the base64 text and then writes it out
#    to the target mp3 filename
#    """
#    print('convert base64 to mp3 file')
#    pass

def which_mp3_file_is_larger(src_mp3_filename_a, src_mp3_filename_b):
    with open(src_mp3_filename_a, 'rb') as srca, open(src_mp3_filename_b, 'rb') as srcb:
        mp3 = srca.read()
        mp32 = srcb.read()
    if len(mp3) > len(mp32):
        print('a')
    elif len(mp3) == len(mp32):
        print('=')
    else:
        print('b')







#    """
#    this takes in two source filenames which are mp3 files
#    and then compares them.
#    IF the the first file is longer (larger, ie., has more bytes) than the second file, then print out "A".  If second is larger then print out
#    "B".  If they are the same size then print out "="
#    """
#    print('which mp3 file is larger')
    #pass
