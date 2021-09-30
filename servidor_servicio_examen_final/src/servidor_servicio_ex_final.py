#!/usr/bin/env python

import rospy
from turtlesim.srv import Spawn, SpawnRequest, Kill,KillRequest
from geometry_msgs.msg import Twist
from turtlesim.msg import Pose
import math
import os
import time
#import subprocess

from servidor_servicio_examen_final.srv import ServicioExamen,ServicioExamenResponse

def my_callback(request):

    global presa
    global mover1
    global depredador
    global mover2

    #os.system("rosrun turtlesim turtlesim_node")
    #time.sleep(2)
    #p=subprocess.Popen('rosrun turtlesim turtlesim_node')
    #p.wait()

    rospy.wait_for_service('/spawn')
    servicio = rospy.ServiceProxy('/spawn',Spawn)
    peticion=SpawnRequest()
    peticion.name='presa'
    peticion.x=request.presa_x
    peticion.y=request.presa_y
    peticion.theta=request.presa_theta
    result = servicio (peticion)

    peticion.name='depredador'
    peticion.x=request.depredador_x
    peticion.y=request.depredador_y
    peticion.theta=request.depredador_theta
    result = servicio (peticion)

    rospy.wait_for_service('/kill')
    servicio = rospy.ServiceProxy('/kill',Kill)
    borrar=KillRequest()
    borrar.name='turtle1'
    result=servicio(borrar)
 
    respuesta=ServicioExamenResponse()
    respuesta.success=True
    return respuesta


rospy.init_node('servidor_configuracion_inicial')
my_service=rospy.Service('/servicio_configuracion_inicial',ServicioExamen,my_callback)
rospy.spin()