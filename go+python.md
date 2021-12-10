
salt-dev机器google otp登录老是会报错，调试办法：
在本地vmware机器上传私钥后，ssh -i ./id_rsa zhangyiwen117968@172.16.108.142 -vvvv
根据返回的日志分析问题。
审计日志：
less /var/log/audit/audit.log
登录日志： (日志并没有输出到这里)
/var/log/auth.log

开发、测试环境机器列表：

devops03 -- 172.16.108.119 -- 开发环境，我自己做实验的机器        devops
elk1     -- 172.16.108.137 -- 测试环境的elk，也是现在的zabbix-server      elk
elk2     -- 172.16.108.138 -- 测试环境，目前没有做啥操作            elk   
esports-webdev01 -- 172.16.108.139 -- 电竞官网开发环境    √    esports-webdev
esports-webdev02 -- 172.16.108.140 -- 电竞官网测试环境    √    esports-webdev
esports-webdev03 -- 172.16.108.141 -- 电竞官网发版环境    √    esports-webdev


salt-dev  -- 172.16.108.142	-- 开发环境的salt-master      √    esports-webdev
scpvp-php-qa -- 172.16.108.124 -- PVP PHP Staging 环境    √    pvp
scpvp-php-dev -- 172.16.108.106 -- PVP PHP 开发环境       √    pvp
scpvp-c-qa -- 172.16.108.125 -- PVP C模块 Staging 环境         pvp
scdev02 -- 172.16.108.103 -- qa机器                 √        qa
centos7-base(app-engine) -- 172.16.108.114 -- qa机器         qa
k8s-master01-dev -- 172.16.108.149	-- k8s机器master01     k8s
k8s-master02-dev --	172.16.108.149                         k8s
k8s-master03-dev --	172.16.108.149                         k8s
k8s-node01-dev --	172.16.108.152	-- k8s机器node01         k8s
k8s-node02-dev --	172.16.108.153	                         k8s
k8s-node03-dev --	172.16.108.154                           k8s
k8s-node04-dev -- 172.16.108.155	                         k8s
k8s-node05-dev -- 172.16.108.156                           k8s


自动发现：devops03主机跑了tomcat，开启了端口8080--8085，浏览器访问http://172.16.108.119:8085/
tomcat端口列表：
```
/usr/bin/netstat -tnl|grep -v 8090|egrep -i "$1"|awk {'print $4'}|awk -F':' '{if ($NF~/^8[0-9]{3}*$/) print $NF}'|sort |uniq 2>/dev/null
```
反向过滤8090端口，这是开启在tomcat服务器上与zabbix-java-gateway的10052端口通信的端口。


跟scpvp-php-qa的ga保持一致了

# zhangriqiong
YSSE4I6LUOYS2VM7CMMVOASWAM

hi，qa新机器权限帮你开好了，这台机器也是使用Google otp登录的。
ip：172.16.108.120
登录名：zhangriqiong
密码：和scpvp-php-qa（172.16.108.124） 机器是一样的6位动态码

要是忘记了密钥的话：
google otp：YSSE4I6LUOYS2VM7CMMVOASWAM

你登下试试

# sachunlin  
ZBNSUSITST7PVKAY

hi，qa新机器权限帮你开好了，这台机器也是使用Google otp登录的。
ip：172.16.108.120
登录名：sachunlin
密码：和scpvp-php-qa（172.16.108.124） 机器是一样的6位动态码

要是忘记了密钥的话：
google otp：ZBNSUSITST7PVKAY

你登下试试

# qinxigui  
5YXDT6HF7X3EKE6E6NNVIJPOMA

hi，qa新机器权限帮你开好了，这台机器也是使用Google otp登录的。
ip：172.16.108.120
登录名：qinxigui
密码：和scpvp-php-qa（172.16.108.124） 机器是一样的6位动态码

要是忘记了密钥的话：
google otp：5YXDT6HF7X3EKE6E6NNVIJPOMA

你登下试试

# zhanglei119337 
7MY7WUGJ36H7P4FFM45SPYFHZ4

hi，qa新机器权限帮你开好了，这台机器也是使用Google otp登录的。
ip：172.16.108.120
登录名：zhanglei119337
密码：和scpvp-php-qa（172.16.108.124） 机器是一样的6位动态码

要是忘记了密钥的话：
google otp：7MY7WUGJ36H7P4FFM45SPYFHZ4

你登下试试

# ouwenyu  
ZYSUB4CADCSO7GHLFOWU3ZGADE

hi，qa新机器权限帮你开好了，这台机器也是使用Google otp登录的。
ip：172.16.108.120
登录名：ouwenyu
密码：和scpvp-php-qa（172.16.108.124） 机器是一样的6位动态码

要是忘记了密钥的话：
google otp：ZYSUB4CADCSO7GHLFOWU3ZGADE

你登下试试

# zhangxin120945
55CTBETGL7WKBWMMIIZ24M2TWE

hi，qa新机器权限帮你开好了，这台机器也是使用Google otp登录的。
ip：172.16.108.120
登录名：zhangxin120945
密码：和scpvp-php-qa（172.16.108.124） 机器是一样的6位动态码

要是忘记了密钥的话：
google otp：55CTBETGL7WKBWMMIIZ24M2TWE

你登下试试

# yangjunjun  

hi，qa新机器权限帮你开好了，这台机器也是使用Google otp登录的。
ip：172.16.108.120
登录名：yangjunjun
密码：6位动态码

Your new secret key is: SDPKLE62ADIJ62LY3BIZ4R4PIA

你登下试试

# chenyuhong 
KUO5D6CVUZ6E426IJSU2D3XPAE

hi，qa新机器权限帮你开好了，这台机器也是使用Google otp登录的。
ip：172.16.108.120
登录名：chenyuhong
密码：和scpvp-php-qa（172.16.108.124） 机器是一样的6位动态码

要是忘记了密钥的话：
google otp：KUO5D6CVUZ6E426IJSU2D3XPAE

你登下试试

# yanwei112818 
DJW3WRO5WAMWWUB7


hi，qa新机器权限帮你开好了，这台机器也是使用Google otp登录的。
ip：172.16.108.120
登录名：yanwei112818 
密码：和scpvp-php-qa（172.16.108.124） 机器是一样的6位动态码

要是忘记了密钥的话：
google otp：DJW3WRO5WAMWWUB7

你登下试试


# o.yongshun 

hi，qa新机器权限帮你开好了，这台机器也是使用Google otp登录的。
ip：172.16.108.120
登录名：o.yongshun
密码：6位动态码

google otp：
Your new secret key is: VPZ57V3JDJ2C2PGRT5T5ODTNVQ

你登下试试

# yangyu106565 
IIT7IPFJSMR3CAG7

hi，qa新机器权限帮你开好了，这台机器也是使用Google otp登录的。
ip：172.16.108.120
登录名：yangyu106565
密码：和scpvp-php-qa（172.16.108.124） 机器是一样的6位动态码

要是忘记了密钥的话：
google otp：IIT7IPFJSMR3CAG7

你登下试试


# wangqing118177 

hi，qa新机器权限帮你开好了，这台机器也是使用Google otp登录的。
ip：172.16.108.120
登录名：wangqing118177
密码：6位动态码

google otp：
Your new secret key is: 4FVUPLH3YJUCYMZGEAOZMYGUZ4

你登下试试



新机器自动注册到测试环境zabbix监控系统的流程：
安装zabbix-agent，修改配置文件，添加元数据等信息：

[root@scdev06 ~]# sed -n '/^#/!p' /etc/zabbix/zabbix_agentd.conf | sed -n '/^$/!p'
PidFile=/var/run/zabbix/zabbix_agentd.pid
LogFile=/var/log/zabbix/zabbix_agentd.log
LogFileSize=0
EnableRemoteCommands=1
Server=172.16.108.137
ServerActive=172.16.108.137
Hostname=scdev06
HostMetadata=qa
Include=/etc/zabbix/zabbix_agentd.d/*.conf
UnsafeUserParameters=1

按照主机的分类去定义元数据，开启服务，在zabbix-web界面，可以看到主机就出现了

查看zabbix-agent文件中不以#开头的所有行：
sed -n '/^#/!p' /etc/zabbix/zabbix_agentd.conf|sed -n '/^$/!p' | wc -l


cat install-zabbix-agent.sh
```
#!/bin/bash
# 定义全局变量
nodename=`hostname`
hostmetadata=elk

# 函数，配置yum源并安装zabbix-agent
config_yumrepo(){
    rpm -Uvh https://repo.zabbix.com/zabbix/5.0/rhel/7/x86_64/zabbix-release-5.0-1.el7.noarch.rpm
    yum clean all && yum repolist
    yum install zabbix-agent -y
    echo "yumrepo is ok and zabbix-agent has installed."

}

# 函数，修改配置文件，并开启服务
config_zabbixagent(){
    sed '/^Server=127.0.0.1/cServer=172.16.108.137' -i /etc/zabbix/zabbix_agentd.conf
    sed '/^ServerActive=127.0.0.1/cServerActive=172.16.108.137' -i /etc/zabbix/zabbix_agentd.conf
    sed "s/Hostname=Zabbix server/Hostname=${nodename}/g" -i /etc/zabbix/zabbix_agentd.conf
    echo "EnableRemoteCommands=1" >> /etc/zabbix/zabbix_agentd.conf
    echo "UnsafeUserParameters=1" >> /etc/zabbix/zabbix_agentd.conf
    echo HostMetadata="$hostmetadata" >> /etc/zabbix/zabbix_agentd.conf
}

# 函数，开启服务并设置自启动
service_zabbixagent(){
     systemctl start zabbix-agent.service
     systemctl enable zabbix-agent.service
     systemctl restart zabbix-agent.service
}

# 调用函数
config_yumrepo
config_zabbixagent
service_zabbixagent
```




内容:
{HOST.NAME1}
{IPADDRESS}
{ITEM.KEY1}: {ITEM.VALUE1}

Item info:
Item name: {ITEM.NAME1}

Trigger Info:
Trigger: {TRIGGER.NAME}
Trigger status: {TRIGGER.STATUS}
Trigger severity: {TRIGGER.SEVERITY}

Original event ID: {EVENT.ID}


