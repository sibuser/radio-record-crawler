# Crawler to download music from Radio Record

It turned out that Radio Record keeps all their music publicly available, and you can download from http://history.radiorecord.ru/air/.

To define what stations to download just update the CHANNELS variable in the [settings](./record_crawler/settings.py).

To build and start a container just run:
```bash
# DST is where music will be downloaded to
DST="/media/dst" docker-compose up -d
```

I'm not responsible to any legal issues if you decide to use their files in other ways rather listening 
privately.