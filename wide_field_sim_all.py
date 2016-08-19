import os
import sys
import time
import matplotlib.pyplot as plt
import numpy as np

#the four margins of the map
margin_ra_l = 115
margin_dec_l= -50
margin_ra_h = 145
margin_dec_h= -20
time_stat = []
pixel_sum = []

f= open('statistics.txt','w')



f2 = open('parameters.txt','r')
p = f2.readlines()

plist =p[0].split(' ')
plist.remove('')
f2.close()

fn = int(plist[0])
wn = int(plist[1])
wf = []
wf.append(int(plist[2]))
wf.append(int(plist[3]))

#read the sources' coordination in sky model
f3 = open('skymodel_225.osm','r')
l = f3.readlines()
sources = []
for i in l:
    sources.append(i.split(' ')[0:2])
f3.close()

#2dfft

time1 = time.time()

clean(vis = 'sim_mwa_12h.ms',imagename='sim_image_ft',gridmode= 'widefield', wprojplanes=1,\
facets=1,niter = 1, imsize= [512, 512], cell= ['208.5arcsec', '208.5arcsec'], weighting='natural' )

time2 = time.time()
delt_time =round((time2-time1),2)

imview(raster = 'sim_image_ft.image',out ='2dfft.png')
time_stat.append(delt_time)

# compute the pixel sum of the sources
pixelSum = 0.0
for j in sources:
	print 'circle[['+j[0]+'deg,'+j[1]+'deg'+'],0.04deg]'
	if (float(j[0])-margin_ra_l<0.04) or (float(j[1])-margin_dec_l<0.04):
		continue
	if (margin_ra_h-float(j[0])<0.04) or (margin_dec_h-float(j[1])<0.04):
		continue
	xval = imval('sim_image_ft'+'.image',region='circle[['+j[0]+'deg,'+j[1]+'deg'+'],1.0deg]')
	pixelSum = pixelSum + round(xval['data'].max(),2)
	f.write('\n')
	f.write('the pixelSum is: %s'%str(pixelSum))

pixel_sum.append(pixelSum)

f.write('the statistics of 2DFFT:')
f.write('\n')
f.write('the sum of the squares of the pixel values:')
#f.write(str(xstat['sumsq']))
f.write('\n')
f.write('the simulation time of the 2dfft is:')
f.write(str(delt_time))

#faceting

time3 = time.time()

clean(vis = 'sim_mwa_12h.ms',imagename='sim_image_fc_'+str(fn),gridmode= 'widefield', wprojplanes=1,\
facets=fn, niter = 1, imsize= [512, 512], cell=['208.5arcsec', '208.5arcsec'], weighting='natural')

time4 = time.time()
delt_time2 = round((time4-time3),2)

imview(raster = 'sim_image_fc_'+str(fn)+'.image',out ='faceting'+str(fn)+'.png')
time_stat.append(delt_time2)

# compute the pixel sum of the sources
pixelSum = 0.0
for j in sources:
	print 'circle[['+j[0]+'deg,'+j[1]+'deg'+'],0.04deg]'
	if (float(j[0])-margin_ra_l<0.04) or (float(j[1])-margin_dec_l<0.04):
		continue
	if (margin_ra_h-float(j[0])<0.04) or (margin_dec_h-float(j[1])<0.04):
		continue
	xval = imval('sim_image_fc_'+str(fn)+'.image',region='circle[['+j[0]+'deg,'+j[1]+'deg'+'],1.0deg]')
	pixelSum = pixelSum + round(xval['data'].max(),2)
	f.write('\n')
	f.write('the pixelSum is: %s'%str(pixelSum))

pixel_sum.append(pixelSum)

f.write('\n')
f.write('the statistics of faceting:')
f.write('\n')
f.write('the sum of the squares of the pixel values:')
#f.write(str(xstat['sumsq']))
f.write('\n')
f.write('the simulation time of the faceting is:')
f.write(str(delt_time2))

#w-projection

time5 = time.time()

clean(vis = 'sim_mwa_12h.ms',imagename='sim_image_wp_'+str(wn),gridmode= 'widefield', wprojplanes=wn,\
facets=1,niter = 1, imsize= [512, 512], cell= ['208.5arcsec', '208.5arcsec'], weighting='natural')

time6 = time.time()
delt_time3 =round((time6-time5),2)

imview(raster = 'sim_image_wp_'+str(wn)+'.image',out ='wproj'+str(wn)+'.png')

time_stat.append(delt_time3)

# compute the pixel sum of the sources
pixelSum = 0.0
for j in sources:
	print 'circle[['+j[0]+'deg,'+j[1]+'deg'+'],0.04deg]'
	if (float(j[0])-margin_ra_l<0.04) or (float(j[1])-margin_dec_l<0.04):
		continue
	if (margin_ra_h-float(j[0])<0.04) or (margin_dec_h-float(j[1])<0.04):
		continue
	xval = imval('sim_image_wp_'+str(wn)+'.image',region='circle[['+j[0]+'deg,'+j[1]+'deg'+'],1.0deg]')
	pixelSum = pixelSum + round(xval['data'].max(),2)
	f.write('\n')
	f.write('the pixelSum is: %s'%str(pixelSum))

pixel_sum.append(pixelSum)

f.write('\n')
f.write('the statistics of w-projection:')
f.write('\n')
f.write('the sum of the squares of the pixel values:')
#f.write(str(xstat['sumsq']))
f.write('\n')
f.write('the simulation time of the w-projection is:')
f.write(str(delt_time3))

#wprojection+faceting

time7 = time.time()

clean(vis = 'sim_mwa_12h.ms',imagename='sim_image_wf_f'+str(fn)+'w'+str(wn),gridmode= 'widefield', wprojplanes=wf[1],facets=wf[0],niter = 1, imsize= [512, 512], cell= ['208.5arcsec', '208.5arcsec'], weighting='natural' )

time8 = time.time()
delt_time4 =round((time8-time7),2)

imview(raster = 'sim_image_wf_f'+str(fn)+'w'+str(wn)+'.image',out ='wproj'+str(wf[1])+'fc'+str(wf[0])+'.png')

time_stat.append(delt_time4)

# compute the pixel sum of the sources
pixelSum = 0.0
for j in sources:
	print 'circle[['+j[0]+'deg,'+j[1]+'deg'+'],0.04deg]'
	if (float(j[0])-margin_ra_l<0.04) or (float(j[1])-margin_dec_l<0.04):
		continue
	if (margin_ra_h-float(j[0])<0.04) or (margin_dec_h-float(j[1])<0.04):
		continue
	xval = imval('sim_image_wf_f'+str(fn)+'w'+str(wn)+'.image',region='circle[['+j[0]+'deg,'+j[1]+'deg'+'],1.0deg]')
	pixelSum = pixelSum + round(xval['data'].max(),2)
	f.write('\n')
	f.write('the pixelSum is: %s'%str(pixelSum))

pixel_sum.append(pixelSum)

f.write('\n')
f.write('the statistics of w-projection+faceting:')
f.write('\n')
f.write('the sum of the squares of the pixel values:')
#f.write(str(xstat['sumsq']))
f.write('\n')
f.write('the simulation time of the w-projection is:')
f.write(str(delt_time4))
f.close()


#plot the time and image qulity statistics

fig, ax = plt.subplots(2,figsize=(10,12))

wide_field_tech = ('2dfft', 'fc', 'w-p','w-p+fc')
y_pos = np.arange(len(wide_field_tech))
performance = np.array(time_stat)
error = np.random.rand(len(wide_field_tech))
height1 = 0.5

time_stat_plt=ax[0].barh(y_pos, performance,height=height1, xerr=error, align='center', alpha=0.8)
ax[0].set_yticks(y_pos)
ax[0].set_yticklabels(wide_field_tech)
ax[0].set_xlabel('time cost/s')
ax[0].set_title('Time-consuming comparison')

performance1 = np.array(pixel_sum)

pixel_stat_plt=ax[1].barh(y_pos, performance1,height=height1, align='center', alpha=0.8)

ax[1].set_yticks(y_pos)
ax[1].set_yticklabels(wide_field_tech)
ax[1].set_xlabel('pixel value')
ax[1].set_title('pixel_sum comparison')

for i in range(len(time_stat_plt)):
	ax[0].text(performance[i]*1.05, y_pos[i], performance[i])

for i in range(len(pixel_stat_plt)):
	ax[1].text(performance1[i]*1.05, y_pos[i], performance1[i])

plt.show()
plt.savefig('pixel&time_stat_all.png',format='png')

time.sleep(10)

os.system('rm casapy* i* clean.last' )
