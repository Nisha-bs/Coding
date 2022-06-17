import paramiko

client_sh=paramiko.SSHClient()
client_sh.set_missing_host_key_policy(paramiko.AutoAddPolicy())
client_sh.connect(hostname='192.168.0.108',username='mieupro',password='startup')
stdin,stdout,stderr=client_sh.exec_command("sudo ls")
stdin.write("startup")
sftp=client_sh.open_sftp()
sftp.get('/home/mieupro/Downloads/eee.py','/home/nisha/ee.py')
print(stdout.readlines())
