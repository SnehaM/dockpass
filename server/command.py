import os
def repolist():
   for filename in os.listdir("/DockerRepo"):
     print  filename
   return;

repolist();

def setup( dockerfile, reponame ):
  git_init = 'ssh root@10.0.2.15 git init --bare --shared /gitserver/%s.git' % reponame
  gitrepo = 'ssh root@10.0.2.15 mkdir -p /gitserver/%s.git' % reponame
  os.system(gitrepo)
  os.system(git_init) 
 # cmd = 'docker build -t %s /DockerRepo/%s' % ( reponame, dockerfile )
##  cmd = 'docker build /DockerRepo/%s' % ( dockerfile )
 # grep_image_id = 'docker images | grep %s | awk \'{print $3}\'' % reponame 
 # os.system(cmd)
 # image_id = os.system(grep_image_id)
 # print image_id 
 # create_git_repo = 'docker run -i -t %s git clone....' % image_id
#  os.system(create_git_repo)
  return;

setup( "Nodejs", "nodejsrepo3" );

#[status,cmdout] = system('who');
#status

def inst_list():
 cmd = 'docker ps'
 os.system(cmd)
 return;
#inst_list();

def delete_image(image_id):
  cmd = 'docker rmi %s' % image_id
  os.system(cmd)
  return;

def delete_container(container_id):
  cmd = 'docker rm %s' % container_id
  os.system(cmd)
  return;

#def run_image(image_id):
  

