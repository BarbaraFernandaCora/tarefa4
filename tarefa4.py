import rospy 
from std_msgs.msg import String

rospy.init_node('tarefa4_no1')

envia = 'nada'

def funcao_envia(msg_envia):
    global envia
    envia = msg_envia.data

def timerCallBack(event):
    msg = String()
    msg.data = '2019000063'
    pub.publish(msg)
    
   

pub = rospy.Publisher('/topic1', String, queue_size=1)
timer = rospy.Timer(rospy.Duration(0.1), timerCallBack)
sub = rospy.Subscriber('/topic2', String, funcao_envia)

rospy.spin()