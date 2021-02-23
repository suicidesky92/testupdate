import prog
import requests
import time
import subprocess
import shlex


URL='http://127.0.0.1:5000'
cmd = shlex.split('/usr/bin/python3 prog.py')

if __name__ == "__main__":
    def check():
        version = requests.get('{URL}/getv').text
        return version

    def update():
        with open('localversion.txt','r+') as fileofv:
            rv = int(check())
            lv = int(fileofv.read())
            print(f'local version {lv}, remote {rv}')
            if lv != rv:
                print('try update')
                with open('prog.py','w') as prog:
                    newversion = requests.get(f'{URL}/newv').text
                    prog.write(newversion)
                    fileofv.truncate()
                    fileofv.seek(0)
                    print(str(rv))
                    fileofv.write(str(rv))
                    print('version updated!')
                    exit(0)
        print('version latest')

    update()


x = subprocess.Popen(cmd)
