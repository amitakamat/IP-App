from netifaces import interfaces, ifaddresses, AF_INET
count = 0
for ifaceName in interfaces():
    addresses = [i['addr'] for i in ifaddresses(ifaceName).setdefault(AF_INET, [{'addr':'No IP addr'}] )]
    count =+ 1
    print('Total IP count =' + str(count))
