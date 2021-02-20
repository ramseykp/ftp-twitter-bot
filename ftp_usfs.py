import ftplib
import ssl
import sys, os
import os.path

root = r'C:\SmartStorageExternalDrive\Flight_0237_8000ft\test'
destdir = r'/nirops/2020_Fires/2020_Tenax_Overwatch/new'

#server url username and password
FTP_HOST = "ftp.nifc.gov"
FTP_PORT = 1021
FTP_USER = "kelseyramsey"
FTP_PASS = "B!k3sandbutts23"

#connect to the FTP server
class Explicit_FTP_TLS(ftplib.FTP_TLS):
    """Explicit FTPS, with shared TLS session"""
    def ntransfercmd(self, cmd, rest=None):
        conn, size = ftplib.FTP.ntransfercmd(self, cmd, rest)
        if self._prot_p:
            conn = self.context.wrap_socket(conn,
                                            server_hostname=self.host,
                                            session=self.sock.session)
        return conn, size

ftp_server = Explicit_FTP_TLS()

#ftp_server.auth()
ftp_server.set_debuglevel(1)
ftp_server.set_pasv(True)
ftp_server.connect(host=FTP_HOST, port=FTP_PORT)
ftp_server.login(user=FTP_USER, passwd=FTP_PASS)
#ftp_server.encoding = "utf-8"
ftp_server.prot_p()
ftp_server.getwelcome()
#ftp_server.cwd(destdir)
print("_______")
ftp_server.pwd()

try:
    ftp_server.cwd(destdir)
except Exception:
    ftp_server.mkd(destdir)
for (dir, _, files) in os.walk(root):
    newdir=destdir+dir[len(root):len(dir)].replace("\\","/")
    try:
        ftp_server.cwd(newdir)
    except Exception:
        ftp_server.mkd(newdir)
    for f in files:
        with open(os.path.join(dir, f),'rb') as file:
            #insert timer
            ftp_server.storbinary('STOR '+f, file, blocksize=8192, callback=None, rest=None)
            #end and print timer
            #file.close()

ftp_server.quit()
print('done')