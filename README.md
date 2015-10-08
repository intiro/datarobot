#################################################################################################
#################################################################################################
# oooooooooo.                 .             ooooooooo.              .o8                     .   # 
# `888'   `Y8b              .o8             `888   `Y88.           "888                   .o8   #
#  888      888  .oooo.   .o888oo  .oooo.    888   .d88'  .ooooo.   888oooo.   .ooooo.  .o888oo #
#  888      888 `P  )88b    888   `P  )88b   888ooo88P'  d88' `88b  d88' `88b d88' `88b   888   #
#  888      888  .oP"888    888    .oP"888   888`88b.    888   888  888   888 888   888   888   #
#  888     d88' d8(  888    888 . d8(  888   888  `88b.  888   888  888   888 888   888   888 . #
# o888bood8P'   `Y888""8o   "888" `Y888""8o o888o  o888o `Y8bod8P'  `Y8bod8P' `Y8bod8P'   "888" #
#################################################################################################

1. Copy Vagrantfile to your VM directory and run 'vagrant up' to start the VM.
2. Check if the ssh connection is available by connecting to port 2222 on localhost.
3. Exchange ssh keys between your host system and the VM or use the password (root/vagrant).
4. Update your ansible.cfg and hosts file with proper IP and port for the target system and add a 
   hosts section for this address called [wordpress].
5. Run ansible-plabook -i wordpress site.yml from the playbook directory.
6. Navigate your browser to http://<vm_ip>:80 or http://localhost:8080 to run the wordpress 
   configuration wizard.
7. Enter name of the blog, username and the password for admin account (these credentials will be
   nedded to run the python script).
8. Edit the post.py script by eding <ip>, <login> and <password> from the last step.
9. Enter desired <Entry title> in  post.py script and edit the content of the post_content.txt file.
10.Check if post.py has execution rights, if no do chmod +x post.py and run the script ./post.py.
11.Contents of the post_content.txt should be available on the blog as last entry.  

  
