# Summpy-Fix
originally from Summpy. this is bug fix version of Summpy.

## License

MIT License

## Requirements 

### Python 2.7.*

+ numpy
+ scipy
+ scikit-learn
+ networkx
+ cherrypy
+ MeCab or janome
+ pulp (if you use ILP-based method)

## Quick start

```sh
brew install mecab
brew install mecab-ipadic
pyenv 2.7.3
pyenv local 2.7.13
pip install git+https://github.com/OnetapInc/summpy-fix.git
pip install mecab-python
python2.7 -m summpy.server -h 127.0.0.1 -p 8080
curl http://127.0.0.1:8080/summarize\?sent_limit\=3\&text\=要約したい文章を入力。
```

## Production Usage
this library has been used in these services.
[TravelMe](https://travelme.jp) is provided by [Onetap Inc](https://onetap.amebaownd.com/)

