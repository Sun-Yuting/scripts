import subprocess
import socket
import time


cmd = 'svtools-prosody-socket\\carlos-svtools.exe'
output_file = 'svtools_output\\shift_name.txt'


def main():
    # start svtools
    subprocess.Popen(cmd)

    # wait for start up
    time.sleep(2)

    # connect to svtools
    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.bind(('127.0.0.1', 20097))
    server.listen(1)
    conn, __ = server.accept()
    with open(output_file, 'w+') as f:
        while True:
            line = conn.recv(2048).decode('utf-8').strip()
            print(line)

            f.write(line)


if __name__ == '__main__':
    main()
