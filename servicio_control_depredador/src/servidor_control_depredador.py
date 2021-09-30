#!/usr/bin/env python

import rospy
import math

from servicio_control_depredador.srv import ServicioDepredadorExamen,ServicioDepredadorExamenResponse

def my_callback(request):

    respuesta=ServicioDepredadorExamenResponse()
    depredador_x=request.depredador_x
    depredador_y=request.depredador_y
    depredador_theta=request.depredador_theta
    presa_x=request.presa_x
    presa_y=request.presa_y
    presa_theta=request.presa_theta

    xb=presa_x-depredador_x
    yb=presa_y-depredador_y
    distancia=math.sqrt(math.pow(xb,2)+math.pow(yb,2))
    
    vel_linear_x = 1.5 * math.sqrt(math.pow((presa_x - depredador_x), 2) + math.pow((presa_y - depredador_y), 2))
    vel_angular_z = 4 * (math.atan2(presa_y - depredador_y, presa_x - depredador_x) - depredador_theta)
    
    respuesta.lineal_depredador=vel_linear_x*0.1
    respuesta.angular_depredador=vel_angular_z
    respuesta.distancia=distancia
 
    return respuesta


rospy.init_node('servidor_control_depredador')
my_service=rospy.Service('/servicio_control_depredador',ServicioDepredadorExamen,my_callback)
rospy.spin()