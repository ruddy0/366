# Modüller
import sys, os

# Sabitler
f0 = sys.argv[0]
f1 = sys.argv[1] # Burada 2. parametreyi alıyoruz ki program mantıklı çalışsın_

if os.name == "nt":
    dizin = "C:/Windows/System32/drivers/etc/hosts"

elif os.name == "posix":
    dizin = "/etc/hosts"

def engelleyici():
    # Şimdi burada da şöye yaptık. Listeyi sıraya soktuk ve gelen değer paramere yada program ismi ise pas geçtik değilse programa ekledik?_ Sıkınrı var mı?
    for i in sys.argv:
        if i == f0 or i == f1:
            pass
        else:
            with open(dizin, "a") as hosts:
                hosts.write("\n" + "127.0.0.1 " + i)
                hosts.close()

def engelKaldir():
    pass

if f1 == "-k": # Ana Kontrolü Yaptık, -k gelirse engelleme fonkisoynu çaışacak.
    engelleyici()
elif f1 == "-a": # Eğer belirtilen sienin kaldırılmasını istiyosak bu çalışacak değil mi??
    engelKaldir()
else:
    print("Yanlış İfade Girdiniz")


