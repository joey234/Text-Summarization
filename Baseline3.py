import spacy
import sys
import glob
import os
nlp = spacy.load('en')

def getSum(article):
    para_list = article.split('\n')
    final_res = ''
    for i in range(len(para_list)):
        if (i < 3) or (i>len(para_list)-2):
            final_res = final_res +  getParaSum(para_list[i]) + '\n'
    return final_res

def getParaSum(para):
    doc = nlp(para)
    list_sents =list(doc.sents)
    if len(list_sents) == 0:
        return ''
    return list_sents[0].text

def main():
    argument_list = sys.argv
    path = argument_list[1]
    outputdir = './output/'
    #os.mkdir(outputdir)
    #Input string
    inputfilelist = glob.glob(os.path.join(path, '*.*'))
    for inputfile in inputfilelist:
        document = open(inputfile,'r',encoding='utf-8').read()
        #split paragraph
        final_res = getSum(document)
        
        outputfile = outputdir +os.path.basename(inputfile)
        #print(outputfile)

        with open(outputfile, 'w' , encoding= 'utf-8') as f:
            f.write(final_res)


if __name__ == "__main__":
    main()
