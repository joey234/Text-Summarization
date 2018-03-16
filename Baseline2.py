from gensim.summarization.summarizer import summarize
import sys
import glob
import os

def getSum(article):
    return summarize(article, ratio = 0.1)

def main():
    argument_list = sys.argv
    path = argument_list[1]
    outputdir = './output/'
    #os.mkdir(outputdir)
    #Input string
    inputfilelist = glob.glob(os.path.join(path, '*.*'))
    for inputfile in inputfilelist:
        document = open(inputfile,'r',encoding='utf-8').read()

        
        outputfile = outputdir + inputfile[inputfile.rfind('/'):]
        #print(outputfile)
        final_res = getSum(document)
        with open(outputfile, 'w' , encoding= 'utf-8') as f:
            f.write(final_res)


if __name__ == "__main__":
    main()


