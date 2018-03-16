import os
import sys
import glob
import Baseline2
import Baseline3

path_baseline1 = 'log/pretrained_model_tf1.2.1/decode'

def outputBaseline1(filename):
    text = open(os.path.join(path_baseline1,filename),'r', encoding='utf-8').read()
    return text
def outputBaseline2(article):
    return Baseline2.getSum(article)
def outputBaseline3(article):
    return Baseline3.getSum(article)

def getSum(filename, article):
    res = '@Approach_1 \n' 
    res = res + outputBaseline1(filename) + '\n'
    res = res + '@Approach_2 \n' + outputBaseline2(article) + '\n'
    print(outputBaseline2(article))
    res = res + '@Approach_3 \n' + outputBaseline3(article)
    return res

def main():
    argument_list = sys.argv
    path = argument_list[1]
    preproces_command = 'python ./make_datafiles/make_datafiles.py ' + path + ' ' + 'tokenized_stories'
    os.system(preproces_command)
    bin_input_dir = 'tokenized_stories/finished_files/chunked/test_*.bin'
    run_baseline1 = 'python run_summarization.py --log_root=log --exp_name=pretrained_model_tf1.2.1 --vocab_path=vocab --mode=decode --data_path='+ bin_input_dir + ' --new_file=True'
    print(run_baseline1)
    os.system(run_baseline1)
    
    outputdir = './output/'
    #os.mkdir(outputdir)
    #Input string
    inputfilelist = glob.glob(os.path.join(path, '*.*'))
    i = 0
    for inputfile in inputfilelist:
        document = open(inputfile,'r',encoding='utf-8').read()
        filename = "{0:0>6}".format(i) + '_decoded.txt'
        # print(filename)
        i += 1

        
        outputfile = outputdir +os.path.basename(inputfile)
        # print(outputfile)
        final_res = getSum(filename,document)
        with open(outputfile, 'w' , encoding= 'utf-8') as f:
            f.write(final_res)

if __name__ == "__main__":
    main()