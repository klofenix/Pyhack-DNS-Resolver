import dns.resolver

def main():
    try:
        objetivo = dns.resolver.query("XXXX.com", "NS")
        for x in objetivo:
            print("[+]"+ x)
    except:
        print("***ERROR DETECTED*** No se puede obtener información")
if __name__ == '__main__':
    try:
        main()
    except KeyboardInterrupt:
        exit()
