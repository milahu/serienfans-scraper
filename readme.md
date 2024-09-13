# serienfans-scraper

scrape download links for TV shows from [serienfans.org](https://serienfans.org/)



## why

get download links for [pyload](https://github.com/pyload/pyload), [jdownloader](https://jdownloader.org/), ...



## todo

- implement cutcaptcha solver. cutcaptcha is used by filecrypt.cc
  - jdownloader: [upcoming CORE-update: Added CutCaptcha support](https://board.jdownloader.org/showthread.php?p=539302#post539302)
  - pyload: [cutcaptcha issues](https://github.com/pyload/pyload/issues?q=cutcaptcha)



## example output

```
$ ./shell.nix.sh

$ time ./serienfans-scraper.py search solar
https://serienfans.org/solar-opposites # Solar Opposites (2020) # Eine Alien-Familie einer sehr wohlhabenden Welt muss in Mittelamerika Zuflucht suchen – zwischen den unterschiedlichen Generationen entbrennt eine Meinungsverschiedenheit, ob die Erde nun eine reine Katastrophe oder einfach nur genial ist.
https://filmfans.org/solaris_1 # Solaris (2002) # Der Psychologe Dr. Chris Kelvin erhält den Auftrag, die unerklärlichen Vorkommnisse auf der Raumstation Prometheus zu untersuchen. Die umkreist derzeit den luminiszierenden Planeten Solaris, von dem auch die angeblichen "Besucher" zu stammen scheinen, die den zwei verbliebenen Crewmitgliedern das Leben schwer machen. Mit der Zeit wird jedoch klar, dass die Wesen lediglich Kreationen der eigenen Erinnerung sind. Wie auch Chris Frau Rheya, die plötzlich neben dem Arzt im Bett liegt - obwohl sie vor Jahren Selbstmord beging.
https://filmfans.org/solaris # Solaris (1972) # In der ausführlichen Exposition, die wie nebenbei in wunderbaren Naturbildern schwelgt, wird das Wesen des Planeten Solaris erklärt, der ganz und gar von einem schaumigen Ozean bedeckt ist und auch nach jahrzehntelanger Forschung ein Mysterium bleibt. Eine Art Verstand oder Bewusstsein soll der Ozean haben, doch die Wissenschaft kapituliert: Ursprünglich für 85 Wissenschaftler gebaut, beherbergt die im Orbit des Planeten schwebende Raumstation nur noch drei Forscher. Der Psychologe Kris Kelvin soll nun zur Station reisen, den Status quo beurteilen und eine Empfehlung für oder gegen das Einstellen der zeit- und kostenintensiven Forschung abgeben.
https://filmfans.org/solarbabies # Solarfighters (1986) # Nach einem Atomkrieg ist die Erde zu einer öden Wüste geworden. Das Protektorat wacht über die Überlebenden und rationiert das knappe Wasser. Rollschuhfahrende Teenager, die sich Solarbabies nennen, finden die Zauberkugel Bohdi, die zum Dreh- und Angelpunkt der Geschichte wird. Strictor Grock, der verlängerte Arm des Protektorates, will Bohdi, um den letzten Hoffnungsfunken der Unterdrückten zu vernichten. Zu diesem Zweck setzt er Söldner auf die Jugendlichen an. Auf verschiedenen Umwegen, wobei auch Nachfahren der Indianer ihr Können zeigen, kommt es zum Showdown.
https://filmfans.org/solar-attack # Solar Attack (2006) # Da helfen keine Sunblocker mehr! Die Sonne gerät außer Kontrolle. Gewaltige Eruptionen aus ihrem Kern formen sich zu bedrohlichen Sonnenstürmen, die auf die Erde zurasen und die Existenz allen Lebens auf dem Planeten bedrohen. Die ersten riesigen Wolken mit geladenen Partikeln treffen auf die Erdatmosphäre, lassen einen Satelliten abstürzen und zerstören eine Raumsonde. Beinahe ohnmächtig müssen die Regierungen der USA und ihrer Verbündeten mit ansehen, wie die Auslöschung der Menschheit immer näher rückt. Bis Dr. Lucas Foster (Mark Dacascos) einen unglaublichen Plan hat, um das Armageddon doch noch abzuwenden: Durch nukleare Sprengungen soll das Eis der Polarkappen in die Atmosphäre geschossen werden, um den tödlichen Hitzesturm abzuwenden. Die Zeit läuft für Lucas Foster...
https://filmfans.org/solitary # Solitary (2020) # A man wakes up inside a room to discover hes a prisoner sent into space to form Earths first colony, and worse - his cell mate Alana is hell bent on destroying everything.

real    0m2.367s
user    0m0.895s
sys     0m0.083s

$ time ./serienfans-scraper.py get https://serienfans.org/solar-opposites
season 1
  release Solar.Opposites.S01.GERMAN.DL.1080P.WEB.H264-WAYNE
    hoster ddownload mixed https://filecrypt.cc/Container/6e6eb65ace.html?mirror=2
    hoster katfile mixed https://filecrypt.cc/Container/6e6eb65ace.html?mirror=3
    hoster rapidgator online https://filecrypt.cc/Container/6e6eb65ace.html?mirror=1
  release Solar.Opposites.S01.German.DL.720p.WEB.h264-WvF
    hoster 1fichier online https://filecrypt.cc/Container/b79059215a.html?mirror=0
    hoster ddownload online https://filecrypt.cc/Container/b79059215a.html?mirror=2
    hoster katfile online https://filecrypt.cc/Container/b79059215a.html?mirror=3
    hoster rapidgator online https://filecrypt.cc/Container/b79059215a.html?mirror=1
  release Solar.Opposites.S01.German.DL.DisneyHD.x264-4SF
    hoster ddownload online https://filecrypt.cc/Container/22417850ba.html?mirror=2
    hoster rapidgator online https://filecrypt.cc/Container/22417850ba.html?mirror=1
season 2
  release Solar.Opposites.S02.GERMAN.DL.1080P.WEB.H264-WAYNE
    hoster 1fichier online https://filecrypt.cc/Container/dbbe515687.html?mirror=0
    hoster ddownload online https://filecrypt.cc/Container/dbbe515687.html?mirror=2
    hoster katfile online https://filecrypt.cc/Container/dbbe515687.html?mirror=3
    hoster rapidgator online https://filecrypt.cc/Container/dbbe515687.html?mirror=1
  release Solar.Opposites.S02.German.DL.720p.WEB.h264-WvF
    hoster ddownload online https://filecrypt.cc/Container/4617ab520f.html?mirror=2
    hoster rapidgator online https://filecrypt.cc/Container/4617ab520f.html?mirror=1
  release Solar.Opposites.S02.German.DL.DisneyHD.x264-4SF
    hoster ddownload online https://filecrypt.cc/Container/f30c6d4e45.html?mirror=2
    hoster rapidgator online https://filecrypt.cc/Container/f30c6d4e45.html?mirror=1
season 3
  release Solar.Opposites.S03.GERMAN.5.1.UNTOUCHED.DUBBED.DL.EAC3.1080p.WEB-DL.h264-TvR
    hoster ddownload online https://filecrypt.cc/Container/37129754eb.html?mirror=0
    hoster rapidgator online https://filecrypt.cc/Container/37129754eb.html?mirror=1
  release Solar.Opposites.S03.GERMAN.DL.1080p.WEB.h264-FENDT
    hoster ddownload online https://filecrypt.cc/Container/945ceb89ae.html?mirror=2
    hoster rapidgator online https://filecrypt.cc/Container/945ceb89ae.html?mirror=1
  release Solar.Opposites.S03.German.DL.720p.WEB.h264-WvF
    hoster ddownload online https://filecrypt.cc/Container/e6b9804efc.html?mirror=2
    hoster rapidgator online https://filecrypt.cc/Container/e6b9804efc.html?mirror=1
  release Solar.Opposites.S03.German.DL.DisneyHD.x264-4SF
    hoster 1fichier online https://filecrypt.cc/Container/c7ea8c026d.html?mirror=0
    hoster ddownload online https://filecrypt.cc/Container/c7ea8c026d.html?mirror=2
    hoster katfile mixed https://filecrypt.cc/Container/c7ea8c026d.html?mirror=3
    hoster rapidgator online https://filecrypt.cc/Container/c7ea8c026d.html?mirror=1
season 4
  release Solar.Opposites.S04.GERMAN.DL.1080P.WEB.H264-WAYNE
    hoster 1fichier online https://filecrypt.cc/Container/25052869c5.html?mirror=0
    hoster ddownload online https://filecrypt.cc/Container/25052869c5.html?mirror=2
    hoster katfile online https://filecrypt.cc/Container/25052869c5.html?mirror=3
    hoster rapidgator online https://filecrypt.cc/Container/25052869c5.html?mirror=1
  release Solar.Opposites.S04.German.DL.720p.WEB.h264-WvF
    hoster ddownload online https://filecrypt.cc/Container/59f9c398c6.html?mirror=2
    hoster rapidgator online https://filecrypt.cc/Container/59f9c398c6.html?mirror=1
  release Solar.Opposites.S04.German.DL.DisneyHD.x264-4SF
    hoster 1fichier online https://filecrypt.cc/Container/37d80bc745.html?mirror=0
    hoster ddownload online https://filecrypt.cc/Container/37d80bc745.html?mirror=2
    hoster katfile online https://filecrypt.cc/Container/37d80bc745.html?mirror=3
    hoster rapidgator online https://filecrypt.cc/Container/37d80bc745.html?mirror=1
season 5
  release Solar.Opposites.S05.GERMAN.DL.1080p.WEB.h264-SAUERKRAUT
    hoster 1fichier online https://filecrypt.cc/Container/119c178125.html?mirror=0
    hoster ddownload online https://filecrypt.cc/Container/119c178125.html?mirror=2
    hoster katfile online https://filecrypt.cc/Container/119c178125.html?mirror=3
    hoster rapidgator online https://filecrypt.cc/Container/119c178125.html?mirror=1
  release Solar.Opposites.S05.GERMAN.DL.720p.WEB.h264-SAUERKRAUT
    hoster 1fichier online https://filecrypt.cc/Container/f134faa3e6.html?mirror=0
    hoster ddownload online https://filecrypt.cc/Container/f134faa3e6.html?mirror=2
    hoster katfile online https://filecrypt.cc/Container/f134faa3e6.html?mirror=3
    hoster rapidgator online https://filecrypt.cc/Container/f134faa3e6.html?mirror=1
  release Solar.Opposites.S05.German.DL.DisneyHD.x264-4SF
    hoster 1fichier online https://filecrypt.cc/Container/bc89f89836.html?mirror=0
    hoster ddownload online https://filecrypt.cc/Container/bc89f89836.html?mirror=2
    hoster katfile online https://filecrypt.cc/Container/bc89f89836.html?mirror=3
    hoster rapidgator online https://filecrypt.cc/Container/bc89f89836.html?mirror=1

real    3m22.120s
user    0m7.759s
sys     0m0.183s
```
