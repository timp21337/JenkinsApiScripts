from jenkinsapi.jenkins import Jenkins
import xml.etree.ElementTree as ET
import re

J = Jenkins('http://localhost:8080')
def doit():
  for jobname in J.keys():
    m = re.search('[^.]+$', jobname)
    if (m is not None):
      dept = m.group(0)
#      print dept
      if (dept.endswith('det')):
        print jobname
        conf = J[jobname].get_config()
        root = ET.fromstring(conf.strip())
#        properties = root.find('properties')
#        print " {}".format(ET.tostring(properties))
        room = root .find('properties/jenkins.plugins.slack.SlackNotifier_-SlackJobProperty/room')
        if room is not None: 
#          room.text = '#music-det'
          print ET.tostring(room)
#          J[jobname].update_config(ET.tostring(root))



doit()
