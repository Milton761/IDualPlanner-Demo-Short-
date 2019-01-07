#!/usr/bin/env gnuplot

set terminal pdf
set output 'time001.pdf'
  

set title "Problem vs Time"

 #set yrange [-1:1]
# set xrange [0:400]

set dgrid3d
set hidden3d
#set grid
#set autoscale

set isosample 40
#set contour base


#set view 60,30
#set view map scale 1

#set xyplane relative 0


#unset surface 
#set style data pm3d
#set style function pm3d

#set pm3d at s
# set lmargin 20
# show margin
set datafile missing '-1.00000'

set colorbox user
set colorbox horizontal origin screen 0.1, 0.1 size screen 0.8, 0.02 front  

splot "exp001.dat" 			using 1:2:4 t "time-2lp" with lines, \
      "exp001.dat" 			using 1:2:3 t "time-vi" with lines

 	 
 	 
 	
