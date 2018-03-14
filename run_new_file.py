import run_summarization
import subprocess
import sys
import os
import getopt


def main(argv):
    #default 
    log_dir = ''
    exp_name = 'log/pretrained_model_tf1.2.1'
    vocab_path = 'vocab'
    input_dir = 'stories'
    output_dir = 'tokenized_stories'
    new_file_flag = 'True'
    #else let user specify path
    opts, args = getopt.getopt(argv,"hi:v:l:n",["ifile=","ofile="])
    for opt,arg in opts:
        if opt == '-i':
            input_dir = arg
        elif opt == '-l':
            log_dir = arg
        elif opt == '-e':
            exp_name = arg
        elif opt == '-v':
            vocab_path = arg
        elif opt == '-n':
            new_file_flag = arg
    preprocess_command = 'python ./make_datafiles/make_datafiles.py ' + input_dir + ' ' + output_dir
    os.system(preprocess_command)
    bin_input_dir = 'tokenized_stories/finished_files/chunked/test_*.bin'

    
    decode_command = 'python run_summarization.py --log_root=' + log_dir + ' --exp_name=' + exp_name +  ' --vocab_path=' + vocab_path + ' --mode=decode' + ' --data_path='+ bin_input_dir + ' --new_file=' + new_file_flag
    os.system(decode_command)


if __name__ == '__main__':
    main(sys.argv[1:])