import prog
import requests
import time


if __name__ == "__main__":
    def check():
        version = requests.get('http://127.0.0.1:5000/').text
        return version

    def update():
        with open('localversion.txt','r+') as fileofv:
            rv = int(check())
            lv = int(fileofv.read())
            print(f'local version {lv}, remote {rv}')
            if lv != rv:
                print('try update')
                with open('prog.py','w') as prog:
                    newversion = requests.get('http://127.0.0.1:5000/newv').text
                    prog.write(newversion)
                    fileofv.truncate()
                    fileofv.seek(0)
                    print(str(rv))
                    fileofv.write(str(rv))
                    print('version updated!')
                    exit(0)
        print('version latest')

    update()


#prog.x()
