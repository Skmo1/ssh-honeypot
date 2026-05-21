def executer_commande(commande):
    if commande == "whoami":
        return "root"

    elif commande == "ls":
        return "Documents  Downloads  Music  Pictures  Videos  notes.txt  todo.md"

    elif commande == "ls -la":
        return (
            "total 48\n"
            "drwx------ 6 root root 4096 May 21 07:14 .\n"
            "drwxr-xr-x 19 root root 4096 May 20 12:00 ..\n"
            "-rw------- 1 root root  220 May 20 12:00 .bash_history\n"
            "-rw-r--r-- 1 root root 3526 May 20 12:00 .bashrc\n"
            "drwx------ 2 root root 4096 May 21 07:10 .ssh\n"
            "-rw-r--r-- 1 root root  807 May 20 12:00 .profile\n"
            "drwxr-xr-x 2 root root 4096 May 21 06:00 Documents\n"
            "drwxr-xr-x 2 root root 4096 May 21 06:00 Downloads\n"
            "-rw-r--r-- 1 root root  142 May 19 14:32 notes.txt\n"
            "-rw-r--r-- 1 root root   87 May 18 09:11 todo.md\n"
            "-rw------- 1 root root 2048 May 20 23:55 backup.tar.gz"
        )

    elif commande == "ls /":
        return "bin  boot  dev  etc  home  lib  lib64  media  mnt  opt  proc  root  run  sbin  srv  sys  tmp  usr  var"

    elif commande == "ls /home":
        return "deploy  ubuntu"

    elif commande == "ls /etc":
        return "apt  bash.bashrc  cron.d  crontab  default  environment  group  hosts  hostname  nginx  os-release  passwd  profile  resolv.conf  shadow  ssh  sudoers"

    elif commande == "ls /var/www/html":
        return "index.html  index.php  wp-config.php  .htaccess"

    elif commande == "ls /var/log":
        return "auth.log  dpkg.log  fail2ban.log  kern.log  nginx  syslog  ufw.log"

    elif commande == "pwd":
        return "/root"

    elif commande == "id":
        return "uid=0(root) gid=0(root) groupes=0(root),24(cdrom),25(floppy),27(sudo),29(audio),30(dip),44(video),46(plugdev),106(netdev),120(bluetooth),126(lpadmin),130(scanner),1000(docker)"

    elif commande == "uname -a":
        return "Linux srv-prod-01 6.18.5 #2 SMP PREEMPT_DYNAMIC Wed Jan 14 17:56:08 UTC 2026 x86_64 x86_64 x86_64 GNU/Linux"

    elif commande == "uname -r":
        return "6.18.5"

    elif commande == "uname -s":
        return "Linux"

    elif commande == "arch":
        return "x86_64"

    elif commande == "hostname":
        return "srv-prod-01"

    elif commande == "hostname -I":
        return "192.168.1.100 10.0.0.5"

    elif commande == "date":
        return "Thu May 21 14:32:01 UTC 2026"

    elif commande == "uptime":
        return " 14:32:01 up 47 days,  3:12,  1 user,  load average: 0.12, 0.08, 0.05"

    elif commande == "uptime -p":
        return "up 6 weeks, 3 days, 3 hours, 12 minutes"

    elif commande == "free -h":
        return (
            "               total        used        free      shared  buff/cache   available\n"
            "Mem:           7.8Gi       1.2Gi       3.8Gi       156Mi       2.8Gi       6.1Gi\n"
            "Swap:          2.0Gi          0B       2.0Gi"
        )

    elif commande == "df -h":
        return (
            "Filesystem      Size  Used Avail Use% Mounted on\n"
            "udev            3.9G     0  3.9G   0% /dev\n"
            "tmpfs           799M  1.1M  798M   1% /run\n"
            "/dev/sda1        50G   18G   30G  38% /\n"
            "tmpfs           3.9G     0  3.9G   0% /dev/shm\n"
            "/dev/sda2       100G   42G   53G  45% /var\n"
            "/dev/sdb1       500G  210G  265G  45% /data"
        )

    elif commande == "env" or commande == "printenv":
        return (
            "SHELL=/bin/bash\n"
            "HOME=/root\n"
            "LOGNAME=root\n"
            "USER=root\n"
            "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin\n"
            "LANG=en_US.UTF-8\n"
            "TERM=xterm-256color\n"
            "PWD=/root"
        )

    elif commande == "echo $SHELL":
        return "/bin/bash"

    elif commande == "echo $HOME":
        return "/root"

    elif commande == "echo $USER":
        return "root"

    elif commande == "echo $PATH":
        return "/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin:/snap/bin"

    elif commande == "cat /etc/os-release":
        return (
            'PRETTY_NAME="Ubuntu 24.04.4 LTS"\n'
            'NAME="Ubuntu"\n'
            'VERSION_ID="24.04"\n'
            'VERSION="24.04.4 LTS (Noble Numbat)"\n'
            'VERSION_CODENAME=noble\n'
            'ID=ubuntu\n'
            'ID_LIKE=debian\n'
            'HOME_URL="https://www.ubuntu.com/"\n'
            'SUPPORT_URL="https://help.ubuntu.com/"\n'
            'BUG_REPORT_URL="https://bugs.launchpad.net/ubuntu/"'
        )

    elif commande == "cat /etc/hostname":
        return "srv-prod-01"

    elif commande == "cat /etc/hosts":
        return (
            "127.0.0.1   localhost\n"
            "127.0.1.1   srv-prod-01\n"
            "::1         localhost ip6-localhost ip6-loopback\n"
            "ff02::1     ip6-allnodes\n"
            "ff02::2     ip6-allrouters"
        )

    elif commande == "cat /etc/resolv.conf":
        return "nameserver 8.8.8.8\nnameserver 1.1.1.1"

    elif commande == "cat /etc/shells":
        return "/bin/sh\n/bin/bash\n/usr/bin/bash\n/bin/dash\n/bin/zsh\n/usr/bin/zsh"

    elif commande == "cat /etc/passwd":
        return (
            "root:x:0:0:root:/root:/bin/bash\n"
            "daemon:x:1:1:daemon:/usr/sbin:/usr/sbin/nologin\n"
            "bin:x:2:2:bin:/bin:/usr/sbin/nologin\n"
            "sys:x:3:3:sys:/dev:/usr/sbin/nologin\n"
            "www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin\n"
            "sshd:x:110:65534::/run/sshd:/usr/sbin/nologin\n"
            "deploy:x:1001:1001::/home/deploy:/bin/bash\n"
            "ubuntu:x:1002:1002::/home/ubuntu:/bin/bash"
        )

    elif commande == "cat /etc/group":
        return (
            "root:x:0:\n"
            "sudo:x:27:ubuntu,deploy\n"
            "www-data:x:33:\n"
            "docker:x:999:root,deploy\n"
            "deploy:x:1001:\n"
            "ubuntu:x:1002:"
        )

    elif commande == "cat /etc/crontab":
        return (
            "# /etc/crontab: system-wide crontab\n"
            "SHELL=/bin/sh\n"
            "PATH=/usr/local/sbin:/usr/local/bin:/sbin:/bin:/usr/sbin:/usr/bin\n\n"
            "# m h dom mon dow user  command\n"
            "17 *    * * *   root    cd / && run-parts --report /etc/cron.hourly\n"
            "25 6    * * *   root    test -x /usr/sbin/anacron || ( cd / && run-parts --report /etc/cron.daily )\n"
            "0  2    * * 0   root    /root/backup.sh"
        )

    elif commande == "cat notes.txt":
        return (
            "TODO:\n"
            "- renouveler cert SSL (expire le 15 juin)\n"
            "- migrer BDD vers nouveau serveur\n"
            "- verifier logs fail2ban\n"
            "mdp db prod: Tr0ub4dor&3"
        )

    elif commande == "cat /root/.bash_history":
        return (
            "apt update\n"
            "apt upgrade -y\n"
            "ufw enable\n"
            "ufw allow 22/tcp\n"
            "ufw allow 80/tcp\n"
            "ufw allow 443/tcp\n"
            "nano /etc/ssh/sshd_config\n"
            "systemctl restart sshd\n"
            "adduser deploy\n"
            "passwd deploy\n"
            "ls /var/www/html\n"
            "nginx -t\n"
            "systemctl status nginx\n"
            "mysql -u root -p\n"
            "cat /etc/passwd"
        )

    elif commande == "history":
        return (
            "    1  apt update\n"
            "    2  apt upgrade -y\n"
            "    3  ufw enable\n"
            "    4  ufw allow 22/tcp\n"
            "    5  ufw allow 80/tcp\n"
            "    6  ufw allow 443/tcp\n"
            "    7  nano /etc/ssh/sshd_config\n"
            "    8  systemctl restart sshd\n"
            "    9  adduser deploy\n"
            "   10  passwd deploy\n"
            "   11  ls /var/www/html\n"
            "   12  nginx -t\n"
            "   13  systemctl status nginx\n"
            "   14  mysql -u root -p\n"
            "   15  history"
        )

    elif commande == "ps aux":
        return (
            "USER       PID %CPU %MEM    VSZ   RSS TTY      STAT START   TIME COMMAND\n"
            "root         1  0.0  0.1  16952  5504 ?        Ss   May20   0:12 /sbin/init\n"
            "root       712  0.0  0.1  14744  5120 ?        Ss   May20   0:00 /usr/sbin/sshd -D\n"
            "www-data   891  0.1  0.5 365124 22012 ?        S    May20   1:42 nginx: worker process\n"
            "mysql      934  0.3  4.2 1254320 172040 ?      Sl   May20  14:21 /usr/sbin/mysqld\n"
            "root      1203  0.0  0.2  21832  8960 ?        Ss   May20   0:01 /usr/sbin/cron -f\n"
            "root      4821  0.0  0.1  15848  5120 pts/0    Ss   14:28   0:00 -bash\n"
            "root      4832  0.0  0.0  17628  2048 pts/0    R+   14:32   0:00 ps aux"
        )

    elif commande == "ps -ef":
        return (
            "UID        PID  PPID  C STIME TTY          TIME CMD\n"
            "root         1     0  0 May20 ?        00:00:12 /sbin/init\n"
            "root       712     1  0 May20 ?        00:00:00 /usr/sbin/sshd -D\n"
            "www-data   891   712  0 May20 ?        00:01:42 nginx: worker process\n"
            "mysql      934     1  0 May20 ?        00:14:21 /usr/sbin/mysqld\n"
            "root      4821   712  0 14:28 pts/0    00:00:00 -bash\n"
            "root      4832  4821  0 14:32 pts/0    00:00:00 ps -ef"
        )

    elif commande == "top":
        return (
            "top - 14:32:01 up 47 days,  3:12,  1 user,  load average: 0.12, 0.08, 0.05\n"
            "Tasks: 102 total,   1 running, 101 sleeping,   0 stopped,   0 zombie\n"
            "%Cpu(s):  2.1 us,  0.8 sy,  0.0 ni, 96.9 id,  0.0 wa,  0.0 hi,  0.2 si\n"
            "MiB Mem :   7989.5 total,   3882.4 free,   1228.6 used,   2878.5 buff/cache\n"
            "MiB Swap:   2048.0 total,   2048.0 free,      0.0 used.   6232.5 avail Mem\n\n"
            "  PID USER      PR  NI    VIRT    RES    SHR S  %CPU  %MEM     TIME+ COMMAND\n"
            "  934 mysql     20   0 1.254g 172040  18432 S   1.0   4.2  14:21.33 mysqld\n"
            "  891 www-data  20   0  365124  22012   8192 S   0.3   0.5   1:42.10 nginx\n"
            "    1 root      20   0   16952   5504   4096 S   0.0   0.1   0:12.04 systemd"
        )

    elif commande == "who":
        return "root     pts/0        2026-05-21 14:28 (41.82.114.5)"

    elif commande == "w":
        return (
            " 14:32:01 up 47 days,  3:12,  1 user,  load average: 0.12, 0.08, 0.05\n"
            "USER     TTY      FROM             LOGIN@   IDLE   JCPU   PCPU WHAT\n"
            "root     pts/0    41.82.114.5      14:28    0.00s  0.04s  0.00s w"
        )

    elif commande == "last":
        return (
            "root     pts/0        41.82.114.5      Thu May 21 14:28   still logged in\n"
            "root     pts/0        41.82.114.5      Wed May 20 23:41 - 01:12  (01:31)\n"
            "deploy   pts/1        10.0.0.5         Wed May 20 18:05 - 18:47  (00:42)\n"
            "root     pts/0        41.82.114.5      Wed May 20 11:02 - 15:33  (04:31)\n\n"
            "wtmp begins Mon Apr  1 00:00:01 2026"
        )

    elif commande == "ip a" or commande == "ip addr" or commande == "ip addr show":
        return (
            "1: lo: <LOOPBACK,UP,LOWER_UP> mtu 65536 qdisc noqueue state UNKNOWN\n"
            "    link/loopback 00:00:00:00:00:00 brd 00:00:00:00:00:00\n"
            "    inet 127.0.0.1/8 scope host lo\n"
            "2: eth0: <BROADCAST,MULTICAST,UP,LOWER_UP> mtu 1500 qdisc fq_codel state UP\n"
            "    link/ether 52:54:00:12:34:56 brd ff:ff:ff:ff:ff:ff\n"
            "    inet 192.168.1.100/24 brd 192.168.1.255 scope global eth0\n"
            "    inet6 fe80::5054:ff:fe12:3456/64 scope link"
        )

    elif commande == "ip r" or commande == "ip route":
        return (
            "default via 192.168.1.1 dev eth0 proto dhcp src 192.168.1.100 metric 100\n"
            "192.168.1.0/24 dev eth0 proto kernel scope link src 192.168.1.100"
        )

    elif commande == "ss -tuln" or commande == "netstat -tuln":
        return (
            "Netid  State   Recv-Q  Send-Q  Local Address:Port  Peer Address:Port\n"
            "tcp    LISTEN  0       128     0.0.0.0:22          0.0.0.0:*\n"
            "tcp    LISTEN  0       128     0.0.0.0:80          0.0.0.0:*\n"
            "tcp    LISTEN  0       128     0.0.0.0:443         0.0.0.0:*\n"
            "tcp    LISTEN  0       70      127.0.0.1:3306      0.0.0.0:*"
        )

    elif commande == "ss -s":
        return (
            "Total: 312\n"
            "TCP:   18 (estab 4, closed 8, orphaned 0, timewait 8)\n\n"
            "Transport Total  IP  IPv6\n"
            "RAW       0      0   0\n"
            "UDP       4      2   2\n"
            "TCP       10     6   4"
        )

    elif commande == "ifconfig":
        return (
            "eth0: flags=4163<UP,BROADCAST,RUNNING,MULTICAST>  mtu 1500\n"
            "        inet 192.168.1.100  netmask 255.255.255.0  broadcast 192.168.1.255\n"
            "        inet6 fe80::5054:ff:fe12:3456  prefixlen 64  scopeid 0x20<link>\n"
            "        ether 52:54:00:12:34:56  txqueuelen 1000  (Ethernet)\n"
            "        RX packets 5823401  bytes 7234123456 (7.2 GB)\n"
            "        TX packets 4123098  bytes 3421098765 (3.4 GB)\n\n"
            "lo: flags=73<UP,LOOPBACK,RUNNING>  mtu 65536\n"
            "        inet 127.0.0.1  netmask 255.0.0.0\n"
            "        loop  txqueuelen 1000  (Local Loopback)"
        )

    elif commande == "curl ifconfig.me" or commande == "curl icanhazip.com":
        return "41.82.114.5"

    elif commande == "lsb_release -a":
        return (
            "No LSB modules are available.\n"
            "Distributor ID:\tUbuntu\n"
            "Description:\tUbuntu 24.04.4 LTS\n"
            "Release:\t24.04\n"
            "Codename:\tnoble"
        )

    elif commande == "cat /proc/cpuinfo":
        return (
            "processor\t: 0\n"
            "vendor_id\t: GenuineIntel\n"
            "model name\t: Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz\n"
            "cpu MHz\t\t: 2399.996\n"
            "cache size\t: 35840 KB\n"
            "cpu cores\t: 4\n"
            "flags\t\t: fpu vme de pse tsc msr pae mce cx8 apic sse sse2 ht"
        )

    elif commande == "cat /proc/meminfo":
        return (
            "MemTotal:        8181760 kB\n"
            "MemFree:         3975168 kB\n"
            "MemAvailable:    6382592 kB\n"
            "Buffers:          102400 kB\n"
            "Cached:          2949120 kB\n"
            "SwapTotal:       2097152 kB\n"
            "SwapFree:        2097152 kB"
        )

    elif commande == "lscpu":
        return (
            "Architecture:            x86_64\n"
            "CPU op-mode(s):          32-bit, 64-bit\n"
            "Byte Order:              Little Endian\n"
            "CPU(s):                  4\n"
            "Model name:              Intel(R) Xeon(R) CPU E5-2680 v4 @ 2.40GHz\n"
            "CPU MHz:                 2399.996\n"
            "L2 cache:                256K\n"
            "L3 cache:                35840K"
        )

    elif commande == "lsblk":
        return (
            "NAME   MAJ:MIN RM   SIZE RO TYPE MOUNTPOINT\n"
            "sda      8:0    0    50G  0 disk\n"
            "├─sda1   8:1    0    49G  0 part /\n"
            "└─sda2   8:2    0     1G  0 part [SWAP]\n"
            "sdb      8:16   0   500G  0 disk\n"
            "└─sdb1   8:17   0   500G  0 part /data"
        )

    elif commande == "systemctl status nginx":
        return (
            "● nginx.service - A high performance web server and a reverse proxy server\n"
            "     Loaded: loaded (/lib/systemd/system/nginx.service; enabled)\n"
            "     Active: active (running) since Mon 2026-04-04 11:20:01 UTC; 47 days ago\n"
            "    Process: 890 ExecStartPre=/usr/sbin/nginx -t (code=exited, status=0/SUCCESS)\n"
            "   Main PID: 891 (nginx)\n"
            "      Tasks: 2 (limit: 4915)\n"
            "     Memory: 8.2M\n"
            "     CGroup: /system.slice/nginx.service\n"
            "             ├─891 nginx: master process\n"
            "             └─892 nginx: worker process"
        )

    elif commande == "systemctl status mysql" or commande == "systemctl status mysqld":
        return (
            "● mysql.service - MySQL Community Server\n"
            "     Loaded: loaded (/lib/systemd/system/mysql.service; enabled)\n"
            "     Active: active (running) since Mon 2026-04-04 11:20:05 UTC; 47 days ago\n"
            "   Main PID: 934 (mysqld)\n"
            "     Status: Server is operational\n"
            "      Tasks: 38 (limit: 4915)\n"
            "     Memory: 172.0M"
        )

    elif commande == "systemctl status ssh" or commande == "systemctl status sshd":
        return (
            "● ssh.service - OpenBSD Secure Shell server\n"
            "     Loaded: loaded (/lib/systemd/system/ssh.service; enabled)\n"
            "     Active: active (running) since Mon 2026-04-04 11:20:00 UTC; 47 days ago\n"
            "   Main PID: 712 (sshd)\n"
            "      Tasks: 1 (limit: 4915)\n"
            "     Memory: 3.2M\n"
            "     CGroup: /system.slice/ssh.service\n"
            "             └─712 /usr/sbin/sshd -D"
        )

    elif commande == "systemctl list-units --type=service --state=running":
        return (
            "UNIT                     LOAD   ACTIVE SUB     DESCRIPTION\n"
            "cron.service             loaded active running Regular background program processing daemon\n"
            "fail2ban.service         loaded active running Fail2Ban Service\n"
            "mysql.service            loaded active running MySQL Community Server\n"
            "nginx.service            loaded active running A high performance web server\n"
            "ssh.service              loaded active running OpenBSD Secure Shell server\n"
            "ufw.service              loaded active running Uncomplicated firewall\n\n"
            "LOAD   = Reflects whether the unit definition was properly loaded.\n"
            "ACTIVE = The high-level unit activation state.\n"
            "SUB    = The low-level unit activation state.\n"
            "6 loaded units listed."
        )

    elif commande == "ufw status":
        return (
            "Status: active\n\n"
            "To                         Action      From\n"
            "--                         ------      ----\n"
            "22/tcp                     ALLOW       Anywhere\n"
            "80/tcp                     ALLOW       Anywhere\n"
            "443/tcp                    ALLOW       Anywhere\n"
            "22/tcp (v6)                ALLOW       Anywhere (v6)\n"
            "80/tcp (v6)                ALLOW       Anywhere (v6)\n"
            "443/tcp (v6)               ALLOW       Anywhere (v6)"
        )

    elif commande == "which python3":
        return "/usr/bin/python3"

    elif commande == "which python":
        return "/usr/bin/python"

    elif commande == "python3 --version":
        return "Python 3.12.3"

    elif commande == "python --version":
        return "Python 3.12.3"

    elif commande == "which bash":
        return "/usr/bin/bash"

    elif commande == "which curl":
        return "/usr/bin/curl"

    elif commande == "which wget":
        return "/usr/bin/wget"

    elif commande == "which nc" or commande == "which netcat":
        return "/usr/bin/nc"

    elif commande == "which nmap":
        return "bash: which: nmap : commande introuvable"

    elif commande == "gcc --version":
        return "gcc (Ubuntu 13.3.0-6ubuntu2~24.04) 13.3.0\nCopyright (C) 2023 Free Software Foundation, Inc."

    elif commande == "make --version":
        return "GNU Make 4.3\nBuilt for x86_64-pc-linux-gnu"

    elif commande == "git --version":
        return "git version 2.43.0"

    elif commande == "docker --version":
        return "Docker version 26.1.3, build b72abbb"

    elif commande == "docker ps":
        return (
            "CONTAINER ID   IMAGE         COMMAND                  CREATED        STATUS        PORTS                   NAMES\n"
            "a3f1e2d9c841   nginx:1.25    \"/docker-entrypoint.…\"   2 weeks ago    Up 2 weeks    0.0.0.0:80->80/tcp      webserver\n"
            "7b2c4e1f0d93   mysql:8.0     \"docker-entrypoint.s…\"   2 weeks ago    Up 2 weeks    127.0.0.1:3306->3306/tcp   database"
        )

    elif commande == "mysql --version":
        return "mysql  Ver 8.0.37 Distrib 8.0.37, for Linux (x86_64) using  EditLine wrapper"

    elif commande == "nginx -v" or commande == "nginx -V":
        return "nginx version: nginx/1.24.0 (Ubuntu)"

    elif commande == "curl --version":
        return "curl 8.5.0 (x86_64-pc-linux-gnu) libcurl/8.5.0 OpenSSL/3.0.13\nRelease-Date: 2023-12-06"

    elif commande == "wget --version":
        return "GNU Wget 1.21.4 built on linux-gnu."

    elif commande == "dpkg -l" or commande == "apt list --installed":
        return (
            "Listing...\n"
            "ii  adduser          3.137ubuntu1   all   add and remove users and groups\n"
            "ii  apt              2.8.3          amd64 commandline package manager\n"
            "ii  bash             5.2.21-2       amd64 GNU Bourne Again SHell\n"
            "ii  curl             8.5.0-2        amd64 command line tool for transferring data\n"
            "ii  docker-ce        26.1.3-1       amd64 Docker CE\n"
            "ii  fail2ban         1.0.2-3        all   ban hosts that cause multiple auth errors\n"
            "ii  git              2.43.0-1       amd64 fast, scalable, distributed revision control\n"
            "ii  mysql-server     8.0.37-1       amd64 MySQL database server\n"
            "ii  nginx            1.24.0-2       amd64 small, powerful, scalable web/proxy server\n"
            "ii  openssh-server   1:9.6p1-3      amd64 secure shell (SSH) server\n"
            "ii  python3          3.12.3-1       amd64 interactive high-level object-oriented language\n"
            "ii  ufw              0.36.2-1       all   program for managing a Netfilter firewall"
        )

    elif commande == "cat /var/log/auth.log":
        return (
            "May 21 14:28:01 srv-prod-01 sshd[4820]: Accepted publickey for root from 41.82.114.5 port 51234 ssh2\n"
            "May 21 12:11:33 srv-prod-01 sshd[4401]: Failed password for invalid user admin from 185.220.101.9 port 44382 ssh2\n"
            "May 21 12:11:35 srv-prod-01 sshd[4402]: Failed password for invalid user admin from 185.220.101.9 port 44384 ssh2\n"
            "May 21 11:58:02 srv-prod-01 sudo:    deploy : TTY=pts/1 ; USER=root ; COMMAND=/usr/bin/systemctl restart nginx\n"
            "May 20 23:41:07 srv-prod-01 sshd[3981]: Accepted publickey for root from 41.82.114.5 port 49871 ssh2"
        )

    elif commande == "cat /var/log/fail2ban.log":
        return (
            "2026-05-21 12:11:36 fail2ban.actions [1203]: NOTICE  [sshd] Ban 185.220.101.9\n"
            "2026-05-20 08:33:14 fail2ban.actions [1203]: NOTICE  [sshd] Ban 91.240.118.172\n"
            "2026-05-19 17:45:02 fail2ban.actions [1203]: NOTICE  [sshd] Ban 194.165.16.11\n"
            "2026-05-18 03:12:51 fail2ban.actions [1203]: NOTICE  [nginx-http-auth] Ban 45.142.212.100"
        )

    elif commande == "find / -perm -4000 -type f 2>/dev/null":
        return (
            "/usr/bin/sudo\n"
            "/usr/bin/passwd\n"
            "/usr/bin/newgrp\n"
            "/usr/bin/chsh\n"
            "/usr/bin/chfn\n"
            "/usr/bin/gpasswd\n"
            "/usr/bin/su\n"
            "/usr/lib/openssh/ssh-keysign\n"
            "/usr/lib/dbus-1.0/dbus-daemon-launch-helper"
        )

    elif commande == "crontab -l":
        return (
            "# Crontab de root\n"
            "0  2  *  *  *  /root/backup.sh >> /var/log/backup.log 2>&1\n"
            "*/5 * *  *  *  /usr/local/bin/monitor.sh\n"
            "0   0  1  *  *  certbot renew --quiet"
        )

    elif commande == "printenv":
        return (
            "SHELL=/bin/bash\n"
            "HOME=/root\n"
            "USER=root\n"
            "PATH=/usr/local/sbin:/usr/local/bin:/usr/sbin:/usr/bin:/sbin:/bin\n"
            "LANG=en_US.UTF-8\n"
            "TERM=xterm-256color"
        )

    elif commande == "clear":
        return "\033[2J\033[H"

   
    else:
        return f"bash: {commande} : commande introuvable"