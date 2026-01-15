#source: https://github.com/ncclient/ncclient

from ncclient import manager
import sys

def get_netconf_config():
    print("--- NetConf Kliens Program ---")
    
    default_host = "devnetsandboxiosxec8k.cisco.com"
    
    host_input = input(f"Add meg a NetConf szerver címét (a portszám bele van kódolva) [Enter = {default_host}]: ")
    host = host_input if host_input else default_host
    username = input(f"Add meg a NetConf szerver fiókod felhasználóját!")
    password = input(f"Add meg a NetConf szerver fiókod jelszavát!")
    
    port = 830

    print(f"\nCsatlakozás ide: {host}:{port} ...")

    try:
        with manager.connect(host=host, port=port, username=username, password=password,
                             hostkey_verify=False) as m:
            
            print("Sikeres csatlakozás!")
            
            xml_data = m.get_config(source='running').data_xml
            print("\n--- Szerver Válasza ---")
            print(xml_data)

            with open("router_config.xml", 'w') as f:
                f.write(xml_data)
            print("\nA teljes konfiguráció mentve a 'router_config.xml' fájlba.")

    except Exception as e:
        print(f"\nHiba történt: {e}")
        print("Ellenőrizd az internetkapcsolatot vagy a szerver adatait!")

if __name__ == '__main__':
    get_netconf_config()