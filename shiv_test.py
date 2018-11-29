import os
from shiv_ps import *

my_dir = os.path.dirname(os.path.realpath(__file__)) + '/'
mp3_filenames = ['sv_intro1.mp3', 'sv_intro2.mp3', 'sv_intro_out.mp3']
out_filename = 'sv_intro_b64.txt'

convert_two_mp3_file_to_one_base64(my_dir + mp3_filenames[0], my_dir + mp3_filenames[1], my_dir + out_filename)

convert_base64_to_mp3_file(my_dir + out_filename, my_dir + mp3_filenames[2])

which_mp3_file_is_larger(mp3_filenames[0], mp3_filenames[2])

which_mp3_file_is_larger(mp3_filenames[0], mp3_filenames[0])
