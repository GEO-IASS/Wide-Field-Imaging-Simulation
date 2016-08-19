'''
author:wyh
date:2016-01-20
'''

import os
import sys
import time
import matplotlib.pyplot as plt
import numpy as np

#mode = raw_input("which mode to run?")

time_stat = []
pixel_sum = []
f= open('statistics.txt','w')

if mode == 'all':
    #fn = int(raw_input("the facets number is:")) #facets number
    #wn = int(raw_input("the wlayers number is:")) #w-layers number
    #wf = []
    #print 'please input the facets number and the wlayers number: '
    #wf.append(int(raw_input("the facets number is")))
    #wf.append(int(raw_input("the wlayers number is")))
  
    #wf_f=(int(raw_input("the facets number of wf is")))
    #wf_q(int(raw_input("the wlayers number of wf is")))
    f2 = open('parameters.txt','r')
    p = f.read()
    plist = []
    for i in p:
	plist.appent(int(i))
    f.close()
    
    fn = plist[0]
    wn = plist[1]
    wf = []
    wf[0] = plist[2]
    wf[0] = plist[3]
    #2dfft
    
    time1 = time.time()
    
    clean(vis = 'sim_mwa_12h.ms',imagename='sim_mwa_image_ft',gridmode= 'widefield', wprojplanes=1,\
    facets=1,niter = 1, imsize= [512, 512], cell= ['208.5arcsec', '208.5arcsec'], weighting='natural' )
    
    time2 = time.time()
    delt_time =round((time2-time1),2)
    
    imview(raster = 'sim_mwa_image_ft.image',out ='2dfft.png')
    xstat =imstat('sim_mwa_image_ft.image')
    time_stat.append(delt_time)
    pixel_sum.append(round(xstat['sumsq']))
    print xstat['sumsq']
    
    f.write('the statistics of 2DFFT:')
    f.write('\n')
    f.write('the sum of the squares of the pixel values:')
    f.write(str(xstat['sumsq']))
    f.write('\n')
    f.write('the simulation time of the 2dfft is:')
    f.write(str(delt_time))
    
    #faceting
    
    time3 = time.time()
    
    clean(vis = 'sim_mwa_12h.ms',imagename='sim_mwa_image_fc',gridmode= 'widefield', wprojplanes=1,\
    facets=fn, niter = 1, imsize= [512, 512], cell=['208.5arcsec', '208.5arcsec'], weighting='natural')
    
    time4 = time.time()
    delt_time2 = round((time4-time3),2)
    
    imview(raster = 'sim_mwa_image_fc.image',out ='faceting'+str(fn)+'.png')
    
    xstat =imstat('sim_mwa_image_fc.image')
    
    time_stat.append(delt_time2)
    pixel_sum.append(round( xstat['sumsq']))
    
    f.write('\n')
    f.write('the statistics of faceting:')
    f.write('\n')
    f.write('the sum of the squares of the pixel values:')
    f.write(str(xstat['sumsq']))
    f.write('\n')
    f.write('the simulation time of the faceting is:')
    f.write(str(delt_time2))
    
    #w-projection
    
    time5 = time.time()
    
    clean(vis = 'sim_mwa_12h.ms',imagename='sim_mwa_image_wp',gridmode= 'widefield', wprojplanes=wn,\
    facets=1,niter = 1, imsize= [512, 512], cell= ['208.5arcsec', '208.5arcsec'], weighting='natural')
    
    time6 = time.time()
    delt_time3 =round((time6-time5),2)
    
    imview(raster = 'sim_mwa_image_wp.image',out ='wproj'+str(wn)+'.png')
    
    xstat =imstat('sim_mwa_image_wp.image')
    
    time_stat.append(delt_time3)
    
    pixel_sum.append(round(xstat['sumsq']))
    
    f.write('\n')
    f.write('the statistics of w-projection:')
    f.write('\n')
    f.write('the sum of the squares of the pixel values:')
    f.write(str(xstat['sumsq']))
    f.write('\n')
    f.write('the simulation time of the w-projection is:')
    f.write(str(delt_time3))
    
    #wprojection+faceting

    time7 = time.time()

    clean(vis = 'sim_mwa_12h.ms',imagename='sim_mwa_image_wf',gridmode= 'widefield', wprojplanes=wf[1],facets=wf[0],niter = 1, imsize= [512, 512], cell= ['208.5arcsec', '208.5arcsec'], weighting='natural' )

    time8 = time.time()
    delt_time4 =round((time8-time7),2)

    imview(raster = 'sim_mwa_image_wf.image',out ='wproj'+str(wf[1])+'fc'+str(wf[0])+'.png')

    xstat =imstat('sim_mwa_image_wf.image')
 
    time_stat.append(delt_time4)

    pixel_sum.append(round(xstat['sumsq']))

    f.write('\n')
    f.write('the statistics of w-projection+faceting:')
    f.write('\n')
    f.write('the sum of the squares of the pixel values:')
    f.write(str(xstat['sumsq']))
    f.write('\n')
    f.write('the simulation time of the w-projection is:')
    f.write(str(delt_time4))
    f.close()
    
    
    #plot the time and image qulity statistics
    
    fig, ax = plt.subplots(2,figsize=(10,12))
    
    wide_field_tech = ('2dfft', 'faceting', 'w-projecting','w-p+fc')
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
    
    pixel_stat_plt=ax[1].barh(y_pos, performance1,height=height1, xerr=error, align='center', alpha=0.8)
    
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
    
elif mode == 'wp':
    
    N = int(raw_input("please input the number of simulation: "))
    wn = []
    for i in range(N):
        print 'the %sst number of wlayers is '%str(i+1)
        wn.append(int(raw_input()))
    for i in range(N):
        time5 = time.time()
        clean(vis = 'sim_mwa_12h.ms',imagename='sim_mwa_image_wp',gridmode= 'widefield', \
        wprojplanes=wn[i],facets=1,niter = 1, imsize= [512, 512], cell= ['208.5arcsec', '208.5arcsec'],\
        weighting='natural' )
        time6 = time.time()
        delt_time3 =round((time6-time5),2)
        
        imview(raster = 'sim_mwa_image_wp.image',out ='wproj'+str(wn[i])+'.png')
        
        xstat =imstat('sim_mwa_image_wp.image')
        
        time_stat.append(delt_time3)
        
        pixel_sum.append(round(xstat['sumsq']))

	f.write('\n')
	f.write('the statistics of w-projection_%s:'%str(wn[i]))
	f.write('\n')
	f.write('the sum of the squares of the pixel values:')
	f.write(str(xstat['sumsq']))
	f.write('\n')
	f.write('the simulation time of the w-projection is:')
	f.write(str(delt_time3))
    f.close()
    
    #plot the time and image qulity statistics
    
    fig, ax = plt.subplots(2,figsize=(10,12))
    
    wide_field_tech = []
    for i in range(N):
        wide_field_tech.append('wprojection_'+str(wn[i]))
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
    
    pixel_stat_plt=ax[1].barh(y_pos, performance1,height=height1, xerr=error, align='center', alpha=0.8)
    
    ax[1].set_yticks(y_pos)
    ax[1].set_yticklabels(wide_field_tech)
    ax[1].set_xlabel('pixel value')
    ax[1].set_title('pixel_sum comparison')
    
    for i in range(len(time_stat_plt)):
        ax[0].text(performance[i]*1.05, y_pos[i], performance[i])
        
    for i in range(len(pixel_stat_plt)):
        ax[1].text(performance1[i]*1.05, y_pos[i], performance1[i])
        
    plt.show()
    plt.savefig('pixel&time_stat_wp.png',format='png')
    
    time.sleep(10)
    
    os.system('rm casapy* i* clean.last' )
    
elif mode == 'fc':
    N = int(raw_input("please input the simulation number :"))
    fn = []
    for i in range(N):
        print 'the %sst number is '%str(i+1)
        fn.append(int(raw_input()))
    for i in range(N):
        time5 = time.time()
        clean(vis = 'sim_mwa_12h.ms',imagename='sim_mwa_image_fc',gridmode= 'widefield', \
        wprojplanes=1,facets=fn[i],niter = 1, imsize= [512, 512], cell= ['208.5arcsec', '208.5arcsec'],\
        weighting='natural' )
        time6 = time.time()
        delt_time3 =round((time6-time5),2)
        
        imview(raster = 'sim_mwa_image_fc.image',out ='faceting'+str(fn[i])+'.png')
        
        xstat =imstat('sim_mwa_image_fc.image')
        
        time_stat.append(delt_time3)
        
        pixel_sum.append(round(xstat['sumsq']))

        f.write('\n')
        f.write('the statistics of faceting:')
        f.write('\n')
        f.write('the sum of the squares of the pixel values:')
        f.write(str(xstat['sumsq']))
        f.write('\n')
        f.write('the simulation time of the w-projection is:')
        f.write(str(delt_time3))
    f.close()

    #plot the time and image qulity statistics
    
    fig, ax = plt.subplots(2,figsize=(10,12))
    
    wide_field_tech = []
    for i in range(N):
        wide_field_tech.append('faceting_'+str(fn[i]))
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
    pixel_stat_plt=ax[1].barh(y_pos, performance1,height=height1, xerr=error, align='center', alpha=0.8)
    
    ax[1].set_yticks(y_pos)
    ax[1].set_yticklabels(wide_field_tech)
    ax[1].set_xlabel('pixel value')
    ax[1].set_title('pixel_sum comparison')
    print "testing!!!" 
    for i in range(len(time_stat_plt)):
        ax[0].text(performance[i]*1.05, y_pos[i], performance[i])
        
    for i in range(len(pixel_stat_plt)):
        ax[1].text(performance1[i]*1.05, y_pos[i], performance1[i])
        
    plt.show()
    plt.savefig('pixel&time_stat_fc.png',format='png')
    
    time.sleep(10)
    
    os.system('rm casapy* i* clean.last' )

elif mode == 'wf':
    N = int(raw_input("please input the simulation number :"))
    fn = []
    wn = []
    for i in range(N):
        print 'the %sst facets number is '%str(i+1)
        fn.append(int(raw_input()))
	print 'the %sst wlayers number is '%str(i+1)
        wn.append(int(raw_input()))
    for i in range(N):
        time7 = time.time()
        clean(vis = 'sim_mwa_12h.ms',imagename='sim_mwa_image_fc+wp',gridmode= 'widefield', \
        wprojplanes=wn[i],facets=fn[i],niter = 1, imsize= [512, 512], cell= ['208.5arcsec', '208.5arcsec'],\
        weighting='natural' )
        time8 = time.time()
        delt_time4 =round((time8-time7),2)
        
        imview(raster = 'sim_mwa_image_fc+wp.image', out ='fc'+str(fn[i])+'wp'+str(wn[i])+'.png')
        
        xstat =imstat('sim_mwa_image_fc+wp.image')
        
        time_stat.append(delt_time4)
        
        pixel_sum.append(round(xstat['sumsq']))

   	f.write('\n')
        f.write('the statistics of w-p+fc:')
        f.write('\n')
        f.write('the sum of the squares of the pixel values:')
        f.write(str(xstat['sumsq']))
        f.write('\n')
        f.write('the simulation time of the w-projection is:')
        f.write(str(delt_time4))
    f.close()
  
  #plot the time and image qulity statistics
    
    fig, ax = plt.subplots(2,figsize=(10,12))
    
    wide_field_tech = []
    for i in range(N):
           wide_field_tech.append('wp_'+str(wn[i])+'fc_'+str(fn[i]))
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
    
    pixel_stat_plt=ax[1].barh(y_pos, performance1,height=height1, xerr=error, align='center', alpha=0.8)
    
    ax[1].set_yticks(y_pos)
    ax[1].set_yticklabels(wide_field_tech)
    ax[1].set_xlabel('pixel value')
    ax[1].set_title('pixel_sum comparison')

    for i in range(len(time_stat_plt)):
        ax[0].text(performance[i]*1.05, y_pos[i], performance[i])
        
    for i in range(len(pixel_stat_plt)):
        ax[1].text(performance1[i]*1.05, y_pos[i], performance1[i])
        
    plt.show()

    plt.savefig('pixel&time_stat_fc+wp.png',format='png')
    
    time.sleep(10)
    
    os.system('rm casapy* i* clean.last' )


    
