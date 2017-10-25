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
**pip install git+https://github.com/OnetapInc/summpy.git**
pip install mecab-python
python2.7 -m summpy.server -h 127.0.0.1 -p 8080
curl http://127.0.0.1:8080/summarize\?sent_limit\=3\&text\=要約したい文章を入力。
```

- G. Erkan and D. Radev. LexRank: graph-based lexical centrality as salience in text summarization. J. Artif. Int. Res. 22(1), pages 457-479, 2004. ([link](http://www.cs.cmu.edu/afs/cs/project/jair/pub/volume22/erkan04a-html/erkan04a.html))
- Q. Mei, J. Guo, and D. Radev. DivRank: the Interplay of Prestige and Diversity in Information Networks. In Proceedings of the 16th ACM SIGKDD International Conference on Knowledge Discovery and Data Mining (KDD '10), pages 1009-1018, 2010. ([link](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.174.7982))

- H. Takamura and M. Okumura. Text Summarization Model Based on Maximum Coverage Problem and its Variant. In Proceedings of the 12th Conference of the European Chapter of the Association for Computational Linguistics (EACL '09), pages 781-789, 2009. ([link](http://citeseerx.ist.psu.edu/viewdoc/summary?doi=10.1.1.222.6945))
