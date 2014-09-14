import os
def setup( dockerfile, reponame ):
  echo_git_dir = 'echo "RUN mkdir -p /gitserver/%s.git" >> /DockerRepo/%s/Dockerfile' %( reponame, dockerfile)
  echo_git_init = 'echo "RUN git init --bare --shared /gitserver/%s.git" >> /DockerRepo/%s/Dockerfile' %( reponame, dockerfile)
  os.system(echo_git_dir) 
  os.system(echo_git_init) 
#docker tag 91a9f658acd7 python:pyapp
 # cmd = 'docker build -t %s /DockerRepo/%s' % ( reponame, dockerfile )

  docker_build = 'docker build /DockerRepo/%s' % ( dockerfile ) 
  os.system(docker_build) 
  return;

setup("Nodejs", "app2")
