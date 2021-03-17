import subprocess
import shutil
in_image = '/home/gerry/aaa.jpg'
out_image = '/home/gerry/aaa_gray.jpg'

cmd = 'convert -quiet' + in_image + '-colorspace cmyk' +  out_image

subprocess.call(cmd, shell = 'True')


