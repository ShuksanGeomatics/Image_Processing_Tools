import subprocess
import shutil
in_image = '/home/gerry/aaa.jpg'
out_image = '/home/gerry/aaa_gray.jpg'

cmd = 'convert ' + in_image + ' -set colorspace Gray -separate -average ' +  out_image

subprocess.call(cmd, shell = 'True')

in_jgw = in_image.split('.')[0] + '.jgw'
out_jgw = out_image.split('.')[0] + '.jgw'

shutil.copy(in_jgw, out_jgw)

