

import cv2
from PIL import Image, ImageEnhance
import numpy as np
import os


INPFILE2 = r'/Users/trc/PycharmProjects/NoTexContent/data/dtructil/inputfile/imutils/PPPhoto_Original.png'
OUTFILE2_pil = r'/Users/trc/PycharmProjects/NoTexContent/data/dtructil/inputfile/imutils/PPPhoto_resize.jpg'



class Opxn_AdjImageDim:
	CNST_cmfrompixel = 2.54/144


	def __init__(self, inppath: str = None,
	             reqwidth: float = None,
	             reqheigth: float = None,
	             outpath: str = None):
		self.inpimgcv2 = cv2.imread(inppath)
		self.inpimgpil = Image.open(inppath)
		self.outimgpath = outpath
		self.reqwidthcm = reqwidth
		self.reqheigthcm = reqheigth
		self.outimgcv2 = self.redimension_cv()
		self.outimgpil = self.pilRredimension_bypxl()


	def redimension_cv(self):
		_outhgt_Pxl = int(1 / self.CNST_cmfrompixel * self.reqheigthcm)
		_outwid_Pxl = int(1 / self.CNST_cmfrompixel * self.reqwidthcm)
		revise_cms = (_outwid_Pxl,_outhgt_Pxl)
		revise_img = cv2.resize(self.inpimgcv2, revise_cms, cv2.INTER_AREA)
		return revise_img

	def pilRredimension_bycm(self):
		self.enhance_image(n = 1.5)
		_outhgt_Pxl = int(1 / self.CNST_cmfrompixel * self.reqheigthcm)
		_outwid_Pxl = int(1 / self.CNST_cmfrompixel * self.reqwidthcm)
		revise_cms = (_outwid_Pxl ,  _outhgt_Pxl)
		self.inpimgpil = self.inpimgpil.convert('RGB')
		revise_img = self.inpimgpil.resize(size = revise_cms)
		return revise_img

	def pilRredimension_bypxl(self):
		self.enhance_image(n = 1.5)
		_outhgt_Pxl = int(self.reqheigthcm)
		_outwid_Pxl = int(self.reqwidthcm)
		revise_cms = (_outwid_Pxl ,  _outhgt_Pxl)
		self.inpimgpil = self.inpimgpil.convert('RGB')
		revise_img = self.inpimgpil.resize(size = revise_cms)
		return revise_img

	def enhance_image(self,n):
		self.inpimgpil = ImageEnhance.Brightness(self.inpimgpil)
		self.inpimgpil = self.inpimgpil.enhance(n)
		self.inpimgpil = ImageEnhance.Contrast(self.inpimgpil)
		self.inpimgpil = self.inpimgpil.enhance(n)
		self.inpimgpil = ImageEnhance.Sharpness(self.inpimgpil)
		self.inpimgpil = self.inpimgpil.enhance(n)
		self.inpimgpil = ImageEnhance.Color(self.inpimgpil)
		self.inpimgpil = self.inpimgpil.enhance(n)

	def write_cv2(self):
		cv2.imwrite(self.outimgpath , self.outimgcv2)


	def write_pil(self):
		self.outimgpil.save(self.outimgpath , dpi = (144 , 144))



if __name__ == "__main__":
	# signature adjustment
	app1 = Opxn_AdjImageDim(inppath = INPFILE2 ,
	                        reqwidth = 150 ,
	                        reqheigth = 125 ,
	                        outpath = OUTFILE2_pil)
	app1.write_pil()
	print(os.stat(app1.outimgpath).st_size)

