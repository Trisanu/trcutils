import docx
import pandas as pd

import docx

def getText(filename):
	doc = docx.Document(filename)
	fullText = {}
	for pnum,para in enumerate(doc.paragraphs):
		fullText.__setitem__(pnum,para.text)
	return fullText

def clean_text(arg):
	txt = str.lstrip(arg)
	# if not txt == '':
	# 	return txt
	# else:
	# 	return '!!'
	return txt



inpfile = r'/Users/trc/Downloads/TVHR.docx'
inpx = (pd.DataFrame.from_dict(
		getText(inpfile), orient = 'index')
        .rename(columns = {0:'pText'})
        )


inpx['pText'] = inpx['pText'].apply(lambda x: clean_text(x))
inpx = inpx.assign(pText = lambda x: clean_text(x.pText))


