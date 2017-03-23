import os

filelist = ['/home/vse/mysite/prog/'+thing for thing in os.listdir('/home/vse/mysite/prog')]
out_complete = open('../outcomplete_WEEK3.txt','w')
for progfile in sorted(filelist):
    if progfile.split('.')[-1] == 'prog':
        out_complete.write('USER: '+progfile.split('.')[0].split('/')[-1]+'\n')
        #print progfile.split('.')[0].split('/')[-1]
        #printstring +=#{'
        for line in sorted(open(progfile,'r').readlines()):
            out_complete.write(line)
            #printstring += "'"+line.split()[0]+"':"
            #print line.split(',')[0],
            #line = line.strip()
            #if len(line.split(',')) > 1:
                #printstring += line.rstrip().split()[1]
        #        print line.rstrip().split()[1],
         #   else:
          #      #printstring += 'False'
           #     print 'False',
        #    print ",",
    #print
#            printstring += ','
#        printstring = printstring[:-1] + '}'
#        print printstring
out_complete.close()