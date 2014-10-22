from jenkinsapi.jenkins import Jenkins
import xml.etree.ElementTree as ET
import re

J = Jenkins('http://localhost:8080')
SLACK_PROPERTY = '''
    <jenkins.plugins.slack.SlackNotifier_-SlackJobProperty plugin="slack@1.2">
      <room>#music-{}</room>
      <startNotification>false</startNotification>
      <notifySuccess>false</notifySuccess>
      <notifyAborted>true</notifyAborted>
      <notifyNotBuilt>true</notifyNotBuilt>
      <notifyUnstable>true</notifyUnstable>
      <notifyFailure>true</notifyFailure>
      <notifyBackToNormal>true</notifyBackToNormal>
    </jenkins.plugins.slack.SlackNotifier_-SlackJobProperty>
'''

ACTIVATE_SLACK= '''
    <jenkins.plugins.slack.SlackNotifier plugin="slack@1.2">
      <teamDomain>blinkbox</teamDomain>
      <authToken>mgyNRhkk2Y7RThD7EWo1uMwi</authToken>
      <buildServerUrl>http://jenkins.we7.local/</buildServerUrl>
      <room>#music-ci</room>
    </jenkins.plugins.slack.SlackNotifier>
'''
def doit():
  for jobname in J.keys():
    m = re.search('[^.]+$', jobname)
    if (m is not None):
      dept = m.group(0)
      print dept
      if (not dept.endswith('det')):
        print jobname
        conf = J[jobname].get_config()
        root = ET.fromstring(conf.strip())
        properties = root.find('properties')
        slackProperty = properties.append(ET.fromstring(SLACK_PROPERTY.format(dept)))
        publishers = root.find('publishers') 
        slackPublisher = publishers.append(ET.fromstring(ACTIVATE_SLACK))
#        print ET.tostring(root)
        J[jobname].update_config(ET.tostring(root))



doit()
