from jenkinsapi.jenkins import Jenkins
J = Jenkins('http://localhost:8080')

for j in J.keys():
  if (j.startswith('bad-prefix')):
    n = j.replace('bad-prefix', 'good-prefix')
    J.rename_job(j, n)