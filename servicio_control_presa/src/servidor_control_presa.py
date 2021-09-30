#!/usr/bin/env python

import rospy
import math

from servicio_control_presa.srv import ServicioPresaExamen,ServicioPresaExamenResponse

def my_callback(request):

    respuesta=ServicioPresaExamenResponse()
    presa_x=request.presa_x
    presa_y=request.presa_y
    presa_theta=request.presa_theta
    objetivo_x=request.objetivo_x
    objetivo_y=request.objetivo_y
    

    xb=objetivo_x-presa_x
    yb=objetivo_y-presa_y
    distancia=math.sqrt(math.pow(xb,2)+math.pow(yb,2))
    
    vel_linear_x = 1.5 * math.sqrt(math.pow((objetivo_x - presa_x), 2) + math.pow((objetivo_y - presa_y), 2))
    vel_angular_z = 4 * (math.atan2(objetivo_y - presa_y, objetivo_x - presa_x) - presa_theta)
    
    respuesta.lineal_presa=vel_linear_x*0.12
    respuesta.angular_presa=vel_angular_z
    respuesta.distancia=distancia
 
    return respuesta


rospy.init_node('servidor_control_presa')
my_service=rospy.Service('/servicio_control_presa',ServicioPresaExamen,my_callback)
rospy.spin()