__author__ = 'timp'

import jenkinsapi
from jenkinsapi.jenkins import Jenkins
import xml.etree.ElementTree as ET
import re

jenkinswalldisplay_version = "0.6.26"

"""
<properties>
  <de.pellepelster.jenkins.walldisplay.WallDisplayJobProperty plugin="jenkinswalldisplay@0.6.26">
    <wallDisplayName>API Develop - Cucumber</wallDisplayName>
  </de.pellepelster.jenkins.walldisplay.WallDisplayJobProperty>
</properties>
"""

J = Jenkins('http://localhost:8080')
#J = Jenkins('http://hades:8081', 'timp', '94bff6285f22db83e8de27b27cf69263')


def displaymatch(match):
  if match is None:
    return None
  return match.groups(0)[0]


job_name_pattern = re.compile(r"^(.*)\.[^\.]+$")

def displayName(job_name):
  display_name_str = displaymatch(job_name_pattern.match(job_name))
  if display_name_str is not None:
    display_name_str = display_name_str.replace('.', ' ')
  return display_name_str

def create_subelement(parent, tag, value):
  sub = ET.SubElement(parent, tag)
  sub.text = value
  return sub

for j in J.keys():
  display_name = displayName(j)
  if display_name is not None:
    conf = J[j].get_config()
    root = ET.fromstring(conf)
    p = root.find('properties')
    if p is not None:
      print display_name
      wdjp = p.find('de.pellepelster.jenkins.walldisplay.WallDisplayJobProperty')
      if wdjp is not None:
        wdn = wdjp.find('wallDisplayName')
        if wdn is None:
          print "Update name 1"
          wdn = create_subelement(wdjp, 'wallDisplayName', display_name)
          J[j].update_config(ET.tostring(root))
        else:
          if wdn.text is None:
            print "Update name 2a"
            wdn.text = display_name
            J[j].update_config(ET.tostring(root))
          else:
            print "No update name 2b"
      else:
        print "Update name 3"
        wdjp = ET.SubElement(p, 'de.pellepelster.jenkins.walldisplay.WallDisplayJobProperty')
        wdjp.set('plugin', "jenkinswalldisplay@{}".format(jenkinswalldisplay_version))
        wdn = create_subelement(wdjp, 'wallDisplayName', display_name)
        J[j].update_config(ET.tostring(root))
